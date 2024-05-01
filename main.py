from tickets import Tickets
from users import Users
from sw import SW
from hw import HW
import mysql.connector

# Conectar ao banco de dados
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

sql = f"select * from users where idColab = '{idColab}' and pin = '{pin}'"
pesquisa = cursor.execute(sql)
resultados = cursor.fetchone()

if resultados:
    userID = resultados[0]
    nome = resultados[1]
    cargo = resultados[3]
    for resultado in resultados:
        print("Dados corretos.")
        print("UserID:" , userID)
        print("Nome:" , nome)
        print("Cargo: " , cargo)
        escolha = int(input("Insira a ação que deseja efetuar:\n"
                        "(1) Criar ticket.\n"
                        "(2) Atender ticket.\n"
                        "(3) Modificar ticket.\n"
                        "(4) Visualizar % tickets atendidos num intervalo de datas.\n"
                        "(5) Visualizar % de tickets resolvidos e não resolvidos.\n"
                        "(6) Visualizar a média de tempo de atendimento de cada tipo de ticket.\n"
                        "(7) Fechar a aplicação"))
        while escolha < 1 or escolha >5:
            escolha = int(input("Por favor insira apenas uma das opções abaixo:\n"
                        "(1) Criar ticket.\n"
                        "(2) Atender ticket.\n"
                        "(3) Modificar ticket.\n"
                        "(4) Visualizar % tickets atendidos num intervalo de datas.\n"
                        "(5) Visualizar % de tickets resolvidos e não resolvidos.\n"
                        "(6) Visualizar a média de tempo de atendimento de cada tipo de ticket.\n"
                        "(7) Fechar a aplicação"))
           
        if escolha == 1:
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

            conexao.commit()
            
        elif escolha == 2:
            pesquisa = cursor.execute("SELECT * FROM ticket WHERE estadoTicket = 'Por atender'")
            resultados = cursor.fetchall()
            lista = []
            for linha in resultados:
                if linha[7] == "HW":
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Equipamento:" , linha[8] , "Avaria:" , linha[9])
                    lista.append(linha[0])
                else:
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Software:" , linha[10] , "Necessidade:" , linha[11])
                    lista.append(linha[0])
            escolha = int((input("Insira o ID do ticket que pretende atender. ")))

            while escolha not in lista:
                print("O ID do ticket que inseriu não consta na base de dados ou já está em atendimento. Por favor inserir um ticket válido.")              
                if linha[7] == "HW":
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Equipamento:" , linha[8] , "Avaria:" , linha[9])
                else:
                    print("TicketID:" , linha[0] , "Data:" , linha[2] , "Tipo:" , linha[7] , "Software:" , linha[10] , "Necessidade:" , linha[11])

                escolha = int(input("Insira o ID do ticket que pretende atender. "))
            
            sql = f"UPDATE ticket SET estadoAtendimento = 'Aberto' , estadoTicket = 'Em atendimento' WHERE idTicket = '{escolha}'"
            pesquisa = cursor.execute(sql)
            conexao.commit()

        elif escolha == "3":
            pesquisa = cursor.execute("SELECT * FROM ticket")
            resultados = cursor.fetchall()
            for resultado in resultados:
                if resultado[7] == "HW":
                    print("TicketID:" , resultado[0] , "Data:" , resultado[2] , "Tipo:" , resultado[7] , "Equipamento:" , resultado[8] , "Avaria:" , resultado[9])
                else:
                    print("TicketID:" , resultado[0] , "Data:" , resultado[2] , "Tipo:" , resultado[7] , "Software:" , resultado[10] , "Necessidade:" , resultado[11])

            escolha = int(input("Insira o ID do ticket que pretende modificar. "))

            while escolha is not resultados[0]:
                print("O ID do ticket que inseriu não consta na base de dados. Por favor inserir um ticket válido.")
                escolha = int(input("Insira o ID do ticket que pretende modificar. "))
            
            if resultado[7] == "HW":
                ticket = HW(resultado)
            else:
                ticket = SW(resultado)
            
            if cargo == "Técnico":
                nDados = input("Quantos dados pretende modificar?(1/2) ")
                dados = []
                for i in range(nDados):
                    dado = input("Que dado pretende modificar?\n"
                                "(1) Estado do atendimento.\n"
                                "(2) Descrição da reparação.\n")
                    if dado == dados[i-1] or dado < 1 or dado > 2:
                        print("A sua escolha deve estar contida na lista e ser diferente das anteriores.")
                        dado = input("Que dado pretende modificar?\n"
                                    "(1) Estado do atendimento.\n"
                                    "(2) Descrição da reparação.\n")
                    dados.append(dado)
                dados.sort()

            else:
                nDados = input("Quantos dados pretende modificar?(1-5) ")
                dados = []
                for i in range(nDados):
                    dado = input("Que dado pretende modificar?\n"
                                "(1) Tipo do Ticket.\n"
                                "(2) Equipamento.\n"
                                "(3) Avaria.\n"
                                "(4) Software.\n"
                                "(5) Necessidade.\n")
                    if dado == dados[0] or dado == dados[1] or dado == dados[2] or dado == dados[3] or dado == dados[4] or dado <1 or dado > 5:
                        print("A sua escolha deve estar contida na lista e ser diferente das anteriores.")
                        dado = input("Que dado pretende modificar?\n"
                                    "(1) Tipo do Ticket.\n"
                                    "(2) Equipamento.\n"
                                    "(3) Avaria.\n"
                                    "(4) Software.\n"
                                    "(5) Necessidade.\n")
                    dados.append(dado)
                dados.sort()
            pesquisa = cursor.execute("UPDATE ticket SET estadoAtendimento = 'Aberto' WHERE idTicket = '{ticket.idTicket}'")
            conexao.commit()

else:
    print("Utilizador sem acesso à aplicação.")

    respostaUser = str.upper(input("Quer adicionar um novo utilizador à base de dados?(S/N) "))
    
    while respostaUser != "S" and respostaUser != "N":
        respostaUser = str.upper(input("Por favor insira apenas 'S' ou 'N'. "))
    
    if respostaUser == 'S':
        novo_idColab = int(input("Insira o ID do utilizador. "))
        novo_nomeColab = input("Insira o nome do utilizador. ")
        novo_pin = int(input("Insira um PIN. (4 dígitos) "))
        novo_cargo = input("Insira o cargo do utilizador: ")
        novo_utilizador = Users(novo_idColab , novo_nomeColab , novo_pin , novo_cargo)
        #print(novo_utilizador)

        sql = f"insert into users(idColab, nomeColab , pin , cargo) values('{novo_utilizador.idColab}' , '{novo_utilizador.nomeColab}' , '{novo_utilizador.pin}' , '{novo_utilizador.cargo}')"
        cursor.execute(sql)
        conexao.commit()
'''       
        pesquisa = cursor.execute("SELECT * FROM users")
        resultados = cursor.fetchall()
        if resultados:
            for resultado in resultados:
                if novo_utilizador.idColab == resultados[0]:
                    print("ID já se encontra na base de dados.")
        else:
            cursor.execute("INSERT INTO users (idColab, nomeColab , pin , cargo) VALUES ('{novo_idColab}' , '{novo_nomeColab}' , '{novo_pin}', '{novo_cargo}')")
            print("Novo utilizador inserido com sucesso.")
        
        conexao.commit()
    else:
        print("Aplicação finalizada.")
'''

conexao.close()
#

