private  int[] ZmianaPodstawy2Wektor(int pods, int liczba)
        {
        int v[] = new int[n];
        int w[] = new int[n];
        int i, j;

        if (liczba < 0) {
        return null;
        }

        if (liczba == 0) {
        v[0] = 1;
        v[1] = 0;
        return v;
        }

        i = 0;
        while (liczba > 0) {
        i++;
        v[i] = liczba % pods;
        liczba = liczba / pods;
        }
        for (j=1; j<i; j++)
        w[j] = v[i-j+2];

        w[0] = i-1;
        return w;
        }