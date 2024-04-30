class Users():
    def __init__(self, *args):
        self._id = 0
        self._utilizador = ""
        self.cargoemp = ""
        if len(args) == 1 and isinstance(args[0], Users):
            self.id = args[0].id
            self.utilizador = args[0].utilizador
            self.cargoemp = args[0].cargoemp
        if len(args) == 3:
            self.id = args[0]
            self.utilizador = args[1]
            self.cargoemp = args[2]

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def utilizador(self):
        return self._utilizador
    @utilizador.setter
    def utilizador(self, valor):
        self._utilizador = valor

    @property
    def cargoemp(self):
        return self._cargoemp

    @cargoemp.setter
    def cargoemp(self, valor):
        self._cargoemp = valor


    def __str__(self):
        return f"Id: {self.id}, utilizador: {self.utilizador}, cargo: {self.cargoemp}."
