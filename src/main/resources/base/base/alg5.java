public static int findMaxValue(int[] array) {
        if (array == null || array.length == 0) {
        throw new IllegalArgumentException("Array is empty or null");
        }
        int maxValue = array[0];
        for (int value : array) {
        if (value > maxValue) {
        maxValue = value;
        }
        }
        return maxValue;
        }
