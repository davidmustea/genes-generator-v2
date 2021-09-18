from flask import Flask, render_template, redirect, url_for, request
from functii import *

app = Flask(__name__)


@app.route('/')
def default():
    return redirect(url_for("genes_generator"))


@app.route('/genes_generator', methods=['GET', 'POST'])
def genes_generator():
    global input_1, input_2

    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        input_1 = request.form.get('input_1')
        input_2 = request.form.get('input_2')

        if len(input_1) == len(input_2) and len(input_1) == 2:
            return redirect(url_for('rezultate_monohibridare'))

        if len(input_1) == len(input_2) and len(input_1) == 4:
            return redirect(url_for('rezultate_dihibridare'))


@app.route('/rezultate_monohibridare', methods=['GET', 'POST'])
def rezultate_monohibridare():
    if request.method == 'GET':
        #input_1 si input_2 impartit in 2 ca string
        split_1_1 = input_1[:len(input_1)//2]
        split_1_2 = input_1[len(input_1)//2:]
        split_2_1 = input_2[:len(input_1)//2]
        split_2_2 = input_2[len(input_1)//2:]

        split_lista = [split_1_1, split_1_2, split_2_1, split_2_2]

        #rezultate f1
        f1_rez_1 = split_1_1 + split_2_1
        f1_rez_2 = split_1_1 + split_2_2
        f1_rez_3 = split_1_2 + split_2_1
        f1_rez_4 = split_1_2 + split_2_2

        f1_rez_neprocesate_lista = [f1_rez_1, f1_rez_2, f1_rez_3, f1_rez_4]
        f1_rez_procesate_lista = list(map(reverse, f1_rez_neprocesate_lista))



        return render_template('rezultate_monohibridare.html', input_1=input_1, input_2=input_2,
        split_lista = split_lista, f1_rez_procesate_lista = f1_rez_procesate_lista)
    if request.method == 'POST':
        pass


@app.route('/rezultate_dihibridare', methods=['GET', 'POST'])
def rezultate_dihibridare():
    if request.method == 'GET':
        return render_template('rezultate_dihibridare.html', input_1=input_1, input_2=input_2)
    if request.method == 'POST':
        pass


if __name__ == "__main__":
    app.run(debug=True)