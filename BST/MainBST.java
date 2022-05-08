public class MainBST {

    public static void main(String args[]){
        MainBST BST = new MainBST();
        Node root = new Node(20);
        root.left = new Node(8);
        root.right = new Node(22);
        root.left.left = new Node(4);
        root.left.right = new Node(12);
        root.left.right.left = new Node(10);
        root.left.right.right = new Node(14);

        Print pt = new Print();
        pt.tree( root,"");

        LCAinBST lca =new LCAinBST();
        int n =lca.findAncestor(root,10,14);
        System.out.print("LCA "+n);
    }

}

