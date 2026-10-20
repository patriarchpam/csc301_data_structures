# Diagram Guide: Reorder List (LeetCode 143)

Draw these by hand (AI diagrams are not allowed). Use graph paper or a ruler.

## How to draw a node
A box split in two: `[ val | • ]`. The dot is the `next` arrow. The last node's dot has an "X" (null).
Use one pen colour per pointer: slow = blue, fast = red, prev = green, curr = orange, first/second = purple.
Write the pointer names under the node they point to.

## Example A: 1 -> 2 -> 3 -> 4 -> 5

**Frame 1 - Original list.** Five boxes joined by arrows, X after 5. Label "head" above 1.

**Frame 2 - Find the middle** (draw one mini-row per step)
- Start: slow = 1, fast = 1
- After loop pass 1: slow = 2, fast = 3
- After loop pass 2: slow = 3, fast = 5
- Stop: fast.next is null. Circle node 3 as the middle.

**Frame 3 - Cut the list.** Cross out the arrow 3 -> 4 and write `slow.next = null`.
You now have two lists: `1 -> 2 -> 3 -> X` and `4 -> 5 -> X`.

**Frame 4 - Reverse the second half** (one row per pass)
- Start: prev = null, curr = 4
- Pass 1: save next = 5; flip 4's arrow to null; prev = 4, curr = 5
- Pass 2: save next = null; flip 5's arrow to 4; prev = 5, curr = null
- Result: `5 -> 4 -> X`. Mark 5 as "second".

**Frame 5 - Merge** (one row per pass)
- Pass 1: first = 1, second = 5. Draw 1 -> 5 and 5 -> 2. Now first = 2, second = 4.
- Pass 2: first = 2, second = 4. Draw 2 -> 4 and 4 -> 3. Now first = 3, second = null. Stop.

**Frame 6 - Final answer:** `1 -> 5 -> 2 -> 4 -> 3 -> X`

## Example B (even length): 1 -> 2 -> 3 -> 4
- Middle: slow = 2 (fast stops at 3 because fast.next.next is null)
- Cut: `1 -> 2` and `3 -> 4`; reverse second: `4 -> 3`
- Merge: `1 -> 4 -> 2 -> 3`

## Tips for marks
- Add a short caption under each frame matching the step in the code comments.
- Redraw arrows after every pointer change; cross out old arrows, don't erase.
- Include a small box showing the three steps and the O(n) time, O(1) space result.
