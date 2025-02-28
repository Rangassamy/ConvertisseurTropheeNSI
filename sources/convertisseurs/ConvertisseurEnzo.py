import tkinter as tk
import subprocess

def retour_accueil():
    fenetre.destroy()  # Fermer la fenêtre du convertisseur
    subprocess.Popen(["python", "sources/main.py"])  # Relancer l'accueil


# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("19000x1080")  # Dimension de base de la fenêtre

######################################################################
############################## Label ##################################
######################################################################

# Modifier le style d'un label d'instruction
label_instruction = tk.Label(
    fenetre,
    text="Comment voulez-vous convertir ?",
    font=("Helvetica", 24),
    bg="lightblue",
    fg="black"
)
label_instruction.grid(row=0, column=0, columnspan=6, pady=20)

# Label pour afficher la conversion sélectionnée
label_resultat = tk.Label(
    fenetre,
    text="",
    font=("Helvetica", 24),
    bg="white",
    fg="black"
)
label_resultat.grid(row=2, column=0, columnspan=6, pady=20)

# Nouveau label pour afficher l'instruction d'entrée
label_entree_instruction = tk.Label(
    fenetre,
    text="",
    font=("Helvetica", 16),
    bg="lightblue",
    fg="black"
)
label_entree_instruction.grid(row=3, column=0, columnspan=6, pady=10)

######################################################################
############################## Fonction ##############################
######################################################################

# Fonction pour convertir binaire en décimal
def binEnDeci(number):
    bin = str(number)
    decompte = len(bin)
    decimal = 0
    for i in range (len(bin)):
        decompte = decompte - 1
        decimal = decimal + int(bin[i]) * 2**decompte
        
    return(decimal)

# Fonction pour convertir hexadécimal en décimal
def hexEnDeci(number):
    hex = str(number)
    decompte = len(hex)
    decimal = 0
    for i in range (len(hex)):
        decompte = decompte - 1
        if hex[i] == "A" or hex[i] == "a": decimal = decimal + 10 * 16**decompte
        elif hex[i] == "B" or hex[i] == "b": decimal = decimal  + 11 * 16**decompte
        elif hex[i] == "C" or hex[i] == "c": decimal = decimal  + 12 * 16**decompte
        elif hex[i] == "D" or hex[i] == "d": decimal = decimal  + 13 * 16**decompte
        elif hex[i] == "E" or hex[i] == "e": decimal = decimal  + 14 * 16**decompte
        elif hex[i] == "F" or hex[i] == "f": decimal = decimal  + 15 * 16**decompte
        else : decimal = decimal + int(hex[i]) * 16**decompte
        
    return decimal
# Fonction pour convertir décimal en hexadécimal
def DeciEnHexa(nombre):
    hexa_nomb = "0123456789ABCDEF"
    hexa = ""
    
    while nombre > 0:
        reste = nombre % 16
        hexa = hexa_nomb[reste] + hexa
        nombre = nombre // 16   
    return hexa

# Fonction pour convertir décimal en binaire
def DeciEnBin(nombres):
    if "." in str(nombres):
        int_part, frac_part = str(nombres).split(".")
        int_part = int(int_part)
        frac_part = float("0." + frac_part)
    else:
        int_part = int(nombres)
        frac_part = 0
    
    int_bin = ""
    while int_part > 0:
        reste = int_part % 2
        int_bin = str(reste) + int_bin
        int_part = int_part // 2
    
    frac_bin = ""
    while frac_part > 0 and len(frac_bin) < 8:
        frac_part *= 2
        bit = int(frac_part)
        frac_bin += str(bit)
        frac_part -= bit
    
    if frac_bin:
        return f"{int_bin}.{frac_bin}"
    else:
        return int_bin

# Fonction pour convertir binaire en hexadécimal
def bin_hex(entry):
    bit = ""
    result = ""
    entry = str(entry)
    while len(entry) % 4 != 0: entry = "0" + entry #rejoute des zero

    if set(entry) - {"0", "1"}:
        return "Erreur : Entrée non valide."

    for x in range(int(len(entry)/4)):
        pack = 0
        for x in range(4):
            bit = str(entry)[x] # recuperer les bits 1 a 1 en partent de la fin en entry
            pack += int(bit)*2**(3-x) #ajouter le bit calculer au character hexa en cours
        #calcule de character
        if int(pack) == 10: result += "A"
        elif int(pack) == 11: result += "B"
        elif int(pack) == 12: result += "C"
        elif int(pack) == 13: result += "D"
        elif int(pack) == 14: result += "E"
        elif int(pack) == 15: result += "F"
        else: result += str(pack)
        entry = str(entry)[4:]#suprime les 4 bits traités
    return(result)

