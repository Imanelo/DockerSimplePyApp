from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello,Here Imane! enjoy the process and remember that doing small little improvements everyday is a good way for bigger achievements :)</h2>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
