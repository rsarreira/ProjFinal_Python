from datetime import datetime
from abc import ABC

class Tickets(ABC):
    def __init__(self , *args):
        self.idColab = None
        self.datahoraGerado = datetime.now()
        self.datahoraAtendido = None
        self.datahoraResolvido = None
        self.estadoTicket = "Por atender"
        self.estadoAtendimento = None
        self.tipoTicket = None
        self.descRep = None

        if len(args) == 1 and isinstance(args[0] , Tickets):
            self.idColab = args[0].idColab
            self.datahoraAtendido = args[0].datahoraAtendido
            self.datahoraResolvido = args[0].datahoraResolvido
            self.estadoTicket = args[0].estadoTicket
            self.estadoAtendimento = args[0].estadoAtendimento
            self.tipoTicket = args[0].tipoTicket
            self.descRep = args[0].descRep   

        elif len(args) == 1:
            self.tipoTicket = args[0]    
 
        elif len(args) == 2:
            self.idColab = args[0]
            self.tipoTicket = args[1]