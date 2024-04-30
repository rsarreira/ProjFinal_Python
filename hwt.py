from datetime import datetime
from tickets import Tickets


class Hwt(Tickets):
    def __init__(self, *args):
        super().__init__()
        self._equipamento = None
        self._avaria = None
        
        if len(args) == 1 and isinstance(args[0], Hwt):
            super().__init__(args[0])
            self.equipamento = args[0].equipamento
            self.avaria = args[0].avaria

        if len(args) == 5: #criação ticket
            super().__init__(args[0],"hw", args[1], args[2])
            self.equipamento = args[3]
            self.avaria = args[4]

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

    def __str__(self):
        return (f"Hardware com avaria no equipamento {self.equipamento}, com a seguinte avaria : {self.avaria} e descrição : {self.desc_rep} .")
