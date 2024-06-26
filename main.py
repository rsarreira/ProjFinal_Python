"""
Para mais informações aceder á wiki : http://tpeisntdanielafabiojoaomanuelronye.wikidot.com/start2

"""

from users import Users  # Importa a classe Users do users.py
from sw import SW  # Importa a classe SW do sw.py
from hw import HW  # Importa a classe HW do hw.py
import estatistica  # Importa a estatistica
import mysql.connector  # Importa o conector MySQL
from datetime import datetime  # Importa a classe datetime para as datas e horas
import os  # Importa o os para funcionalidades do SO ( limpar ecrã )


def apagarTerminal():

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def escolhaOpcoes():

    """
      Solicita ao utilizador a escolha de uma opção e valida se a opção é a correta

      Returns:
          int: A opção escolhida pelo utilizador.
    """

    if idColab == "Master":
        print("***************")
        print("Acesso total.")
        print("UserID: Master")
        print("***************")

    else:
        print("***************")
        print("Dados corretos.")
        print("UserID:", userID)
        print("Nome:", nome)
        print("Cargo:", cargo)
        print("***************")

    while True:
        try:
            escolha = int(input("Insira a ação que deseja efetuar:\n"
                                "(1) Criar ticket.\n"
                                "(2) Atender ticket.\n"
                                "(3) Modificar ticket.\n"
                                "(4) Criar utilizador.\n"
                                "(5) Remover utilizador.\n"
                                "(6) Verificar estado dos tickets.\n"
                                "(7) Visualizar % tickets atendidos num intervalo de datas.\n"
                                "(8) Visualizar % de tickets resolvidos e não resolvidos.\n"
                                "(9) Visualizar a média de tempo de resolução de cada tipo de ticket.\n"
                                "(10) Visualizar equipamento com mais tickets associados.\n"
                                "(11) Visualizar software com mais tickets associados.\n"
                                "(12) Fechar a aplicação.\n"))
            apagarTerminal()
            break
        except:
            apagarTerminal()
            print("Insira apenas números inteiros.")

    while escolha not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        print("***************")
        print("Acesso total.")
        print("UserID: Master")
        print("***************")
        while True:
            try:
                escolha = int(input("Por favor insira apenas uma das opções abaixo:\n"
                                    "(1) Criar ticket.\n"
                                    "(2) Atender ticket.\n"
                                    "(3) Modificar ticket.\n"
                                    "(4) Criar utilizador.\n"
                                    "(5) Apagar utilizador.\n"
                                    "(6) Verificar estado dos tickets.\n"
                                    "(7) Visualizar % tickets atendidos num intervalo de datas.\n"
                                    "(8) Visualizar % de tickets resolvidos e não resolvidos.\n"
                                    "(9) Visualizar a média de tempo de resolução de cada tipo de ticket.\n"
                                    "(10) Visualizar equipamento com mais tickets associados.\n"
                                    "(11) Visualizar software com mais tickets associados.\n"
                                    "(12) Fechar a aplicação.\n"))
                apagarTerminal()
            except:
                apagarTerminal()
                print("Insira apenas números inteiros.")

    return escolha


def criarTicket():

    """
        Cria um novo ticket com base nos dados colocados pelo utilizador
    """

    tipoTicket = str.upper(input("Que tipo de ticket deseja criar?(HW/SW) "))

    while tipoTicket != "HW" and tipoTicket != "SW":
        tipoTicket = str.upper(input("Por favor insira apenas 'SW' ou 'HW'. "))

    if tipoTicket == "HW":
        equipamento = input("Qual o equipamento? ")
        avaria = input("Qual a avaria? ")
        hw = HW(idColab, "HW", equipamento, avaria)
        sql = f"insert into ticket(idColab , datahoraGerado , estadoTicket , tipoTicket , equipamento , avaria) values('{hw.idColab}' , '{hw.datahoraGerado}' , '{hw.estadoTicket}' , '{hw.tipoTicket}' , '{hw.equipamento}' , '{hw.avaria}')"
        cursor.execute(sql)

    if tipoTicket == "SW":
        software = input("Qual o software? ")
        necessidade = input("Qual a necessidade? ")
        sw = SW(idColab, "SW", software, necessidade)
        sql = f"insert into ticket(idColab , datahoraGerado , estadoTicket , tipoTicket , software , necessidade) values('{sw.idColab}' , '{sw.datahoraGerado}' , '{sw.estadoTicket}' , '{sw.tipoTicket}' , '{sw.software}' , '{sw.necessidade}')"
        cursor.execute(sql)

    print("***************")
    print("Ticket criado com sucesso.")
    conexao.commit()


