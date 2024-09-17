import pytest
from temp_converter import c2f

def test_c2f_valid_case():
    # Valid case for c2f
    assert round(c2f(0), 2) == 32.0     # Freezing point of water
    assert round(c2f(100), 2) == 212.0   # Boiling point of water
    assert round(c2f(-40), 2) == -40.0   # Special case where Celsius and Fahrenheit are the same

def test_c2f_fail_case_1():
    # Deliberate failing case for c2f
    assert round(c2f(0), 2) == 30.0  #  expected value

def test_c2f_fail_case_2():
    # Deliberate failing case for c2f
    assert round(c2f(100), 2) == 210.0  #  expected value

def test_c2f_fail_case_3():
    # Deliberate failing case for c2f
    assert round(c2f(37.78), 2) == 102.0  #  expected value
