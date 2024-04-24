public static int selectElement(int[] array, int index, int defaultValue) {
        if (array == null || index < 0 || index >= array.length) {
        return defaultValue;
        }
        return array[index];
        }