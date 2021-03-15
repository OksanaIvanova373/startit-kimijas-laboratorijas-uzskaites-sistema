
import sqlite3
import requests

conn = sqlite3.connect('Dati.db')


c = conn.cursor()

inventars_api_res = requests.get('https://pytonc.eu.pythonanywhere.com/api/v1/inventars')

inventars = inventars_api_res.json()

for inv in inventars:
    c.execute("INSERT INTO Inventars (ID, NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, KOMENTARI) values (?, ?, ?, ?, ?, ?)", [inv['id'], inv['nosaukums'], inv['tips'], inv['apakstips'], inv['skaits'], inv['komentari']])



#print(inventars)

c.execute('CREATE TABLE IF NOT EXISTS Inventars (ID INTEGER PRIMARY KEY, NOSAUKUMS TEXT, TIPS TEXT, APAKSTIPS TEXT, SKAITS INTEGER, KOMENTARI TEXT)')
#c.execute("INSERT INTO Inventars (NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, KOMENTARI) VALUES ('Mērkolba','Trauks','Mērtrauks',2,'Trauks ar tiplumu 300ml, kas paredzēts šķidrumu mērīšanai')")
c.execute("DELETE FROM Inventars WHERE ID > 1")

c.execute("UPDATE Inventars SET APAKSTIPS = 'Trauki' WHERE ID = 1")

conn.commit()



c.execute("SELECT * FROM Inventars")
print(c.fetchall())



c.close()
conn.close()
