public <T> TreeNode<T> searchParentTreeNode(TreeNode<T> element, Object matchingTitle) {
        if (element == null || element.children == null) {
        return null;
        }

        for (TreeNode<T> child : element.children) {
        if (child.key.equals(matchingTitle)) {
        return element;
        }
        TreeNode<T> parent = searchParentTreeNode(child, matchingTitle);
        if (parent != null) {
        return parent;
        }
        }
        return null;
        }
