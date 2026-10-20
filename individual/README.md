# CSC 301: Data Structures - Individual Assignment

## Student Information
- **Name:** Pam Patriarch
- **Matric / Reg No:** VUG/SEN/24/12478
- **Topic:** Linked List In-Place Reordering (LeetCode 143)

---

## Architecture & Design Approach: Modular Decomposition

Unlike a single procedural monolithic function, this personal implementation uses **Modular Decomposition (Single Responsibility Principle)** by separating the problem into three isolated, independently verifiable helper methods:

```
reorderList(head)
   ├── 1. findMiddle(head)  --> Fast & Slow Tortoise-and-Hare technique
   ├── 2. reverse(head)     --> Iterative In-Place 3-pointer reversal
   └── 3. merge(l1, l2)     --> Interleaving merge of two list heads
```

### Advantages of this Format:
1. **Separation of Concerns:** Each helper method does exactly one thing well.
2. **Reusability & Testability:** `findMiddle` and `reverse` can be unit-tested or reused independently for other linked list problems (e.g. Palindrome Linked List, Reverse Linked List).
3. **Readability:** High-level algorithm flow in `reorderList` is clean and self-explanatory in under 15 lines of code.

---

## Complexity Analysis

| Metric | Complexity | Explanation |
|---|---|---|
| **Time Complexity** | $\mathcal{O}(n)$ | Finding middle takes $n/2$ steps, reversing takes $n/2$ steps, and merging takes $n$ steps. Total operations $= 2n \in \mathcal{O}(n)$. |
| **Space Complexity** | $\mathcal{O}(1)$ | All operations manipulate pointers directly in memory. No additional data structures (like arrays, stacks, or recursion frames) are allocated. |

---

## Verification & Test Results

The solution was verified against multiple test scenarios including odd-length lists, even-length lists, and boundary edge cases:

| Case | Input List | Output List | Result |
|:---:|:---|:---|:---:|
| 1 | `1 -> 2 -> 3 -> 4 -> 5` | `1 -> 5 -> 2 -> 4 -> 3` | Passed |
| 2 | `1 -> 2 -> 3 -> 4` | `1 -> 4 -> 2 -> 3` | Passed |
| 3 | `10 -> 20 -> 30 -> 40 -> 50 -> 60` | `10 -> 60 -> 20 -> 50 -> 30 -> 40` | Passed |
| 4 | `7 -> 9` | `7 -> 9` | Passed |
| 5 | `42` | `42` | Passed |

---

## How to Run

From this directory:
```bash
javac ReorderList.java
java ReorderList
```
