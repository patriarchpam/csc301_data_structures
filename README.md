# CSC 301: Data Structures - Reorder List (LeetCode 143)

## Group Members

| S/N | Full Name | Matric / Reg Number |
|:---:|:---|:---|
| 1 | Pam Patriarch | VUG/SEN/24/12478 |
| 2 | Eboh Adaeze Michelle | VUG/SEN/24/11365 |
| 3 | Obi Celestine Tawo | VUG/SEN/24/11868 |
| 4 | Danzoss Blessing Teyei | VUG/SEN/24/11728 |
| 5 | Vlachos Ebikere Nina | VUG/SEN/24/11747 |
| 6 | Emmanuel Annah Kuje | VUG/SEN/24/11247 |
| 7 | Mgbemena Chimsimdi | VUG/SEN/24/11214 |
| 8 | Ike Nancy Nnenna | VUG/SEN/24/12359 |
| 9 | John Patience Godenaan | VUG/SEN/24/12079 |
| 10 | Essen Josephine Utibe | VUG/SEN/24/13127 |

---

## Project Overview

This project implements the solution for **LeetCode 143: Reorder List** in Java.

Given a singly linked list $L: L_0 \to L_1 \to \dots \to L_{n - 1} \to L_n$, reorder it to:
$$L_0 \to L_n \to L_1 \to L_{n - 1} \to L_2 \to L_{n - 2} \to \dots$$

### Algorithm Steps:
1. **Find Middle**: Use slow and fast pointers to locate the middle of the linked list.
2. **Reverse Second Half**: Invert the pointers of the second half in-place.
3. **Merge**: Interleave nodes alternately from the first and reversed second halves.

### Complexity:
- **Time Complexity**: $\mathcal{O}(n)$
- **Space Complexity**: $\mathcal{O}(1)$ (in-place)

---

## Files
- `ReorderList.java`: Full Java implementation with explanations.
- `DIAGRAM_GUIDE.md`: Step-by-step diagramming breakdown for each pointer transition.
