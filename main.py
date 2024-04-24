from tickets import Tickets
import mysql.connector

#p1 = Tickets ()
#print (p1)

#p2 = Tickets("233444","por atender","HW")
#print(p2)


# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ticket2help"
)

cursor = conexao.cursor()

idcolab = input("Qual o seu id colaborador: ")
tipo = input("Qual o tipo do seu ticket: ")

sql = (f"insert into tickets(codigo_colaborador, estado,tipo,data_hora) values('{idcolab}','{tipo}','{tipo},"
       f"'{idcolab}');")

# Executar um insert
criacao = Tickets(cursor.execute(sql))

# Executar um update
# cursor.execute("update client set city='VNGaia' where name='rui';")

# Executar um delete
#cursor.execute("delete from client where name='rui';")

# IMPORTANTE: Confirmar a transaÃ§Ã£o
conexao.commit()


conexao.close()
