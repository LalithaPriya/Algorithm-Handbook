public class MainBST {

    public static void main(String args[]) {
        MainBST BST = new MainBST();
        Node root = new Node(20);
        root.left = new Node(8);
        root.right = new Node(22);
        root.left.left = new Node(4);
        root.left.right = new Node(12);
        root.left.right.left = new Node(10);
        root.left.right.right = new Node(14);

//        Print pt = new Print();
//        pt.tree( root,"");

//        LCAinBST lca =new LCAinBST();
//        int n =lca.findAncestor(root,10,14);
//        System.out.println("LCA "+n);

//        SecondMax secondMax = new SecondMax();
//        secondMax.findSecondMax(root,0,2);
        Node root1 = new Node(15);
        root1.left = new Node(10);
        root1.right = new Node(20);
        root1.left.left = new Node(5);
        root1.left.right = new Node(12);
        root1.right.right = new Node(25);

        // Second BST
        Node root2 = new Node(15);
        root2.left = new Node(12);
        root2.right = new Node(20);
        root2.left.left = new Node(5);
        root2.left.left.right = new Node(10);
        root2.right.right = new Node(25);


        CheckTwoBSTs ch = new CheckTwoBSTs();
        System.out.print(ch.validateBST(root1, root2));
    }

}

