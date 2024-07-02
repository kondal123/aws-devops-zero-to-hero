from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello people, This is my first CI/CD project!!!!'

if __name__ == '__main__':
    app.run()

