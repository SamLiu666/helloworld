package leet_code_java;


import com.sun.source.tree.BinaryTree;

class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x){ val=x;}
}

public class Tree_problem
{
    // 938. Range Sum of BST
    int ans;
    public int rangeSumBST(TreeNode root, int L, int R) {
        ans = 0;
        dfs(root, L, R);
        return ans;
    }

    public void dfs(TreeNode node, int L, int R) {
        if (node != null) {
            if (L <= node.val && node.val <= R)
                ans += node.val;
            if (L < node.val)
                dfs(node.left, L, R);
            if (node.val < R)
                dfs(node.right, L, R);
        }
    }

    public static void main(String[] args){
        BinarySearchTree root = new BinarySearchTree();
        root.insert(10);


    }


}
