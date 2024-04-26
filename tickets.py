'''
from datetime import datetime

class Tickets():
    def __init__(self, *args):
        now = datetime.now()
        self.data = datetime(now.year, now.month, now.day, now.hour, now.minute)
        self._idColab = None
        self.status = "por atender"
        self.tipo = "HW"

        if len(args)==1 and isinstance(args[0], Tickets):
            self.idColab = args[0].idColab
            self.status = args[0].status
            self.tipo = args[0].tipo
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
'''