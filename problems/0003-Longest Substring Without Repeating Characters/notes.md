# 3. Longest Substring Without Repeating Characters

**Pattern**: Sliding Window + HashSet

**Problem**:  
Given a string `s`, find the length of the **longest substring** without duplicate characters.  
- Digits and letters are allowed.  
- Substring = contiguous part of the string.  

**Examples**:  
- `s = "abcabcbb"` → answer = 3 ("abc")  
- `s = "bbbbb"` → answer = 1 ("b")  
- `s = "pwwkew"` → answer = 3 ("wke")  

---

**Idea**:  
- Use two pointers: `left` (window start) and `right` (window end).  
- Maintain a set `seen` with the characters in the current window.  
- For each `right`:
  - While `s[right]` is already in `seen`, remove `s[left]` and move `left++`.  
  - Add `s[right]` to `seen`.  
  - Update `max_len = max(max_len, right - left + 1)`.

---

**Time Complexity**: O(n), each char enters and leaves set at most once.  
**Space Complexity**: O(min(n, Σ)) where Σ = charset (26 for letters, up to 128 for ASCII).  

---

**Edge Cases**:  
- Empty string → 0  
- All same characters → 1  
- Alternating pattern like `"dvdf"` → longest = 3 (`"vdf"`)  
- Mixed length strings with special characters also work.
