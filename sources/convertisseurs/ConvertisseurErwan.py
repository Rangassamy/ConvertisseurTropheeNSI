from random import *
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import clipboard
import subprocess


def retour_accueil():
    root.destroy()  # Fermer la fenêtre du convertisseur
    subprocess.Popen(["python", "sources/main.py"])  # Relancer l'accueil

#Nolan
def dec_hex(nombre):
    nombre = int(nombre)
    hexa_nomb = "0123456789ABCDEF"
    hexa = ""
    
    while nombre > 0 :
        reste = nombre % 16
        hexa = hexa_nomb[reste] + hexa
        nombre = nombre // 16   
    return hexa

def dec_bin(nombres):
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

#Enzo
def bin_dec(number):
    bin = str(number)
    decompte = len(bin)
    decimal = 0
    for i in range (len(bin)):
        decompte = decompte - 1
        decimal = decimal + int(bin[i]) * 2**decompte
        
    return(decimal)
    
    
def hex_dec(number):
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

#Erwan
def bin_hex(entry):
    bit = ""
    result = ""
    entry = str(entry)
    while len(entry) % 4 != 0: entry = "0" + entry

    for x in range(int(len(entry)/4)):
        pack = 0
        for x in range(4):
            bit = str(entry)[x]
            pack += int(bit)*2**(3-x)
        if int(pack) == 10: result += "A"
        elif int(pack) == 11: result += "B"
        elif int(pack) == 12: result += "C"
        elif int(pack) == 13: result += "D"
        elif int(pack) == 14: result += "E"
        elif int(pack) == 15: result += "F"
        else: result += str(pack)
        entry = str(entry)[4:]
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

#_______________________________________________________________________________________________________________________
#-----------------------------------------------------------------------------------------------------------------------
#_______________________________________________________________________________________________________________________
color1 = ["#01539d", "#0f1920", "#f96266", "#cdf281", "#fe69b1", "#ee4f35", "#980212", "#8aaae4"]
color2 = ["#eea47e", "#ffe716", "#fbe67d", "#4832d4", "#03ffff", "#fcecda", "#fbf6f5", "#feffff"]
choixColor = randint(0, 7)
charHex =["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a", "B", "b", "C", "c", "D", "d", "E", "e",  "F", "f"]
charDec =[".", "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
charBin = ["", "0", "1"]


def OnValidate(S, d):
    if d != '0':
        if combo_entre.get() == "Hex":
            for i in range(len(S)):
                for  x in range(len(charHex)):
                    if S[i] == charHex[x] : break
                    if x == len(charHex)-1 : 
                        label_sortie['text'] = "caractère invalide ! Entrer pour rafraîchir."
                        return False
            if combo_sortie.get() == "Dec":label_sortie['text'] = hex_dec(label_entry.get() + S)
            if combo_sortie.get() == "Bin":label_sortie['text'] = hex_bin(label_entry.get() + S)
            return True
        
        if combo_entre.get() == "Dec":
            for i in range(len(S)):
                for  x in range(len(charDec)):
                    if S[i] == charDec[x]: break
                    if x == len(charDec)-1 : 
                        label_sortie['text'] = "caractère invalide ! Entrer pour rafraîchir."
                        return False
            if combo_sortie.get() == "Hex":label_sortie['text'] = dec_hex(label_entry.get() + S)
            if combo_sortie.get() == "Bin":label_sortie['text'] = dec_bin(label_entry.get() + S)
            return True
                
        if combo_entre.get() == "Bin":
            for i in range(len(S)):
                for  x in range(len(charBin)):
                    if S[i] == charBin[x]: break
                    if x == len(charBin)-1 : 
                        label_sortie['text'] = "caractère invalide ! Entrer pour rafraîchir."
                        return False
            if combo_sortie.get() == "Dec":label_sortie['text'] = bin_dec(label_entry.get() + S)
            if combo_sortie.get() == "Hex":label_sortie['text'] = bin_hex(label_entry.get() + S)
            return True
    else: return True

def CopySortie():
    clipboard.copy(label_sortie['text'])

def keypress(e):
    if e.char == '\r': OnValidate('', 1)
def OnChoose(a):
    label_entry.delete(0, END)
    if combo_entre.get() == "Hex":
        combo_sortie['values'] = ('Bin', 'Dec')
        if combo_sortie.get() == "Hex" : combo_sortie.set("Bin")
    if combo_entre.get() == "Dec":
        combo_sortie['values'] = ('Bin', 'Hex')
        if combo_sortie.get() == "Dec" : combo_sortie.set("Bin")
    if combo_entre.get() == "Bin":
        combo_sortie['values'] = ('Hex', 'Dec')
        if combo_sortie.get() == "Bin" : combo_sortie.set("Hex")

root = Tk()
root.title("Convertiseur Universel")
root.geometry("500x300")
root.bind("<KeyPress>", keypress)

combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {
                                     'TCombobox':
                                     {'configure':
                                      {'selectbackground': color1[choixColor],
                                       'fieldbackground': color1[choixColor],
                                       'background': color2[choixColor],
                                       'arrowcolor' : color1[choixColor],
                                       'foreground': color2[choixColor],
                                       'selectforeground' : color2[choixColor],
                                       'padding' :0
                                       }}}
                         )
