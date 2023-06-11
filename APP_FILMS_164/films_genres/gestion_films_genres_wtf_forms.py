"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterFilmsGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    adresse_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    adresse_wtf = StringField("Insérer l'adresse ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(adresse_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    ville_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    ville_wtf = StringField("Insérer la ville ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(ville_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    code_postal_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    code_postal_wtf = StringField("Insérer le code postal", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(code_postal_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    pays_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    pays_wtf = StringField("Insérer le pays ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(pays_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Enregistrer l'adresse")


class FormWTFUpdateFilmsGenres(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    adresse_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    adresse_wtf = StringField("Insérer l'adresse ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                             Regexp(adresse_regexp,
                                                                    message="Pas de chiffres, de caractères "
                                                                            "spéciaux, "
                                                                            "d'espace à double, de double "
                                                                            "apostrophe, de double trait union")
                                                             ])
    ville_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    ville_wtf = StringField("Insérer la ville ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                              Regexp(ville_regexp,
                                                                     message="Pas de chiffres, de caractères "
                                                                             "spéciaux, "
                                                                             "d'espace à double, de double "
                                                                             "apostrophe, de double trait union")
                                                              ])
    code_postal_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    code_postal_wtf = StringField("Insérer le code postal", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                    Regexp(code_postal_regexp,
                                                                           message="Pas de chiffres, de caractères "
                                                                                   "spéciaux, "
                                                                                   "d'espace à double, de double "
                                                                                   "apostrophe, de double trait union")
                                                                    ])
    pays_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    pays_wtf = StringField("Insérer le pays", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                             Regexp(pays_regexp,
                                                                    message="Pas de chiffres, de caractères "
                                                                            "spéciaux, "
                                                                            "d'espace à double, de double "
                                                                            "apostrophe, de double trait union")
                                                             ])
    submit = SubmitField("Update adresse")


class FormWTFDeleteFilmsGenres(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    adresse_wtf = StringField("Effacer cette adresse")
    ville_wtf = StringField("Effacer cette ville")
    code_postal_wtf = StringField("Effacer ce code postal")
    pays_wtf = StringField("Effacer ce pays")
    submit_btn_del_adresse = SubmitField("Effacer l'adresse ?")
    submit_btn_conf_del_adresse = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
