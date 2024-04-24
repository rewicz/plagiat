public <T> List<String> searchAllChildrenKeys(TreeNode<T> element, T tempKey) {
        if (element == null || element.key.equals(tempKey)) {
        return new ArrayList<>();
        }
        List<String> arrayKeys = new ArrayList<>();
        arrayKeys.add(element.key.toString());
        if (element.children == null) {
        return arrayKeys;
        }

        for (TreeNode<T> child : element.children) {
        List<String> parentKeys = searchAllChildrenKeys(child, tempKey);
        arrayKeys.addAll(parentKeys);
        }
        return arrayKeys;
        }
