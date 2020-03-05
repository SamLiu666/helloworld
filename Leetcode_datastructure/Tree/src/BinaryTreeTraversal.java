import com.sun.source.tree.BinaryTree;

import javax.swing.tree.TreeNode;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeTraversal {
    //顺序遍历：先访问根节点，然后遍历左边，最后遍历右边
    public List<Integer> pre_orderTraversal(TreeNode root){
        List<Integer> pre = new LinkedList<Integer>();
        if (root == null) return pre;
        pre.add(root.val);
        pre.addAll(pre_orderTraversal(root.left));
        pre.addAll(pre_orderTraversal(root.right));
        return pre;
    }

}
