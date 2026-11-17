import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# Color Palette
NAVY = RGBColor(27, 54, 93)       # #1B365D Primary Header
SLATE = RGBColor(60, 82, 112)     # Subheader
CHARCOAL = RGBColor(35, 35, 35)   # Body text
MUTED = RGBColor(100, 110, 125)   # Captions / notes

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=130, right=130):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="D0D7DE", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def add_h1(doc, text):
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

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = SLATE
    return p

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = CHARCOAL
    return p

def add_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.bold = True
        r_pre.font.size = Pt(10.5)
        r_pre.font.color.rgb = CHARCOAL
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10.5)
    run.font.color.rgb = CHARCOAL
    return p

def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.bold = True
        r_pre.font.size = Pt(10)
        r_pre.font.color.rgb = CHARCOAL
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.font.color.rgb = CHARCOAL
    return p

def add_code_block(doc, code_str):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, color="CBD5E1", sz="6")
    cell = tbl.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, "F4F6F8")
    set_cell_margins(cell, 90, 90, 130, 130)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.08
    run = p.add_run(code_str.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.8)
    run.font.color.rgb = RGBColor(25, 25, 25)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_styled_table(doc, headers, rows_data, col_widths=None):
    tbl = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, color="C4CDD5", sz="4")

    hdr_row = tbl.rows[0]
    for idx, h_text in enumerate(headers):
        cell = hdr_row.cells[idx]
        if col_widths:
            cell.width = Inches(col_widths[idx])
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, 75, 75, 95, 95)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = "Arial"
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    for r_idx, row_vals in enumerate(rows_data):
        row = tbl.rows[r_idx + 1]
        bg_hex = "FFFFFF" if r_idx % 2 == 0 else "F4F7FA"
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            if col_widths:
                cell.width = Inches(col_widths[c_idx])
            set_cell_background(cell, bg_hex)
            set_cell_margins(cell, 65, 65, 95, 95)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.1
            r = p.add_run(str(val))
            r.font.name = "Arial"
            r.font.size = Pt(9.5)
            if c_idx == 0:
                r.font.bold = True
            r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return tbl

def add_image_figure(doc, img_path, caption_text, width_inches=4.8):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(2)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_inches))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(caption_text)
        run_cap.font.name = "Arial"
        run_cap.font.size = Pt(9)
        run_cap.font.italic = True
        run_cap.font.color.rgb = MUTED


