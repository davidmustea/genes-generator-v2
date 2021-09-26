from flask import Flask, render_template, redirect, url_for, request, flash
from functii import *

app = Flask(__name__)
app.secret_key = "delocsecret"

@app.route('/')
def default():
    global nume_gena_1, nume_gena_2, nume_gena_3, nume_gena_4
    #sa nu dea form eroare ca nu are variabile definite
    nume_gena_1 = ''
    nume_gena_2 = ''
    nume_gena_3 = ''
    nume_gena_4 = ''
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
            if input_1.isupper() and input_2.islower():
                return redirect(url_for('rezultate_monohibridare'))
            else:
                flash("Inputul trebuie sa fie Gena dominanta - gena recesiva - ex AA - aa nu Aa - Aa")
                return redirect(url_for('default'))
                

        if len(input_1) == len(input_2) and len(input_1) == 4:
            if input_1.isupper() and input_2.islower():
                return redirect(url_for('rezultate_dihibridare'))
            else:
                flash("input trebuie sa fie de genul NNGG - zzvv")
                return redirect(url_for('default'))


@app.route('/rezultate_monohibridare', methods=['GET', 'POST'])
def rezultate_monohibridare():
    #sa rezolv cumva sa resetez nume_gena_1 si nume_gena_2 cu buton de reset
    global nume_gena_1, nume_gena_2
    
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

        #f2 split ( /2)
        f2_split_1_1 = f1_rez_1[:len(f1_rez_1)//2]
        f2_split_1_2 = f1_rez_1[len(f1_rez_1)//2:]
        f2_split_2_1 = f1_rez_1[:len(f1_rez_1)//2]
        f2_split_2_2 = f1_rez_1[len(f1_rez_1)//2:]

        f2_split_lista = [f2_split_1_1, f2_split_1_2, f2_split_2_1, f2_split_2_2]

        #rezultate f2
        f2_rez_1 = f2_split_1_1 + f2_split_2_1
        f2_rez_2 = f2_split_1_1 + f2_split_2_2
        f2_rez_3 = f2_split_1_2 + f2_split_2_1
        f2_rez_4 = f2_split_1_2 + f2_split_2_2

        #reverse in caz de 'aA'
        f2_rez_neprocesate_lista = [f2_rez_1, f2_rez_2, f2_rez_3, f2_rez_4]
        f2_rez_procesate_lista = list(map(reverse, f2_rez_neprocesate_lista))

        return render_template('rezultate_monohibridare.html', input_1=input_1, input_2=input_2,
        split_lista = split_lista, f1_rez_procesate_lista = f1_rez_procesate_lista,
        f2_split_lista = f2_split_lista, f2_rez_procesate_lista = f2_rez_procesate_lista,
        nume_gena_1 = nume_gena_1, nume_gena_2 = nume_gena_2)

    if request.method == 'POST':
        nume_gena_1 = request.form.get("nume_gena_1")
        nume_gena_2 = request.form.get("nume_gena_2")

        return redirect(url_for("rezultate_monohibridare"))

        


@app.route('/rezultate_dihibridare', methods=['GET', 'POST'])
def rezultate_dihibridare():
    global nume_gena_1, nume_gena_2, nume_gena_3, nume_gena_4
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
        cols_and_rand_lista = cols_and_rand_lista,
        nume_gena_1 = nume_gena_1, nume_gena_2 = nume_gena_2, nume_gena_3 = nume_gena_3, nume_gena_4 = nume_gena_4)

    if request.method == 'POST':
        nume_gena_1 = request.form.get("nume_gena_1")
        nume_gena_2 = request.form.get("nume_gena_2")
        nume_gena_3 = request.form.get("nume_gena_3")
        nume_gena_4 = request.form.get("nume_gena_4")

        return redirect(url_for("rezultate_dihibridare"))


if __name__ == "__main__":
    app.run(debug=True)