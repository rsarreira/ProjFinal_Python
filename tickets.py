from abc import ABC
from datetime import datetime
import mysql.connector

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

        elif len(args) == 3:
            self.estadoAtendimento = 'Aberto'
            self.estadoTicket = 'Em atendimento'
            self.datahoraAtendido = args[2]



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

    def contar_tickets_atendidos_no_intervalo(self, data_inicio, data_fim,cursor):
        contador_total = 0
        contador_atendidos = 0

        sql = f"SELECT COUNT(*) FROM ticket WHERE estadoTicket = 'Em atendimento' AND datahoraAtendido BETWEEN '{data_inicio}' AND '{data_fim}'"
        cursor.execute(sql)
        contador_atendidos = cursor.fetchone()[0]

        sql_total = f"SELECT COUNT(*) FROM ticket WHERE datahoraGerado BETWEEN '{data_inicio}' AND '{data_fim}'"
        cursor.execute(sql_total)
        contador_total = cursor.fetchone()[0]

        if contador_total == 0:
            return 0  # Evitar divisão por zero

        porcentagem_atendidos = round((contador_atendidos / contador_total) * 100, 2)
        return contador_atendidos, porcentagem_atendidos

    def calcular_porcentagem_tickets_resolvidos(self, data_inicio, data_fim, cursor):

        sql = f"SELECT COUNT(*) FROM ticket WHERE datahoraResolvido BETWEEN '{data_inicio}' AND '{data_fim}'"
        cursor.execute(sql)
        tickets_resolvidos = cursor.fetchone()[0]


        sql_total = f"SELECT COUNT(*) FROM ticket WHERE datahoraAtendido BETWEEN '{data_inicio}' AND '{data_fim}'"
        cursor.execute(sql_total)
        total_tickets = cursor.fetchone()[0]

        if total_tickets == 0:
            porcentagem_resolvidos = 0
        else:
            porcentagem_resolvidos = round((tickets_resolvidos / total_tickets) * 100,2)

        porcentagem_nao_resolvidos = 100 - porcentagem_resolvidos

        return porcentagem_resolvidos, porcentagem_nao_resolvidos