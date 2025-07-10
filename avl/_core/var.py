# Copyright 2024 Apheleia
#
# Description:
# Apheleia Verification Library Variable Base Class

from __future__ import annotations

import random
import weakref
from collections.abc import Callable
from typing import Any

from z3 import BitVecNumRef, BoolRef, IntNumRef, Optimize, RatNumRef, sat


class Var:
    _count_ = 0
    _lookup_ = weakref.WeakValueDictionary()

    @staticmethod
    def _register_(cls : Var) -> None:
        Var._lookup_[Var._count_] = cls
        cls._idx_ = Var._count_
        Var._count_ += 1

    def __copy__(self) -> Var:
        """
        Copy the Var - always make a copy to ensure randomness is preserved.

        :return: Copied Var.
        :rtype: Var
        """
        new_obj = self.__class__(self.name, self.value, auto_random=self._auto_random_, fmt=self._fmt_)
        new_obj._constraints_ = {
            k: v.copy() for k, v in self._constraints_.items()
        }
        return  new_obj

    def __deepcopy__(self, memo) -> Var:
        """
        Deep copy the Var - always make a copy to ensure randomness is preserved.

        :param memo: Dictionary to keep track of already copied objects.
        :type memo: dict
        :return: Deep copied Var.
        :rtype: Var
        """
        new_obj = self.__copy__()
        memo[id(self)] = new_obj
        return new_obj

    def __init__(self, name: str, value: Any, auto_random: bool = True, fmt: Callable[..., int] = str, width: int = 32) -> None:
        """
        Initialize an instance of the class.

        :param name: The name of the instance.
        :type name: str
        :param value: The value associated with the instance.
        :type value: Any
        :param auto_random: Flag to enable or disable automatic randomness. Defaults to True.
        :type auto_random: bool, optional
        :param width: The width of the variable in bits, defaults to 32.
        :type width: int, optional
        :raises ValueError: If the width is not a positive integer.
        """

        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        self.width = int(width)

        # Lookup
        Var._register_(self)

        self.name = name
        self.value = self._cast_(value)
        self._auto_random_ = auto_random
        self._fmt_ = fmt

        # Randomness and constraints
        self._rand_ = None
        self._constraints_ = {True : {}, False: {}}

        if self._auto_random_:
            self._rand_ = self._z3_()

    def _cast_(self, other: Any) -> Any:
        """
        Cast the other value to the type of this variable's value.

        :param other: The value to cast.
        :type other: Any
        :return: The casted value.
        :rtype: Any
        """
        v = other.value if isinstance(other, type(self)) else other
        return type(self.value)(v)

    def _wrap_(self, result):
        """
        Wrap the result in an Var instance.

        :param result: The result to wrap.
        :type result: Any
        :return: An Var instance with the result.
        :rtype: Var
        """
        return type(self)(self.name, result, auto_random=self._auto_random_, fmt=self._fmt_)

    def _range_(self) -> tuple[Any, Any]:
        """
        Get the range of the variable.

        :return: A tuple containing the minimum and maximum values of the variable.
        :rtype: tuple[Any, Any]
        """
        raise NotImplementedError("Var does not implement _range_ method. Please override in subclass.")

    def _z3_(self) -> BoolRef | IntNumRef | BitVecNumRef | RatNumRef:
        """
        Return the Z3 representation of the variable.

        :return: The Z3 representation of the variable.
        :rtype: BoolRef | IntNumRef | BitVecNumRef | RatNumRef
        """
        raise NotImplementedError("Var does not implement _z3_ method. Please override in subclass.")

    def _random_value_(self, bounds: tuple[int, int] = None) -> Any:
        """
        Get a random value for the variable within the specified bounds.

        :param bounds: Optional tuple containing the minimum and maximum bounds for the random value.
        :type bounds: tuple[int, int], optional
        :return: A random value within the specified bounds.
        :rtype: Any
        """
        if bounds is None:
            bounds = self._range_()
        return random.randint(bounds[0], bounds[1])

    # Binary arithmetic
    def __add__(self, other): return self._wrap_(self._cast_(self.value + other))
    def __sub__(self, other): return self._wrap_(self._cast_(self.value - other))
    def __mul__(self, other): return self._wrap_(self._cast_(self.value * other))
    def __truediv__(self, other): return self._wrap_(self._cast_(self.value / other))
    def __floordiv__(self, other): return self._wrap_(self._cast_(self.value // other))
    def __mod__(self, other): return self._wrap_(self._cast_(self.value % other))
    def __pow__(self, other): return self._wrap_(self._cast_(self.value ** other))
    def __divmod__(self, other):
        a = self.value
        b = other.value if isinstance(other, Var) else other
        return tuple(self._wrap_(x) for x in divmod(a, b))

    def __iadd__(self, other):
        self.value = self._cast_(self.value + other)
        return self

    def __isub__(self, other):
        self.value = self._cast_(self.value - other)
        return self

    def __imul__(self, other):
        self.value = self._cast_(self.value * other)
        return self

    def __itruediv__(self, other):
        self.value = self._cast_(self.value / other)
        return self

    def __ifloordiv__(self, other):
        self.value = self._cast_(self.value // other)
        return self

    def __imod__(self, other):
        self.value = self._cast_(self.value % other)
        return self

    def __ipow__(self, other):
        self.value = self._cast_(self.value ** other)
        return self

    def __radd__(self, other): return self._wrap_(self._cast_(other + self.value))
    def __rsub__(self, other): return self._wrap_(self._cast_(other - self.value))
    def __rmul__(self, other): return self._wrap_(self._cast_(other * self.value))
    def __rtruediv__(self, other): return self._wrap_(self._cast_(other / self.value))
    def __rfloordiv__(self, other): return self._wrap_(self._cast_(other // self.value))
    def __rmod__(self, other): return self._wrap_(self._cast_(other % self.value))
    def __rpow__(self, other): return self._wrap_(self._cast_(other ** self.value))
    def __rdivmod__(self, other):
        a = other.value if isinstance(other, Var) else other
        b = self.value
        return tuple(self._wrap_(x) for x in divmod(a, b))

    # Bitwise
    def __and__(self, other): return self._wrap_(self._cast_(self.value & other))
    def __or__(self, other): return self._wrap_(self._cast_(self.value | other))
    def __xor__(self, other): return self._wrap_(self._cast_(self.value ^ other))
    def __lshift__(self, other): return self._wrap_(self._cast_(self.value << other))
    def __rshift__(self, other): return self._wrap_(self._cast_(self.value >> other))

    def __iand__(self, other):
        self.value = self._cast_(self.value & other)
        return self

    def __ior__(self, other):
        self.value = self._cast_(self.value | other)
        return self

    def __ixor__(self, other):
        self.value = self._cast_(self.value ^ other)
        return self

    def __ilshift__(self, other):
        self.value = self._cast_(self.value << other)
        return self

    def __irshift__(self, other):
        self.value = self._cast_(self.value >> other)
        return self

    def __rand__(self, other): return self._wrap_(self._cast_(other & self.value))
    def __ror__(self, other): return self._wrap_(self._cast_(other | self.value))
    def __rxor__(self, other): return self._wrap_(self._cast_(other ^ self.value))
    def __rlshift__(self, other): return self._wrap_(self._cast_(other << self.value))
    def __rrshift__(self, other): return self._wrap_(self._cast_(other >> self.value))

    # Unary
    def __neg__(self): return self._wrap_(-self.value)
    def __pos__(self): return self._wrap_(+self.value)
    def __abs__(self): return self._wrap_(abs(self.value))
    def __invert__(self): return self._wrap_(~self.value)

    # Comparison
    def __eq__(self, other): return self.value == other
    def __ne__(self, other): return not self.__eq__(other)
    def __lt__(self, other): return self.value < other
    def __le__(self, other): return self.__lt__(other) or self.__eq__(other)
    def __gt__(self, other): return not self.__le__(other)
    def __ge__(self, other): return not self.__lt__(other)

    # Conversion
    def __int__(self): return int(self.value)
    def __float__(self): return float(self.value)
    def __index__(self): return int(self.value)
    def __bool__(self): return bool(self.value)

    # String / representation
    def __repr__(self): return f"Var(name={self.name!r}, value={self.value!r}, auto_random={self._auto_random_}, fmt={self._fmt_.__name__})"
    def __str__(self): return self._fmt_(self.value)

    # Hashing
    def __hash__(self): return hash((self.name, self.value))

    def get_min(self) -> int:
        """
        Get the minimum value that can be represented by this variable.

        :return: The minimum value based on the sign and width of the variable.
        :rtype: int
        """
        return self._range_()[0]

    def get_max(self) -> int:
        """
        Get the maximum value that can be represented by this variable.

        :return: The maximum value.
        :rtype: int
        """
        return self._range_()[1]

    def add_constraint(
        self, name: str, constraint: BoolRef, hard: bool = True, target: dict = None
    ):
        """
        Add a constraint to the object.

        :param name: The name of the constraint.
        :type name: str
        :param constraint: The constraint function to add.
        :type constraint: function
        :param hard: Flag to indicate if the constraint is hard or soft. Defaults to True.
        :type hard: bool, optional
        :param target: The target dictionary to store the constraint. Defaults to None.
        :type target: dict, optional
        """
        if not self._auto_random_:
            raise ValueError("Cannot add constraints to non-random variables")

        if target is None:
            self._constraints_[hard][name] = constraint
        else:
            target[name] = constraint

    def remove_constraint(self, name: str) -> None:
        """
        Remove a constraint from the object.

        :param name: The name of the constraint to remove.
        :type name: str
        """
        if not self._auto_random_:
            raise ValueError("Cannot remove constraints from non-random variables")

        if name in self._constraints_[True]:
            del self._constraints_[True][name]

        if name in self._constraints_[False]:
            del self._constraints_[False][name]

    def pre_randomize(self) -> None:
        """
        Pre-randomization function.
        """
        pass

    def post_randomize(self) -> None:
        """
        Post-randomization function.
        """
        pass

    def _apply_constraints(self, solver : Optimize) -> None:
        """
        Apply the constraints to the solver.

        :param solver: The optimization solver to apply the constraints to.
        :type solver: Optimize
        """
        for c in self._constraints_[True].values():
            solver.add(c(self._rand_))

        for c in self._constraints_[False].values():
            solver.add_soft(c(self._rand_), weight=100)

    def randomize(self, hard: bool = None, soft: bool = None) -> None:
        """
        This method randomizes the value of the variable by considering hard and soft constraints.
        It uses an optimization solver to find a suitable value that satisfies the constraints.

        :param hard: Optional list of hard constraints to be added. Each constraint is a tuple where the first element is the constraint expression and the second element is the constraint value.
        :type hard: list, optional
        :param soft: Optional list of soft constraints to be added. Each constraint is a tuple where the first element is the constraint expression and the second element is the constraint value.
        :type soft: list, optional

        Hard and soft constraints follow the SV naming convention.
        Hard constraints must be satisfied, otherwise an error is raised.
        Soft constraints will attempt to be satisfied, but if not, the solver will
        return a solution that minimizes the number of unsatisfied constraints.

        :raises ValueError: If an unknown variable is encountered in the model.
        :raises Exception: If the solver fails to randomize the variable.
        """

        def new_solver():
            solver = Optimize()
            self._apply_constraints(solver)

            return solver

        def cast(solver, obj):
            if solver.check() == sat:
                model = solver.model()
                val = model.eval(obj.value() if hasattr(obj, "value") else obj, model_completion=True)
                if isinstance(val, RatNumRef):
                    cast_value = self._cast_(val.as_decimal(20).rstrip("?"))
                elif isinstance(val, (IntNumRef | BitVecNumRef)):
                    cast_value = self._cast_(val.as_long())
                else:
                    cast_value = self._cast_(val)
            else:
                raise Exception(f"Solver failed to randomize {self.name}")
            return cast_value

        # User defined pre-randomization function
        self.pre_randomize()

        # Constraints
        constraints = self._constraints_.copy()

        if hard is not None:
            idx = 0
            for c in hard:
                self.add_constraint(f"_c_hard_{idx}", c, hard=True, target=constraints[True])
                idx += 1
        if soft is not None:
            idx = 0
            for c in soft:
                self.add_constraint(f"_c_soft_{idx}", c, hard=False, target=constraints[False])
                idx += 1

        # Calculate the range of the random variable
        max_solver = new_solver()
        obj_max = max_solver.maximize(self._rand_)
        min_solver = new_solver()
        obj_min = min_solver.minimize(self._rand_)
        _range_ = [cast(min_solver, obj_min), cast(max_solver, obj_max)]

        # Create a new solver
        solver = new_solver()

        # Add in randomization
        solver.add_soft(
            self._rand_ == self._random_value_(bounds=(min(_range_), max(_range_))), weight=100
        )
        if random.choice([True, False]):
            solver.add_soft(self._rand_ != self.value, weight=100)

        # Assign value
        self.value = cast(solver, self._rand_)

        # User defined post-randomization function
        self.post_randomize()

__all__ = ["Var"]
