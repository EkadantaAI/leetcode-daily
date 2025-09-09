import pytest
from longest_substring import Solution

def test_example_1():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3

def test_example_2():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1

def test_example_3():
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3

def test_empty_string():
    assert Solution().lengthOfLongestSubstring("") == 0

def test_single_char():
    assert Solution().lengthOfLongestSubstring("a") == 1

def test_mixed_chars():
    assert Solution().lengthOfLongestSubstring("dvdf") == 3  # "vdf"
