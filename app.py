from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shinta')
def shinta():
    return render_template('shinta.taa.html')

@app.route('/tambah')
def tambah():
    return render_template('tambah.html')

if __name__ == '__main__':
    app.run(debug=True)
