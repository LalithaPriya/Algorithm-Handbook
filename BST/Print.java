public class Print {
    public void tree(Node node, String prefix) {
        if (node == null) return;
        tree(node.left, prefix + " ");
        System.out.println(prefix + " + " + node.value);
        tree(node.right, prefix + " ");
    }

}
