void b_sort(int tablica[],int ile_liczb){
    int temp,i,zmiana;
        do{
        zmiana=0;
        i=ile_liczb-1;
        do{
        i--;
        if(tablica[i+1]<tablica[i]){
        temp=tablica[i];
        tablica[i]=tablica[i+1];
        tablica[i+1]=temp;
        zmiana=1;
        }
        }while(i!=0);
        }while(zmiana!=0);
        }
