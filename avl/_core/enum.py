# Copyright 2024 Apheleia
#
# Description:
# Apheleia Verification Library Variable Class

import random
from collections.abc import Callable
from typing import Any
from math import ceil, log2

from z3 import Int, Or

from .var import Var


class Enum(Var):

    def __copy__(self):
        """
        Copy the Logic - always make a copy to ensure randomness is preserved.

        Slightly unusual. Explicitly create an enum, then change type.
        This is to allow a user to subclass an enum with a pre-defined set of values.

        :return: Copied Var.
        :rtype: Var
        """
        new_obj = Enum(self.name,
                                 self.value,
                                 values=self.values.copy(),
                                 auto_random=self._auto_random_,
                                 fmt=self._fmt_)
        new_obj._constraints_ = {
            k: v.copy() for k, v in self._constraints_.items()
        }
        new_obj.__class__ = self.__class__
        return  new_obj

    def __init__(
        self, name: str,
        value: Any,
        values: dict[str, Any],
        auto_random: bool = True,
        fmt : Callable [..., Any] = str,
        width : int | None = None
    ) -> None:
        """
        Initialize an enumeration variable.
        This class represents an enumeration variable that can take on a set of predefined values.
        The variable can be automatically randomized if `auto_random` is set to True.

        :param name: The name of the variable.
        :type name: str
        :param value: The initial value of the variable. It should be one of the values defined in `values`.
        :type value: Any
        :param values: A dictionary where keys are the names of the enumeration values and values are the corresponding values.
        :type values: dict[str, Any]
        :param auto_random: If True, the variable can be automatically randomized. Defaults to True.
        :type auto_random: bool
        :raises ValueError: If the provided `value` is not in the list of `values`.
        """
        if value in values.keys():
            self.value = values[value]
        elif value in values.values():
            self.value = value
        else:
            raise ValueError(f"Value {value} is not in the list of values {values}")

        # Define the values
        self.values = values
        for k, v in values.items():
            setattr(self, k, v)


        # Determine the minimum possible bit width
        min_value_representation = min(self.values.values())
        max_value_representation = max(self.values.values())

        signed = min_value_representation < 0

        if signed:
            bit_width_for_max_value = ceil(log2(max_value_representation + 1)) + 1
            bit_width_for_min_value = ceil(log2(-min_value_representation)) + 1

            bit_width = max(bit_width_for_min_value, bit_width_for_max_value)

        else:
            bit_width = ceil(log2(max_value_representation + 1))

        # Check user-defined width if provided, otherwise use minimum possible bit width
        if width is not None:
            if width < bit_width:
                raise ValueError(f"Width {width} is less than number of bits required to represent {len(self.values)} values")
            
        else:
            width = bit_width
        

        super().__init__(name, value, auto_random=auto_random, fmt=fmt, width=width)

    def _cast_(self, other: Any) -> Any:
        """
        Cast the other value to the type of this variable's value.

        :param other: The value to cast.
        :type other: Any
        :return: The casted value.
        :rtype: Any
        """
        v = other.value if isinstance(other, type(self)) else other
        if v in self.values.keys():
            return type(self.value)(self.values[v])
        elif v in self.values.values():
            return type(self.value)(v)
        else:
            raise ValueError(f"Value {v} is not in the list of values {self.values}")

    def _wrap_(self, result):
        """
        Wrap the result in an Var instance.

        :param result: The result to wrap.
        :type result: Any
        :return: An Var instance with the result.
        :rtype: Var
        """
        return type(self)(self.name, result, self.values, auto_random=self._auto_random_, fmt=self._fmt_)

    def _range_(self) -> tuple[Any, Any]:
        """
        Get the range of the variable.

        :return: A tuple containing the minimum and maximum values of the variable.
        :rtype: tuple[Any, Any]
        """
        return (min(self.values.values()), max(self.values.values()))

    def _z3_(self) -> Int:
        """
        Return the Z3 representation of the variable.

        :return: The Z3 representation of the variable.
        :rtype: BoolRef | IntNumRef | BitVecNumRef | RatNumRef
        """
        self.add_constraint(
            "_c_range_",
            lambda x: Or([x == v for v in self.values.values()]),
            hard=True,
        )
        return Int(f"{self._idx_}")

    # Type Conversions
    def __str__(self) -> str:
        """
        Returns the string representation of the current instance.

        Iterates through the `values` dictionary and returns the key
        corresponding to the current `value`.

        :return: The string representation of the current instance.
        :rtype: str
        """
        for k, v in self.values.items():
            if v == self.value:
                return self._fmt_(k)

    def _random_value_(self, bounds: tuple[Any, Any] = None) -> Any:
        """
        Randomize the value of the variable.
        """
        if bounds is not None:
            values = []
            for v in self.values.values():
                if v >= min(bounds) and v <= max(bounds):
                    values.append(v)
            return random.choice(values)
        else:
            return random.choice(list(self.values.values()))

__all__ = ["Enum"]
