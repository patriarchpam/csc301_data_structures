
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

def set_cell_margins(cell, top=90, bottom=90, left=140, right=140):
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
    p.paragraph_format.space_before = Pt(16)
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
    set_cell_margins(cell, 100, 100, 140, 140)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.08
    run = p.add_run(code_str.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(25, 25, 25)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_styled_table(doc, headers, rows_data, col_widths=None):
    tbl = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, color="C4CDD5", sz="4")

    # Header row
    hdr_row = tbl.rows[0]
    for idx, h_text in enumerate(headers):
        cell = hdr_row.cells[idx]
        if col_widths:
            cell.width = Inches(col_widths[idx])
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = "Arial"
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    # Data rows
    for r_idx, row_vals in enumerate(rows_data):
        row = tbl.rows[r_idx + 1]
        bg_hex = "FFFFFF" if r_idx % 2 == 0 else "F4F7FA"
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            if col_widths:
                cell.width = Inches(col_widths[c_idx])
            set_cell_background(cell, bg_hex)
            set_cell_margins(cell, 70, 70, 100, 100)
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

def add_image_figure(doc, img_path, caption_text):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(4.8))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(caption_text)
        run_cap.font.name = "Arial"
        run_cap.font.size = Pt(9.5)
        run_cap.font.italic = True
        run_cap.font.color.rgb = MUTED

