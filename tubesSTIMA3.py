# Tugas Besar Strategi Algoritma 3
# Ilham Firdausi Putra - 13516140
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/solution', methods=['POST'])
def solution():
    inputKeyword = request.get_json(force=True)

if __name__ == '__main__':
    app.run(debug=True,port=5000)