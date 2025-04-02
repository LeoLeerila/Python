from flask import Flask, request
import mysql.connector

app = Flask(__name__)
@app.route("/kenttä/<ICAO>")

def kenttä(ICAO):
    tiedot = haeTiedot(ICAO)
    
    vastaus = {
        "ICAO": ICAO,
        "Name": tiedot[0][0],
        "Municipality": tiedot[0][1]
    }
    
    return vastaus

def haeTiedot(Koodi):
    yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='leo',
    password='Leerila',
    autocommit=True
    )

    kursori = yhteys.cursor()
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{Koodi}"'
    kursori.execute(sql)
    tulos = kursori.fetchall()
    
    return tulos



if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)