from datetime import datetime
from tickets import Tickets


class Hwt(Tickets):
    def __init__(self, *args):
        super().__init__()
        self._equipamento = None
        self._avaria = None
        self._desc_rep = None

        if len(args) == 1 and isinstance(args[0], Hwt):
            super().__init__(args[0])
            self.equipamento = args[0].equipamento
            self.avaria = args[0].avaria
            self.desc_rep = args[0].desc_rep

        if len(args) == 6:
            super().__init__(args[0], args[1], args[2])
            self.equipamento = args[3]
            self.avaria = args[4]
            self.desc_rep = args[5]

    @property
    def equipamento(self):
        return self._equipamento

    @equipamento.setter
    def equipamento(self, valor):
        self._equipamento = valor

    @property
    def avaria(self):
        return self._avaria

    @avaria.setter
    def avaria(self, valor):
        self._avaria = valor

    @property
    def desc_rep(self):
        return self._desc_rep

    @desc_rep.setter
    def desc_rep(self, valor):
        self._desc_rep = valor

    def __str__(self):
        return (f"Hardware com avaria no equipamento {self.equipamento}, com a seguinte avaria : {self.avaria} e descrição : {self.desc_rep} .")
