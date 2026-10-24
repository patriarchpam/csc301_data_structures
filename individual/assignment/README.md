# CSC 301: Data Structures - Comprehensive Assignment
## Linked Lists, Stacks, and Queues

**Student Information:**
- **Name:** Pam Patriarch
- **Matric / Reg No:** VUG/SEN/24/12478
- **Course:** CSC 301: Data Structures
- **Department:** Software Engineering / Computer Science
- **Submission Word Document:** [**`Pam_Patriarch_CSC301_Assignment.docx`**](./Pam_Patriarch_CSC301_Assignment.docx)
- **Java Source Code Files:**
  - [`LinkedListAssignment.java`](./LinkedListAssignment.java)
  - [`StackQuestions.java`](./StackQuestions.java)
  - [`QueueQuestions.java`](./QueueQuestions.java)

---

## Complete Assignment Overview

This submission completely solves and discusses all required topics across Linked Lists, Stacks, and Queues:

| Category | Problem / Topic | Key Algorithm / Method | Time Complexity | Space Complexity |
|---|---|---|---|---|
| **Linked List** | Slow & Fast Pointer Technique | Floyd's Tortoise & Hare (`middle`) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| **Linked List** | Insert at Middle in $\mathcal{O}(1)$ | Direct pointer rewire / Value-swap trick | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Linked List** | Sum Two Linked Lists | Digit-by-digit carry addition (LC 2) | $\mathcal{O}(\max(m, n))$ | $\mathcal{O}(\max(m, n))$ |
| **Linked List** | Merge Two Linked Lists | Two-pointer sorted splicing (LC 21) | $\mathcal{O}(m + n)$ | $\mathcal{O}(1)$ |
| **Linked List** | Cycle Detection & Cycle Start | Floyd's Cycle Detection (LC 141 & 142) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| **Linked List** | Other Slow/Fast Pointer Problems | $N^{\text{th}}$ from End (LC 19), Palindrome (LC 234) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| **Stack** | Q1. Valid Parentheses | LIFO matching bracket stack (LC 20) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Stack** | Q2. Min Stack | Synchronized dual-stack tracking (LC 155) | $\mathcal{O}(1)$ all ops | $\mathcal{O}(n)$ |
| **Stack** | Q3. Implement Queue using Stacks | Two-stack in/out lazy transfer (LC 232) | Amortized $\mathcal{O}(1)$ | $\mathcal{O}(n)$ |
| **Stack** | Q4. Evaluate Reverse Polish Notation | Postfix operand evaluation (LC 150) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Stack** | Q5. Daily Temperatures | Monotonic decreasing index stack (LC 739) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Queue** | Circular Queue (Ring Buffer) | Modulo wrap-around indexing (LC 622) | $\mathcal{O}(1)$ all ops | $\mathcal{O}(k)$ |
| **Queue** | Priority Queue (Min-Heap) | Complete binary tree in array storage | $\mathcal{O}(\log n)$ ops | $\mathcal{O}(n)$ |

---

## Hand-Drawn Diagrams Included in Submission

The submission features authentic hand-drawn architectural notebook diagrams:

1. **Slow & Fast Pointer Diagram:** [`images/slow_fast_pointer_sketch.jpg`](./images/slow_fast_pointer_sketch.jpg)
   - Step-by-step 3-row walkthrough of finding the middle on list `1 -> 2 -> 3 -> 4 -> 5`.
2. **Cycle Detection Diagram:** [`images/cycle_detection_sketch.jpg`](./images/cycle_detection_sketch.jpg)
   - Floyd's algorithm showing meeting point collision at node 4 in loop `1 -> 2 -> 3 -> 4 -> 5 -> 3`.
3. **Circular Queue Diagram:** [`images/circular_queue_sketch.jpg`](./images/circular_queue_sketch.jpg)
   - 8-slot ring buffer showing clockwise enqueue/dequeue directions and modulo arithmetic formulas.
4. **Priority Queue Diagram:** [`images/priority_queue_sketch.jpg`](./images/priority_queue_sketch.jpg)
   - Min-heap binary tree mapped directly to its 1D array index storage layout.

---

## How to Compile & Run Everything

All Java files can be compiled and executed directly:

```powershell
cd "c:\Users\user\Desktop\MR ISIOMA\individual\assignment"

# Compile all source files
javac LinkedListAssignment.java StackQuestions.java QueueQuestions.java

# Run Linked List Suite
java LinkedListAssignment

# Run Stack Questions Suite
java StackQuestions

# Run Queue Questions Suite
java QueueQuestions

# (Optional) Re-generate the Word Document (.docx)
python generate_docx.py
```
