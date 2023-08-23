import mysql.connector

#Aonde serão colocados os dados do seu mysql
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='crud'
)
cursor = conexao.cursor()

# Create
nome_produto = "sapato"
valor = 70
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#Read
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
for pos, v in enumerate(resultado):
    print(f'ID: {v[0]} Nome: "{v[1]}" Valor: {v[2]}')


#Update
nome_produto = "sapato"
valor = 50
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#Delete
nome_produto = "sapato"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()