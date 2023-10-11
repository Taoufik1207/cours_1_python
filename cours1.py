import tkinter as tk
from PIL import Image, ImageTk


# Fonction pour vérifier le code entré
def verifier_code():
    code_entre = int(entrer_code.get())
    if code_entre == code_correct:
        resultat.config(text="Cadenas déverrouillé !", font=("Helvetica", 14, "bold"), fg="green")
        afficher_message_secret()
    else:
        resultat.config(text="Code incorrect. Réessayez.", font=("Helvetica", 12), fg="red")


# Fonction pour afficher le message secret
def afficher_message_secret():
    message_secret = "Félicitations !\nVous avez découvert le code.  Voici le lien vers un mystérieux carnet de notes : "
    message.config(text=message_secret, font=("Helvetica", 16, "italic"), fg="blue")


# Fonction pour vérifier le résultat de chaque opération
def verifier_resultat(operation_index):
    reponse = entrees_resultats[operation_index].get()
    indice = indices[operation_index]

    if float(reponse) == eval(indice["operation"]):
        etiquettes_indices[operation_index].config(text='Indice ' + str(operation_index + 1) + ' => ' +indice["texte"], fg="purple")
    else:
        etiquettes_indices[operation_index].config(text="Mauvaise réponse", fg="red")


# Code du coffre
code_correct = 153

# Opérations et indices
indices = [
    {"operation": "2 * 5 - 3", "texte": "7 9 3 : un chiffre est correct et à la bonne place"},
    {"operation": "20 / 2 + 4", "texte": "7 2 5 : un chiffre est correct et à la mauvaise place"},
    {"operation": "8 + 12 - 7", "texte": "3 1 7 : deux chiffres sont corrects mais à la mauvaise place"},
    {"operation": "9 * 3 - 10", "texte": "8 4 9 : aucun de ces chiffres n'est correct"},
    {"operation": "15 / 3 + 5", "texte": "8 9 1 : un chiffre est correct et à la mauvaise place"}
]

# Création de la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Mystère du Cadenas")

# Chargement de l'image du cadenas et redimensionnement
image_cadenas = Image.open(
    "cadenas.jpg")  # Assurez-vous d'avoir un fichier "cadenas.png" dans le même répertoire que votre script
largeur_image = 300  # Définissez la largeur souhaitée
hauteur_image = (largeur_image * image_cadenas.height) // image_cadenas.width  # Calculez la hauteur proportionnellement
image_cadenas = image_cadenas.resize((largeur_image, hauteur_image), Image.ANTIALIAS)  # Redimensionnez l'image
photo_cadenas = ImageTk.PhotoImage(image_cadenas)

# Création des widgets Tkinter
label_cadenas = tk.Label(fenetre, image=photo_cadenas)
label_code = tk.Label(fenetre, text="Entrez le code à 3 chiffres :")
entrer_code = tk.Entry(fenetre)
bouton_verifier = tk.Button(fenetre, text="Vérifier", command=verifier_code)
resultat = tk.Label(fenetre, text="")
message = tk.Label(fenetre, text="")

# Initialisation des étiquettes d'indice
etiquettes_indices = []
entrees_resultats = []

for i, indice in enumerate(indices):
    etiquette = tk.Label(fenetre, text=indice["operation"], font=("Helvetica", 12))
    entree_resultat = tk.Entry(fenetre)
    bouton_resultat = tk.Button(fenetre, text="Résoudre", command=lambda i=i: verifier_resultat(i))

    etiquettes_indices.append(etiquette)
    entrees_resultats.append(entree_resultat)

    etiquette.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entree_resultat.grid(row=i, column=1, padx=10, pady=5)
    bouton_resultat.grid(row=i, column=2, padx=10, pady=5)

# Placement des widgets dans la fenêtre
label_cadenas.grid(row=len(indices), column=0, columnspan=3)
label_code.grid(row=len(indices) + 1, column=0, columnspan=2)
entrer_code.grid(row=len(indices) + 1, column=2)
bouton_verifier.grid(row=len(indices) + 2, column=0, columnspan=3)
resultat.grid(row=len(indices) + 3, column=0, columnspan=3)
message.grid(row=len(indices) + 4, column=0, columnspan=3)

# Démarrage de la boucle principale Tkinter
fenetre.mainloop()
