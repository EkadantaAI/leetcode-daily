import math
from median_two_sorted import Solution  # rename if your file name differs

sol = Solution()

def almost_equal(a, b, eps=1e-9):
    return abs(a - b) < eps

def test_example_1():
    assert almost_equal(sol.findMedianSortedArrays([1,3], [2]), 2.0)

def test_example_2():
    assert almost_equal(sol.findMedianSortedArrays([1,2], [3,4]), 2.5)

def test_one_empty_array():
    assert almost_equal(sol.findMedianSortedArrays([], [1]), 1.0)
    assert almost_equal(sol.findMedianSortedArrays([2], []), 2.0)

def test_all_zeros():
    assert almost_equal(sol.findMedianSortedArrays([0,0], [0,0]), 0.0)

def test_different_lengths():
    # Your earlier case with sorted nums2
    assert almost_equal(sol.findMedianSortedArrays([1,3,9], [2,4,6,8]), 4.0)

def test_negatives_and_mixed():
    # merged: [-5,-3,-2,-1,4] -> median = -2
    assert almost_equal(sol.findMedianSortedArrays([-5,-3,-1], [-2,4]), -2.0)

def test_many_duplicates():
    # merged: [1,2,2,2,2,3,4] -> median = 2
    assert almost_equal(sol.findMedianSortedArrays([1,2,2], [2,2,3,4]), 2.0)
