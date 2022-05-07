//kth-smallest-element-in-a-bst
public static Node kthSmallest(Node root, int k)
    {
        if (root == null)
            return null;
         Node lt = kthSmallest(root.left, k);
        if (lt != null)
            return left;
        count++;
        if (count == k)
            return root;
        return kthSmallest(root.right, k);
    }
 
