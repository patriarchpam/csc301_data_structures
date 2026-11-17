# Hand-Drawn Diagram Guide: Question 3 (Level Order Traversal)

**Important Rule:** *Use of AI for diagrams is not allowed.*  
Draw this diagram neatly by hand on plain white paper or graph paper using a ruler and two pen colours (e.g. **Blue** for tree nodes/levels, **Red** for the traversal arrows and Queue box), snap a clear photo, and insert it into the placeholder box in the Word document (or use Word's built-in Circle/Arrow shapes manually).

---

## Part 1: Draw the Binary Tree with Horizontal Level Lines

1. **Draw 3 horizontal dashed lines** across your page and label them on the left margin:
   - `Level 0 (Root)`
   - `Level 1`
   - `Level 2`
2. **Draw the circles (nodes)** on each level:
   - **Level 0:** Draw `( 10 )` in the top centre.
   - **Level 1:** Below `10`, draw `( 15 )` on the left and `( 40 )` on the right. Connect `10 -> 15` and `10 -> 40`.
   - **Level 2:**
     - Below `15`, draw `( 20 )` on the left and `( 25 )` on the right. Connect `15 -> 20` and `15 -> 25`.
     - Below `40`, draw `( 35 )` on the left and `( 50 )` on the right. Connect `40 -> 35` and `40 -> 50`.
3. **Draw sweeping left-to-right horizontal arrows** across each level:
   - At Level 0: Arrow pointing to `10` (Label: *1st*)
   - At Level 1: Arrow going left-to-right from `15 ---> 40` (Label: *2nd, 3rd*)
   - At Level 2: Arrow going left-to-right from `20 ---> 25 ---> 35 ---> 50` (Label: *4th, 5th, 6th, 7th*)

---

## Part 2: Draw the FIFO Queue Box Trace Below the Tree

Draw an open-ended horizontal pipe/box labeled **FIFO Queue (`Front` on left, `Rear` on right)** for each step:

- **Init:** `Front -> [ 10 ] <- Rear` *(Root enqueued)*
- **Step 1 (Dequeue 10, Enqueue 15, 40):** `Front -> [ 15 | 40 ] <- Rear`  | **Visited:** `10`
- **Step 2 (Dequeue 15, Enqueue 20, 25):** `Front -> [ 40 | 20 | 25 ] <- Rear` | **Visited:** `10, 15`
- **Step 3 (Dequeue 40, Enqueue 35, 50):** `Front -> [ 20 | 25 | 35 | 50 ] <- Rear` | **Visited:** `10, 15, 40`
- **Step 4 (Dequeue 20, leaf):** `Front -> [ 25 | 35 | 50 ] <- Rear` | **Visited:** `10, 15, 40, 20`
- **Step 5 (Dequeue 25, leaf):** `Front -> [ 35 | 50 ] <- Rear` | **Visited:** `10, 15, 40, 20, 25`
- **Step 6 (Dequeue 35, leaf):** `Front -> [ 50 ] <- Rear` | **Visited:** `10, 15, 40, 20, 25, 35`
- **Step 7 (Dequeue 50, leaf):** `Front -> [ EMPTY ] <- Rear` | **Final Output:** `10 -> 15 -> 40 -> 20 -> 25 -> 35 -> 50`

