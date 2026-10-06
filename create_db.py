import sqlite3

conexao = sqlite3.connect('series.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS catalogo (
    titulo TEXT PRIMARY KEY,
    genero TEXT,
    ano_lancamento INTEGER,
    temporadas INTEGER
)
''')

conexao.commit()
conexao.close()