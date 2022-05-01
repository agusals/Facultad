import csv

class abuelita:
    __elpepe = "---"
    __lista = [23, 24, 25, 26]
    def init(self, str):
        self.__elpepe = str
    def print(self):
        print(self.__elpepe)
    def getlis(self):
        return self.__lista

class brocsv:
    __archivo = open("bro.csv")
    reader = csv.reader(__archivo, delimiter=";")
    def closer(self):
        self.__archivo.close()
        print("csv cerrado!")


    
if __name__ == "__main__":
    print("\n")
    ojeto = abuelita()
    ojeto.init("hola mami salgo en la terminal")
    ojeto.print()
    print("\n")
    for i in ojeto.getlis():
        print("num:",i)
    
    csvobj = brocsv()
    print("\n")
    for renglon in csvobj.reader:
        print(renglon)
    
    csvobj.closer()

    ingreso = input("mete cosa:")
    print("in es:",ingreso)