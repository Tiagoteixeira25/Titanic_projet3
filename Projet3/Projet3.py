# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import matplotlib.pyplot as plt
import sys




def ExitSystem():
    sys.exit()



def infos():   
    data = pd.read_excel('titanic3.xls')
    data = data.drop(['classe','état', 'nom', 'sexe', 'ticket',\
                    'age', 'ticket', 'prix payé', 'cabine', 'point d embarquation', 'destination'],axis=1)
    data.dropna()
    lignes_début = len(data.axes[0])
    if sex.get() == 1:
        data = data[data['sexe'] == 'homme']
    if sex.get() == 2:
        data = data[data['sexe'] == 'femme']
    if classe.get() == 1:
        data = data[data['classe'] == 1]
    if classe.get() == 2:
        data = data[data['classe'] == 2]
    if classe.get() == 3:
        data = data[data['classe'] == 3]
    if age.get() == 1:
        data = data[data['age'] < 18]
    if age.get() == 2:
        data = data[data['age'] > 18]
    if etat.get() == 1:
        data = data[data['état'] == 1]
    if etat.get() == 2:
        data = data[data['état'] == 0]
    if embark.get() == 1:
        data = data[data['point d embarquation'] == 'S']
    if embark.get() == 2:
        data = data[data['point d embarquation'] == 'C']
    if embark.get() == 3:
        data = data[data['point d embarquation'] == 'Q']
    if embark.get() == 4:
        data = data[data['point d embarquation'] == 'inconnu']
    total_lignes = len(data.axes[0]) 
    lignes_fin = lignes_début - total_lignes
    return total_lignes,lignes_fin


def graph_show():
    x = infos()
    plt.pie(x, labels = ['Population visée', 'Reste population'],
    couleurs = ['black', '1d110f'],
    explode = [0.3, 0],
    autopct = lambda x: str(round(x, 2)) + '%',
    pctdistance = 0.7, labeldistance = 1.4,
    shadow = True)
    plt.show()





def NouvelleFenetre():
    sex.set(0)
    classe.set(0)
    age.set(0)
    etat.set(0)
    embark.set(0)
    
    canvas_pour_image.delete(ALL)


    window.title("Projet 3 Titanic")
    window.geometry("1200x800")
    window.config(background = "#048B9A")
    window.resizable(width=False,height=False)
    
    canvas_pour_image.create_image(0,0,image = image_de_fond2,anchor='nw')
    canvas_pour_image.create_text(300,25,text="Critères",\
                                 font=("Roman",65, "bold"),anchor='nw')
    canvas_pour_image.create_text(30,125,text="sexe :",\
                                 font=("Roman",33, "bold"),anchor='nw')
    canvas_pour_image.create_text(560,125,text=" classe  :",\
                                 font=("Roman",33, "bold"),anchor='nw')
    canvas_pour_image.create_text(30,300,text="age:",\
                                 font=("Roman",33, "bold"),anchor='nw')
    canvas_pour_image.create_text(560,300,text="état:",\
                                 font=("Roman",33, "bold"),anchor='nw')
    canvas_pour_image.create_text(30,450,text="point d'embarquation:",\
                                 font=("Roman",33, "bold"),anchor='nw')




    case_theme1_option1 = Radiobutton(window,text ='Homme',bg='#F0DA1A',\
                        fg='yellow',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=sex,value=1)
    case_theme1_option2 = Radiobutton(window,text ='Femme',bg='#BF80B9',\
                        fg='pink',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=sex,value=2)


    case_theme2_option1 = Radiobutton(window,text ='1ère Classe',bg='#1AACF0',\
                        fg='blue',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=classe,value=1)
    case_theme2_option2 = Radiobutton(window,text ='2e Classe',bg='#F01A54',\
                        fg='red',font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=classe,value=2)
    case_theme2_option3 = Radiobutton(window,text ='3e Classe',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=classe,value=3)


    case_theme3_option1 = Radiobutton(window,text ='Mineur',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=1)
    case_theme3_option2 = Radiobutton(window,text ='Senior',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=2)
    

    case_theme4_option1 = Radiobutton(window,text ='Oui',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=1)
    case_theme4_option2 = Radiobutton(window,text ='Non',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=2)
        
    case_theme5_option1 = Radiobutton(window,text ='S',bg='#FADF8F',\
                         fg='black',font=("Roman",15),activeforeground='white',\
                         activebackground='#048B9A',variable=age,value=2)
    case_theme5_option2 = Radiobutton(window,text ='C',bg='#FADF8F',\
                         fg='black',font=("Roman",15),activeforeground='white',\
                         activebackground='#048B9A',variable=age,value=2)
    case_theme5_option3 = Radiobutton(window,text ='Q',bg='#FADF8F',\
                         fg='black',font=("Roman",15),activeforeground='white',\
                         activebackground='#048B9A',variable=age,value=2)
        

    button_rechercher = Button(window,text='rechercher',bg='#FDD663',fg='black',\
                        font=("Roman",20),activeforeground='white',\
                        activebackground='#048B9A',command=afficher_graphique)


    case_theme1_option1.place(x=50,y=180)
    case_theme1_option2.place(x=50,y=220)


    case_theme2_option1.place(x=580,y=180)
    case_theme2_option2.place(x=580,y=220)
    case_theme2_option3.place(x=580,y=260)


    case_theme3_option1.place(x=50,y=360)
    case_theme3_option2.place(x=50,y=400)


    case_theme4_option1.place(x=580,y=360)
    case_theme4_option2.place(x=580,y=400)
    
    case_theme5_option1.place(x=50,y=440)
    case_theme5_option2.place(x=50,y=480)
    case_theme5_option1.place(x=50,y=520)
    


    button_rechercher.place(x=380,y=480)


    menu_bar = Menu(window)
    menu_fill = Menu(menu_bar, tearoff=0)
    menu_fill.add_command(label="Choix des stats", command=NouvelleFenetre)
    menu_fill.add_command(label="Quitter", command=ExitSystem)
    menu_bar.add_cascade(label="Fonction", menu=menu_fill)
    window.config(menu=menu_bar)



window = Tk()


sex = IntVar(master= window, value= 0)
classe = IntVar(master= window, value= 0)
age = IntVar(master= window, value= 0)
etat = IntVar(master= window, value= 0)
embark = IntVar(master= window, value= 0)


window.title("Projet 3 Titanic")
window.geometry("710x444")
window.config(background = "#7A7019")
window.resizable(width=False,height=False)

image_de_fond = PhotoImage(file = "Titanic-PNG.png")
image_de_fond2 = PhotoImage(file = "Titanic-PNG2.png")
image_bouton = PhotoImage(file="Rectangle.png")


canvas_pour_image = Canvas(window,width=1300,height=813, bg='white',bd=0,highlightthickness=0)
canvas_pour_image.create_image(0,0,image = image_de_fond,anchor='nw')
canvas_pour_image.create_text(20,150,text="Bienvenue",\
                              font=("Script",35),anchor='nw')
canvas_pour_image.place(x=0,y=0)

menu_bar = Menu(window)
menu_fill = Menu(menu_bar, tearoff=0)
menu_fill.add_command(label="Quitter", command=ExitSystem)
menu_bar.add_cascade(label="Fonction", menu=menu_fill)
window.config(menu=menu_bar)


button1 = Button(window,image= image_bouton,borderwidth=0,\
                                highlightthickness=0,command=NouvelleFenetre)
my_button1_window = canvas_pour_image.create_window\
                    (255,450/2,anchor = "nw",window=button1)




window.mainloop()
