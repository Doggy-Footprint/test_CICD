# test_string_utils.py

import pytest
from .string_utils import find_pattern

def test_find_pattern():
    text = "The quick brown fox jumps over the lazy dog."
    
    # Test for simple words
    assert find_pattern(text, r"fox") == ["fox"]
    assert find_pattern(text, r"dog") == ["dog"]
    
    # Test for multiple occurrences
    assert find_pattern(text, r"o.") == ["ow", "ox", "ov", "og"]
    
    # Test for no match
    assert find_pattern(text, r"cat") == []
    
    # Test with special characters
    assert find_pattern("hello@world.com", r"@\w+") == ["@world"]
    
    # Test with case sensitivity
    assert find_pattern(text, r"THE") == []  # Case-sensitive by default
    assert find_pattern(text, r"(?i)the") == ["The", "the"]  # Case-insensitive