# Fonction pour convertir hexadécimal en binaire
def hex_bin(entry):
    dec = ""
    result = ""
    entry = str(entry)
    for x in range(len(entry)):
        pack = ""
        depack = ""
        bit = entry[len(entry)-x-1]
        if bit == "A" or bit == "a": dec = 10
        elif bit == "B" or bit == "b": dec = 11
        elif bit == "C" or bit == "c": dec = 12
        elif bit == "D" or bit == "d": dec = 13
        elif bit == "E" or bit == "e": dec = 14
        elif bit == "F" or bit == "f": dec = 15
        else: dec = int(bit)
        reste = dec
        it = 0
        while reste != 0:
            pack += str(reste % 2)
            reste = reste//2
            it += 1
        for x in range(len(pack)):depack = depack + pack[len(pack)-x-1]
        for x in range(4 - it): depack = "0" + depack
        result = depack + result
    return(result)


# Fonction pour gérer le clic sur un bouton
def bouton_clique(texte):
    valeur_bouton.set(texte)
    label_resultat.config(text=f"Vous avez sélectionné : {texte}")
    label_entree_instruction.config(text=f"Veuillez entrer une valeur en {texte.split(' ')[0]}.")
    entree_valeur.grid()
    entree_valeur.focus()

    def valider_entree(event):
        valeur = entree_valeur.get()
        try:
            if texte == "Binaire en Decimal":
                label_resultat.config(text=f"Résultat : {binEnDeci(valeur)}")
            elif texte == "Hexadecimal en Decimal":
                label_resultat.config(text=f"Résultat : {hexEnDeci(valeur)}")
            elif texte == "Decimal en Binaire":
                label_resultat.config(text=f"Résultat : {DeciEnBin(float(valeur))}")
            elif texte == "Decimal en Hexadecimal":
                label_resultat.config(text=f"Résultat : {DeciEnHexa(int(valeur))}")
            elif texte == "Hexadecimal en Binaire":
                label_resultat.config(text=f"Résultat : {hex_bin(valeur)}")
            elif texte == "Binaire en Hexadecimal":
                label_resultat.config(text=f"Résultat : {bin_hex(valeur)}")
        except ValueError:
            label_resultat.config(text="Erreur : Entrée non valide.")

    fenetre.bind('<Return>', valider_entree)

######################################################################
############################## Bouton ################################
######################################################################

entree_valeur = tk.Entry(fenetre, font=("Arial", 14), bg="white", fg="black")
entree_valeur.grid(row=4, column=0, columnspan=6, pady=10)
entree_valeur.grid_remove()

valeur_bouton = tk.StringVar()

boutons = {
    "Decimal en Binaire": "lightgreen",
    "Decimal en Hexadecimal": "lightcoral",
    "Binaire en Decimal": "lightyellow",
    "Hexadecimal en Decimal": "lightpink",
    "Hexadecimal en Binaire": "lightblue",
    "Binaire en Hexadecimal": "lightgrey"
}

for i, (texte, couleur) in enumerate(boutons.items()):
    bouton = tk.Button(
        fenetre,
        text=texte,
        font=("Arial", 14, "bold"),
        bg=couleur,
        fg="black",
        command=lambda t=texte: bouton_clique(t)
    )
    bouton.grid(row=1, column=i, padx=10, pady=10)

for i in range(len(boutons)):
    fenetre.grid_columnconfigure(i, weight=1)


# Ajouter un bouton pour revenir à l'accueil
bouton_retour = tk.Button(
    fenetre,
    text="Retour à l'accueil",
    font=("Arial", 14),
    bg="lightgrey",
    fg="black",
    command=retour_accueil
)
bouton_retour.grid(row=5, column=0, columnspan=6, pady=20)

def fermer_fenetre(event):
    fenetre.destroy()

fenetre.bind('<Escape>', fermer_fenetre)
fenetre.mainloop()


################################################################
########################Plan de travail#########################
################################################################

# Enzo à fait l'interface graphique et connecter les convertisseurs
#
# Nolan à fait les programmes de conversions : decimal > hexadecimal et decimal > binaire 
#
# Erwan à fait les programmes de conversions : hexadecimal > binaire et bianire > hexadecimal
#
# Enzo à fait Les programmes de conversions : binaire > decimal et hexadecimal > decimal