def atenderTicket(cargo, idColab):

    """
     Atendimento do ticket criado anteriormente pelo utilizador

     Args:
         cargo (str): O cargo do utilizador.
         idColab (str): O ID do utilizador.

     """
    cursor.execute("select * from ticket where estadoTicket = 'Por atender'")
    resultados = cursor.fetchall()
    lista = []
    if cargo == "Técnico" or idColab == "Master":
        for linha in resultados:
            if linha[7] == "HW":
                print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Equipamento:", linha[8],
                      "Avaria:", linha[9])
                lista.append(linha[0])
            else:
                print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Software:", linha[10],
                      "Necessidade:", linha[11])
                lista.append(linha[0])

        while True:
            try:
                escolha = int((input("Insira o ID do ticket que pretende atender.\n")))
                apagarTerminal()
                break
            except:
                print("Insira apenas números inteiros.")

        while escolha not in lista:
            for linha in resultados:
                if linha[7] == "HW":
                    print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Equipamento:",
                          linha[8], "Avaria:", linha[9])
                else:
                    print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Software:",
                          linha[10], "Necessidade:", linha[11])

            while True:
                try:
                    escolha = int(input(
                        "O ID do ticket que inseriu não consta na base de dados ou já está em atendimento. Por favor insira um ticket válido.\n"))
                    apagarTerminal()
                    break
                except:
                    print("Insira apenas números inteiros.")
            apagarTerminal()

        atendido = datetime.now()
        sql = f"update ticket set estadoAtendimento = 'Aberto' , estadoTicket = 'Em atendimento' , datahoraAtendido = '{atendido}' where idTicket = '{escolha}'"
        cursor.execute(sql)
        print("***************")
        print("Ticket atendido com sucesso.")
        conexao.commit()
    else:
        print("***************")
        print("Utilizador sem acesso à opção selecionada.")


