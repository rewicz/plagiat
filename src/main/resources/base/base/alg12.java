public static Integer findLeader(int[] array) {
        int count = 0;
        Integer candidate = null;

        for (int number : array) {
        if (count == 0) {
        candidate = number;
        }
        if (number == candidate) {
        count++;
        } else {
        count--;
        }
        }

        count = 0;
        for (int number : array) {
        if (number == candidate) {
        count++;
        }
        }

        if (count > array.length / 2) {
        return candidate;
        }
        return null;
        }