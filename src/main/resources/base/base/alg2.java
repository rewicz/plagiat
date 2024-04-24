public <T> TreeNode<T> updateChildrenInParent(TreeNode<T> element, Object matchingTitle, List<TreeNode<T>> newNodes) {
        if (element == null) {
        return null;
        }
        if (element.key.equals(matchingTitle)) {
        if (element.children != null) {
        element.children.clear();
        element.children.addAll(newNodes);
        }
        element.triggered = true;
        return element;
        }
        if (element.children != null) {
        for (TreeNode<T> child : element.children) {
        updateChildrenInParent(child, matchingTitle, newNodes);
        }
        }
        return element;
        }