def modificarTicket(cargo, idColab):

    """
      Modifica um ticket ( resolver ou retificar o ticket )

      Args:
          cargo (str): O cargo do utilizador.
          idColab (str): O ID do utilizador.

    """

    if cargo == "Técnico" or idColab == "Master":
        while True:
            try:
                ret_res = int(input("Pretende:\n"
                                    "(1) Resolver ticket.\n"
                                    "(2) Retificar ticket.\n"))
                apagarTerminal()
                break
            except:
                apagarTerminal()
                print("Insira apenas números inteiros.")

        while ret_res not in [1, 2]:
            while True:
                try:
                    ret_res = int(input("Escolha inválida.\n"
                                        "Pretende:\n"
                                        "(1) Resolver ticket.\n"
                                        "(2) Retificar ticket.\n"))
                    apagarTerminal()
                    break
                except:
                    apagarTerminal()

        if ret_res == 1:
            cursor.execute("select * from ticket where estadoTicket = 'Em atendimento'")
            resultados = cursor.fetchall()
            lista = []
            apagarTerminal()
            if resultados:
                for linha in resultados:
                    if linha[7] == "HW":
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Tipo:", linha[7], "Equipamento:", linha[8], "Avaria:", linha[9])
                        lista.append(linha[0])
                    else:
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Tipo:", linha[7], "Software:", linha[10], "Necessidade:", linha[11])
                        lista.append(linha[0])

                while True:
                    try:
                        escolha = int((input("Insira o ID do ticket que pretende modificar.\n")))
                        apagarTerminal()
                        break
                    except:
                        print("Insira apenas números inteiros.")

                while escolha not in lista:
                    for linha in resultados:
                        if linha[7] == "HW":
                            print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                                  "Tipo:", linha[7], "Equipamento:", linha[8], "Avaria:", linha[9])
                        else:
                            print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                                  "Tipo:", linha[7], "Software:", linha[10], "Necessidade:", linha[11])

                    while True:
                        try:
                            escolha = int(input(
                                "O ID do ticket que inseriu não consta na base de dados ou não está em atendimento. Por favor insira um ticket válido.\n"))
                            apagarTerminal()
                            break
                        except:
                            print("Insira apenas números inteiros.")

                res = str.upper(input("O problema ficou resolvido?(S/N) "))
                while res != "S" and res != "N":
                    res = str.upper(input("Por favor insira apenas 'S' ou 'N'. "))
                    apagarTerminal()

                if res == "S":
                    estadoAtend = "Resolvido"
                else:
                    estadoAtend = "Não resolvido"
                apagarTerminal()

                reparacao = input("Insira uma breve descrição da resolução do problema.\n")

                resolvido = datetime.now()
                sql = f"update ticket set estadoAtendimento = '{estadoAtend}' , estadoTicket = 'Atendido' , datahoraResolvido = '{resolvido}' , descRep = '{reparacao}' where idTicket = '{escolha}'"
                cursor.execute(sql)
                conexao.commit()
                apagarTerminal()
                print("Ticket modificado com sucesso.")

            else:
                apagarTerminal()
                print("Não existem tickets em atendimento.")

        else:
            cursor.execute("select * from ticket where estadoTicket = 'Por atender'")
            resultados = cursor.fetchall()
            lista = []
            apagarTerminal()
            for linha in resultados:
                if linha[7] == "HW":
                    print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Equipamento:",
                          linha[8], "Avaria:", linha[9])
                    lista.append(linha[0])
                else:
                    print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Software:",
                          linha[10], "Necessidade:", linha[11])
                    lista.append(linha[0])
            escolha = int((input("Insira o ID do ticket que pretende modificar.\n")))
            apagarTerminal()

            while escolha not in lista:
                for linha in resultados:
                    if linha[7] == "HW":
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Equipamento:",
                              linha[8], "Avaria:", linha[9])
                    else:
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Software:",
                              linha[10], "Necessidade:", linha[11])
                escolha = int(input(
                    "O ID do ticket que inseriu não consta na base de dados ou já está em atendimento. Por favor insira um ticket válido.\n"))
            apagarTerminal()

            tipo = str.upper(input("Qual o tipo do ticket?(HW/SW) "))

            while tipo != "HW" and tipo != "SW":
                tipo = str.upper(input("Por favor insira apenas 'HW' ou 'SW'. "))

            if tipo == 'HW':
                equipamento = input("Qual o equipamento? ")
                avaria = input("Qual a avaria? ")
                sql = f"update ticket set tipoTicket = 'HW' , equipamento = '{equipamento}' , avaria = '{avaria}' , software = NULL , necessidade = NULL where idTicket = '{escolha}'"
                cursor.execute(sql)

            else:
                software = input("Qual o software? ")
                necessidade = input("Qual a necessidade? ")
                sql = f"update ticket set tipoTicket = 'SW' , software = '{software}' , necessidade = '{necessidade}' , equipamento = NULL , avaria = NULL where idTicket = '{escolha}'"
                cursor.execute(sql)

            conexao.commit()
            apagarTerminal()
            print("Ticket modificado com sucesso.")

    else:
        sql = f"select * from ticket where estadoTicket = 'Por atender' and idColab = '{userID}'"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            lista = []
            for linha in resultados:
                if linha[7] == "HW":
                    print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Equipamento:",
                          linha[8], "Avaria:", linha[9])
                    lista.append(linha[0])
                else:
                    print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Software:",
                          linha[10], "Necessidade:", linha[11])
                    lista.append(linha[0])
            escolha = int((input("Insira o ID do ticket que pretende modificar.\n")))
            apagarTerminal()

            while escolha not in lista:
                for linha in resultados:
                    if linha[7] == "HW":
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Equipamento:",
                              linha[8], "Avaria:", linha[9])
                    else:
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Tipo:", linha[7], "Software:",
                              linha[10], "Necessidade:", linha[11])
                escolha = int(input(
                    "O ID do ticket que inseriu não consta na base de dados, já está em atendimento ou pertence a outro utilizador. Por favor insira um ticket válido.\n"))
            apagarTerminal()

            tipo = str.upper(input("Qual o tipo do ticket?(HW/SW) "))

            while tipo != "HW" and tipo != "SW":
                tipo = str.upper(input("Por favor insira apenas 'HW' ou 'SW'. "))

            if tipo == 'HW':
                equipamento = input("Qual o equipamento? ")
                avaria = input("Qual a avaria? ")
                sql = f"update ticket set tipoTicket = 'HW' , equipamento = '{equipamento}' , avaria = '{avaria}' , software = NULL , necessidade = NULL where idTicket = '{escolha}'"
                cursor.execute(sql)

            else:
                software = input("Qual o software? ")
                necessidade = input("Qual a necessidade? ")
                sql = f"update ticket set tipoTicket = 'SW' , software = '{software}' , necessidade = '{necessidade}' , equipamento = NULL , avaria = NULL where idTicket = '{escolha}'"
                cursor.execute(sql)

            conexao.commit()
            apagarTerminal()
            print("Ticket modificado com sucesso.")

        else:
            apagarTerminal()
            print("Já não tem tickets por atender. Contacte diretamente um técnico.")


