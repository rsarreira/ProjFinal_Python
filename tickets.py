from abc import ABC
from datetime import datetime

class Tickets(ABC):

    def __init__(self, *args):
        now = datetime.now()
        self.datahora_gerado = datetime(now.year, now.month, now.day, now.hour, now.minute)
        self._cod_colab = None
        self._estado_ticket = "por atender"
        self.tipo = None
        self._estado_atend = None
        self.desc_rep = None

        if len(args)==1 and isinstance(args[0], Tickets):
            self.cod_colab = args[0].cod_colab
            self.estado_ticket = args[0].estado_ticket
            self.tipo = args[0].tipo
            self.estado_atend = args[0].estado_atend
            self.desc_rep = args[0].desc_rep

        if len(args)==4:
            self.cod_colab = args[0]
            self.tipo = args[1]
            self.estado_atend= args[2]
            self.desc_rep = args[3]


    @property
    def cod_colab(self):
        return self._cod_colab

    @cod_colab.setter
    def cod_colab(self, valor):
        self._cod_colab = valor

    @property
    def estado_ticket(self):
        return self._estado_ticket

    @estado_ticket.setter
    def estado_ticket(self, valor):
        if valor in ("por atender","em atendimento", "atendido"):
            self._estado_ticket = valor

    @property
    def estado_atend(self):
        return self._estado_atend

    @estado_atend.setter
    def estado_atend(self, valor):
        if valor in ("aberto", "resolvido", "não resolvido"):
            self._estado_atend = valor

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if valor in ("HW", "SW"):
            self._tipo = valor

    @property
    def desc_rep(self):
        return self._desc_rep
    
    @desc_rep.setter
    def desc_rep(self, valor):
        self._desc_rep = valor

    def __str__(self):
        return (f"Tickets: {self.cod_colab}, status: {self.estado_ticket}, tipo: {self.tipo}, data: {self.datahora_gerado}")