# ==============================================================================
# QUESTION 1
# ==============================================================================
def write_question_1(doc, img_dir):
    add_h1(doc, "QUESTION 1: CALLING A RECURSIVE FUNCTION INSIDE A FOR LOOP")
    add_p(doc, "Question: When you call a recursive function in a for loop, what happens? Use String Permutation and 2 more as examples. Include diagram.", bold_prefix="Prompt: ")

    add_h2(doc, "1.1 What Happens When Recursion is Called Inside a For Loop?")
    add_p(
        doc,
        "When a recursive function is called inside a for loop, the algorithm combines horizontal iteration (across loop choices at the current level) with vertical recursion (diving deeper into subproblems). This mechanism is known as recursion with branching (or multi-way / tree recursion) and forms the foundation of backtracking and exhaustive state-space search:"
    )
    add_bullet(doc, " The outer for loop begins iterating over a sequence of available choices at the current depth.", bold_prefix="1. Loop Initiation:")
    add_bullet(doc, " On iteration i = 0, the function invokes itself recursively. The parent loop pauses at i = 0 and its local state is pushed onto the Call Stack while the child call starts its own for loop from the beginning.", bold_prefix="2. Depth-First Suspension:")
    add_bullet(doc, " Each child call spawns further recursive calls inside its own loop, creating a multi-branching Recursion Tree where the loop controls the width (branching factor) and the recursion controls the depth.", bold_prefix="3. Multi-Way Branching:")
    add_bullet(doc, " Deepest calls eventually hit the base condition and return to their caller.", bold_prefix="4. Base Condition Termination:")
    add_bullet(doc, " Once a recursive call returns, the paused parent for loop resumes, advances to the next iteration (i + 1), and explores the next branch until all loop iterations at all levels complete.", bold_prefix="5. Backtracking & Next Iteration:")

    # Example 1: String Permutation
    add_h2(doc, "1.2 Example 1: String Permutation (Arranging Letters of \"ABC\")")
    add_p(
        doc,
        "String permutation arranges the characters of a string in all possible orders (for a string of length n, there are n! permutations). A recursive function uses a for loop to pick each character one by one as the current prefix character, and then recursively calls itself to permute the remaining characters."
    )
    add_p(doc, "For the word \"ABC\", the 3! = 6 possible permutations generated are:")
    for perm in ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]:
        add_bullet(doc, perm)

    add_image_figure(
        doc,
        os.path.join(img_dir, "q1_img1.jpg"),
        "Figure 1.1: Hand-Drawn Recursion Tree Diagram for String Permutations of \"ABC\"",
        width_inches=4.8
    )

    add_p(doc, "Java Implementation of String Permutation (Recursion inside a For Loop):", bold_prefix="Code Example 1: ")
    add_code_block(doc, """public static void permute(String remaining, String prefix) {
    // Base Condition: When no characters remain, print the completed permutation
    if (remaining.length() == 0) {
        System.out.println(prefix);
        return;
    }
    // For loop picks each character at index i and recurses on the rest
    for (int i = 0; i < remaining.length(); i++) {
        char ch = remaining.charAt(i);
        String rest = remaining.substring(0, i) + remaining.substring(i + 1);
        permute(rest, prefix + ch); // Recursive call inside the for loop
    }
}""")

    # Example 2: Finding Subsets (Power Set)
    add_h2(doc, "1.3 Example 2: Finding Subsets (Power Set Generation)")
    add_p(
        doc,
        "A subset is a group of elements selected from a given set. A recursive function uses a for loop to iterate through candidate elements starting from the current index, adding an element to the current subset and calling itself recursively to explore all larger subsets that include that element."
    )
    add_p(doc, "For the set {A, B}, the four possible subsets are:")
    add_bullet(doc, " {} — Nothing selected (empty subset)")
    add_bullet(doc, " {A} — Only A selected")
    add_bullet(doc, " {B} — Only B selected")
    add_bullet(doc, " {A, B} — Both A and B selected")
    add_p(doc, "Similarly, for a 3-element set {A, B, C}, there are 2^3 = 8 subsets ({}, {A}, {B}, {C}, {A,B}, {A,C}, {B,C}, {A,B,C}), as illustrated in the hand-drawn decision tree below:")

    add_image_figure(
        doc,
        os.path.join(img_dir, "q1_img2.jpg"),
        "Figure 1.2: Hand-Drawn Recursion Tree Diagram for Finding All Subsets of {A, B, C}",
        width_inches=4.8
    )

    add_p(doc, "Java Implementation of Finding Subsets (Recursion inside a For Loop):", bold_prefix="Code Example 2: ")
    add_code_block(doc, """public static void generateSubsets(char[] set, int index, String currentSubset) {
    System.out.println("{ " + currentSubset + "}");
    // For loop explores including each remaining element from 'index' onward
    for (int i = index; i < set.length; i++) {
        generateSubsets(set, i + 1, currentSubset + set[i] + " ");
    }
}""")

    # Example 3: Depth-First Search (DFS) on a Tree / Graph
    add_h2(doc, "1.4 Example 3: Depth-First Search (DFS) on a Tree / Graph")
    add_p(
        doc,
        "Depth-First Search (DFS) is an algorithm used to traverse or search nodes in a tree or graph. At each node, the recursive function uses a for loop to iterate over all adjacent child/neighbor nodes. Whenever it finds an unvisited neighbor, it calls itself recursively to plunge deep down that branch until a leaf/dead-end is reached before the loop moves to the next sibling branch."
    )

    add_image_figure(
        doc,
        os.path.join(img_dir, "q1_img3.jpg"),
        "Figure 1.3: Hand-Drawn Diagram of Multi-Branch Tree / Graph Explored via Recursive DFS",
        width_inches=4.8
    )

    add_p(doc, "Java Implementation of Recursive DFS Inside a For Loop:", bold_prefix="Code Example 3: ")
    add_code_block(doc, """public static void dfs(int node, List<List<Integer>> adjList, boolean[] visited) {
    visited[node] = true;
    System.out.print(node + " ");

    // For loop iterates over every neighbor of the current node
    for (int neighbor : adjList.get(node)) {
        if (!visited[neighbor]) {
            dfs(neighbor, adjList, visited); // Recursive call inside for loop
        }
    }
}""")


