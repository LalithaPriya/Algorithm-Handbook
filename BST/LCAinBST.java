public class LCAinBST {

    public int findAncestor(Node root, int n1,int n2) {
        if(root == null){
            return -1;
        }
        if(root.value< n1 &&  root.value<n2){
            return findAncestor(root.right, n1,n2);
        }
        if(root.value> n1 &&  root.value>n2){
            return findAncestor(root.left, n1,n2);
        }
        return root.value;
    }
}
