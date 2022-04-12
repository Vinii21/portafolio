from flask import Flask, render_template

app = Flask(__name__);

@app.route('/')
def muebleria():
    return render_template('portafolio.html')

""" @app.route('/b3ie2nes-ra3ic1es')
def bienesRaices():
    return render_template('raices.html'); """

if __name__ == '__main__':
    app.run(debug=True)