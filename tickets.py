from datetime import datetime
from abc import ABC


class Tickets(ABC):

    """
           Inicializar um objeto da classe Tickets.

           Args:
               *args: Argumentos variáveis para inicializar o objeto.

           Note:
               - O idColab é o identificador do colaborador associado ao ticket.
               - A datahoraGerado é a data/hora em que o ticket foi gerado, inicializada com a data e hora do sistema atuais.
               - A datahoraAtendido é a data/hora em que o ticket foi atendido.
               - A datahoraResolvido é a data/hora em que o ticket foi resolvido.
               - O estadoTicket indica o estado atual do ticket, iniciado como "Por atender".
               - O estadoAtendimento indica o estado de atendimento do ticket.
               - O tipoTicket é o tipo de ticket ("HW" para hardware - "SW" para software).
               - A descRep é a descrição da reposta indicada pelo técnico associada ao ticket.

    """
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