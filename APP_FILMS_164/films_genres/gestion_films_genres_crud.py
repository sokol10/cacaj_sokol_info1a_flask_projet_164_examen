"""
    Fichier : gestion_films_genres_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les films et les genres.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.films_genres.gestion_films_genres_wtf_forms import FormWTFUpdateFilmsGenres
from APP_FILMS_164.films_genres.gestion_films_genres_wtf_forms import FormWTFAjouterFilmsGenres
from APP_FILMS_164.films_genres.gestion_films_genres_wtf_forms import FormWTFDeleteFilmsGenres
"""
    Nom : films_genres_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /films_genres_afficher
    
    But : Afficher les films avec les genres associés pour chaque film.
    
    Paramètres : id_genre_sel = 0 >> tous les films.
                 id_genre_sel = "n" affiche le film dont l'id est "n"
                 
"""


@app.route("/films_genres_afficher/<int:id_adresse_sel>", methods=['GET', 'POST'])
def films_genres_afficher(id_adresse_sel):
    print("films_genres_afficher id_adresse_sel ", id_adresse_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_genres_films_afficher_data = """SELECT id, adresse, ville, code_postal, pays FROM t_adresse"""
                if id_adresse_sel == 0:
                    mc_afficher.execute(strsql_genres_films_afficher_data + " ORDER BY id")
                else:
                    valeur_id_adresse_selected_dictionnaire = {"value_id_adresse_selected": id_adresse_sel}
                    strsql_genres_films_afficher_data += " WHERE id = %(value_id_adresse_selected)s ORDER BY id"
                    mc_afficher.execute(strsql_genres_films_afficher_data, valeur_id_adresse_selected_dictionnaire)

                data_genres_films_afficher = mc_afficher.fetchall()
                print("data_genres ", data_genres_films_afficher, " Type : ", type(data_genres_films_afficher))

                if not data_genres_films_afficher and id_adresse_sel == 0:
                    flash("""La table "t_adresse" est vide. !""", "warning")
                elif not data_genres_films_afficher and id_adresse_sel > 0:
                    flash(f"L'adresse du film {id_adresse_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données des films et des adresses affichées !!", "success")

        except Exception as Exception_films_genres_afficher:
            raise ExceptionFilmsGenresAfficher(f"fichier : {Path(__file__).name}  ;  {films_genres_afficher.__name__} ;"
                                               f"{Exception_films_genres_afficher}")

    return render_template("films_genres/films_genres_afficher.html", data_genres=data_genres_films_afficher)


@app.route("/films_genres_ajouter", methods=['GET', 'POST'])
def films_genres_ajouter():
    form = FormWTFAjouterFilmsGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                adresse_wtf = form.adresse_wtf.data
                adresse = adresse_wtf.lower()
                ville_wtf = form.ville_wtf.data
                ville = ville_wtf.lower()
                code_postal_wtf = form.code_postal_wtf.data
                code_postal = code_postal_wtf.lower()
                pays_wtf = form.pays_wtf.data
                pays = pays_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_adresse": adresse,
                                                  "value_ville": ville,
                                                  "value_cp": code_postal,
                                                  "value_pays": pays}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_adresse = """INSERT INTO t_adresse (adresse, ville, code_postal, pays) VALUES (%(value_adresse)s, %(value_ville)s, %(value_code_postal)s, %(value_pays)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_adresse, valeurs_insertion_dictionnaire)

                flash("L'adresse a été ajoutée avec succès !", "success")
                return redirect(url_for("films_genres_afficher", id_adresse_sel=0))

        except Exception as Exception_films_genres_ajouter:
            raise ExceptionFilmsGenresAjouter(f"fichier : {Path(__file__).name}  ;  {films_genres_ajouter.__name__} ;"
                                              f"{Exception_films_genres_ajouter}")

    return render_template("films_genres/films_genres_ajouter_wtf.html", form=form)


@app.route("/films_genres_update/<int:id_adresse_sel>", methods=['GET', 'POST'])
def films_genres_update_wtf(id_adresse_sel):
    form = FormWTFUpdateFilmsGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                adresse_wtf = form.adresse_wtf.data
                adresse = adresse_wtf.lower()
                ville_wtf = form.ville_wtf.data
                ville = ville_wtf.lower()
                code_postal_wtf = form.code_postal_wtf.data
                code_postal = code_postal_wtf.lower()
                pays_wtf = form.pays_wtf.data
                pays = pays_wtf.lower()
                valeurs_update_dictionnaire = {"value_adresse": adresse,
                                                  "value_ville": ville,
                                                  "value_cp": code_postal,
                                                  "value_pays": pays}
                print("valeurs_update_dictionnaire ", valeurs_update_dictionnaire)

                with DBconnection() as mc_modifier:
                    # Exécuter la requête SQL pour mettre à jour l'enregistrement
                    strsql_modifier = "UPDATE t_adresse SET adresse = %s, ville = %s, code_postal = %s, pays = %s WHERE id = %s"
                    valeurs = (adresse, ville, code_postal, pays, id_adresse_sel)
                    mc_modifier.execute(strsql_modifier, valeurs)

                flash("L'adresse a été modifiée avec succès !", "success")
                return redirect(url_for("films_genres_afficher", id_adresse_sel=0))

        except Exception as Exception_films_genres_update_wtf:
            raise ExceptionFilmsGenresUpdateWTF(f"fichier : {Path(__file__).name}  ;  {films_genres_update_wtf.__name__} ;"
                                                f"{Exception_films_genres_update_wtf}")

    return render_template("films_genres/films_genres_update_wtf.html", form=form, id_adresse_sel=id_adresse_sel)


@app.route("/films_genres_delete/<int:id_adresse_sel>", methods=['GET', 'POST'])
def films_genres_delete(id_adresse_sel):
    form = FormWTFDeleteFilmsGenres()

    if request.method == "POST":
        try:
            if form.validate_on_submit():

                # Récupère le nom du film pour le message de confirmation
                with DBconnection() as mconn_bd:
                    strsql_select_adresse = f"SELECT id, adresse, ville, code_postal, pays FROM t_adresse WHERE id = {id_adresse_sel}"
                    mconn_bd.execute(strsql_select_adresse)
                    data_adresse = mconn_bd.fetchone()
                    adresse = data_adresse["adresse"]
                    ville = data_adresse["ville"]
                    code_postal = data_adresse["code_postal"]
                    pays = data_adresse["pays"]

                with DBconnection() as mc_delete:
                    # Supprimer l'enregistrement du film
                    strsql_delete = f"DELETE FROM t_adresse WHERE id = {id_adresse_sel}"
                    mc_delete.execute(strsql_delete)

                flash(f"L'adresse {adresse}, {ville}, {code_postal}, {pays} a été supprimée avec succès !", "success")
                return redirect(url_for("films_genres_afficher", id_adresse_sel=0))

        except Exception as Exception_films_genres_delete:
            raise ExceptionFilmsGenresDelete(f"fichier : {Path(__file__).name}  ;  {films_genres_delete.__name__} ;"
                                             f"{Exception_films_genres_delete}")

    return render_template("films_genres/films_genres_delete_wtf.html", form=form, id_adresse_sel=id_adresse_sel)