# ==============================================================================
# QUESTION 2
# ==============================================================================
def write_question_2(doc, img_dir):
    add_h1(doc, "QUESTION 2: EXPLAIN BINARY SEARCH TREE (BST) & TRAVERSALS")
    add_p(
        doc,
        "Question: Explain Binary Search Tree (BST): (I) Draw the diagram, (II) Use recursive algorithm to explain, (III) Explain (a) In-order traversal, (b) Pre-order traversal, and (c) Post-order traversal.",
        bold_prefix="Prompt: "
    )

    add_h2(doc, "2.1 What is a Binary Search Tree (BST)?")
    add_p(
        doc,
        "A Binary Search Tree (BST) is a hierarchical, node-based binary tree data structure in which every node has at most two children (a left child and a right child) and strictly satisfies the Binary Search Tree Ordering Property (Invariant):"
    )
    add_bullet(doc, " Every node in the left subtree of a node N contains a key strictly less than N's key (Left < Root).", bold_prefix="Left Subtree Property:")
    add_bullet(doc, " Every node in the right subtree of a node N contains a key strictly greater than N's key (Right > Root).", bold_prefix="Right Subtree Property:")
    add_bullet(doc, " Both the left and right subtrees must themselves be valid Binary Search Trees.", bold_prefix="Recursive Substructure:")
    add_p(
        doc,
        "Because of this ordering property, searching, insertion, and deletion in a balanced BST eliminate half of the remaining tree at each step (just like Binary Search on an array), achieving O(log n) average time complexity."
    )

    # I. Draw the Diagram
    add_h2(doc, "2.2 (I) Hand-Drawn Diagram of a Binary Search Tree (BST)")
    add_image_figure(
        doc,
        os.path.join(img_dir, "bst_sketch.jpg"),
        "Figure 2.1: Hand-Drawn Notebook Diagram of a Binary Search Tree (Root = 50) and its Three DFS Traversals",
        width_inches=4.8
    )

    # II. Use Recursive Algorithm to Explain
    add_h2(doc, "2.3 (II) Explaining BST Operations Using Recursive Algorithms")
    add_p(
        doc,
        "Because a Binary Search Tree is inherently recursive in structure (every child is the root of a smaller BST), its core operations—Search and Insertion—are most naturally expressed using recursion:"
    )
    add_h3(doc, "A. Recursive BST Search Algorithm")
    add_bullet(doc, " If root == null (key not found) or root.data == target (key found), return root.", bold_prefix="Base Case:")
    add_bullet(doc, " If target < root.data, the target can only exist in the left subtree, so recursively return search(root.left, target).", bold_prefix="Recursive Left Step:")
    add_bullet(doc, " If target > root.data, the target can only exist in the right subtree, so recursively return search(root.right, target).", bold_prefix="Recursive Right Step:")

    add_h3(doc, "B. Recursive BST Insertion Algorithm")
    add_bullet(doc, " If root == null, we have reached the exact empty spot where the new value belongs; allocate and return new Node(val).", bold_prefix="Base Case:")
    add_bullet(doc, " If val < root.data, recursively insert into the left subtree: root.left = insert(root.left, val).", bold_prefix="Recursive Left Step:")
    add_bullet(doc, " If val > root.data, recursively insert into the right subtree: root.right = insert(root.right, val).", bold_prefix="Recursive Right Step:")

    add_code_block(doc, """public class BinarySearchTree {
    static class Node {
        int data;
        Node left, right;
        Node(int data) { this.data = data; }
    }

    // Recursive Insertion into BST
    public static Node insert(Node root, int val) {
        if (root == null) {
            return new Node(val); // Base case: attach new leaf node here
        }
        if (val < root.data) {
            root.left = insert(root.left, val);   // Recurse down left subtree
        } else if (val > root.data) {
            root.right = insert(root.right, val); // Recurse down right subtree
        }
        return root;
    }

    // Recursive Search in BST
    public static boolean search(Node root, int target) {
        if (root == null) return false;       // Base case 1: empty subtree (not found)
        if (root.data == target) return true; // Base case 2: target found at current node

        if (target < root.data) {
            return search(root.left, target); // Search left subtree
        } else {
            return search(root.right, target); // Search right subtree
        }
    }
}""")

    # III. Explain In-order, Pre-order, and Post-order Traversals
    add_h2(doc, "2.4 (III) Depth-First Tree Traversals: In-Order, Pre-Order, and Post-Order")
    add_p(
        doc,
        "Using the BST shown in Figure 2.1 (Root = 50, Left Subtree = [30 with children 20, 40], Right Subtree = [70 with children 60, 80]), the three recursive Depth-First Traversals work as follows:"
    )

    add_h3(doc, "a. In-Order Traversal (Left -> Root -> Right)")
    add_p(
        doc,
        "In an In-Order traversal, the algorithm recursively visits the entire left subtree first, then visits/prints the current root node, and finally recursively visits the entire right subtree. Crucial Property: On any Binary Search Tree, In-Order Traversal always outputs the keys in strictly sorted (ascending) order."
    )
    add_bullet(doc, " 1. Traverse Left Subtree of 50 -> (visits 20, then 30, then 40) | 2. Visit Root (50) | 3. Traverse Right Subtree of 50 -> (visits 60, then 70, then 80).", bold_prefix="Execution on Figure 2.1 BST:")
    add_bullet(doc, " 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 (Sorted ascending order!).", bold_prefix="In-Order Output:")
    add_code_block(doc, """public static void inOrder(Node root) {
    if (root == null) return;
    inOrder(root.left);                // 1. Visit Left Subtree
    System.out.print(root.data + " "); // 2. Visit Root Node
    inOrder(root.right);               // 3. Visit Right Subtree
}""")

    add_h3(doc, "b. Pre-Order Traversal (Root -> Left -> Right)")
    add_p(
        doc,
        "In a Pre-Order traversal, the current root node is visited first before either of its subtrees, followed recursively by the entire left subtree and then the entire right subtree. It is widely used to clone/duplicate a tree or serialize a BST so it can be reconstructed in the exact same shape."
    )
    add_bullet(doc, " 1. Visit Root (50) | 2. Traverse Left Subtree in Pre-Order (30 -> 20 -> 40) | 3. Traverse Right Subtree in Pre-Order (70 -> 60 -> 80).", bold_prefix="Execution on Figure 2.1 BST:")
    add_bullet(doc, " 50 -> 30 -> 20 -> 40 -> 70 -> 60 -> 80", bold_prefix="Pre-Order Output:")
    add_code_block(doc, """public static void preOrder(Node root) {
    if (root == null) return;
    System.out.print(root.data + " "); // 1. Visit Root Node first
    preOrder(root.left);               // 2. Visit Left Subtree
    preOrder(root.right);              // 3. Visit Right Subtree
}""")

    add_h3(doc, "c. Post-Order Traversal (Left -> Right -> Root)")
    add_p(
        doc,
        "In a Post-Order traversal, the algorithm recursively visits the entire left subtree first, then the entire right subtree, and visits the current root node last. Because children are always processed before their parent, Post-Order is used for bottom-up operations like deleting/freeing a tree, computing subtree heights, and evaluating postfix arithmetic expression trees."
    )
    add_bullet(doc, " 1. Traverse Left Subtree in Post-Order (20 -> 40 -> 30) | 2. Traverse Right Subtree in Post-Order (60 -> 80 -> 70) | 3. Visit Root last (50).", bold_prefix="Execution on Figure 2.1 BST:")
    add_bullet(doc, " 20 -> 40 -> 30 -> 60 -> 80 -> 70 -> 50", bold_prefix="Post-Order Output:")
    add_code_block(doc, """public static void postOrder(Node root) {
    if (root == null) return;
    postOrder(root.left);              // 1. Visit Left Subtree
    postOrder(root.right);             // 2. Visit Right Subtree
    System.out.print(root.data + " "); // 3. Visit Root Node last
}""")

    add_styled_table(
        doc,
        ["Traversal Type", "Visit Order", "Output on Figure 2.1 BST", "Primary Application"],
        [
            ["In-Order", "Left -> Root -> Right", "20, 30, 40, 50, 60, 70, 80", "Retrieving BST elements in sorted ascending order"],
            ["Pre-Order", "Root -> Left -> Right", "50, 30, 20, 40, 70, 60, 80", "Cloning/copying trees and prefix expression serialization"],
            ["Post-Order", "Left -> Right -> Root", "20, 40, 30, 60, 80, 70, 50", "Bottom-up tree deletion, subtree height, postfix evaluation"]
        ],
        col_widths=[1.2, 1.45, 1.95, 1.9]
    )