def criarUser():

    """
        Criação de novo utilizador
    """

    while True:
        try:
            novo_idColab = int(input("Insira o ID do utilizador. "))
            break
        except:
            print("Insira apenas números inteiros.")
    novo_nomeColab = input("Insira o nome do utilizador.(Default: Convidado) ")
    while True:
        try:
            novo_pin = int(input("Insira um PIN. (4 dígitos) "))
            break
        except:
            print("Insira apenas números inteiros.")
    novo_cargo = input("Insira o cargo do utilizador:(Técnico, Vendedor, Operador. Default: Convidado) ")
    novo_utilizador = Users(novo_idColab, novo_nomeColab, novo_pin, novo_cargo)
    apagarTerminal()

    cursor.execute("select * from users")
    resultados = cursor.fetchall()
    lista = []
    for linha in resultados:
        lista.append(linha[0])

    if novo_utilizador.idColab in lista:
        print("Utilizador já se encontra na base de dados.\n"
              "Aplicação encerrada.")
        exit()

    else:
        sql = f"insert into users(idColab, nomeColab , pin , cargo) values('{novo_utilizador.idColab}' , '{novo_utilizador.nomeColab}' , '{novo_utilizador.pin}' , '{novo_utilizador.cargo}')"
        cursor.execute(sql)
        print("***************")
        print("Utilizador adicionado com sucesso.")

    conexao.commit()


def removerUser():

    """
       Remover um utilizador
    """
    cursor.execute("select * from users")
    resultados = cursor.fetchall()
    lista = []
    for linha in resultados:
        print("UserID:", linha[0], "Nome:", linha[1], "Cargo:", linha[2])
        lista.append(linha[0])

    while True:
        try:
            escolha = int((input("Insira o ID de utilizador que pretende remover.\n")))
            apagarTerminal()
            break
        except:
            print("Insira apenas números inteiros.")

    while escolha not in lista:
        for linha in resultados:
            print("UserID:", linha[0], "Nome:", linha[1], "Cargo:", linha[2])

        while True:
            try:
                escolha = int(input(
                    "O ID de utilizador que inseriu não consta na base de dados. Por favor insira um ID válido.\n"))
                apagarTerminal()
                break
            except:
                print("Insira apenas números inteiros.")

    sql = f"delete from users where idColab = '{escolha}'"
    cursor.execute(sql)
    print("Utilizador removido com sucesso.")
    conexao.commit()


