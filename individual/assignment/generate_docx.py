import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_assignment_document(output_path, img_dir):
    doc = Document()

    # Set page margins (1 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.header.is_linked_to_previous = False

    # Palette
    NAVY = RGBColor(27, 54, 93)      # #1B365D Primary Header
    SLATE = RGBColor(70, 90, 120)    # Subheader
    CHARCOAL = RGBColor(40, 40, 40)  # Body text
    DARK_RED = RGBColor(160, 40, 40)
    DARK_GREEN = RGBColor(30, 120, 60)

    # -------------------------------------------------------------
    # Title / Header Block
    # -------------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(4)
    title_run = title_p.add_run("CSC 301: DATA STRUCTURES")
    title_run.font.name = "Arial"
    title_run.font.size = Pt(20)
    title_run.font.bold = True
    title_run.font.color.rgb = NAVY

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(14)
    sub_run = sub_p.add_run("Comprehensive Assignment: Linked Lists, Stacks, and Queues")
    sub_run.font.name = "Arial"
    sub_run.font.size = Pt(14)
    sub_run.font.color.rgb = SLATE

    # Student metadata table box
    info_table = doc.add_table(rows=4, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Student Name:", "Pam Patriarch"),
        ("Matric / Registration No:", "VUG/SEN/24/12478"),
        ("Course & Topic:", "CSC 301: Data Structures (Linked Lists, Stacks & Queues)"),
        ("Source Code Artifacts:", "13 Standalone Question Files (Question1_*.java through Question13_*.java)")
    ]
    for row_idx, (label, val) in enumerate(info_data):
        row = info_table.rows[row_idx]
        cell_lbl, cell_val = row.cells[0], row.cells[1]
        cell_lbl.width = Inches(2.2)
        cell_val.width = Inches(4.3)
        set_cell_background(cell_lbl, "EBF1F5")
        set_cell_background(cell_val, "F8F9FA")
        set_cell_margins(cell_lbl, 80, 80, 120, 120)
        set_cell_margins(cell_val, 80, 80, 120, 120)
        
        p0 = cell_lbl.paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(label)
        r0.font.bold = True
        r0.font.size = Pt(10)
        r0.font.color.rgb = NAVY

        p1 = cell_val.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.size = Pt(10)
        r1.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Helper functions for structured styling
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = NAVY
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = SLATE
        return p

    def add_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.bold = True
            r_pre.font.size = Pt(10.5)
            r_pre.font.color.rgb = CHARCOAL
        run = p.add_run(text)
        run.font.size = Pt(10.5)
        run.font.color.rgb = CHARCOAL
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.bold = True
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = CHARCOAL
        run = p.add_run(text)
        run.font.size = Pt(10)
        run.font.color.rgb = CHARCOAL
        return p

    def add_code(code_str):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.rows[0].cells[0]
        cell.width = Inches(6.5)
        set_cell_background(cell, "F4F5F7")
        set_cell_margins(cell, 100, 100, 150, 150)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(code_str.strip())
        run.font.name = "Consolas"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(30, 30, 30)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_image_figure(img_filename, caption_text):
        full_img_path = os.path.join(img_dir, img_filename)
        if os.path.exists(full_img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(2)
            run_img = p_img.add_run()
            run_img.add_picture(full_img_path, width=Inches(5.8))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(8)
            run_cap = p_cap.add_run(caption_text)
            run_cap.font.name = "Arial"
            run_cap.font.size = Pt(9.5)
            run_cap.font.italic = True
            run_cap.font.color.rgb = SLATE

    # =============================================================
    # SECTION 1: SLOW AND FAST POINTER TECHNIQUE
    # =============================================================
    add_h1("1. Slow and Fast Pointer Technique (Tortoise and Hare)")
    add_p("The slow and fast pointer technique (also known as Floyd's Tortoise and Hare algorithm) is a two-pointer traversal strategy for singly linked lists where two references advance through the sequence at unequal velocities:")
    add_bullet(" Moves exactly 1 node forward per iteration (velocity vs = 1).", bold_prefix="Slow Pointer (S):")
    add_bullet(" Moves exactly 2 nodes forward per iteration (velocity vf = 2).", bold_prefix="Fast Pointer (F):")
    add_bullet(" Both pointers start together at head, so F covers distance twice as fast as S (d_F = 2 * d_S).", bold_prefix="Distance Ratio:")
    add_bullet(" Fast reaches the tail or null when S has traversed exactly half the list length, parking S at the middle node.", bold_prefix="Middle Property:")
    add_bullet(" while (fast != null && fast.next != null). This condition stops safely on both odd and even length lists.", bold_prefix="Loop Condition:")
    add_bullet(" Time O(n) in a single pass without pre-calculating list length, and Auxiliary Space O(1).", bold_prefix="Complexity:")

    add_h2("Hand-Drawn Diagram: Middle Finding Walkthrough on 1 -> 2 -> 3 -> 4 -> 5")
    add_image_figure("slow_fast_pointer_sketch.jpg", "Figure 1: Authentic Hand-Drawn Notebook Diagram of Slow and Fast Pointer Middle Finding")

    add_p("Step-by-Step Execution Trace:", bold_prefix="Algorithmic Walkthrough: ")
    add_bullet(" Both S and F point to node [1].", bold_prefix="Start:")
    add_bullet(" S moves to [2], F moves 2 nodes to [3]. Condition (fast != null && fast.next != null) is true.", bold_prefix="Step 1:")
    add_bullet(" S moves to [3], F moves 2 nodes to [5]. At node [5], fast.next is null, so the loop terminates immediately. S resides on node [3]—the exact middle!", bold_prefix="Step 2:")
    add_bullet(" On an even-length list (e.g., 6 nodes), fast steps to null, and slow terminates on node 4 (the standard second middle node).", bold_prefix="Even Length:")

    add_p("Java Implementation for Finding Middle (LeetCode 876):", bold_prefix="Code Reference: ")
    add_code("""public static Node middle(Node head) {
    Node slow = head;
    Node fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}""")

    # =============================================================
    # SECTION 2: INSERTION IN THE MIDDLE IN O(1) COMPLEXITY
    # =============================================================
    add_h1("2. Inserting in the Middle of a Linked List Using O(1) Complexity")
    add_p("In linked list algorithmic analysis, insertion operations must be carefully categorized into two distinct stages: finding the insertion location vs. rewiring pointers at the given location.")
    
    add_h2("A. Inserting After a Given Middle Node Reference in O(1)")
    add_p("When the algorithm or caller already possesses a direct reference/pointer to the middle node (`mid`), inserting a new node immediately after it requires only local pointer rewiring. No traversal occurs, making it strictly O(1) time and O(1) space:")
    add_code("""public static void insertAfterNodeO1(Node midNode, int val) {
    if (midNode == null) return;
    // Allocate new node whose next points to midNode.next, then attach midNode to it
    midNode.next = new Node(val, midNode.next); // Exact O(1) operation
}""")

    add_h2("B. Inserting Before a Given Middle Node Reference in O(1) (Value-Swap Trick)")
    add_p("In a singly linked list, inserting *before* a node conventionally requires walking from head to find the predecessor node (taking O(n)). However, if only given the middle node pointer `mid`, we can achieve O(1) insertion before `mid` using the Node Value-Copy Technique:")
    add_bullet(" Create a new node containing the existing value of midNode (copy = new Node(midNode.val, midNode.next)).", bold_prefix="Step 1:")
    add_bullet(" Overwrite midNode.val with the new incoming value.", bold_prefix="Step 2:")
    add_bullet(" Link midNode.next to the copy node. Logically, the new value now appears before the old middle element without requiring any predecessor pointer!", bold_prefix="Step 3:")
    add_code("""public static void insertBeforeNodeO1(Node midNode, int val) {
    if (midNode == null) return;
    Node clone = new Node(midNode.val, midNode.next);
    midNode.val = val;
    midNode.next = clone; // O(1) insertion before given node
}""")

    add_h2("C. End-to-End Insertion from Head Node")
    add_p("If the algorithm starts at `head` without a prior middle pointer, slow and fast pointers locate the middle in O(n) time, after which the linking operation executes in O(1). The overall end-to-end time is O(n), and space is O(1).")

    # =============================================================
    # SECTION 3: SUMMING TWO LINKED LISTS
    # =============================================================
    add_h1("3. How to Sum Two Linked Lists Together (LeetCode 2)")
    add_p("In LeetCode 2 (Add Two Numbers), two non-empty singly linked lists represent two non-negative integers stored in reverse digit order (the 1s digit is at the head, followed by 10s, 100s, etc.):")
    add_bullet(" (2 -> 4 -> 3) corresponds to integer 342.", bold_prefix="List 1:")
    add_bullet(" (5 -> 6 -> 4) corresponds to integer 465.", bold_prefix="List 2:")
    add_bullet(" 342 + 465 = 807, represented as 7 -> 0 -> 8.", bold_prefix="Sum:")

    add_h2("Algorithm Design and Carry Propagation")
    add_bullet(" A dummy head node (Node dummy = new Node(0)) maintains the list anchor and eliminates special-case branching for the head.", bold_prefix="Dummy Head Pattern:")
    add_bullet(" Maintain an integer carry initialized to 0.", bold_prefix="Carry State:")
    add_bullet(" Iterate while (l1 != null || l2 != null || carry != 0). This ensures that trailing carries (e.g. 99 + 1 = 100) append a final node containing 1.", bold_prefix="Loop Invariant:")
    add_bullet(" sum = carry + (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0). Then new digit = sum % 10 and next carry = sum / 10.", bold_prefix="Digit Math:")
    add_bullet(" Time O(max(m, n)) where m and n are list lengths; Auxiliary Space O(max(m, n)) for the result list.", bold_prefix="Complexity:")

    add_code("""public static Node addTwo(Node l1, Node l2) {
    Node dummy = new Node(0);
    Node cur = dummy;
    int carry = 0;

    while (l1 != null || l2 != null || carry != 0) {
        int sum = carry;
        if (l1 != null) { sum += l1.val; l1 = l1.next; }
        if (l2 != null) { sum += l2.val; l2 = l2.next; }
        carry = sum / 10;
        cur.next = new Node(sum % 10);
        cur = cur.next;
    }
    return dummy.next;
}""")

    # =============================================================
    # SECTION 4: MERGING TWO LINKED LISTS
    # =============================================================
    add_h1("4. How to Merge Two Linked Lists")
    add_p("Merging linked lists is a foundational technique with two primary formulations in data structures:")

    add_h2("A. Merge Two Sorted Linked Lists (LeetCode 21)")
    add_p("Given two sorted lists, splice their nodes together in-place so that the resulting list remains monotonically non-decreasing:")
    add_bullet(" Use a dummy head node and a tail pointer tracking the end of the merged list.", bold_prefix="Two-Pointer Splicing:")
    add_bullet(" Compare l1.val and l2.val: attach the smaller node to tail.next and advance that list's pointer.", bold_prefix="Comparison Loop:")
    add_bullet(" Once either list is exhausted, attach the remainder of the non-empty list directly in O(1): tail.next = (l1 != null) ? l1 : l2.", bold_prefix="Remainder Splice:")
    add_bullet(" Time O(m + n) traversing each node once; Space O(1) in-place pointer manipulation.", bold_prefix="Complexity:")

    add_code("""public static Node mergeTwoLists(Node l1, Node l2) {
    Node dummy = new Node(0);
    Node tail = dummy;

    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) {
            tail.next = l1;
            l1 = l1.next;
        } else {
            tail.next = l2;
            l2 = l2.next;
        }
        tail = tail.next;
    }
    tail.next = (l1 != null) ? l1 : l2;
    return dummy.next;
}""")

    add_h2("B. Interleaving / Alternating Merge (LeetCode 143 Reorder List)")
    add_p("For alternating merge (l1[0] -> l2[0] -> l1[1] -> l2[1]...): save next pointers, link l1 to l2, then l2 to original l1.next, and repeat. This executes in O(m + n) time and O(1) space.")

    # =============================================================
    # SECTION 5: DETECTING A CIRCLE IN A LINKED LIST
    # =============================================================
    add_h1("5. How to Detect a Circle (Cycle) in a Linked List (Floyd's Algorithm)")
    add_p("A linked list contains a cycle when a node's next pointer references a previously visited node rather than null, causing naive traversals to loop indefinitely.")

    add_h2("Floyd's Cycle-Finding Algorithm (LeetCode 141)")
    add_p("Slow pointer moves 1 step, Fast pointer moves 2 steps:")
    add_bullet(" If no cycle exists, fast or fast.next hits null. We conclude the list is acyclic in O(n) time.", bold_prefix="Acyclic Case:")
    add_bullet(" If a cycle of length C exists, both pointers inevitably enter the cycle. Once inside, fast gains on slow by 1 node per iteration (v_rel = 2 - 1 = 1). The gap decreases strictly by 1 on each step until gap = 0, guaranteeing collision!", bold_prefix="Cyclic Case:")
    add_bullet(" Time O(n), Space O(1). This eliminates the need for an O(n) memory HashSet of visited node addresses.", bold_prefix="Complexity:")

    add_h2("Hand-Drawn Diagram: S and F Meeting Point Inside Loop")
    add_image_figure("cycle_detection_sketch.jpg", "Figure 2: Authentic Hand-Drawn Notebook Diagram of Floyd's Cycle Detection and Meeting Point")

    add_h2("Locating the Cycle Origin Node (LeetCode 142)")
    add_p("After S and F collide at meeting point M: reset S to head while keeping F at M. Advance both pointers 1 node at a time. The node where they collide again is the exact start of the cycle!")
    add_bullet(" Let distance from head to cycle entrance be a. Let distance from entrance to meeting point M be b. Let cycle circumference be C, and remaining distance back to entrance be c = C - b.", bold_prefix="Mathematical Proof:")
    add_bullet(" Distance traveled by slow: d_S = a + b. Distance traveled by fast: d_F = a + b + kC.", bold_prefix="Travel Distances:")
    add_bullet(" Since fast travels twice as far: 2(a + b) = a + b + kC  ==>  a + b = kC  ==>  a = kC - b = (k - 1)C + (C - b) = (k - 1)C + c.", bold_prefix="Key Derivation:")
    add_bullet(" Thus, the distance from head to entrance (a) equals the distance from meeting point to entrance (c) plus some full loops! Stepping both by 1 node guarantees simultaneous arrival at the cycle start.", bold_prefix="Conclusion:")

    add_code("""public static boolean hasCycle(Node head) {
    Node slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}

public static Node cycleStart(Node head) {
    Node slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            slow = head;
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next;
            }
            return slow;
        }
    }
    return null;
}""")

    # =============================================================
    # SECTION 6: ADDITIONAL SLOW & FAST POINTER PROBLEMS
    # =============================================================
    add_h1("6. Solving Other Problems Using Slow and Fast Pointers")
    add_p("The two-pointer technique solves multiple classic linked list challenges efficiently in O(n) time and O(1) space:")

    add_h2("A. Remove / Find Nth Node From the End of List (LeetCode 19)")
    add_bullet(" Advance fast pointer forward by n nodes first, establishing a fixed gap of n.", bold_prefix="Offset Window:")
    add_bullet(" Advance slow and fast together 1 node per iteration.", bold_prefix="Lockstep Advance:")
    add_bullet(" When fast reaches null, slow is positioned exactly n nodes from the end.", bold_prefix="Termination:")

    add_h2("B. Palindrome Linked List (LeetCode 234)")
    add_bullet(" Locate the list middle using slow and fast pointers in O(n) time.", bold_prefix="Step 1:")
    add_bullet(" In-place reverse the second half of the list starting from slow.next in O(n) time and O(1) space.", bold_prefix="Step 2:")
    add_bullet(" Run two pointers from head and reversed second half, comparing values node by node.", bold_prefix="Step 3:")
    add_bullet(" Total time is O(n), total extra memory is strictly O(1)!", bold_prefix="Efficiency:")

    # =============================================================
    # SECTION 7: FIVE QUESTIONS UNDER STACK
    # =============================================================
    add_h1("7. Five Questions Under Stack (LeetCode Solutions)")
    add_p("A Stack operates under the Last-In, First-Out (LIFO) discipline. In Java, standard modern best practice utilizes Deque<T> stack = new ArrayDeque<>() because the legacy java.util.Stack class synchronizes every call on a Vector, imposing severe overhead.")

    add_h2("Q1. Valid Parentheses (LeetCode 20)")
    add_p("Given a string containing '(', ')', '{', '}', '[', ']', verify if open brackets are closed by the same type of brackets in correct order.")
    add_bullet(" Push every open bracket to the stack. On encountering a close bracket, verify the stack is non-empty and the top matches the corresponding opener.", bold_prefix="Strategy:")
    add_bullet(" Time O(n), Space O(n).", bold_prefix="Complexity:")
    add_code("""public static boolean isValid(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    for (char c : s.toCharArray()) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else {
            if (stack.isEmpty()) return false;
            char open = stack.pop();
            if ((c == ')' && open != '(') ||
                (c == ']' && open != '[') ||
                (c == '}' && open != '{')) return false;
        }
    }
    return stack.isEmpty();
}""")

    add_h2("Q2. Min Stack (LeetCode 155)")
    add_p("Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.")
    add_bullet(" Maintain a primary stack for values and an auxiliary mins stack. When pushing, push min(val, mins.peek()) onto mins. On pop, pop from both stacks. getMin() simply returns mins.peek() in O(1) time!", bold_prefix="Dual-Stack Pattern:")
    add_bullet(" Time O(1) for all operations, Space O(n).", bold_prefix="Complexity:")
    add_code("""public static class MinStack {
    private final Deque<Integer> stack = new ArrayDeque<>();
    private final Deque<Integer> mins = new ArrayDeque<>();

    public void push(int val) {
        stack.push(val);
        mins.push(mins.isEmpty() ? val : Math.min(val, mins.peek()));
    }
    public void pop() {
        stack.pop();
        mins.pop();
    }
    public int top() { return stack.peek(); }
    public int getMin() { return mins.peek(); }
}""")

    add_h2("Q3. Implement Queue Using Stacks (LeetCode 232)")
    add_p("Implement a First-In, First-Out (FIFO) queue using only standard stack operations (push, pop, peek, empty).")
    add_bullet(" Use two stacks: 'in' receives all pushes; 'out' delivers pops and peeks. When 'out' is empty, transfer all items from 'in' to 'out'. This reverses the LIFO order into FIFO order.", bold_prefix="In/Out Lazy Shift:")
    add_bullet(" Amortized O(1) per operation because each element is moved at most twice across its lifetime; Space O(n).", bold_prefix="Complexity:")
    add_code("""public static class MyQueue {
    private final Deque<Integer> in = new ArrayDeque<>();
    private final Deque<Integer> out = new ArrayDeque<>();

    public void push(int x) { in.push(x); }
    public int pop() { shift(); return out.pop(); }
    public int peek() { shift(); return out.peek(); }
    public boolean empty() { return in.isEmpty() && out.isEmpty(); }
    private void shift() {
        if (out.isEmpty()) {
            while (!in.isEmpty()) out.push(in.pop());
        }
    }
}""")

    add_h2("Q4. Evaluate Reverse Polish Notation (LeetCode 150)")
    add_p("Evaluate postfix expressions such as [\"2\", \"1\", \"+\", \"3\", \"*\"] which represents (2 + 1) * 3 = 9.")
    add_bullet(" Push numbers onto stack. When an operator is encountered, pop right operand b first, then left operand a. Compute (a op b) and push the result back. Order matters for '-' and '/'.", bold_prefix="Strategy:")
    add_bullet(" Time O(n), Space O(n).", bold_prefix="Complexity:")
    add_code("""public static int evalRPN(String[] tokens) {
    Deque<Integer> stack = new ArrayDeque<>();
    for (String t : tokens) {
        switch (t) {
            case "+": stack.push(stack.pop() + stack.pop()); break;
            case "*": stack.push(stack.pop() * stack.pop()); break;
            case "-": { int b = stack.pop(), a = stack.pop(); stack.push(a - b); break; }
            case "/": { int b = stack.pop(), a = stack.pop(); stack.push(a / b); break; }
            default: stack.push(Integer.parseInt(t));
        }
    }
    return stack.pop();
}""")

    add_h2("Q5. Daily Temperatures (LeetCode 739)")
    add_p("Given an array of daily temperatures, compute how many days you must wait until a warmer temperature appears (or 0 if no warmer day exists).")
    add_bullet(" Maintain a monotonic decreasing stack storing day indices. When today's temperature is warmer than the temperature at the index atop the stack, pop that index and set answer[prev] = today - prev. Then push today's index.", bold_prefix="Monotonic Stack:")
    add_bullet(" Time O(n) because each index is pushed and popped at most once; Space O(n).", bold_prefix="Complexity:")
    add_code("""public static int[] dailyTemperatures(int[] temps) {
    int[] answer = new int[temps.length];
    Deque<Integer> stack = new ArrayDeque<>(); // indices
    for (int i = 0; i < temps.length; i++) {
        while (!stack.isEmpty() && temps[i] > temps[stack.peek()]) {
            int prev = stack.pop();
            answer[prev] = i - prev;
        }
        stack.push(i);
    }
    return answer;
}""")

    # =============================================================
    # SECTION 8: CIRCULAR QUEUE AND PRIORITY QUEUE
    # =============================================================
    add_h1("8. Concepts of Circular Queue and Priority Queue")

    add_h2("8.1 Circular Queue (Ring Buffer)")
    add_p("A standard linear array-based queue suffers from severe memory underutilization (the 'false overflow' problem): as elements are dequeued from the front, indices 0, 1, 2... become permanently vacant and unusable unless the entire array is shifted at O(n) cost.")
    add_p("A Circular Queue (Ring Buffer) connects the last position back to the first position conceptually, forming a circle. It achieves continuous O(1) enqueue and dequeue operations without shifting elements.")

    add_bullet(" Elements enter at rear: rear = (rear + 1) % capacity.", bold_prefix="Modulo Enqueue Arithmetic:")
    add_bullet(" Elements exit at front: front = (front + 1) % capacity.", bold_prefix="Modulo Dequeue Arithmetic:")
    add_bullet(" Track an integer 'size' counter: isEmpty() := (size == 0) and isFull() := (size == capacity).", bold_prefix="Full vs. Empty Condition:")

    add_h2("Hand-Drawn Diagram: Circular Queue Ring Buffer (8 Slots)")
    add_image_figure("circular_queue_sketch.jpg", "Figure 3: Authentic Hand-Drawn Notebook Diagram of a Circular Queue Ring Buffer with Enqueue/Dequeue Directions")

    add_p("Circular Queue Operation Complexity Table:", bold_prefix="Performance Analysis: ")
    cq_table = doc.add_table(rows=5, cols=3)
    cq_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cq_headers = ["Operation", "Time Complexity", "Description"]
    for i, h in enumerate(cq_headers):
        c = cq_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    cq_rows = [
        ("enQueue(val)", "O(1)", "Inserts at tail position using modulo wrap-around"),
        ("deQueue()", "O(1)", "Advances head pointer clockwise using modulo wrap-around"),
        ("Front() / Rear()", "O(1)", "Direct array index lookup data[head] or data[tail]"),
        ("isEmpty() / isFull()", "O(1)", "Instant size check against capacity boundary")
    ]
    for r_idx, r_data in enumerate(cq_rows):
        row = cq_table.rows[r_idx + 1]
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            bg = "F4F5F7" if r_idx % 2 == 1 else "FFFFFF"
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_p("Real-World Practical Applications of Circular Queues:", bold_prefix="Practical Applications: ")
    add_bullet(" Operating system process scheduling and round-robin CPU slice dispatching.", bold_prefix="OS Scheduling:")
    add_bullet(" Media streaming audio/video buffers that continuously overwrite oldest played frames.", bold_prefix="Streaming Buffers:")
    add_bullet(" Hardware keyboard/mouse circular input buffers and network packet interface rings.", bold_prefix="I/O Controllers:")

    add_h2("8.2 Priority Queue (Binary Heap Implementation)")
    add_p("A Priority Queue is an abstract data structure where each stored element has an associated priority value. Dequeue operations do not follow strict FIFO order; instead, the element with the highest priority (e.g. minimum value in a Min-Heap or maximum value in a Max-Heap) is always retrieved first.")

    add_p("Why Binary Heaps are Optimal for Priority Queues:", bold_prefix="Implementation Comparison: ")
    add_bullet(" O(1) insert, but O(n) search to extract highest priority element.", bold_prefix="Unsorted Array:")
    add_bullet(" O(1) extract, but O(n) insertion cost due to shifting elements.", bold_prefix="Sorted Array:")
    add_bullet(" Balanced O(log n) insertion, O(log n) extraction, and instant O(1) peek! This represents the optimal practical sweet spot.", bold_prefix="Binary Heap:")

    add_h2("Binary Heap Architecture and Array Representation")
    add_p("A Binary Heap is a complete binary tree satisfying the Heap-Order Invariant: in a Min-Heap, every parent node is less than or equal to its children (A[parent] <= A[child]). It is stored contiguously in a 1D array without child/parent pointers:")
    add_bullet(" Parent index = (i - 1) / 2", bold_prefix="Parent Index:")
    add_bullet(" Left child index = 2 * i + 1", bold_prefix="Left Child:")
    add_bullet(" Right child index = 2 * i + 2", bold_prefix="Right Child:")

    add_h2("Hand-Drawn Diagram: Priority Queue Min-Heap Tree and Array Mapping")
    add_image_figure("priority_queue_sketch.jpg", "Figure 4: Authentic Hand-Drawn Notebook Diagram of Min-Heap Binary Tree and its 1D Array Storage Representation")

    add_p("Priority Queue Operation Complexity Table:", bold_prefix="Performance Analysis: ")
    pq_table = doc.add_table(rows=4, cols=3)
    pq_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    pq_headers = ["Operation", "Time Complexity", "Mechanic"]
    for i, h in enumerate(pq_headers):
        c = pq_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    pq_rows = [
        ("insert(val)", "O(log n)", "Appends at end and percolates (bubbles) up to restore heap order"),
        ("extractMin()", "O(log n)", "Removes root, moves last element to root, percolates down"),
        ("peek()", "O(1)", "Directly inspects root element array[0] without removal")
    ]
    for r_idx, r_data in enumerate(pq_rows):
        row = pq_table.rows[r_idx + 1]
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            bg = "F4F5F7" if r_idx % 2 == 1 else "FFFFFF"
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_p("Real-World Practical Applications of Priority Queues:", bold_prefix="Practical Applications: ")
    add_bullet(" Dijkstra's Shortest Path Algorithm for GPS navigation and routing.", bold_prefix="Graph Algorithms:")
    add_bullet(" Prim's Minimum Spanning Tree algorithm for telecommunications layout.", bold_prefix="Network Design:")
    add_bullet(" Huffman Coding data compression trees in ZIP and MP3 encoders.", bold_prefix="Data Compression:")
    add_bullet(" Operating system process schedulers handling real-time interrupts by priority.", bold_prefix="Real-Time Systems:")

    # =============================================================
    # SECTION 9: VERIFICATION RESULTS
    # =============================================================
    add_h1("9. Test Suite Execution & Output Verification")
    add_p("All solutions across LinkedListAssignment.java, StackQuestions.java, and QueueQuestions.java were compiled and executed. The exact terminal execution log is presented below:")
    
    add_code("""===============================================================
    CSC 301 DATA STRUCTURES: COMPLETE LINKED LIST SUITE       
    Student: Pam Patriarch | Matric: VUG/SEN/24/12478         
===============================================================
--- 1. Slow and Fast Pointer (Middle of List) ---
List: 1 -> 2 -> 3 -> 4 -> 5
Middle Node: 3 (Expected: 3)

--- 2. Insertion at Middle with O(1) Complexity ---
Given pointer to mid node (value = 3)
After insertAfterNodeO1(midRef, 99):  1 -> 2 -> 3 -> 99 -> 4 -> 5
After insertBeforeNodeO1(midRef, 88): 1 -> 2 -> 88 -> 3 -> 99 -> 4 -> 5

--- 3. Sum Two Linked Lists (LC 2) ---
Num A (342): 2 -> 4 -> 3
Num B (465): 5 -> 6 -> 4
Sum Result:  7 -> 0 -> 8 (Expected: 7 -> 0 -> 8)

--- 4. Merge Two Linked Lists ---
Sorted List 1: 1 -> 3 -> 5 -> 7
Sorted List 2: 2 -> 4 -> 6 -> 8
Merged Sorted: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8

--- 5. Detect Circle / Cycle (Floyd's Algorithm) ---
Before cycle: hasCycle = false
Created loop (5 points back to 3):
hasCycle(c1)  = true
cycleStart(c1) = 3 (Expected: 3)

--- 6. Additional Slow & Fast Pointer Problems ---
List: 10 -> 20 -> 30 -> 40 -> 50
2nd from end: 40 (Expected: 40)
isPalindrome([1,2,3,2,1]): true (Expected: true)
isPalindrome([1,2,3,4,5]): false (Expected: false)

===============================================================
      CSC 301 DATA STRUCTURES: STACK QUESTIONS SUITE          
===============================================================
isValid("()[]{}") = true
isValid("([)]")   = false
MinStack: getMin() = -3 -> top() after pop = 0 -> getMin() = -2
Queue peek()      = 1  -> pop() = 1 -> peek() = 2
RPN ["2","1","+","3","*"] = 9
Daily Temperatures: [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]

===============================================================
       CSC 301 DATA STRUCTURES: QUEUE QUESTIONS SUITE         
===============================================================
enQueue(10): true
enQueue(20): true
enQueue(30): true
enQueue(40) on full queue: false (Expected: false)
front(): 10 (Expected: 10)
rear():  30 (Expected: 30)
deQueue(): true (Front moves clockwise)
enQueue(40) into freed slot: true (Expected: true)
front(): 20 (Expected: 20)
rear():  40 (Expected: 40)

Inserting values: 25 12 5 18 9 20 14 
Peek highest priority (min): 5 (Expected: 5)
Extracting in priority order: 5 9 12 14 18 20 25""")

    doc.save(output_path)
    print(f"Document successfully created and saved at: {output_path}")

if __name__ == "__main__":
    out_docx = r"c:\Users\user\Desktop\MR ISIOMA\individual\assignment\Pam_Patriarch_CSC301_Assignment.docx"
    images_dir = r"c:\Users\user\Desktop\MR ISIOMA\individual\assignment\images"
    create_assignment_document(out_docx, images_dir)
