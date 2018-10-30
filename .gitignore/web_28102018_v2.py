from flask import Flask
app = Flask(__name__)

@app.route('/')
def texting():
    text = '<h1>Here is my text - it works great<h1>'
    return text

if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)
