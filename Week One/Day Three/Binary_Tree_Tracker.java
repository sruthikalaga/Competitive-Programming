public class BinaryTreeTracker {

    public static class Node {

        public int value;
        public Node left;
        public Node right;

        public Node(int value) {

            this.value = value;
        }

        public Node insertLeft(int Valuel) {

            this.left = new Node(Valuel);
            return this.left;
        }

        public Node insertRight(int Valuer) {

            this.right = new Node(Valuer);
            return this.right;
        }
    }

    public static boolean isBinarySearchTree(Node root) {


        return isBSTUtil(root, Integer.MIN_VALUE,
                               Integer.MAX_VALUE);
        
    }
    
    public static boolean isBSTUtil(Node root, int min, int max)
    {
        
        if (root == null)
            return true;
 
        if (root.value < min || root.value > max)
            return false;
 
        return (isBSTUtil(root.left, min, root.value-1) &&
                isBSTUtil(root.right, root.value+1, max));
    }
