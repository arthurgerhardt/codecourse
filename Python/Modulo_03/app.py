from flask import Flask


# __name__ é uma variável que o Python cria automaticamente - __name__ = "__main__"
app = Flask(__name__)

@app.route('/')
def home():
	return "Hello World!"

@app.route('/about')
def sobre():
	return "Sobre o site"

if __name__ == "__main__":
	app.run(debug=True)
