import sqlite3

conn = sqlite3.connect("dbed.db")
cur = conn.cursor()


def retrouver_matieres(id_eleve):
"""Retourne toutes les matières d'un élève."""
# On a besoin d'utiliser cette fonction au lieu d'une requête SQL car la relation ELEVE plusieurs clés étrangères pour chaque matière stockées sous la forme de texte.
    cur.execute(f"SELECT id,id_matieres FROM ELEVES WHERE id = {id_eleve}")
    matieres = []
    for id_mat in str(cur.fetchone()[1]).split(','):
        cur.execute(f"SELECT * from MATIERES WHERE id = {id_mat}")
        matieres.append(cur.fetchone())
    return matieres


# recuperer les valeurs des notes de l'eleve 2 (raphaël) en la matière 2 (NSI)
cur.execute("SELECT valeur from NOTES where id_eleve = 2 AND NOTES.id_matiere = 2")
print(cur.fetchall())
