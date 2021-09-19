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
        #input_1 si input_2 impartit in 2 ca string 'a'
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
        #reverse in caz de 'aA'
        f1_rez_neprocesate_lista = [f1_rez_1, f1_rez_2, f1_rez_3, f1_rez_4]
        f1_rez_procesate_lista = list(map(reverse, f1_rez_neprocesate_lista))


        return render_template('rezultate_monohibridare.html', input_1=input_1, input_2=input_2,
        split_lista = split_lista, f1_rez_procesate_lista = f1_rez_procesate_lista)
    if request.method == 'POST':
        pass


@app.route('/rezultate_dihibridare', methods=['GET', 'POST'])
def rezultate_dihibridare():
    if request.method == 'GET':
        #input_1 si input_2 impartit in 2 ca string 'aa'
        split_1_1 = input_1[:len(input_1)//2]
        split_1_2 = input_1[len(input_1)//2:]
        split_2_1 = input_2[:len(input_1)//2]
        split_2_2 = input_2[len(input_1)//2:]

        split_lista = [split_1_1, split_1_2, split_2_1, split_2_2]
        #split_x_x impartit din nou in 2
        split2_1_1 = split_1_1[:len(split_1_1)//2]
        split2_1_2 = split_1_1[len(split_1_1)//2:]
        split2_2_1 = split_1_2[:len(split_1_2)//2]
        split2_2_2 = split_1_2[len(split_1_2)//2:]
        split2_3_1 = split_2_1[:len(split_2_1)//2]
        split2_3_2 = split_2_1[len(split_2_1)//2:]
        split2_4_1 = split_2_2[:len(split_2_1)//2]
        split2_4_2 = split_2_2[len(split_2_1)//2:]

        split2_lista = [split2_1_1, split2_1_2, split2_2_1, split2_2_2, split2_3_1, split2_3_2, split2_4_1, split2_4_2]

        f1_rez = split2_1_1 + split2_3_1 + split2_2_1 + split2_4_1

        #inputs pentru table
        table_input_1 = f1_rez[0] + f1_rez[2]
        table_input_2 = f1_rez[0] + f1_rez[3]
        table_input_3 = f1_rez[2] + f1_rez[1]
        table_input_4 = f1_rez[1] + f1_rez[3]

        table_inputs = [table_input_1, table_input_2, table_input_3, table_input_4]

        col_1_rand_1 = table_input_1[0] * 2 + table_input_1[1] * 2
        col_1_rand_2 = table_input_1[0] * 2 + table_input_1[1] + table_input_2[1]
        col_1_rand_3 = table_input_1[0] + table_input_3[1] + table_input_1[1] + table_input_3[0]
        col_1_rand_4 = table_input_1[0] + table_input_4[0] + table_input_1[1] + table_input_4[1]
        col_2_rand_1 = table_input_1[0] + table_input_2[0] + table_input_1[1] + table_input_2[1]
        col_2_rand_2 = table_input_2[0] * 2 + table_input_2[1] * 2
        col_2_rand_3 = table_input_2[0] + table_input_3[1] + table_input_3[0] + table_input_2[1]
        col_2_rand_4 = table_input_2[0] + table_input_4[0] + table_input_2[1] + table_input_4[1]
        col_3_rand_1 = table_input_1[0] + table_input_3[1] + table_input_1[1] + table_input_3[0]
        col_3_rand_2 = table_input_2[0] + table_input_3[1] + table_input_3[0] + table_input_2[1]
        col_3_rand_3 = table_input_3[0] * 2 + table_input_3[1] * 2
        col_3_rand_4 = table_input_4[0] + table_input_3[1] + table_input_3[0] + table_input_4[1]
        col_4_rand_1 = table_input_1[0] + table_input_4[0] + table_input_1[1] + table_input_4[1]
        col_4_rand_2 = table_input_2[0] + table_input_4[0] + table_input_2[1] + table_input_4[1]
        col_4_rand_3 = table_input_3[1] + table_input_4[0] + table_input_3[0] + table_input_4[1]
        col_4_rand_4 = table_input_4[0] * 2 + table_input_4[1] * 2

        cols_and_rand_lista = [col_1_rand_1, col_1_rand_2, col_1_rand_3, col_1_rand_4,
                            col_2_rand_1, col_2_rand_2, col_2_rand_3, col_2_rand_4,
                            col_3_rand_1, col_3_rand_2, col_3_rand_3, col_3_rand_4,
                            col_4_rand_1, col_4_rand_2, col_4_rand_3, col_4_rand_4]

        return render_template('rezultate_dihibridare.html', input_1=input_1, input_2=input_2,
        split_lista = split_lista,
        f1_rez = f1_rez, table_inputs = table_inputs,
        cols_and_rand_lista = cols_and_rand_lista)

    if request.method == 'POST':
        pass


if __name__ == "__main__":
    app.run(debug=True)