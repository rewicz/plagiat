public static boolean[] sieveOfEratosthenes(int n) {
        boolean[] primes = new boolean[n + 1];
        Arrays.fill(primes, true);
        primes[0] = false;
        primes[1] = false;

        for (int i = 2; i * i <= n; i++) {
        if (primes[i]) {
        for (int j = i * i; j <= n; j += i) {
        primes[j] = false;
        }
        }
        }
        return primes;
        }