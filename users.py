class Users():
    def __init__(self, *args):
        self._idColab = 9999
        self._nomeColab = "Convidado"
        self._pin = 1234
        self._cargo = "Convidado"
        if len(args) == 1 and isinstance(args[0], Users):
            self.idColab = args[0].idColab
            self.nomeColab = args[0].nomeColab
            self.pin = args[0].pin
            self.cargo = args[0].cargo
        if len(args) == 4:
            self.idColab = args[0]
            self.nomeColab = args[1]
            self.pin = args[2]
            self.cargo = args[3]

    @property
    def idColab(self):
        return self._idColab

    @idColab.setter
    def idColab(self, valor):
        if valor > 0:
            self._idColab = valor

    @property
    def nomeColab(self):
        return self._nomeColab

    @nomeColab.setter
    def nomeColab(self, valor):
        if valor == str:
            self._nomeColab = valor

    @property
    def pin(self):
        return self._pin
    
    @pin.setter
    def pin(self, valor):
        if valor >= 1000 and valor <= 9999:
            self._pin = valor
    
    @property
    def cargo(self):
        return self._cargo
    
    @cargo.setter
    def cargo(self, valor):
        if valor == "Técnico" or valor == "Vendedor" or valor == "Operador":
            self._cargo = valor
        
    def __str__(self):
        return f"ID: {self.idColab}, Nome: {self.nomeColab}, PIN: {self.pin} , Cargo: {self.cargo}."
