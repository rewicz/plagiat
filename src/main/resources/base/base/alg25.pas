        function ZmianaPodstwy2Liczba(pods: Integer; v: vector): Integer;
        var
            suma: Integer;
            i,j : Integer;
        begin
            suma:=0;
            j:=0;
                for i:=v[1]+1 downto 2 do begin
                suma:=suma+(v[i]*pow(pods,j));
                inc(j);
            end;
            ZmianaPodstwy2Liczba:=suma;
    end;
