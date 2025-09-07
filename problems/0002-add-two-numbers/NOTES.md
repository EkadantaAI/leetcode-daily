# 2. Add Two Numbers

**Pattern**: Linked List + Carry Forward Addition  

**Problem**:  
Two numbers are represented as linked lists in reverse order. Each node is a digit.  
We must add them and return the sum as a new linked list.  

**Idea**:  
- Use a dummy head and pointer.  
- Traverse both lists simultaneously.  
- For each node: `digit = (x + y + carry) % 10`, update `carry = (x + y + carry) // 10`.  
- Append the new node with `digit`.  
- At the end, return `dummy.next`.  

**Why naive string/int join fails**:  
- `l1` and `l2` are **linked lists**, not Python arrays.  
- You cannot directly `''.join(l1)`.  
- Even if converted, the correct approach is **digit-wise carry addition**.  

**Complexity**:  
- Time: O(max(m, n)) where m, n = lengths of lists  
- Space: O(max(m, n)) for the result list  

**Edge cases**:  
- Different lengths (e.g., [2,4,3] + [5,6])  
- Carry propagation (e.g., [9,9] + [1] → [0,0,1])  
- Empty list (treat as 0)
