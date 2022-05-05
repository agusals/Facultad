class promedio:

    __prom = 0.00
    __cant = 0

    def tempPromedio(self, arr):
        for i in range(30):
            for o in range(24):
                if arr[i][o] != "-":
                    self.__prom += arr[i][o].gettemp()
                    self.__cant += 1

        return (self.__prom / self.__cant)