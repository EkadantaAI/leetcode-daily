from add_two_numbers import Solution, list_to_linked, linked_to_list

def solve(l1_list, l2_list):
    l1 = list_to_linked(l1_list)
    l2 = list_to_linked(l2_list)
    ans_node = Solution().addTwoNumbers(l1, l2)
    return linked_to_list(ans_node)

def test_example_1():
    # 342 + 465 = 807 → [7,0,8]
    assert solve([2,4,3], [5,6,4]) == [7,0,8]

def test_example_2_carry_chain():
    # 99 + 1 = 100 → [0,0,1]
    assert solve([9,9], [1]) == [0,0,1]

def test_example_3_diff_lengths():
    # 18 + 0 = 18 → [8,1]
    assert solve([8,1], []) == [8,1]

def test_large_carry():
    # 999 + 999 = 1998 → [8,9,9,1]
    assert solve([9,9,9], [9,9,9]) == [8,9,9,1]
