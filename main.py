from tickets import Tickets
from users import Users
from sw import SW
from hw import HW
import mysql.connector
from datetime import datetime

def escolhaOpcoes():
    escolha = int(input("Insira a ação que deseja efetuar:\n"
                            "(1) Criar ticket.\n"
                            "(2) Atender ticket.\n"
                            "(3) Modificar ticket.\n"
                            "(4) Visualizar % tickets atendidos num intervalo de datas.\n"
                            "(5) Visualizar % de tickets resolvidos e não resolvidos.\n"
                            "(6) Visualizar a média de tempo de atendimento de cada tipo de ticket.\n"
                            "(7) Fechar a aplicação\n"))
    while escolha < 1 or escolha > 7:
        escolha = int(input("Por favor insira apenas uma das opções abaixo:\n"
                    "(1) Criar ticket.\n"
                    "(2) Atender ticket.\n"
                    "(3) Modificar ticket.\n"
                    "(4) Visualizar % tickets atendidos num intervalo de datas.\n"
                    "(5) Visualizar % de tickets resolvidos e não resolvidos.\n"
                    "(6) Visualizar a média de tempo de atendimento de cada tipo de ticket.\n"
                    "(7) Fechar a aplicação\n"))
        
    return escolha

def criarUser():
    novo_idColab = int(input("Insira o ID do utilizador. "))
    novo_nomeColab = input("Insira o nome do utilizador. ")
    novo_pin = int(input("Insira um PIN. (4 dígitos) ")) 
    novo_cargo = input("Insira o cargo do utilizador: ")
    novo_utilizador = Users(novo_idColab , novo_nomeColab , novo_pin , novo_cargo)

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
        print("Utilizador adicionado com sucesso.")
        conexao.commit()

def criarTicket():
    tipoTicket = str.upper(input("Que tipo de ticket deseja criar?(HW/SW) "))

    while tipoTicket != "HW" and tipoTicket != "SW":
        tipoTicket = str.upper(input("Por favor insira apenas 'SW' ou 'HW'. "))

    if tipoTicket == "HW":
        equipamento = input("Qual o equipamento? ")
        avaria = input("Qual a avaria? ")
        hw = HW(idColab , "HW" , equipamento , avaria)
        sql = f"insert into ticket(idColab , datahoraGerado , estadoTicket , tipoTicket , equipamento , avaria) values('{hw.idColab}' , '{hw.datahoraGerado}' , '{hw.estadoTicket}' , '{hw.tipoTicket}' , '{hw.equipamento}' , '{hw.avaria}')"
        cursor.execute(sql)

    if tipoTicket == "SW":
        software = input("Qual o software? ")
        necessidade = input("Qual a necessidade? ")
        sw = SW(idColab , "SW" , software , necessidade)
        sql = f"insert into ticket(idColab , datahoraGerado , estadoTicket , tipoTicket , software , necessidade) values('{sw.idColab}' , '{sw.datahoraGerado}' , '{sw.estadoTicket}' , '{sw.tipoTicket}' , '{sw.software}' , '{sw.necessidade}')"
        cursor.execute(sql)
        
    print("Ticket criado com sucesso.")
    conexao.commit()

def atenderTicket():
    cursor.execute("select * from ticket where estadoTicket = 'Por atender'")
    resultados = cursor.fetchall()
    lista = []
    if cargo == "Técnico" or cargo == "Master":
        for linha in resultados:
            if linha[7] == "HW":
                print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Equipamento:" , linha[8] , "Avaria:" , linha[9])
                lista.append(linha[0])
            else:
                print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Software:" , linha[10] , "Necessidade:" , linha[11])
                lista.append(linha[0])
        escolha = int((input("Insira o ID do ticket que pretende atender.\n")))

        while escolha not in lista:
            for linha in resultados:       
                if linha[7] == "HW":
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Equipamento:" , linha[8] , "Avaria:" , linha[9])
                else:
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Software:" , linha[10] , "Necessidade:" , linha[11])
            escolha = int(input("O ID do ticket que inseriu não consta na base de dados ou já está em atendimento. Por favor insira um ticket válido.\n"))
        
        atendido = datetime.now()
        sql = f"update ticket set estadoAtendimento = 'Aberto' , estadoTicket = 'Em atendimento' , datahoraAtendido = '{atendido}' where idTicket = '{escolha}'"
        cursor.execute(sql)
        print("Ticket atendido com sucesso.")
        conexao.commit()
    else:
        print("Utilizador sem acesso à opção selecionada.")

