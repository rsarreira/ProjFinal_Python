from tickets import Tickets
from users import Users
import mysql.connector

#t1 = Tickets("26", "", "SW")
#print (t1)
#p1 = Users ()
#print (p1)

#p2 = Users("ronye","informatico")
#print(p2)


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
        #print("ID:", resultado[0])
        #print("Utilizador:", resultado[1])
        print("UserId/Password corretos")
        print("********************")
        escolha = input("Quer inserir novo Ticket (1)\n"
                              "listar os tickets atendidos num intervalo de datas(2)\n"
                              "listar tickets resolvidos (3)\n"
                              "listar tickets não resolvidos (4)\n"
                              "media de tempo de atendimento de cada tipo de ticket (5)\n")
        if escolha=="1":
            tipoTicket = input("Qual o tipo de ticket que quer abrir: ")
            t1 = Tickets(idcolab, "", tipoTicket)
            print(t1)
            #sql = f"insert into ticket(datahora_gerado, cod_colab, tipo, estado_ticket) values('{t1.data}','{idcolab}','{tipoTicket}','{t1.status}');"


            if tipoTicket=="HW":
                equipamento = input("Qual o tipo de equipamento: ")
                avaria = input("Qual o tipo de avaria: ")
            if tipoTicket=="SW":
                tiposw = input("Qual o tipo de sw: ")
                descnes = input("Qual a descricao/necessidade: ")
                sql = f"insert into ticket(datahora_gerado, cod_colab, tipo, estado_ticket, desc_necess, software) values('{t1.data}','{idcolab}','{tipoTicket}','{t1.status}','{descnes}','{tiposw}');"
            cursor.execute(sql)
            conexao.commit()
                #sql2 = f"SELECT * FROM ticket WHERE cod_colab = {idcolab} AND datahora_gerado = '{t1.data}'"
                #pesquisa2 = Tickets(cursor.execute(sql2))
                #resultados2 = cursor.fetchall()
                #if resultados2:
                #    for resultado in resultados2:
                #        print("ID:", resultado[0])
                #sql3 = f"insert into tickets(datahora_gerado, cod_colab, tipo, estado_ticket) values('{t1.data}','{idcolab}','{tipoTicket}','{t1.status}');"


else:
    print("UserId sem acesso á aplicação")
    print("********************")
    respostaUser = input("Quer inserir novo User (S/N) : ")
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