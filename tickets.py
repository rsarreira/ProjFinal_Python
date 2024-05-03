from datetime import datetime

class Tickets():
    def __init__(self, *args):
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

    
    def tickets_atendidos_intervalo_datas(self, data_inicio, data_fim,cursor):
        soma_total = 0
        soma_atendidos = 0

        sql = f"SELECT COUNT(*) FROM ticket WHERE estadoTicket = 'Em atendimento' AND datahoraAtendido BETWEEN '{data_inicio}' AND '{data_fim}'"
        cursor.execute(sql)
        soma_atendidos = cursor.fetchone()[0]

        sql_total = f"SELECT COUNT(*) FROM ticket WHERE datahoraGerado BETWEEN '{data_inicio}' AND '{data_fim}'"
        cursor.execute(sql_total)
        soma_total = cursor.fetchone()[0]

        if soma_total == 0:
            return 0  # Evitar divisão por zero

        porcentagem_atendidos = round((soma_atendidos / soma_total) * 100, 2)
        return soma_atendidos, porcentagem_atendidos

    def porcentagem_tickets_resolvidos_naoresolvidos(self, data_inicio, data_fim, cursor):

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

    def media_tempo_atendimento_por_tipo(self, cursor):

        result_sw = None
        result_hw = None

        sql_hw = "SELECT ROUND(AVG(TIMESTAMPDIFF(MINUTE, datahoraAtendido, datahoraResolvido))) FROM ticket WHERE estadoTicket = 'Atendido' and tipoTicket = 'HW';"
        cursor.execute(sql_hw)
        result_hw = cursor.fetchone()[0]

        sql_sw = "SELECT ROUND(AVG(TIMESTAMPDIFF(MINUTE, datahoraAtendido, datahoraResolvido))) FROM ticket WHERE estadoTicket = 'Atendido' and tipoTicket = 'SW';"
        cursor.execute(sql_sw)
        result_sw = cursor.fetchone()[0]

        return result_hw, result_sw