# ==============================================================================
# QUESTION 3
# ==============================================================================
def write_question_3(doc, img_dir):
    add_h1(doc, "QUESTION 3: EXPLAIN LEVEL ORDER TRAVERSAL")

    add_h2(doc, "3.1 Definition and Core Concept")
    add_p(
        doc,
        "Level Order Traversal (also known as Breadth-First Search or BFS) is a method to traverse a tree such that all nodes present on the same level are traversed completely from left to right before traversing the next deeper level. Starting at the root node (Level 0), it visits Level 0, then Level 1, then Level 2, and so on until the deepest level is completed."
    )
    add_p(
        doc,
        "Unlike Depth-First traversals (In-order, Pre-order, and Post-order) which rely on recursion and a LIFO Call Stack to dive deep into branches first, Level Order Traversal uses a Queue data structure (First-In, First-Out — FIFO) to keep track of nodes to visit next."
    )

    add_h2(doc, "3.2 How It Works (Step-by-Step FIFO Queue Mechanism)")
    add_bullet(doc, " Create an empty FIFO Queue and insert (enqueue) the root node into it.", bold_prefix="1. Initialize:")
    add_bullet(doc, " While the queue is not empty:", bold_prefix="2. Iterative Loop:")
    add_bullet(doc, " Remove (dequeue / q.poll()) the node at the front of the queue and print/process its value.", bold_prefix="   a. Dequeue Front:")
    add_bullet(doc, " If the dequeued node has a non-null left child, enqueue the left child (q.add(node.left)).", bold_prefix="   b. Enqueue Left Child:")
    add_bullet(doc, " If the dequeued node has a non-null right child, enqueue the right child (q.add(node.right)).", bold_prefix="   c. Enqueue Right Child:")
    add_bullet(doc, " Repeat until the queue becomes completely empty, meaning every level of the tree has been visited.", bold_prefix="3. Terminate:")

    add_h2(doc, "3.3 Hand-Drawn Diagrams and Worked Examples")

    # Example A: Complete 3-Level Binary Tree (10, 15, 40, 20, 25, 35, 50)
    add_h3(doc, "Worked Example 1: 3-Level Binary Tree [10, 15, 40, 20, 25, 35, 50]")
    add_image_figure(
        doc,
        os.path.join(img_dir, "level_order_sketch.jpg"),
        "Figure 3.1: Hand-Drawn Notebook Diagram of Level Order Traversal (BFS) and FIFO Queue Trace",
        width_inches=4.8
    )

    add_styled_table(
        doc,
        ["Step", "Operation Performed", "Node Visited", "Children Enqueued", "Queue State [Front -> Rear]", "Output So Far"],
        [
            ["Init", "Enqueue root (10)", "—", "10", "[ 10 ]", "—"],
            ["1", "Dequeue 10; visit 10", "10 (Level 0)", "15 (L), 40 (R)", "[ 15, 40 ]", "10"],
            ["2", "Dequeue 15; visit 15", "15 (Level 1)", "20 (L), 25 (R)", "[ 40, 20, 25 ]", "10, 15"],
            ["3", "Dequeue 40; visit 40", "40 (Level 1)", "35 (L), 50 (R)", "[ 20, 25, 35, 50 ]", "10, 15, 40"],
            ["4", "Dequeue 20; visit 20", "20 (Level 2)", "None (Leaf)", "[ 25, 35, 50 ]", "10, 15, 40, 20"],
            ["5", "Dequeue 25; visit 25", "25 (Level 2)", "None (Leaf)", "[ 35, 50 ]", "10, 15, 40, 20, 25"],
            ["6", "Dequeue 35; visit 35", "35 (Level 2)", "None (Leaf)", "[ 50 ]", "10, 15, 40, 20, 25, 35"],
            ["7", "Dequeue 50; visit 50", "50 (Level 2)", "None (Leaf)", "[ Empty ]", "10, 15, 40, 20, 25, 35, 50"]
        ],
        col_widths=[0.5, 1.35, 0.9, 1.1, 1.3, 1.35]
    )

    # Example B: Groupmate Hand-Drawn Tree [3, 9, 40, 12, 19]
    add_h3(doc, "Worked Example 2: Asymmetric Binary Tree [3, 9, 40, 12, 19]")
    add_p(doc, "In this example, 3 is the root node (Level 1), 9 and 40 are the children of 3 (Level 2), and 12 and 19 are the left and right children of 40 (Level 3):")
    add_image_figure(
        doc,
        os.path.join(img_dir, "q3_member_img1.png"),
        "Figure 3.2: Hand-Drawn Notebook Diagram for Tree [3, 9, 40, 12, 19]",
        width_inches=4.5
    )
    add_bullet(doc, " Node 3 -> Output is [3]", bold_prefix="Level 1:")
    add_bullet(doc, " Nodes 9, 40 -> Output is [9, 40]", bold_prefix="Level 2:")
    add_bullet(doc, " Nodes 12, 19 -> Output is [12, 19]", bold_prefix="Level 3:")
    add_bullet(doc, " [[3], [9, 40], [12, 19]] (or flat order: 3 -> 9 -> 40 -> 12 -> 19).", bold_prefix="Final Level Order Result:")

    # Example C: 6-Node Tree [10, 20, 30, 40, 50, 60]
    add_h3(doc, "Worked Example 3: Step-by-Step Queue Trace on [10, 20, 30, 40, 50, 60]")
    add_bullet(doc, " Enqueue 10. Queue: [10]", bold_prefix="Step 1:")
    add_bullet(doc, " Dequeue 10 (Print 10), enqueue its children 20 and 30. Queue: [20, 30]", bold_prefix="Step 2:")
    add_bullet(doc, " Dequeue 20 (Print 20), enqueue its children 40 and 50. Queue: [30, 40, 50]", bold_prefix="Step 3:")
    add_bullet(doc, " Dequeue 30 (Print 30), enqueue its right child 60. Queue: [40, 50, 60]", bold_prefix="Step 4:")
    add_bullet(doc, " Dequeue 40 (Print 40), no children. Queue: [50, 60]", bold_prefix="Step 5:")
    add_bullet(doc, " Dequeue 50 (Print 50), no children. Queue: [60]", bold_prefix="Step 6:")
    add_bullet(doc, " Dequeue 60 (Print 60), no children. Queue: [] (Empty — Stop). Final Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60.", bold_prefix="Step 7:")

    add_h2(doc, "3.4 Java Code Implementation (Flat BFS & Grouped Level-by-Level)")
    add_code_block(doc, """import java.util.*;

public class LevelOrderTraversal {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) {
            this.val = val;
        }
    }

    // 1. Standard Flat Level Order Traversal (prints nodes level by level)
    public static void levelOrderFlat(TreeNode root) {
        if (root == null) return;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode current = queue.poll();
            System.out.print(current.val + " ");

            if (current.left != null) queue.add(current.left);
            if (current.right != null) queue.add(current.right);
        }
    }

    // 2. Grouped Level-by-Level Traversal (returns List<List<Integer>>)
    public static List<List<Integer>> levelOrderGrouped(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            result.add(level);
        }
        return result;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(40);
        root.right.left = new TreeNode(12);
        root.right.right = new TreeNode(19);

        System.out.print("Flat Level Order:    ");
        levelOrderFlat(root); // Output: 3 9 40 12 19
        System.out.println("\\nGrouped Level Order: " + levelOrderGrouped(root));
        // Output: [[3], [9, 40], [12, 19]]
    }
}""")

    add_h2(doc, "3.5 Time and Space Complexity")
    add_bullet(doc, " O(n), where n is the total number of nodes in the tree, because every node is enqueued and dequeued exactly once.", bold_prefix="Time Complexity:")
    add_bullet(doc, " O(w), where w is the maximum width of the tree (maximum number of nodes on any single level). In the worst case of a complete binary tree, the bottom level holds roughly n/2 nodes, giving O(n) space.", bold_prefix="Space Complexity:")