def modificarTicket():
    if cargo == "Técnico" or cargo == "Master":
        cursor.execute("select * from ticket where estadoTicket = 'Em atendimento'")
        resultados = cursor.fetchall()
        lista = []
        for linha in resultados:
            if linha[7] == "HW":
                print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Equipamento:" , linha[8] , "Avaria:" , linha[9])
                lista.append(linha[0])
            else:
                print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Software:" , linha[10] , "Necessidade:" , linha[11])
                lista.append(linha[0])
        escolha = int((input("Insira o ID do ticket que pretende modificar.\n")))

        while escolha not in lista:
            for linha in resultados:
                if linha[7] == "HW":
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Equipamento:" , linha[8] , "Avaria:" , linha[9])
                else:
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Software:" , linha[10] , "Necessidade:" , linha[11])
            escolha = int(input("O ID do ticket que inseriu não consta na base de dados ou não está em atendimento. Por favor inserir um ticket válido.\n"))

        res = str.upper(input("O problema ficou resolvido?(S/N) "))
        while res != "S" and res != "N":
            res = str.upper(input("Por favor insira apenas 'S' ou 'N'. "))

        if res == "S":
            estadoAtend = "Resolvido"
        else:
            estadoAtend = "Não resolvido"
        
        reparacao = input("Insira uma breve descrição da resolução do problema.\n")

        resolvido = datetime.now()
        sql = f"update ticket set estadoAtendimento = '{estadoAtend}' , estadoTicket = 'Atendido' , datahoraResolvido = '{resolvido}' , descRep = '{reparacao}' where idTicket = '{escolha}'"
        cursor.execute(sql)
        print("Ticket modificado com sucesso.")
        conexao.commit()

    else:
        sql = f"select * from ticket where estadoTicket = 'Por atender' and idColab = '{userID}'"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        lista = []
        for linha in resultados:
            if linha[7] == "HW":            
                print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Equipamento:" , linha[8] , "Avaria:" , linha[9])
                lista.append(linha[0])
            else:
                print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Software:" , linha[10] , "Necessidade:" , linha[11])
                lista.append(linha[0])
        escolha = int((input("Insira o ID do ticket que pretende modificar.\n")))

        while escolha not in lista:
            for linha in resultados:
                if linha[7] == "HW":
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Equipamento:" , linha[8] , "Avaria:" , linha[9])
                else:
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Software:" , linha[10] , "Necessidade:" , linha[11])
            escolha = int(input("O ID do ticket que inseriu não consta na base de dados, já está em atendimento ou pertence a outro utilizador. Por favor inserir um ticket válido.\n"))

        tipo = str.upper(input("Deseja modificar o tipo do ticket?(S/N) "))
        while tipo != "S" and tipo != "N":
            tipo = str.upper(input("Por favor insira apenas 'S' ou 'N'. "))

        if tipo == 'S':
            tipo2 = str.upper(input("Insira o novo tipo para o ticket.(HW/SW) "))       
            while tipo2 != "HW" and tipo2 != "SW":
                tipo2 = str.upper(input("Por favor insira apenas 'HW' ou 'SW'. "))

            if tipo2 == "HW":
                equipamento = input("Qual o equipamento? ")
                avaria = input("Qual a avaria? ")
                #hw = HW("HW" , equipamento , avaria)
                sql = f"update ticket set tipoTicket = 'HW' , equipamento = '{equipamento}' , avaria = '{avaria}' , software = NULL , necessidade = NULL where idTicket = '{escolha}'"
                cursor.execute(sql)
            
            else:
                software = input("Qual o software? ")
                necessidade = input("Qual a necessidade? ")
                #sw = SW("SW" , software , necessidade)
                sql = f"update ticket set tipoTicket = 'SW' , software = '{software}' , necessidade = '{necessidade}' , equipamento = NULL , avaria = NULL where idTicket = '{escolha}'"
                cursor.execute(sql)

        else:
            
        print("Ticket modificado com sucesso.")
        conexao.commit()


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ticket2help"
)


