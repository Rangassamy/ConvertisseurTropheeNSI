import tkinter as tk
import subprocess


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Convertisseur")
        self.geometry("1000x700")
        
        self.grid_columnconfigure(0, weight=1)  # Colonne gauche
        self.grid_columnconfigure(1, weight=1)  # Colonne droite
        self.grid_rowconfigure(0, weight=1)     # Ligne principale
        self.grid_rowconfigure(1, weight=0)     # Ligne pour la zone d'entrée

        # Création des cadres
        self.left_frame = tk.Frame(self, bg="lightgray")
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        
        self.right_frame = tk.Frame(self, bg="lightgray")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        
        # Ajouter les convertisseurs de chaque côté
        self.left_converter = ConverterSide(self.left_frame, self, "Base", other_side="Resultat")
        self.right_converter = ConverterSide(self.right_frame, self, "Resultat", other_side="Base")
        
        # Zone de saisie pour le nombre
        self.entry_var = tk.StringVar()  # Stocker le texte
        self.input_entry = tk.Entry(self, textvariable=self.entry_var, font=('Helvetica', 18), width=20)
        self.input_entry.grid(row=1, column=0, columnspan=2, pady=20, sticky="ew")
        
        # Mise à jour de la conversion en cas de changement
        self.entry_var.trace_add('write', self.convert)  # Chaque fois que le contenu de entry_var change, la fonction convert est appelée
        tk.Button(self, text="Retour à l'accueil", command=self.retour_accueil, width=20, height=2).grid(row=2, column=0, columnspan=2, pady=10)

    def retour_accueil(self):
        self.destroy()  # Ferme la fenêtre du convertisseur
        subprocess.Popen(["python", "sources/main.py"])  # Rouvre l'accueil
    
    def convert(self, *args):
        input_value = self.entry_var.get()
        if input_value:
            try:
                # Vérifier si l'entrée est un nombre valide
                source_base = self.left_converter.get_base()
                target_base = self.right_converter.get_base()

                # Conversion
                converted_value = self.convert_between_bases(input_value, source_base, target_base)

                # Mise à jour de l'affichage
                self.left_converter.output_label.config(text=f"Nombre : {input_value}")
                self.right_converter.output_label.config(text=f"Résultat : {converted_value}")
            except ValueError:
                self.right_converter.output_label.config(text="Résultat : Erreur")
        else:
            self.left_converter.output_label.config(text="Nombre : ")
            self.right_converter.output_label.config(text="Résultat : ")

    def convert_between_bases(self, value, source_base, target_base):
        if source_base == target_base:
            return value  # Si les bases sont identiques, aucun traitement nécessaire
 
        # Étape 1 : Conversion en base décimale
        if source_base == 2 and target_base == 16:
            return bin_hex(value)
        
        elif source_base == 16 and target_base == 2:
            return hex_bin(value)
        
        elif source_base == 2:
            decimal_value = binEnDeci(value)
            
        elif source_base == 16:
            decimal_value = hexEnDeci(value)
            
        else:
            decimal_value = float(value)

        # Étape 2 : Conversion vers la base cible
        if target_base == 2:
            return DeciEnBin(decimal_value)
        elif target_base == 16:
            return DeciEnHexa(int(decimal_value))
        else:
            return str(decimal_value)


class ConverterSide:
    def __init__(self, parent, controller, side_name, other_side):
        self.controller = controller
        self.side_name = side_name
        self.current_base = 10
        self.parent = parent
        self.other_side = other_side
        
        # Titre du côté
        self.label = tk.Label(self.parent, text=f"{self.side_name}", font=('Helvetica', 16))
        self.label.pack(pady=10)
        
        # Bouton de sélection de base
        self.toggle_button = tk.Button(self.parent, text="Choisir la base", command=self.toggle_base)
        self.toggle_button.pack(pady=10)
        
        # Affichage de la conversion
        self.output_label = tk.Label(self.parent, text="", font=('Helvetica', 16))
        self.output_label.pack(pady=20)
        
        # Affichage de la base sélectionnée
        self.base_label = tk.Label(self.parent, text="Base actuelle : Décimal", font=('Helvetica', 14))
        self.base_label.pack(pady=10)

    def toggle_base(self):
        # Obtenir la base actuelle de l'autre côté
        other_base = self.controller.right_converter.current_base if self.side_name == "Base" else self.controller.left_converter.current_base

        # Parcourir les bases possibles en ignorant celle de l'autre côté
        bases = [2, 10, 16]
        current_index = bases.index(self.current_base)
        next_index = (current_index + 1) % len(bases)

        while bases[next_index] == other_base:
            next_index = (next_index + 1) % len(bases)

        self.current_base = bases[next_index]

        # Mettre à jour l'affichage avec de belles couleurs 🌈
        if self.current_base == 2:
            self.parent.config(bg="lightblue")
            self.base_label.config(text="Base actuelle : Binaire")
        elif self.current_base == 16:
            self.parent.config(bg="lightpink")
            self.base_label.config(text="Base actuelle : Hexadécimal")
        else:
            self.parent.config(bg="lightgreen")
            self.base_label.config(text="Base actuelle : Décimal")
        
        # Mise à jour de la conversion
        self.controller.convert()

    def get_base(self):
        return self.current_base



# Fonctions de conversion
################################### programme de enzo ######################################################

def binEnDeci(number):
    bin_str = str(number)
    decompte = len(bin_str)
    decimal = 0
    for c in bin_str:
        if c != "0" and c != "1":
            return "Entrée non valide"
    
    for i in range(len(bin_str)):
        decompte -= 1
        decimal += int(bin_str[i]) * 2**decompte
    
    return decimal

def hexEnDeci(number):
    hex_value = str(number).upper() 
    decompte = len(hex_value)
    decimal = 0
    for i in range(len(hex_value)):
        decompte -= 1
        if hex_value[i] == "A": 
            decimal += 10 * 16**decompte
        elif hex_value[i] == "B": 
            decimal += 11 * 16**decompte
        elif hex_value[i] == "C": 
            decimal += 12 * 16**decompte
        elif hex_value[i] == "D": 
            decimal += 13 * 16**decompte
        elif hex_value[i] == "E": 
            decimal += 14 * 16**decompte
        elif hex_value[i] == "F": 
            decimal += 15 * 16**decompte
        else: 
            decimal += int(hex_value[i]) * 16**decompte
    return decimal

####################################### programme de nolane #################################################

def DeciEnHexa(nombre):
    hex_digits = "0123456789ABCDEF"
    hexa = ""
    if nombre == 0:
        return "0"
    while nombre > 0:
        hexa = hex_digits[nombre % 16] + hexa
        nombre //= 16
    return hexa

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
        int_part //= 2
    
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

################################### programme de erwan ########################################
    
def bin_hex(entry):
    bit = ""
    result = ""
    entry = str(entry)
    while len(entry) % 4 != 0: entry = "0" + entry #rejoute des zero

    for x in range(int(len(entry)/4)):
        pack = 0
        for x in range(4):
             bit = entry[x]
             if bit == "0" or bit == "1":
                 pack += int(bit)*2**(3-x)
             else:
                 return "Entrée non valide"
            
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



if __name__ == "__main__":
    app = Application()
    app.mainloop()
