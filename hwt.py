
from datetime import datetime

class Hwt():
    def __init__(self, *args):
        super().__init__()
        now = datetime.now()
        #self.idHw = ""
        self.idTicket = ""
        self.equipamento = None
        self.avaria = None
        self.descReparacao = None
        self.dataHw = datetime(now.year, now.month, now.day, now.hour, now.minute)
        self.dataHwf = datetime(now.year, now.month, now.day, now.hour, now.minute)
        self.status = "aberto"

        if len(args)==1 and isinstance(args[0], Hwt):
            super().__init__(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
            self.estadoHW = args[7]
        #   self.dataHw  =
        #   self.data_horarHW = args[9]
        #   self.dataHwf = args[9]

        if len(args)==3:
            self.idColab = args[0]
            self.status = args[1]
            self.tipo = args[2]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, valor):
        self._data= valor

    @property
    def idColab(self):
        return self._idColab


    @idColab.setter
    def idColab(self, valor):
            self._idColab=valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        if valor in ("por atender", "atendido"):
            self._status = valor

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if valor in ("HW", "SW"):
            self._tipo = valor
    def __str__(self):

        return (f"Colaborador: {self.idColab}, status: {self.status}, tipo: {self.tipo}, data: {self.data}")
