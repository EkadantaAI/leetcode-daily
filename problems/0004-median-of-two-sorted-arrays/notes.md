If true:
- **Odd total**: median = `min(Aright, Bright)`
- **Even total**: median = `(max(Aleft, Bleft) + min(Aright, Bright)) / 2`

If not:
- If `Aleft > Bright` ⇒ we took **too many** from A ⇒ move `hi = i - 1`
- Else (`Bleft > Aright`) ⇒ we took **too few** from A ⇒ move `lo = i + 1`

We binary-search `i` **only on the smaller array** to keep the log factor.

---

## Dry Run (quick)
`A=[1,3]`, `B=[2,4]`, `total=4`, `half=2`.  
Try `i=1`, `j=1`:  
`Aleft=1, Aright=3, Bleft=2, Bright=4`  
`1<=4` and `2<=3` ✅ → even total → median = `(max(1,2)+min(3,4))/2 = (2+3)/2 = 2.5`.

---

## Complexity
- **Time**: `O(log(min(m, n)))`
- **Space**: `O(1)`

---

## Pitfalls / Notes
- **Both arrays must be sorted** (non-decreasing). Passing an unsorted array breaks the partition logic.
- Always binary-search the **smaller** array.
- Handle boundaries with sentinels `-∞` / `+∞` to avoid index errors.
- Works with duplicates and negative numbers.

