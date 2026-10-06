import sqlite3

conn = sqlite3.connect('series.db')
cursor = conn.cursor()

cursor.execute(
    '''
        INSERT INTO catalogo(
            titulo, genero, ano_lancamento, temporadas
        ) VALUES (?, ?, ?, ?)
    ''',
    ("Friends", "Sitcom", 1994, 10)
)












conn.commit()
conn.close()
