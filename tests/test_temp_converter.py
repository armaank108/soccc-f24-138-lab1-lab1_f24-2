import pytest
from temp_converter import c2f

def test_c2f_pass():
    # Valid case for c2f
    assert round(c2f(0), 2) == 32.0     # Freezing point of water

def test_c2f_fail_case_1():
    # Failing case for c2f
    assert round(c2f(0), 2) == 30.0  # This should fail based on your function

def test_c2f_fail_case_2():
    # Failing case for c2f
    assert round(c2f(100), 2) == 210.0  # This should fail based on your function

def test_c2f_fail_case_3():
    # Failing case for c2f
    assert round(c2f(37.78), 2) == 102.0  # This should fail based on your function
