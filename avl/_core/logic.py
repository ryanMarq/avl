# Copyright 2024 Apheleia
#
# Description:
# Apheleia Verification Library Variable Class

from __future__ import annotations

import random
from collections.abc import Callable
from typing import Any

from z3 import BitVec, Extract, Optimize

from .var import Var


class Logic(Var):

    def __copy__(self):
        """
        Copy the Logic - always make a copy to ensure randomness is preserved.

        :return: Copied Var.
        :rtype: Var
        """
        new_obj = Logic(self.value, auto_random=self._auto_random_, fmt=self._fmt_, width=self.width)
        new_obj._constraints_ = {
            k: v.copy() for k, v in self._constraints_.items()
        }
        return  new_obj

    def __init__(
        self,
        *args,
        auto_random: bool = True,
        fmt: Callable[..., int] = hex,
        width: int = 32
    ) -> None:
        """
        Initialize an instance of the class.

        :param value: The initial value of the variable.
        :type value: any
        :param auto_random: Indicates if the variable should be automatically randomized, defaults to True.
        :type auto_random: bool, optional
        :param fmt: The format of the variable, defaults to hex.
        :type fmt: type, optional
        :param width: The width of the variable in bits, defaults to 32.
        :type width: int, optional
        :raises ValueError: If the width is not a positive integer.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        self.width = int(width)

        super().__init__(*args, auto_random=auto_random, fmt=fmt)

    def _cast_(self, other: Any) -> int:
        """
        Cast the value to the appropriate type based on the width of the variable.

        :param other: The value to be cast.
        :type other: Any
        :return: The casted value.
        :rtype: int
        """
        v = other.value if isinstance(other, Logic) else other
        return int(v & self._range_()[1])

    def _wrap_(self, result : Any) -> Logic:
        """
        Wrap the result in an Logic instance.

        :param result: The result to be wrapped.
        :type result: Any
        :return: An instance of Logic with the result.
        :rtype: Logic
        """
        return type(self)(result, auto_random=self._auto_random_, fmt=self._fmt_, width=self.width)

    def _range_(self) -> tuple[int, int]:
        """
        Get the range of values that can be represented by this variable.

        :return: A tuple containing the minimum and maximum values.
        :rtype: tuple[int, int]
        """
        return (0, (1 << self.width) - 1)

    def _z3_(self) -> BitVec:
        """
        Get the Z3 representation of the variable.

        :return: The Z3 BitVec representation of the variable.
        :rtype: z3.BitVecRef
        """
        return BitVec(f"{self._idx_}", self.width)
    
    def _apply_randomizing_constraints(self, solver: Optimize, random_range) -> None:
        random_val = self._random_value_(bounds=(min(random_range), max(random_range)))

        for i in range(self.width):
            random_val_bit = random_val >> i & 1
            solver.add_soft(Extract(i, i, self._rand_) == random_val_bit)
        
        if random.choice([True, False]):
            solver.add_soft(self._rand_ != self.value, weight="100")


__all__ = ["Logic"]
