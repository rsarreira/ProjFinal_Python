from tickets import Tickets
from users import Users
from swt import Swt
from hwt import Hwt
import mysql.connector

'''
t1 = Tickets("26", "", "HW")
print (t1)

a1 = Swt("26", "", "SW","windows","install")
print (a1)

h1 = Hwt("26", "", "HW","desktop","partiu","descrever")
print (h1)

#p1 = Users ()
#print (p1)

#p2 = Users("ronye","informatico")
#print(p2)

'''

# Conectar ao banco de dados~
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ticket2help"
)

cursor = conexao.cursor()
print ("********************")
idcolab = input("UserId: ")
password = input("password: ")
print ("********************")


sql = f"SELECT * FROM users WHERE cod_colab = {idcolab} AND utilizador = '{password}'"
pesquisa = Users(cursor.execute(sql))
resultados = cursor.fetchall()




if resultados:
    for resultado in resultados:
        print("ID:", resultado[2])
        #print("Utilizador:", resultado[1])
        print("UserId/Password corretos")
        print("********************")
        escolha = input("Quer inserir novo Ticket (1)\n"
                              "listar os tickets atendidos num intervalo de datas(2)\n"
                              "listar tickets resolvidos (3)\n"
                              "listar tickets não resolvidos (4)\n"
                              "media de tempo de atendimento de cada tipo de ticket (5)\n"
                              "Atender ticket (6)\n")
        if escolha=="1":
            tipoTicket = str.upper(input("Qual o tipo de ticket que quer abrir: "))
            #t1 = Tickets(idcolab,"", tipoTicket)
            #print(t1)
            #sql = f"insert into ticket(datahora_gerado, cod_colab, tipo, estado_ticket) values('{t1.data}','{idcolab}','{tipoTicket}','{t1.status}');"

            if tipoTicket=="HW":
                equipamento = input("Qual o tipo de equipamento: ")
                avaria = input("Qual o tipo de avaria: ")
                desc_rep = None
                estado_atend = None
                hw1 = Hwt(idcolab, "", tipoTicket, equipamento, avaria, desc_rep, estado_atend)
                #print(a1)
                sql = f"INSERT INTO ticket(datahora_gerado, cod_colab, tipo, estado_ticket, equipamento, avaria, desc_rep, estado_atend) VALUES('{hw1.datahora_gerado}', '{hw1.cod_colab}', '{hw1.tipo}', '{hw1.estado_ticket}', '{hw1.equipamento}', '{hw1.avaria}', '{hw1.desc_rep}', '{hw1.estado_atend}');"
            if tipoTicket=="SW":
                tipo = input("Qual o tipo de sw: ")
                descnes = input("Qual a descricao/necessidade: ")
                estado_atend = None
                sw1 = Swt(idcolab, "", tipoTicket, tipo, descnes, estado_atend)
                #print(a1)
                sql = f"INSERT INTO ticket(datahora_gerado, cod_colab, tipo, estado_ticket, desc_necess, software, estado_atend) VALUES('{sw1.datahora_gerado}', '{sw1.cod_colab}', '{sw1.tipo}', '{sw1.estado_ticket}', '{sw1.desc_necess}', '{sw1.software}', '{sw1.estado_atend}');"

            cursor.execute(sql)
            conexao.commit()
                #sql2 = f"SELECT * FROM ticket WHERE cod_colab = {idcolab} AND datahora_gerado = '{t1.data}'"
                #pesquisa2 = Tickets(cursor.execute(sql2))
                #resultados2 = cursor.fetchall()
                #if resultados2:
                #    for resultado in resultados2:
                #        print("ID:", resultado[0])
                #sql3 = f"insert into tickets(datahora_gerado, cod_colab, tipo, estado_ticket) values('{t1.data}','{idcolab}','{tipoTicket}','{t1.status}');"

        elif escolha=="6":
            sql2 = f"SELECT * FROM ticket WHERE estado_ticket = 'por atender'"
            pesquisa2 = cursor.execute(sql2)
            resultados2 = cursor.fetchall()
            for resultado in resultados2:
                if resultado[4] == 'HW':
                    print("ID:", resultado[0],"Data:", resultado[1],"Tipo:", resultado[4], "Equipamento:", resultado[7],"Avaria:", resultado[8])
                else:
                    print("ID:", resultado[0],"Data:", resultado[1],"Tipo:", resultado[4], "Software:", resultado[10],"Descrição problema:", resultado[11])
        
            escolha = int(input("Inserir o ID do ticket que quer atender: "))
            sql2 = f"UPDATE tickets SET estado_atend = 'Em atendimento' WHERE id = {escolha}"
            pesquisa2 = cursor.execute(sql2)
            
            atend = str.upper(input("O problema ficou resolvido? (S/N)"))
            if atend == "S":
                sql2 = f"UPDATE tickets SET estado_atend = 'Em atendimento' WHERE id = {escolha}"
            elif atend == "N":
                


else:
    print("UserId sem acesso á aplicação")
    print("********************")
    respostaUser = str.upper(input("Quer inserir novo User (S/N) : "))
    print("********************")
    if respostaUser == 'S':
        novo_utilizador = input("Novo utilizador: ")
        novo_cargoemp = input("Cargo do novo utilizador: ")
        sql_insert = f"INSERT INTO users (utilizador, cargoemp) VALUES ('{novo_utilizador}', '{novo_cargoemp}')"
        cursor.execute(sql_insert)
        conexao.commit()
        print("Novo utilizador inserido com sucesso!")
        cursor.execute(f"SELECT * FROM users WHERE utilizador = '{novo_utilizador}'")
        novo_usuario = cursor.fetchone()
        if novo_usuario:
            novo_usuario_objeto = Users(novo_usuario[0], novo_usuario[1],novo_usuario[2])
            print("Dados:", novo_usuario_objeto)
        else:
            print("Erro ao encontrar novo utilizador inserido.")
    else:

        #print("Erro ao inserir novo utilizador.")
        print("Insira")


# Executar um delete
#cursor.execute("delete from client where name='rui';")

# IMPORTANTE: Confirmar a transaÃ§Ã£o
conexao.commit()


conexao.close()
#
