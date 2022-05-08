public class CheckTwoBSTs {
    int[] arr1 = new int[10];
    int[] arr2 = new int[10];
    int i = 0;

    boolean validateBST(Node n1, Node n2) {
        if ((n1 == null && n2 != null) || (n1 != null && n2 == null))
            return false;
        convertoArr(n1, arr1);
        i = 0;
        convertoArr(n2, arr2);
        if (arr1.length != arr2.length)
            return false;
        for (int j = 0; j < arr1.length; j++) {
            if (arr1[j] != arr2[j]) {
                return false;
            }
        }
        return true;
    }

    void convertoArr(Node n, int[] arr) {
        if (n == null) return;
        convertoArr(n.left, arr);
        arr[i++] = n.value;
        convertoArr(n.right, arr);
    }
}
