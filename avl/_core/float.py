# Copyright 2024 Apheleia
#
# Description:
# Apheleia Verification Library Variable Class

from __future__ import annotations

import warnings
from collections.abc import Callable
from typing import Any

import numpy as np
from z3 import And, Real

from .var import Var


class Fp16(Var):
    def __init__(self, name: str, value: float, auto_random: bool = True, fmt: Callable[..., float] = str, width: int = 16) -> None:
        """
        Initialize an instance of the class.

        :param name: The name of the instance.
        :type name: str
        :param value: The value to be assigned to the instance.
        :type value: int
        :param auto_random: Flag to enable automatic randomization, defaults to True.
        :type auto_random: bool, optional
        :param fmt: The format to be used, defaults to hex.
        :type fmt: function, optional
        """
        if not hasattr(self, "value"):
            self.value = np.float16(0)
            self._bits_ = np.uint16(0)
        super().__init__(name, value, auto_random=auto_random, fmt=fmt, width=width)

    def _cast_(self, other: Any) -> Any:
        """
        Cast the other value to the type of this variable's value.

        :param other: The value to cast.
        :type other: Any
        :return: The casted value.
        :rtype: Any
        """
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=RuntimeWarning, message="overflow encountered in cast")
            return super()._cast_(other)

    def _range_(self) -> tuple[int, int]:
        """
        Get the range of values that can be represented by this variable.

        :return: A tuple containing the minimum and maximum values.
        :rtype: tuple[int, int]
        """
        return (-np.finfo(self.value).max, np.finfo(self.value).max)

    def _z3_(self) -> Real:
        """
        Get the Z3 representation of the variable.

        :return: The Z3 FP representation of the variable.
        :rtype: FP
        """
        self.add_constraint(
            "c_range_",
            lambda x: And(x >= self._range_()[0], x <= self._range_()[1]),
            hard=True,
        )
        return Real(f"{self._idx_}")

    def _random_value_(self, bounds: tuple[float, float] = None) -> float:
        """
        Randomize the value of the variable.

        :param bounds: Optional bounds for the random value.
        :type bounds: tuple[float, float], optional
        :return: A random float value within the specified bounds or the maximum value.
        :rtype: float
        """
        if bounds is None:
            bounds = self._range_()
        x = np.random.uniform(min(bounds), max(bounds))
        return self._cast_(x)

    def to_bits(self) -> int:
        """
        Get the raw representation of the variable.

        :return: The raw value.
        :rtype: float
        """
        return int(self.value.view(type(self._bits_)))

    def from_bits(self, raw: int) -> None:
        """
        Convert the raw representation back to a float.

        :param raw: The raw value.
        :type raw: int
        """
        self.value = self._cast_(type(self._bits_)(int(raw)).view(type(self.value)))

    # Bitwise
    def __and__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __or__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __xor__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __lshift__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __rshift__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __iand__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __ior__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __ixor__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __ilshift__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __irshift__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __rand__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __ror__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __rxor__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __rlshift__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")
    def __rrshift__(self, other): raise NotImplementedError("Bitwise operations are not supported for floating-point variables.")

    # Comparison - need to override to handle NaN and other cases
    def __eq__(self, other):
        other_val = self._cast_(other)
        return not (np.isnan(self.value) or np.isnan(other_val)) and self.value == other_val

    def __ne__(self, other):
        other_val = self._cast_(other)
        return np.isnan(self.value) or np.isnan(other_val) or self.value != other_val

    def __lt__(self, other):
        other_val = self._cast_(other)
        return not (np.isnan(self.value) or np.isnan(other_val)) and self.value < other_val

    def __le__(self, other):
        other_val = self._cast_(other)
        return not (np.isnan(self.value) or np.isnan(other_val)) and self.value <= other_val

    def __gt__(self, other):
        other_val = self._cast_(other)
        return not (np.isnan(self.value) or np.isnan(other_val)) and self.value > other_val

    def __ge__(self, other):
        other_val = self._cast_(other)
        return not (np.isnan(self.value) or np.isnan(other_val)) and self.value >= other_val

class Fp32(Fp16):
    def __init__(self, name: str, value: float, auto_random: bool = True, fmt: Callable[..., float] = str) -> None:
        """
        Initialize an instance of the class.

        :param name: The name of the instance.
        :type name: str
        :param value: The value to be assigned to the instance.
        :type value: int
        :param auto_random: Flag to enable automatic randomization, defaults to True.
        :type auto_random: bool, optional
        :param fmt: The format to be used, defaults to hex.
        :type fmt: function, optional
        """
        if not hasattr(self, "value"):
            self.value = np.float32(0)
            self._bits_ = np.uint32(0)
        super().__init__(name, value, auto_random=auto_random, width=32)

class Fp64(Fp16):
    def __init__(self, name: str, value: float, auto_random: bool = True, fmt: Callable[..., float] = str) -> None:
        """
        Initialize an instance of the class.

        :param name: The name of the instance.
        :type name: str
        :param value: The value to be assigned to the instance.
        :type value: int
        :param auto_random: Flag to enable automatic randomization, defaults to True.
        :type auto_random: bool, optional
        :param fmt: The format to be used, defaults to hex.
        :type fmt: function, optional
        """
        if not hasattr(self, "value"):
            self.value = np.float64(0)
            self._bits_ = np.uint64(0)
        super().__init__(name, value, auto_random=auto_random, width=64)

    def _range_(self) -> tuple[int, int]:
        """
        Get the range of values that can be represented by this variable.

        :return: A tuple containing the minimum and maximum values.
        :rtype: tuple[int, int]
        """
        return (-1e100, 1e100) # Reduced to allow randomization

Half = Fp16
Float = Fp32
Double = Fp64

__all__ = ["Fp16", "Fp32", "Fp64", "Half", "Float", "Double"]
