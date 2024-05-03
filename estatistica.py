def tickets_atendidos_intervalo_datas(data_inicio, data_fim,cursor):
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

    porcentagem_nao_resolvidos = 100 - porcentagem_resolvidos

    return porcentagem_resolvidos, porcentagem_nao_resolvidos

def media_tempo_atendimento_por_tipo(cursor):

    sql_hw = "select ROUND(AVG(TIMESTAMPDIFF(MINUTE, datahoraAtendido, datahoraResolvido))) from ticket where estadoTicket = 'Atendido' and tipoTicket = 'HW';"
    cursor.execute(sql_hw)
    result_hw = cursor.fetchone()[0]

    sql_sw = "select ROUND(AVG(TIMESTAMPDIFF(MINUTE, datahoraAtendido, datahoraResolvido))) from ticket where estadoTicket = 'Atendido' and tipoTicket = 'SW';"
    cursor.execute(sql_sw)
    result_sw = cursor.fetchone()[0]

    return result_hw, result_sw