cursor = conexao.cursor()
print ("Login na aplicação Ticket2Help.")
idColab = input("UserID: ")
pin = input("PIN: ")

#if idColab == "Master" and pin == 9999


sql = f"select * from users where idColab = '{idColab}' and pin = '{pin}'"
pesquisa = cursor.execute(sql)
resultados = cursor.fetchone()


if resultados:
    userID = resultados[0]
    nome = resultados[1]
    cargo = resultados[3]
    print("*****")
    print("Dados corretos.")
    print("UserID:" , userID)
    print("Nome:" , nome)
    print("Cargo:" , cargo)
    print("*****")
    escolha = None
    while escolha != 7:

        escolha = escolhaOpcoes()

        if escolha == 1:
            criarTicket()

        elif escolha == 2:
            atenderTicket()

        elif escolha == 3:
            modificarTicket()
        
        elif escolha == 4:

            #data_inicio_str = input("Insira a data de início (YYYY-MM-DD): ")
            #data_fim_str = input("Insira a data de fim (YYYY-MM-DD): ")
            data_inicio_str = '2020-01-01'
            data_fim_str = '2025-01-01'
            # Converta as strings de data para objetos datetime
            data_inicio = datetime.strptime(data_inicio_str, "%Y-%m-%d")
            data_fim = datetime.strptime(data_fim_str, "%Y-%m-%d")

            # Chame o método para contar os tickets atendidos no intervalo
            tickets = Tickets(cursor)
            tickets_atendidos, porcentagem_atendidos = tickets.contar_tickets_atendidos_no_intervalo(data_inicio, data_fim, cursor)
            print("no intervalo de datas mencionado estão",tickets_atendidos,"tickets atendidos sendo a percentagem=",porcentagem_atendidos,"%")


        elif escolha == 5:

            #data_inicio_str = input("Insira a data de início (YYYY-MM-DD): ")
            #data_fim_str = input("Insira a data de fim (YYYY-MM-DD): ")
            data_inicio_str = '2020-01-01'
            data_fim_str = '2025-01-01'
            # Converta as strings de data para objetos datetime
            data_inicio = datetime.strptime(data_inicio_str, "%Y-%m-%d")
            data_fim = datetime.strptime(data_fim_str, "%Y-%m-%d")

            # Chame o método para contar os tickets atendidos no intervalo
            tickets = Tickets(cursor)
            porcentagem_resolvidos, porcentagem_nao_resolvidos = tickets.calcular_porcentagem_tickets_resolvidos(data_inicio, data_fim, cursor)
            print("A porcentagem de tickets resolvidos é",porcentagem_resolvidos,"e nao resolvidos é",porcentagem_nao_resolvidos,"%")


        elif escolha == 7:
            print("Aplicação encerrada.")
            exit()

else:
    print("Utilizador sem acesso à aplicação ou dados inseridos errados.")

    respostaUser = str.upper(input("Deseja adicionar um novo utilizador à base de dados?(S/N) "))
    
    while respostaUser != "S" and respostaUser != "N":
        respostaUser = str.upper(input("Por favor insira apenas 'S' ou 'N'. "))
    
    if respostaUser == 'S':
        criarUser()
    else:
        print("Aplicação encerrada.")
        exit()

conexao.close()
#exit()