def verificarTicket():

    """
      Verificar o estado dos tickets ( filtro por utilizador / ticket id )
    """

    sql = f"select * from ticket"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    listaTicket = []
    listaColab = []
    if resultados:
        for linha in resultados:
            if linha[7] == "HW":
                print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                      "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:", linha[6],
                      "Tipo:", linha[7], "Equipamento:", linha[8], "Avaria:", linha[9], "Desc. da reparação:",
                      linha[12])
                listaTicket.append(linha[0])
                listaColab.append(linha[1])
            else:
                print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                      "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:", linha[6],
                      "Tipo:", linha[7], "Software:", linha[10], "Necessidade:", linha[11], "Desc. da reparação:",
                      linha[12])
                listaTicket.append(linha[0])
                listaColab.append(linha[1])

        while True:
            try:
                escolha = int((input("Filtrar por:\n"
                                     "(1) Utilizador.\n"
                                     "(2) Ticket ID.\n"
                                     "(3) Sair.\n")))
                apagarTerminal()
                break
            except:
                print("Insira apenas números inteiros.")

        while escolha not in [1, 2, 3]:
            for linha in resultados:
                if linha[7] == "HW":
                    print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                          "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                          linha[6], "Tipo:", linha[7], "Equipamento:", linha[8], "Avaria:", linha[9],
                          "Desc. da reparação:", linha[12])
                else:
                    print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                          "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                          linha[6], "Tipo:", linha[7], "Software:", linha[10], "Necessidade:", linha[11],
                          "Desc. da reparação:", linha[12])

            while True:
                try:
                    escolha = int((input("Escolha inválida.\n"
                                         "Filtrar por:\n"
                                         "(1) Utilizador.\n"
                                         "(2) Ticket ID.\n"
                                         "(3) Sair.\n")))
                    apagarTerminal()
                    break
                except:
                    print("Insira apenas números inteiros.")

        if escolha == 1:
            while True:
                try:
                    user = int(input("Insira o ID do utilizador. "))
                    apagarTerminal()
                    break
                except:
                    print("Insira apenas números inteiros.")

            if user not in listaColab:
                for linha in resultados:
                    if linha[7] == "HW":
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                              linha[6], "Tipo:", linha[7], "Equipamento:", linha[8], "Avaria:", linha[9],
                              "Desc. da reparação:", linha[12])
                    else:
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                              linha[6], "Tipo:", linha[7], "Software:", linha[10], "Necessidade:", linha[11],
                              "Desc. da reparação:", linha[12])
                apagarTerminal()
                print("O utilizador não tem tickets registados na base de dados. ")

            else:
                sql = f"select * from ticket where idColab = '{user}'"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                for linha in resultados:
                    if linha[7] == "HW":
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                              linha[6], "Tipo:", linha[7], "Equipamento:", linha[8], "Avaria:", linha[9],
                              "Desc. da reparação:", linha[12])
                    else:
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                              linha[6], "Tipo:", linha[7], "Software:", linha[10], "Necessidade:", linha[11],
                              "Desc. da reparação:", linha[12])

        elif escolha == 2:
            while True:
                try:
                    ticket = int(input("Insira o ID do ticket. "))
                    apagarTerminal()
                    break
                except:
                    print("Insira apenas números inteiros.")

            if ticket not in listaTicket:
                for linha in resultados:
                    if linha[7] == "HW":
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                              linha[6], "Tipo:", linha[7], "Equipamento:", linha[8], "Avaria:", linha[9],
                              "Desc. da reparação:", linha[12])
                    else:
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                              linha[6], "Tipo:", linha[7], "Software:", linha[10], "Necessidade:", linha[11],
                              "Desc. da reparação:", linha[12])
                apagarTerminal()
                print("O ticket que inseriu não existe na base de dados. ")

            else:
                sql = f"select * from ticket where idTicket = '{ticket}'"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                for linha in resultados:
                    if linha[7] == "HW":
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                              linha[6], "Tipo:", linha[7], "Equipamento:", linha[8], "Avaria:", linha[9],
                              "Desc. da reparação:", linha[12])
                    else:
                        print("TicketID:", linha[0], "Data de criação:", linha[2], "Data de atendimento:", linha[3],
                              "Data de resolução:", linha[4], "Estado do ticket:", linha[5], "Estado do atendimento:",
                              linha[6], "Tipo:", linha[7], "Software:", linha[10], "Necessidade:", linha[11],
                              "Desc. da reparação:", linha[12])


def ticketsAtendidos():

    """
          Utiliza a função que está no ficheiro estatistica para calcular os tickets atendidos num intervalo datas
    """

    data_inicio_str = input("Insira a data de início (YYYY-MM-DD): ")
    data_fim_str = input("Insira a data de fim (YYYY-MM-DD): ")
    data_inicio = datetime.strptime(data_inicio_str, "%Y-%m-%d")
    data_fim = datetime.strptime(data_fim_str, "%Y-%m-%d")

    tickets_atendidos, porcentagem_atendidos = estatistica.tickets_atendidos_intervalo_datas(data_inicio, data_fim,
                                                                                             cursor)
    print("No intervalo de datas mencionado está(ão) ", tickets_atendidos,
          " ticket(s) atendido(s) sendo a percentagem igual a ", porcentagem_atendidos, "%.", sep="", end="\n")


def ticketsResolvidos():
    """
        Utiliza a função que está no ficheiro estatistica para calcular a percentagem dos tickets resolvidos / não resolvidos
    """
    porcentagem_resolvidos, porcentagem_nao_resolvidos = estatistica.porcentagem_tickets_resolvidos_naoresolvidos(
        cursor)
    print("A percentagem de tickets resolvidos é de ", porcentagem_resolvidos, "% e de não resolvidos é de ",
          porcentagem_nao_resolvidos, "%.", sep="", end="\n")