def write_question_3_content(doc):
    add_h1(doc, "QUESTION 3: EXPLAIN LEVEL ORDER TRAVERSAL")

    # 3.1 Definition & Core Concept
    add_h2(doc, "3.1 Definition and Core Concept")
    add_p(
        doc,
        "Level Order Traversal (also known as Breadth-First Search or BFS on a tree) is a systematic tree traversal algorithm that visits every node in a tree level by level (depth by depth), starting at the root node (Level 0) and moving downward one level at a time. Within each horizontal level, nodes are visited strictly from left to right before advancing to the next deeper level."
    )
    add_p(
        doc,
        "Unlike Depth-First Search (DFS) traversals (In-order, Pre-order, and Post-order), which plunge deep down a single subtree branch to a leaf node using a LIFO Stack (or recursion) before backtracking, Level Order Traversal explores the tree breadth-wise across all siblings and cousins at distance d from the root before visiting any node at distance d + 1."
    )

    # 3.2 Role of the FIFO Queue Data Structure
    add_h2(doc, "3.2 Why Level Order Traversal Uses a Queue (FIFO)")
    add_p(
        doc,
        "A tree node only holds direct pointers to its immediate children (node.left and node.right); it does not have a pointer to its sibling or cousin on the same level. To remember which nodes on the next level must be visited after finishing the current level, Level Order Traversal uses a Queue (First-In, First-Out / FIFO) data structure:"
    )
    add_bullet(
        doc,
        " When a node at Level d is removed (dequeued) from the front of the queue and visited, its non-null left child and right child (which belong to Level d + 1) are immediately inserted (enqueued) at the rear of the queue.",
        bold_prefix="1. Discovering Children in Order:"
    )
    add_bullet(
        doc,
        " Because a Queue strictly follows the First-In, First-Out (FIFO) rule, every node already waiting in the queue at Level d will be dequeued and visited before any newly enqueued node at Level d + 1 reaches the front.",
        bold_prefix="2. Preserving Level-by-Level Ordering:"
    )
    add_bullet(
        doc,
        " Because current.left is always enqueued before current.right, nodes within the same level are guaranteed to be processed strictly from left to right.",
        bold_prefix="3. Preserving Left-to-Right Order:"
    )

    # Comparison table: DFS vs Level Order (BFS)
    add_h2(doc, "3.3 Comparison: Depth-First Traversals vs. Level Order Traversal")
    add_styled_table(
        doc,
        ["Feature", "DFS Traversals (In / Pre / Post-Order)", "Level Order Traversal (BFS)"],
        [
            ["Exploration Direction", "Vertical (plunges deep down a branch first)", "Horizontal (sweeps across each level left-to-right)"],
            ["Underlying Data Structure", "Stack (LIFO) — via recursion call stack", "Queue (FIFO) — via java.util.Queue / LinkedList"],
            ["Order of Node Visits", "Subtree by subtree", "Level 0 -> Level 1 -> Level 2 -> ... -> Level h"],
            ["Time Complexity", "O(n) — visits every node once", "O(n) — enqueues and dequeues every node once"],
            ["Auxiliary Space Complexity", "O(h) where h is tree height", "O(w) where w is maximum tree width (up to O(n))"],
            ["Best Suited For", "BST sorting, expression trees, subtree deletion", "Shortest path from root, level grouping, min depth"]
        ],
        col_widths=[1.6, 2.45, 2.45]
    )

    # 3.4 Step-by-Step Algorithm
    add_h2(doc, "3.4 Step-by-Step Algorithm for Level Order Traversal")
    add_p(doc, "Given the root node of a Binary Tree, the iterative Level Order Traversal algorithm proceeds as follows:")
    add_bullet(doc, " If root == null, the tree is empty; return immediately.", bold_prefix="Step 1 (Base Case Check):")
    add_bullet(doc, " Create an empty FIFO Queue q (e.g., Queue<Node> q = new LinkedList<>()).", bold_prefix="Step 2 (Initialize Queue):")
    add_bullet(doc, " Insert the root node into the queue: q.add(root).", bold_prefix="Step 3 (Enqueue Root):")
    add_bullet(doc, " Loop while the queue is not empty (while (!q.isEmpty())):", bold_prefix="Step 4 (Iterative BFS Loop):")
    add_bullet(doc, " Remove the node at the front of the queue: Node current = q.poll(), and print/process current.data.", bold_prefix="   Step 4a (Dequeue & Visit):")
    add_bullet(doc, " If current.left != null, enqueue the left child: q.add(current.left).", bold_prefix="   Step 4b (Enqueue Left Child):")
    add_bullet(doc, " If current.right != null, enqueue the right child: q.add(current.right).", bold_prefix="   Step 4c (Enqueue Right Child):")
    add_bullet(doc, " When q becomes empty, all nodes across all levels have been visited in level order.", bold_prefix="Step 5 (Termination):")

    # 3.5 Hand-Drawn Diagram & Dry Run Walkthroughs
    add_h2(doc, "3.5 Hand-Drawn Diagram and Step-by-Step Execution Traces")
    img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "level_order_sketch.jpg")
    add_image_figure(
        doc,
        img_path,
        "Figure 3.1: Hand-Drawn Notebook Diagram of Binary Tree Level Order Traversal (BFS) and FIFO Queue"
    )

    # Example 1 (Mr Isioma's Class Tree from Tree.java)
    add_p(doc, "Consider the 4-node Binary Tree from class lectures (Root = 10, Left = 15, Right = 40, and 15's Left = 20):", bold_prefix="Worked Example 1 (Class Lecture Tree): ")
    add_bullet(doc, " 10", bold_prefix="Level 0 (Root):")
    add_bullet(doc, " 15 (left child of 10), 40 (right child of 10)", bold_prefix="Level 1:")
    add_bullet(doc, " 20 (left child of 15)", bold_prefix="Level 2:")

    add_p(doc, "Queue State Trace for Example 1:", bold_prefix="Trace Table 1: ")
    add_styled_table(
        doc,
        ["Step", "Operation Performed", "Node Visited", "Children Enqueued", "Queue State [Front -> Rear]", "Output So Far"],
        [
            ["Init", "Enqueue root (10)", "—", "10", "[ 10 ]", "—"],
            ["1", "Dequeue 10; visit 10", "10 (Level 0)", "15 (L), 40 (R)", "[ 15, 40 ]", "10"],
            ["2", "Dequeue 15; visit 15", "15 (Level 1)", "20 (L)", "[ 40, 20 ]", "10, 15"],
            ["3", "Dequeue 40; visit 40", "40 (Level 1)", "None (Leaf)", "[ 20 ]", "10, 15, 40"],
            ["4", "Dequeue 20; visit 20", "20 (Level 2)", "None (Leaf)", "[ Empty ]", "10, 15, 40, 20"]
        ],
        col_widths=[0.55, 1.45, 0.95, 1.15, 1.25, 1.15]
    )

    # Example 2 (Full 3-Level 7-Node Binary Tree)
    add_p(doc, "Consider a complete 3-level Binary Tree containing 7 nodes across Levels 0, 1, and 2:", bold_prefix="Worked Example 2 (Complete 3-Level Binary Tree): ")
    add_bullet(doc, " 10", bold_prefix="Level 0 (Root):")
    add_bullet(doc, " 15 (left child of 10) and 40 (right child of 10)", bold_prefix="Level 1:")
    add_bullet(doc, " 20, 25 (children of 15) and 35, 50 (children of 40)", bold_prefix="Level 2:")

    add_p(doc, "Queue State Trace for Example 2:", bold_prefix="Trace Table 2: ")
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

    # 3.6 Java Implementation
    add_h2(doc, "3.6 Java Implementation of Level Order Traversal")
    add_p(doc, "Below is the complete, compilable Java implementation demonstrating both the standard flat BFS Level Order Traversal and the Level-by-Level Grouped variant:")
    add_code_block(doc, """import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Question3_LevelOrderTraversal {

    static class Node {
        int data;
        Node left, right;

        public Node(int data) {
            this.data = data;
        }
    }

    // 1. Standard Iterative Level Order Traversal (BFS using FIFO Queue)
    public static void levelOrder(Node root) {
        if (root == null) {
            return;
        }

        Queue<Node> q = new LinkedList<>();
        q.add(root); // Enqueue root at Level 0

        while (!q.isEmpty()) {
            Node current = q.poll();           // Dequeue front node
            System.out.print(current.data + " "); // Visit node

            if (current.left != null) {
                q.add(current.left);           // Enqueue left child
            }
            if (current.right != null) {
                q.add(current.right);          // Enqueue right child
            }
        }
    }

    // 2. Level-by-Level Grouped Traversal (separates output by level)
    public static List<List<Integer>> levelOrderGrouped(Node root) {
        List<List<Integer>> levels = new ArrayList<>();
        if (root == null) return levels;

        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int levelSize = q.size(); // Number of nodes on the current level
            List<Integer> currentLevel = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                Node current = q.poll();
                currentLevel.add(current.data);

                if (current.left != null) q.add(current.left);
                if (current.right != null) q.add(current.right);
            }
            levels.add(currentLevel);
        }
        return levels;
    }

    public static void main(String[] args) {
        // Construct Example 2 Binary Tree
        Node root = new Node(10);
        root.left = new Node(15);
        root.right = new Node(40);
        root.left.left = new Node(20);
        root.left.right = new Node(25);
        root.right.left = new Node(35);
        root.right.right = new Node(50);

        System.out.print("Level Order Traversal: ");
        levelOrder(root); // Output: 10 15 40 20 25 35 50
        System.out.println("\\nGrouped by Level:      " + levelOrderGrouped(root));
        // Output: [[10], [15, 40], [20, 25, 35, 50]]
    }
}""")

    # 3.7 Complexity Analysis & Applications
    add_h2(doc, "3.7 Time and Space Complexity Analysis")
    add_styled_table(
        doc,
        ["Metric", "Complexity", "Detailed Justification"],
        [
            ["Time Complexity", "O(n)", "Every node in the binary tree of size n is enqueued (q.add) exactly once and dequeued (q.poll) exactly once. Each queue operation takes O(1) time, yielding 2n operations = O(n)."],
            ["Space Complexity (Worst Case — Balanced/Complete Tree)", "O(w) = O(n)", "At any moment, the queue holds at most one full level of nodes. In a complete binary tree, the bottom level contains up to ceil(n / 2) nodes, so maximum queue width w = O(n)."],
            ["Space Complexity (Best Case — Skewed Tree)", "O(1)", "In a degenerate (left-skewed or right-skewed) tree where each node has only 1 child, the queue never holds more than 1 node at a time, using O(1) auxiliary space."]
        ],
        col_widths=[1.6, 1.1, 3.8]
    )

    add_h2(doc, "3.8 Practical Applications of Level Order Traversal")
    add_bullet(doc, " Finds the minimum number of edges from the root to a target node or the nearest leaf node (Minimum Depth of a Binary Tree).", bold_prefix="1. Shortest Path & Minimum Depth:")
    add_bullet(doc, " Used to serialize a binary tree into a compact level-order array (such as Binary Heaps stored in arrays where children of index i are at 2i + 1 and 2i + 2).", bold_prefix="2. Tree Serialization & Heap Representation:")
    add_bullet(doc, " Computes the maximum width of a binary tree, level averages, right/left side views, and connects sibling nodes at the same depth.", bold_prefix="3. Level-Based Tree Problems:")
    add_bullet(doc, " Forms the foundation of Breadth-First Search in graphs for web crawlers, peer-to-peer broadcasting, and finding degrees of separation in social networks.", bold_prefix="4. Network Broadcasting & Web Crawling:")