# ==============================================================================
# QUESTION 4
# ==============================================================================
def write_question_4(doc):
    add_h1(doc, "QUESTION 4: SORTING ALGORITHMS WITH 2 EXAMPLES EACH")
    add_p(
        doc,
        "Question: Explain the following sorting algorithms with 2 examples each: (I) Insertion Sort, (II) Merge Sort, (III) Quick Sort, (IV) Selection Sort, and (V) Bubble Sort.",
        bold_prefix="Prompt: "
    )

    # I. Insertion Sort
    add_h2(doc, "4.1 (I) Insertion Sort")
    add_p(
        doc,
        "Insertion sort works the way most people sort a hand of playing cards. It divides the list into a sorted section (on the left) and an unsorted section (on the right), taking one element at a time from the unsorted part and inserting it into its exact correct position within the sorted part by shifting larger elements one position to the right."
    )
    add_h3(doc, "Example 1 (Numbers): Sort [8, 3, 5, 2]")
    add_bullet(doc, " [8] is considered sorted.", bold_prefix="Start:")
    add_bullet(doc, " Insert 3 before 8 -> [3, 8, 5, 2]", bold_prefix="Pass 1 (take 3):")
    add_bullet(doc, " Insert 5 between 3 and 8 -> [3, 5, 8, 2]", bold_prefix="Pass 2 (take 5):")
    add_bullet(doc, " Insert 2 at the very beginning -> [2, 3, 5, 8] (Sorted!)", bold_prefix="Pass 3 (take 2):")

    add_h3(doc, "Example 2 (Letters): Sort ['D', 'B', 'A', 'C']")
    add_bullet(doc, " Shift 'D' right, insert 'B' -> ['B', 'D', 'A', 'C']", bold_prefix="Pass 1 (take 'B'):")
    add_bullet(doc, " Shift 'D' and 'B' right, insert 'A' -> ['A', 'B', 'D', 'C']", bold_prefix="Pass 2 (take 'A'):")
    add_bullet(doc, " Shift 'D' right, insert 'C' -> ['A', 'B', 'C', 'D'] (Sorted!)", bold_prefix="Pass 3 (take 'C'):")

    add_code_block(doc, """public static void insertionSort(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j]; // Shift larger elements right
            j--;
        }
        arr[j + 1] = key; // Insert key into correct sorted position
    }
}""")

    # II. Merge Sort
    add_h2(doc, "4.2 (II) Merge Sort")
    add_p(
        doc,
        "Merge sort is a classic \"Divide and Conquer\" sorting algorithm. It recursively splits the list into two halves until every sublist has only one element (which is inherently sorted), and then repeatedly merges those sorted sublists back together in the correct order."
    )
    add_h3(doc, "Example 1 (Numbers): Sort [6, 2, 9, 1]")
    add_bullet(doc, " Split [6, 2, 9, 1] into [6, 2] and [9, 1], then into single-element lists [6], [2], [9], [1].", bold_prefix="Divide:")
    add_bullet(doc, " Compare and combine [6] & [2] -> [2, 6]; combine [9] & [1] -> [1, 9].", bold_prefix="Merge (Level 1):")
    add_bullet(doc, " Compare front elements of [2, 6] and [1, 9] to build the final sorted list -> [1, 2, 6, 9].", bold_prefix="Merge (Level 2):")

    add_h3(doc, "Example 2 (Words): Sort [\"Dog\", \"Cat\", \"Bat\", \"Ant\"]")
    add_bullet(doc, " Split into [\"Dog\", \"Cat\"] and [\"Bat\", \"Ant\"] -> [\"Dog\"], [\"Cat\"], [\"Bat\"], [\"Ant\"].", bold_prefix="Divide:")
    add_bullet(doc, " Merge pairs alphabetically into [\"Cat\", \"Dog\"] and [\"Ant\", \"Bat\"].", bold_prefix="Merge (Level 1):")
    add_bullet(doc, " Merge the two sorted halves alphabetically -> [\"Ant\", \"Bat\", \"Cat\", \"Dog\"].", bold_prefix="Merge (Level 2):")

    add_code_block(doc, """public static void mergeSort(int[] arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);       // Divide left half
    mergeSort(arr, mid + 1, right);  // Divide right half
    merge(arr, left, mid, right);    // Conquer: merge sorted halves
}""")

    # III. Quick Sort
    add_h2(doc, "4.3 (III) Quick Sort")
    add_p(
        doc,
        "Quick sort is also a \"Divide and Conquer\" sorting algorithm, but it relies on partitioning around a pivot element. It selects one element as the pivot and partitions the remaining elements into two sublists: elements smaller than the pivot move to its left, and elements larger than the pivot move to its right. It then recursively sorts the left and right sublists."
    )
    add_h3(doc, "Example 1 (Numbers — Last Element as Pivot): Sort [7, 3, 1, 9, 5]")
    add_bullet(doc, " Partition into smaller ([3, 1]) and larger ([7, 9]) -> [3, 1], 5, [7, 9].", bold_prefix="Pivot = 5:")
    add_bullet(doc, " Partition [3, 1] around Pivot = 1 into [], 1, [3] -> [1, 3].", bold_prefix="Sort Left ([3, 1]):")
    add_bullet(doc, " Partition [7, 9] around Pivot = 9 into [7], 9, [] -> [7, 9].", bold_prefix="Sort Right ([7, 9]):")
    add_bullet(doc, " [1, 3, 5, 7, 9] (Sorted!)", bold_prefix="Combine:")

    add_h3(doc, "Example 2 (Numbers — First Element as Pivot): Sort [4, 8, 2, 6]")
    add_bullet(doc, " Partition into smaller ([2]) and larger ([8, 6]) -> [2], 4, [8, 6].", bold_prefix="Pivot = 4:")
    add_bullet(doc, " Partition [8, 6] around Pivot = 8 into [6], 8, [] -> [6, 8].", bold_prefix="Sort Right ([8, 6]):")
    add_bullet(doc, " [2, 4, 6, 8] (Sorted!)", bold_prefix="Combine:")

    add_code_block(doc, """public static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);  // Recursively sort elements < pivot
        quickSort(arr, pivotIndex + 1, high); // Recursively sort elements > pivot
    }
}""")

    # IV. Selection Sort
    add_h2(doc, "4.4 (IV) Selection Sort")
    add_p(
        doc,
        "Selection sort repeatedly scans the unsorted portion of the list to find the minimum (smallest) element and swaps it directly into the first unsorted position, growing the sorted boundary one element at a time from left to right."
    )
    add_h3(doc, "Example 1 (Numbers): Sort [9, 4, 7, 2]")
    add_bullet(doc, " Smallest in [9, 4, 7, 2] is 2. Swap 2 with 9 -> [2, 4, 7, 9]", bold_prefix="Pass 1:")
    add_bullet(doc, " Smallest in remaining [4, 7, 9] is 4. It stays in place -> [2, 4, 7, 9]", bold_prefix="Pass 2:")
    add_bullet(doc, " Smallest in remaining [7, 9] is 7. It stays in place -> [2, 4, 7, 9] (Sorted!)", bold_prefix="Pass 3:")

    add_h3(doc, "Example 2 (Numbers): Sort [15, 10, 20, 5]")
    add_bullet(doc, " Smallest in [15, 10, 20, 5] is 5. Swap 5 with 15 -> [5, 10, 20, 15]", bold_prefix="Pass 1:")
    add_bullet(doc, " Smallest in remaining [10, 20, 15] is 10. Stays in place -> [5, 10, 20, 15]", bold_prefix="Pass 2:")
    add_bullet(doc, " Smallest in remaining [20, 15] is 15. Swap 15 with 20 -> [5, 10, 15, 20] (Sorted!)", bold_prefix="Pass 3:")

    add_code_block(doc, """public static void selectionSort(int[] arr) {
    for (int i = 0; i < arr.length - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIdx]) minIdx = j;
        }
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}""")

    # V. Bubble Sort
    add_h2(doc, "4.5 (V) Bubble Sort")
    add_p(
        doc,
        "Bubble sort repeatedly steps through the list, compares adjacent pairs of elements (arr[j] and arr[j + 1]), and swaps them if they are in the wrong order. With each full pass through the list, the largest remaining unsorted element \"bubbles up\" to its final locked position at the end of the list."
    )
    add_h3(doc, "Example 1 (Numbers): Sort [5, 1, 4, 2]")
    add_bullet(doc, " Compare (5, 1) -> swap -> [1, 5, 4, 2]; Compare (5, 4) -> swap -> [1, 4, 5, 2]; Compare (5, 2) -> swap -> [1, 4, 2, 5] (5 is now locked in place).", bold_prefix="Pass 1:")
    add_bullet(doc, " Compare (1, 4) -> no swap; Compare (4, 2) -> swap -> [1, 2, 4, 5] (4 is now locked in place).", bold_prefix="Pass 2:")
    add_bullet(doc, " Compare (1, 2) -> no swaps occur, so sorting terminates early -> [1, 2, 4, 5] (Sorted!).", bold_prefix="Pass 3:")

    add_h3(doc, "Example 2 (Numbers): Sort [3, 2, 1]")
    add_bullet(doc, " Swap (3, 2) -> [2, 3, 1]; Swap (3, 1) -> [2, 1, 3] (3 is locked at the end).", bold_prefix="Pass 1:")
    add_bullet(doc, " Swap (2, 1) -> [1, 2, 3] (2 is locked).", bold_prefix="Pass 2:")
    add_bullet(doc, " No swaps needed -> [1, 2, 3] (Sorted!).", bold_prefix="Pass 3:")

    add_code_block(doc, """public static void bubbleSort(int[] arr) {
    for (int i = 0; i < arr.length - 1; i++) {
        boolean swapped = false;
        for (int j = 0; j < arr.length - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break; // Early exit if already sorted
    }
}""")

    # Summary Comparison Table of All 5 Sorting Algorithms
    add_h2(doc, "4.6 Complexity Summary of All Five Sorting Algorithms")
    add_styled_table(
        doc,
        ["Sorting Algorithm", "Best Time", "Average Time", "Worst Time", "Space", "Stable?"],
        [
            ["I. Insertion Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)", "Yes"],
            ["II. Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Yes"],
            ["III. Quick Sort", "O(n log n)", "O(n log n)", "O(n^2)", "O(log n)", "No"],
            ["IV. Selection Sort", "O(n^2)", "O(n^2)", "O(n^2)", "O(1)", "No"],
            ["V. Bubble Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)", "Yes"]
        ],
        col_widths=[1.5, 1.0, 1.1, 1.0, 0.9, 1.0]
    )


