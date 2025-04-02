from flask import Flask, request
app = Flask(__name__)
@app.route("/alkuluku/<kokonaisluku>")
def alkuluku(kokonaisluku):
    prime = int(kokonaisluku)
    primecount = 2

    for i in range(1, prime + 1):
        if prime%i == 0:
            primecount -= 1
    

    if primecount < 0:
        vastaus = {
            "Number": prime,
            "isPrime": False
        }
    else:
        vastaus = {
            "Number": prime,
            "isPrime": True
        }
    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)