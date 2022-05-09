from Modulos.MedicamentosMod import Medicamento as med
from Modulos.CamaMod import Cama as cama
from datetime import date

class Listador:

    @classmethod
    def showdatos(cls, med: med, camarr: cama, nya: str, idcam: int):
        hoy = date.today()
        fecha = hoy.strftime("%d/%m/%Y")

        print("Paciente: {}             Cama: {}        Habitación:{}\n" .format(nya, idcam+1, camarr[idcam].gethab()))
        print("Diagnóstico: {}          Fecha de internación: {}\n" .format(camarr[idcam].getdiag(), camarr[idcam].getfechain()))
        print("Fecha de Alta: {}\n" .format(fecha))
        print("Medicamento/monodroga        Presentacion        Cantidad        Precio\n")

        totaladeudado = 0
        for o in med:
            if o.getidcama() == idcam+1:
                print("{}/{}            {}          {}             {}" .format(o.getnomco(), o.getmono(), o.getpres(), o.getcantap(), o.getprecio()))
                totaladeudado += o.getprecio()
                
        print("Total adeudado:                                                   {}\n" .format(totaladeudado))

           

        input()

    @classmethod
    def listardatos(cls, med: med, camarr: cama, nya: str):

        bandera = False
        e=" "
        idcam = -1
        i=0
        while e != nya:
            if nya == camarr[i].getnya():
                e=nya
                idcam=i
                bandera=True
            i+=1

        if bandera:
            cls.showdatos(med, camarr, nya, idcam)

    @classmethod
    def listarpordiag(cls, med: med, camarr: cama, diag: str):
        for p in range(len(camarr)):
            if camarr[p] != None:
                if camarr[p].getdiag() == diag and camarr[p].getestado():
                    cls.showdatos(med, camarr, camarr[p].getnya(), p)