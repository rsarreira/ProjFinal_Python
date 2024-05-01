from abc import ABC
from datetime import datetime

class Tickets(ABC):

    def __init__(self, *args):
        now = datetime.now()
        self.idColab = None
        self.datahoraGerado = datetime(now.year, now.month, now.day, now.hour, now.minute)
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
 
        elif len(args) == 2:
            self.idColab = args[0]
            self.tipoTicket = args[1]

        '''
        elif len(args) == 7:
            self.idColab = args[0]
            self.datahoraAtendido = args[0]
            self.datahoraResolvido = args[0]
            self.estadoTicket = "Por atender."
            self.estadoAtendimento = args[0]
            self.tipoTicket = args[0]
            self.descRep = args[0]   
            now.strftime("%H:%M %d/%m/%Y")  
            '''     