def mediaTempo():
    """
            Utiliza a função que está no ficheiro estatistica para calcular a media do tempo de atendimento por tipo ( HW / SW )
    """
    media_hw, media_sw = estatistica.media_tempo_atendimento_por_tipo(cursor)
    if media_hw == None:
        print("Média de tempo de resolução para tickets do tipo HW: Sem registos.")
    else:
        print("Média de tempo de resolução para tickets do tipo HW:", media_hw,
              "minutos(s) desde o momento em que foi atendido.")

    if media_sw == None:
        print("Média de tempo de resolução para tickets do tipo SW: Sem registos.")
    else:
        print("Média de tempo de resolução para tickets do tipo SW:", media_sw,
              "minutos(s) desde o momento em que foi atendido.")


def equipamentoTickets():

    """
        Utiliza a função que está no ficheiro estatistica para calcular o equipamento com mais tickets criados
    """

    equipamento_com_mais_tickets, total_tickets_equipamento = estatistica.equipamento_mais_tickets(cursor)
    if equipamento_com_mais_tickets:
        print(
            f"O equipamento com mais tickets associados é o '{equipamento_com_mais_tickets}' com um total de {total_tickets_equipamento} tickets criados.")
    else:
        print("Não há tickets de hardware registrados na base de dados.")


def softwareTickets():

    """
            Utiliza a função que está no ficheiro estatistica para calcular o software com mais tickets criados
    """

    software_com_mais_tickets, total_tickets_software = estatistica.software_mais_tickets(cursor)
    if software_com_mais_tickets:
        print(
            f"O software com mais tickets associados é o '{software_com_mais_tickets}' com um total de {total_tickets_software} tickets criados.")
    else:
        print("Não há tickets de software registrados na base de dados.")


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ticket2help"
)

cursor = conexao.cursor()
print("***************")
print("Login na aplicação Ticket2Help.")
print("***************")
idColab = input("UserID: ")
while True:
    try:
        pin = int(input("PIN: "))
        apagarTerminal()
        break
    except:
        print("Insira apenas números inteiros.")

if idColab == "Master" and pin == 9999:
    escolha = None
    while escolha != 12:

        escolha = escolhaOpcoes()

        if escolha == 1:
            criarTicket()

        elif escolha == 2:
            atenderTicket(None, idColab)

        elif escolha == 3:
            modificarTicket(None, idColab)

        elif escolha == 4:
            criarUser()

        elif escolha == 5:
            removerUser()

        elif escolha == 6:
            verificarTicket()

        elif escolha == 7:
            ticketsAtendidos()

        elif escolha == 8:
            ticketsResolvidos()

        elif escolha == 9:
            mediaTempo()

        elif escolha == 10:
            equipamentoTickets()

        elif escolha == 11:
            softwareTickets()

        elif escolha == 12:
            print("Aplicação encerrada.")
            exit()

sql = f"select * from users where idColab = '{idColab}' and pin = '{pin}'"
cursor.execute(sql)
resultados = cursor.fetchone()

if resultados:
    userID = resultados[0]
    nome = resultados[1]
    cargo = resultados[3]
    escolha = None
    while escolha != 12:

        escolha = escolhaOpcoes()

        if escolha == 1:
            criarTicket()

        elif escolha == 2:
            if cargo == "Técnico":
                atenderTicket(cargo, idColab)
            else:
                print("Utilizador sem acesso a esta função.")

        elif escolha == 3:
            modificarTicket(cargo, idColab)

        elif escolha == 4:
            if cargo == "Técnico":
                criarUser()
            else:
                print("Utilizador sem acesso a esta função.")

        elif escolha == 5:
            if cargo == "Técnico":
                removerUser()
            else:
                print("Utilizador sem acesso a esta função.")

        elif escolha == 6:
            verificarTicket()

        elif escolha == 7:
            ticketsAtendidos()

        elif escolha == 8:
            ticketsResolvidos()

        elif escolha == 9:
            mediaTempo()

        elif escolha == 10:
            equipamentoTickets()

        elif escolha == 11:
            softwareTickets()

        elif escolha == 12:
            print("Aplicação encerrada.")
            conexao.close()
            exit()

else:
    print(
        "Utilizador sem acesso à aplicação ou dados inseridos errados. Caso continue sem conseguir fazer login, por favor contacte um técnico.")
    print("Aplicação encerrada.")
    conexao.close()
    exit()