def build_standalone_q3_doc(output_path):
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Header
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    r_title = title_p.add_run("CSC 301: DATA STRUCTURES — GROUP ASSIGNMENT")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(10)
    r_sub = sub_p.add_run("Question 3: Comprehensive Explanation of Level Order Traversal")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = SLATE

    write_question_3_content(doc)
    doc.save(output_path)


def build_master_group_doc(output_path):
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Cover / Header Block
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    r_title = title_p.add_run("CSC 301: DATA STRUCTURES")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(12)
    r_sub = sub_p.add_run("Group Assignment — Recursion, Binary Search Trees, Tree Traversals & Sorting Algorithms")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(12)
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

    # Placeholder for Question 1
    add_h1(doc, "QUESTION 1: CALLING A RECURSIVE FUNCTION IN A FOR LOOP")
    add_p(doc, "[Awaiting compilation from group members — Include String Permutation + 2 more examples and hand-drawn recursion tree diagrams.]")

    # Placeholder for Question 2
    add_h1(doc, "QUESTION 2: BINARY SEARCH TREE (BST) & DFS TRAVERSALS")
    add_p(doc, "[Awaiting compilation from group members — Include (I) Hand-drawn BST Diagram, (II) Recursive BST Algorithm, and (III) In-order, Pre-order, and Post-order Traversals.]")

    # Complete Question 3
    write_question_3_content(doc)

    # Placeholder for Question 4
    add_h1(doc, "QUESTION 4: SORTING ALGORITHMS (WITH 2 EXAMPLES EACH)")
    add_p(doc, "[Awaiting compilation from group members — Include (I) Insertion Sort, (II) Merge Sort, (III) Quick Sort, (IV) Selection Sort, and (V) Bubble Sort with 2 worked examples each.]")

    doc.save(output_path)


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    q3_path = os.path.join(out_dir, "Question3_LevelOrderTraversal.docx")
    master_path = os.path.join(out_dir, "CSC301_Group_Assignment_Master.docx")
    build_standalone_q3_doc(q3_path)
    build_master_group_doc(master_path)
    print("Generated:", q3_path)
    print("Generated:", master_path)
