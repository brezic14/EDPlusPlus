import sqlite3

conn = sqlite3.connect("dbed.db")
cur = conn.cursor()

def retrouver_matieres(id_eleve):
    cur.execute(f"SELECT id,id_matieres FROM ELEVES WHERE id = {id_eleve}")
    matieres = []
    for id_mat in str(cur.fetchone()[1]).split(','):
        cur.execute(f"SELECT * from MATIERES WHERE id = {id_mat}")
        matieres.append(cur.fetchone())
    return matieres


# recuperer les valeurs des notes de l'eleve 2 en NSI
cur.execute("SELECT valeur from NOTES where id_eleve = 2 AND NOTES.id_matiere = 2")
print(cur.fetchall())
