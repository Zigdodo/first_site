from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def Main_Page():
    return render_template('Main.html')


if __name__ == '__main__':
    app.run()