class listador:

    def listar(self, arr, i: int):
        i -= 1
        print("Hora         Temp.            Humedad         Presion atmos.\n")
        for o in range(24):
                if arr[i][o] != "-":
                    
                    print(" {}           {}                 {}                  {}\n" .format(o, arr[i][o].gettemp(), arr[i][o].gethum(), arr[i][o].getpresion()))

                else:

                    print(" {}           --                 --                  --\n" .format(o))

        
