from Reg import Registro as r

class maximini:
    __maximot = -99999
    __diatemp = -1
    __horatemp = -1

    __maximoh = -99999
    __diahum = -1
    __horahum = -1

    __maximop = -99999
    __diapres = -1
    __horapres = -1

    __mint = 99999
    __diat = -1
    __horat = -1

    __minh = 99999
    __diah = -1
    __horah = -1

    __minp = 99999
    __diap = -1
    __horap = -1

    def maximo(self, arr):

        for i in range(30):
            for o in range(24):
                if arr[i][o] != "-":
                    if arr[i][o].gettemp() > self.__maximot:
                        self.__maximot = arr[i][o].gettemp()
                        self.__diatemp = i+1
                        self.__horatemp = o+1
                    if arr[i][o].gethum() > self.__maximoh:
                        self.__maximoh = arr[i][o].gethum()
                        self.__diahum = i+1
                        self.__horahum = o+1
                    if arr[i][o].getpresion() > self.__maximop:
                        self.__maximop = arr[i][o].getpresion()
                        self.__diapres = i+1
                        self.__horapres = o+1

        return {"Max Temp":[self.__diatemp, self.__horatemp], "Max Hum":[self.__diahum, self.__horahum], "Max Presion":[self.__diapres, self.__horapres]}

    def minimo(self, arr):

        for i in range(30):
            for o in range(24):
                if arr[i][o] != "-":
                    if arr[i][o].gettemp() < self.__mint:                    
                        self.__mint = arr[i][o].gettemp()
                        self.__diat = i+1
                        self.__horat = o+1
                    if arr[i][o].gethum() < self.__minh:
                        self.__minh = arr[i][o].gethum()
                        self.__diah = i+1
                        self.__horah = o+1
                    if arr[i][o].getpresion() < self.__minp:
                        self.__minp = arr[i][o].getpresion()
                        self.__diap = i+1
                        self.__horap = o+1

        return {"Min Temp":[self.__diat, self.__horat], "Min Hum":[self.__diah, self.__horah], "Min Presion":[self.__diap, self.__horap]}
