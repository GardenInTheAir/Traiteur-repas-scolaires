from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__ , static_url_path="" , static_folder="static")
form_data = {
    "Parent":"",
    "Enfant":"",
    "Age":"",
    "Ecole":"",
    "Lundi":"",
    "Mardi":"",
    "Mercredi":"",
    "Jeudi":"",
    "Vendredi":""
}


def save_form () :
    i=0
    with open("./static/txt/commandes.txt", 'a+', encoding='utf-8') as f :
        for key, value in form_data.items():
            if i == len(form_data)-1 :
                f.write(key + ":" + value + "\n")
            else :
                f.write(key + ":" + value + ", ")
            i = i+1


@app.route('/')
def accueil() :
    return render_template('index.html')


@app.route('/informations')
def infos() :
    return render_template('informations.html')


@app.route('/contact')
def contact() :
    return render_template('contact.html')


@app.route('/commande')
def formulaire() :
    return render_template('commande.html')


@app.route('/submit', methods=['POST'])
def donnees_formulaire() :
    form_data['Parent']=request.form['Parent']
    form_data['Enfant']=request.form['Enfant']
    form_data['Age']=request.form['Age']
    form_data['Ecole']=request.form['Ecole']
    form_data['Lundi']=request.form['Lundi']
    form_data['Mardi']=request.form['Mardi']
    form_data['Mercredi']=request.form['Mercredi']
    form_data['Jeudi']=request.form['Jeudi']
    form_data['Vendredi']=request.form['Vendredi']
    save_form()
    return redirect('/confirmation')


@app.route('/confirmation')
def confirmation() :
    nomEnfant=form_data.get("Enfant")
    return render_template('confirmation.html', enfant=nomEnfant)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html'), 400