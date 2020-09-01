#/usr/bin/python3
#script that starts a Flask web application


from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    repl = text.replace("_", " ")
    return 'C {}'.format(repl)

@app.route('/python/', defaults={'text':'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    repl = text.replace("_", " ")
    return 'Python {}'.format(repl)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)