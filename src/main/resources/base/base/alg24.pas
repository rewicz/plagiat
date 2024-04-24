    function ZmianaPodstawy2Wektor(pods: Integer; liczba: Integer): vector;
        var
            v,w: vector;
            i,j: Integer;
        begin

        if (liczba<0) then begin
            exit;
        end;
        if (liczba=0) then begin
            v[1]:=1;
            v[2]:=0;
            ZmianaPodstawy2Wektor:=v;
        end;
        i:=1;
        while (liczba>0) do begin
            inc(i);
            v[i]:=liczba mod pods;
            liczba:=liczba div pods;
        end;
        for j:=2 to i do w[j]:=v[i-j+2];
        w[1]:=i-1;
        ZmianaPodstawy2Wektor:=w;
    end;