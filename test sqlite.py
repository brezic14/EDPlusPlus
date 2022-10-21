# Bibliothèque sqlite pour interagir avec des bases de données en Python.
import sqlite3

# Établissement d'une connection avec le fichier de base de donnée.
conn = sqlite3.connect("dbed.db")
# Création du curseur, un objet qui permet de parcourir la BDD et d'exécuter des requêtes SQL.
cur = conn.cursor()

# On fait une jointure entre COURS et MATIERES. On récupère les noms des matières de l'élève 3 (Raphaël) qui ont pour type "Option".
cur.execute('SELECT nom FROM COURS,MATIERES WHERE id_matiere = id AND id_eleve = 3 AND type = "Option"')
# Équivalent à
# cur.execute('SELECT nom FROM COURS INNER JOIN MATIERES ON id_matiere = id WHERE type = "Option"')

# fetchall() dépile toutes les lignes du résultat et on aplatit la liste de tuples retournée en utilisant la compréhension.
print("Options de Raphaël : ", ", ".join(item for sublist in cur.fetchall() for item in sublist))

# On sélectionne plusieurs attributs de la jointure NOTES/EVALUATIONS pour l'élève 3 (Raphaël) dans la matière 16 (NSI)
cur.execute("SELECT titre,valeur,noteMax,coef, valeur FROM NOTES,EVALUATIONS WHERE id_evaluation=id AND id_eleve = 3 AND id_matiere = 16")

# On utilise l'interpoliation de chaîne pour afficher le résultat.
print("Notes de Raphaël en NSI : ", ", ".join(f"{m[0]} {m[1]}/{m[2]} ({m[3]})" for m in cur.fetchall()))