combostyle.theme_use('combostyle') 
root.option_add("*TCombobox*Listbox*Background", color2[choixColor])
root.option_add('*TCombobox*Listbox*Foreground', color1[choixColor])

label_choix_entre = Label(root, text = "De", bg=color1[choixColor], fg=color2[choixColor])
type_entre=["Hex", "Bin","Dec"]
combo_entre = ttk.Combobox(root, values=type_entre, state="readonly")
combo_entre.bind("<<ComboboxSelected>>", OnChoose)
combo_entre.current(0)

combo_entre.place(x=50, y=75)
label_choix_entre.place(x=50, y=50)


label_choix_sortie = Label(root, text = "Vers", bg=color1[choixColor], fg=color2[choixColor])
type_sortie=["Bin","Dec"]
combo_sortie = ttk.Combobox(root, values=type_sortie, state="readonly")
combo_sortie.current(0)

combo_sortie.place(x=50, y=150)
label_choix_sortie.place(x=50, y=125)


label = Label(root, text = "Entrer", bg=color1[choixColor], fg=color2[choixColor])
validatecmd = (root.register(OnValidate), '%S', '%d')
label_entry = Entry(root, validate="key", bg=color2[choixColor], fg=color1[choixColor], insertbackground=color1[choixColor], highlightcolor=color1[choixColor], highlightbackground=color2[choixColor], vcmd=validatecmd)
label.place(x=50, y=200)
label_entry.place(x=50, y=225)

label_sortie = Label(root, text = "", bg=color1[choixColor], fg=color2[choixColor])
label_sortie.place(x=200, y=225)

copy_button = Button(root, text="COPIER", bg=color2[choixColor], fg=color1[choixColor], command=CopySortie)
copy_button.place(x=125, y=250)

# LABEL UNI CONV
font1 = tkFont.Font(family="Arial", size=47, weight="bold")
conv = Label(root, text = "CO   V", bg=color1[choixColor], fg=color2[choixColor])
conv.configure(font = font1)
conv.place(x=250, y=90)
u = Label(root, text = "U", bg=color2[choixColor], fg=color1[choixColor])
u.configure(font = font1)
u.place(x=347, y=20)
n = Label(root, text = "N", bg=color2[choixColor], fg=color1[choixColor])
n.configure(font = font1)
n.place(x=347, y=90)
font2 = tkFont.Font(family="Arial", size=40, weight="bold")
i = Label(root, text = " I ", bg=color2[choixColor], fg=color1[choixColor])
i.configure(font = font2)
i.place(x=347, y=160)

root.configure(bg = color1[choixColor])

# Ajouter un bouton pour revenir à l'accueil
bouton_retour = Button(
    root,
    text="Retour à l'accueil",
    font=("Arial", 14),
    bg=color2[choixColor],
    fg=color1[choixColor],
    command=retour_accueil
)
bouton_retour.place(x=50, y=250)

root.mainloop()
