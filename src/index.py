from flask import Flask, render_template

app = Flask(__name__);

@app.route('/')
def muebleria():
    return render_template('portafolio.html')

if __name__ == '__main__':
    app.run(debug=True)