from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Labrīt!"

@app.route('/sveiki')
def sveiki():
  return "Nav vairs nekāds rīts!"

@app.route('/sveiki/<vards>')  
def sveikiPersona(vards):
  return "Sveiki {}".format(vards)#f"Sveiki {vards}"#

@app.route('/cik/<sk1>/<sk2>')    
def reizinajums(sk1,sk2):
  sk1=int(sk1)
  sk2=int(sk2)
  reizinajums = sk1 * sk2
  return reizinajums

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)

