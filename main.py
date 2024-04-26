#from tickets import Tickets
from users import Users
import mysql.connector

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
#tipo = input("Qual o tipo do seu ticket: ")

#sql = (f"insert into tickets(codigo_colaborador, estado,tipo,data_hora) values('{idcolab}','{tipo}','{tipo},"
 #      f"'{idcolab}');")

#sql = (f"select * from users where {id} = 1")
 #      f"'{idcolab}');")

# Executar um insert
#criacao = Tickets(cursor.execute(sql))

# Executar um update
 #cursor.execute("update client set city='VNGaia' where name='rui';")

sql = f"SELECT * FROM users WHERE id = {idcolab} AND utilizador = '{password}'"
pesquisa = Users(cursor.execute(sql))
resultados = cursor.fetchall()

if resultados:
    for resultado in resultados:
        #print("ID:", resultado[0])
        #print("Utilizador:", resultado[1])
        print("UserId/Password corretos")
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
        print("Erro ao inserir novo utilizador.")



# Executar um delete
#cursor.execute("delete from client where name='rui';")

# IMPORTANTE: Confirmar a transaÃ§Ã£o
conexao.commit()


conexao.close()
#