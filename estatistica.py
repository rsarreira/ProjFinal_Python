
def tickets_atendidos_intervalo_datas(data_inicio, data_fim,cursor):

    """
        Calcula a quantidade de tickets atendidos dentro de um intervalo de datas fornecidos pelo utilizador.

        Args:
            data_inicio (str): Data de início do intervalo no formato 'YYYY-MM-DD'.
            data_fim (str): Data de fim do intervalo no formato 'YYYY-MM-DD'.
            cursor: Conexão da BD para execução das consultas SQL.

        Returns:
            número total de tickets atendidos e a respectiva porcentagem de tickets atendidos dentro do intervalo fornecidos
            pelo utilizador.
    """

    soma_total = 0
    soma_atendidos = 0

    sql = f"select count(*) from ticket where estadoTicket = 'Atendido' and datahoraAtendido between '{data_inicio}' and '{data_fim}'"
    cursor.execute(sql)
    soma_atendidos = cursor.fetchone()[0]

    sql_total = f"select count(*) from ticket"
    cursor.execute(sql_total)
    soma_total = cursor.fetchone()[0]

    if soma_total == 0:
        return 0  # Evitar divisão por zero

    porcentagem_atendidos = round((soma_atendidos / soma_total) * 100, 1)
    return soma_atendidos, porcentagem_atendidos


def porcentagem_tickets_resolvidos_naoresolvidos(cursor):

    """
        Calcula a porcentagem de tickets resolvidos e não resolvidos.

        Args:
            cursor: Conexão da BD para execução das consultas SQL.

        Returns:
             A porcentagem de tickets resolvidos e a de tickets não resolvidos.
    """

    sql = f"select count(*) from ticket where estadoAtendimento = 'Resolvido'"
    cursor.execute(sql)
    tickets_resolvidos = cursor.fetchone()[0]


    sql_total = f"select count(*) from ticket"
    cursor.execute(sql_total)
    total_tickets = cursor.fetchone()[0]

    if total_tickets == 0:
        porcentagem_resolvidos = 0
    else:
        porcentagem_resolvidos = round((tickets_resolvidos / total_tickets) * 100,1)

    porcentagem_nao_resolvidos = round(100 - porcentagem_resolvidos,1)

    return porcentagem_resolvidos, porcentagem_nao_resolvidos


def media_tempo_atendimento_por_tipo(cursor):

    """
        Calcula a média do tempo de atendimento por tipo de ticket (SW/HW).

        Args:
            cursor: Conexão da BD para execução das consultas SQL.

        Returns:
            A média do tempo de atendimento para tickets do tipo HW/SW.
    """
    sql_hw = "select round(avg(timestampdiff(minute, datahoraAtendido, datahoraResolvido))) from ticket where estadoTicket = 'Atendido' and tipoTicket = 'HW';"
    cursor.execute(sql_hw)
    result_hw = cursor.fetchone()[0]

    sql_sw = "select round(avg(timestampdiff(minute, datahoraAtendido, datahoraResolvido))) from ticket where estadoTicket = 'Atendido' and tipoTicket = 'SW';"
    cursor.execute(sql_sw)
    result_sw = cursor.fetchone()[0]

    return result_hw, result_sw


def equipamento_mais_tickets(cursor):

    """
        Identifica o equipamento com mais tickets registados.

        Args:
            cursor: Conexão da BD para execução das consultas SQL.

        Returns:
            O nome do equipamento com mais tickets e o número total de tickets associados ao mesmo.
    """

    sql_hw = "select equipamento, count(*) as total_tickets from ticket where tipoTicket = 'HW' group by equipamento order by total_tickets desc limit 1"
    cursor.execute(sql_hw)
    result_hw = cursor.fetchone()
    if result_hw:
        equipamento, total_tickets = result_hw
        return equipamento, total_tickets
    else:
        return None


def software_mais_tickets(cursor):

    """
        Identifica o software com mais tickets registados.

        Args:
            cursor: Conexão da BD para execução das consultas SQL.

        Returns:
            O nome do software com mais tickets e o número total de tickets associados ao mesmo.
    """
    sql_sw = "select software, count(*) as total_tickets from ticket where tipoTicket = 'SW' group by software order by total_tickets desc limit 1"
    cursor.execute(sql_sw)
    result_hw = cursor.fetchone()
    if result_hw:
        software, total_tickets = result_hw
        return software, total_tickets
    else:
        return None