def build_compiled_group_assignment(output_path, img_dir):
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(0.9)
        section.bottom_margin = Inches(0.9)
        section.left_margin = Inches(0.95)
        section.right_margin = Inches(0.95)

    # Cover / Header Block
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    r_title = title_p.add_run("CSC 301: DATA STRUCTURES — GROUP ASSIGNMENT")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(10)
    r_sub = sub_p.add_run("Lecturer: Mr. Isioma  |  Topics: Recursion in Loops, Binary Search Trees (BST), Tree Traversals & Sorting Algorithms")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = SLATE

    # Group Members Table
    add_h2(doc, "Group Members")
    members = [
        ["1", "Pam Patriarch", "VUG/SEN/24/12478"],
        ["2", "Eboh Adaeze Michelle", "VUG/SEN/24/11365"],
        ["3", "Obi Celestine Tawo", "VUG/SEN/24/11868"],
        ["4", "Danzoss Blessing Teyei", "VUG/SEN/24/11728"],
        ["5", "Vlachos Ebikere Nina", "VUG/SEN/24/11747"],
        ["6", "Emmanuel Annah Kuje", "VUG/SEN/24/11247"],
        ["7", "Mgbemena Chimsimdi", "VUG/SEN/24/11214"],
        ["8", "Ike Nancy Nnenna", "VUG/SEN/24/12359"],
        ["9", "John Patience Godenaan", "VUG/SEN/24/12079"],
        ["10", "Essen Josephine Utibe", "VUG/SEN/24/13127"],
    ]
    add_styled_table(doc, ["S/N", "Full Name", "Matric / Registration Number"], members, col_widths=[0.6, 3.2, 2.7])

    # Write all 4 questions
    write_question_1(doc, img_dir)
    doc.add_page_break()
    write_question_2(doc, img_dir)
    doc.add_page_break()
    write_question_3(doc, img_dir)
    doc.add_page_break()
    write_question_4(doc)

    doc.save(output_path)
    print("Compiled successfully:", output_path)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(base_dir, "images")
    out_master = os.path.join(base_dir, "CSC301_Group_Assignment_Final_Submission.docx")
    out_master2 = os.path.join(base_dir, "CSC301_Group_Assignment_Master.docx")
    build_compiled_group_assignment(out_master, img_dir)
    build_compiled_group_assignment(out_master2, img_dir)

