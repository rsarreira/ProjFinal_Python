from datetime import datetime
from tickets import Tickets


class Swt(Tickets):
    def __init__(self, *args):
        super().__init__()
        self._software = None
        self._desc_necess = None

        if len(args) == 1 and isinstance(args[0], Swt):
            super().__init__(args[0])
            self.software = args[0].software
            self.desc_necess = args[0].desc_necess

        if len(args) == 6:
            super().__init__(args[0], args[1], args[2], args[3])
            self.software = args[4]
            self.desc_necess = args[5]

    @property
    def software(self):
        return self._software

    @software.setter
    def software(self, valor):
        self._software = valor

    @property
    def desc_necess(self):
        return self._desc_necess

    @desc_necess.setter
    def desc_necess(self, valor):
        self._desc_necess = valor

    def __str__(self):
        return (f"Software {self.software}, com a seguinte necessidade : {self.desc_necess}.")