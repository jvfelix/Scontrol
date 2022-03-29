import numpy as np
import control as co
from control import *
from control.matlab import *
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg
from PIL import ImageTk,Image
from math import *
import os
import random
from decimal import Decimal


root = Tk()
root.title('Scontrol 2.0')
img = Image.open("logo.png")
resized = img.resize((246,100),Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(resized)
mylabel = Label(root,image=new_img)
mylabel.place(x = 350,y = 281)
root.geometry("615x615")
root.resizable(0,0)

#funcao para calcular
def calcular(estado):
    if len(gain.get()) == 0:
        kain = 1
    else:
        kain = float(gain.get())
    if estado == 0:
        msg.showwarning("Erro","Selecione entre os tipos: polinomial ou racional")
        return 0
    if (estado == 1):
        stringy_num = numerador.get()
        stringy_den = denominador.get()
        #convertendo numerador
        conv_num = stringy_num.split()
        num = []
        for casa in conv_num:
            num.append(float(casa))
        #convertendo denominador
        conv_den = stringy_den.split()
        den = []
        for casa in conv_den:
            den.append(float(casa))

        if len(num) > len(den):
            msg.showwarning("Control Error","O numerador não pode ter mais coeficientes que o denominador")
            return 0
        #texto para o numerador
        x = 1
        key = 0
        texto = ""
        for i in num:
            if key == 0:
                frase = str(i) + "s^" + str((len(num)-x)) + " "
                key = 1
            else:
                if i > 0:
                    texto = texto + "+"
                    
                frase = str(i) + "s^" + str((len(num)-x)) + " "
                
                
                    
                
                    
            #print(len(num) - x)
            x = x + 1
            texto = texto + frase 
            #texto para o denominador
        x = 1
        key = 0
        texto2 = ""
        for i in den:
            if key == 0:
                frase = str(i) + "s^" + str((len(den)-x)) + " "
                key = 1
            else:
                if i > 0:
                    texto2 = texto2 + "+"
                
                frase = str(i) + "s^" + str((len(den)-x)) + " "
                if i == 0:
                   frase = "+" + str(i) + "s^" + str((len(den)-x)) + " " 
            #print(len(num) - x)
            x = x + 1
            texto2 = texto2 + frase
        #plotagem da linha
        linha = ""
        linha_tb = ""
        for i in texto2:
            linha_tb = "-" + linha_tb
        #plotagem
        i = 500
        while(i > 0):
            linha = "-----------" + linha
            i = i - 1
        #print(texto)
        lb_transfi = Label(lb_transf,text = texto,bg = "white",fg = "black",width = 40)
        lb_transfi.grid(row = 1, column = 1,sticky = W)
        lb_transfi1 = Label(lb_transf,text = texto2,bg = "white",fg = "black",width = 40)
        lb_transfi1.grid(row = 3, column = 1,sticky = W)
        lb_transfi2 = Label(lb_transf,text = linha_tb,bg = "white",fg = "black",width = 40)
        lb_transfi2.grid(row = 2, column = 1,sticky = W)
        ###display
        coluna = 3
        #ganho
        display_planta_topo = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_planta_topo.grid(row = 1, column = 3,sticky = W)
        display_planta = Label(lb_display,text = '-----',bg = "white",fg = "black",width = 5)
        display_planta.grid(row = 2, column = 3,sticky = W)
        display_planta1 = Label(lb_display,text = '--'+'|'+str(kain)+'|'+'--',bg = "white",fg = "black",width = 5)
        display_planta1.grid(row = 3, column = 3,sticky = W)
        display_planta2 = Label(lb_display,text = '-----',bg = "white",fg = "black",width = 5)
        display_planta2.grid(row = 4, column = 3,sticky = W)
        display_planta_baixo = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_planta_baixo.grid(row = 5, column = 3,sticky = W)
        #planta
        display_planta_topo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = 35)
        display_planta_topo.grid(row = 1, column = 4,sticky = W)
        display_planta = Label(lb_display,text = texto,bg = "white",fg = "black",width = 35)
        display_planta.grid(row = 2, column = 4,sticky = W)
        display_planta1 = Label(lb_display,text = linha,bg = "white",fg = "black",width = 35)
        display_planta1.grid(row = 3, column = 4,sticky = W)
        display_planta2 = Label(lb_display,text = texto2,bg = "white",fg = "black",width = 35)
        display_planta2.grid(row = 4, column = 4,sticky = W)
        display_planta_baixo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = 35)
        display_planta_baixo.grid(row = 5, column = 4,sticky = W)
        #display realimentaçao
        espaço = 10
        coluna = 3
        display_feed = Label(lb_display,text = linha,bg = "white",fg = "black",width = 35)
        display_feed.grid(row = 6, column = 4,sticky = W)
        display_feed = Label(lb_display,text = linha,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 6, column = 3,sticky = W)
        coluna = 1
        display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 1, column = coluna,sticky = W)
        display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 2, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "(S-)----",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 3, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 4, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 5, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "  |------",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 6, column = coluna,sticky = W)

        coluna = 5
        display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 1, column = coluna,sticky = W)
        display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 2, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "--------|",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 3, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "             |",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 4, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "             |",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 5, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "--------|",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 6, column = coluna,sticky = W)
        #print(texto)
        G = kain*co.tf(num,den)
        polor = co.pole(G)
        zeror = co.zero(G)
        polos = np.round(polor,2)
        zeros = np.round(zeror,2)
        resultado_zero = Label(lb_transf,text = str(zeros),bg = "white",fg = "black",width= 40).grid(row = 7, column = 1,sticky = W)
        resultado_polo = Label(lb_transf,text = str(polos),bg = "white",fg = "black",width= 40).grid(row = 9, column = 1,sticky = W)
        vetor_rac_inv = np.roots(den)
        vetor_rac = -np.round(vetor_rac_inv,2)
        #print(vetor_rac)
        x = len(vetor_rac)
        i = 0
        while(x>0):
            if(den[i] > 0):
                conteudo = "(" + "s" + " " + "+" + " " + str(vetor_rac[i]) + ")"
            if(den[i] < 0):
                conteudo = "(" + "s" + " " + str(vetor_rac[i]) + ")"
            if(den[i] == 0):
                conteudo = "s"             
            if(i==0):
                texto2 = conteudo
            else:
                texto2 = texto2 + conteudo
            i = i + 1
            x = x - 1
        linha = ""
        for i in texto2:
            linha = "-" + linha
        lb_transfi_rac = Label(lb_transf_rac,text = texto,bg = "white",fg = "black",width = 40)
        lb_transfi_rac.grid(row = 1, column = 1,sticky = W)
        lb_transfi1_rac = Label(lb_transf_rac,text = texto2,bg = "white",fg = "black",width = 40)
        lb_transfi1_rac.grid(row = 3, column = 1,sticky = W)
        lb_transfi2_rac = Label(lb_transf_rac,text = linha,bg = "white",fg = "black",width = 40)
        lb_transfi2_rac.grid(row = 2, column = 1,sticky = W)
        print(G)
        
        return G
    if(estado == 2):
        if len(gain.get()) == 0:
            kain = 1

        else:
            kain = float(gain.get())
        
        stringy_num = numerador.get()
        stringy_den = denominador.get()
        #convertendo numerador
        conv_num = stringy_num.split()
        num = []
        for casa in conv_num:
            num.append(float(casa))
        #convertendo denominador
        conv_den = stringy_den.split()
        den = []
        for casa in conv_den:
            den.append(float(casa))

        if len(num) > len(den):
            msg.showwarning("Error","O numerador não pode ter mais coeficientes que o denominador")
            return 0
        if 4 < len(den):
            msg.showwarning("Error","Limite de denominador extrapolado")
            return 0
        #texto para o numerador
        x = 1
        key = 0
        texto = ""
        for i in num:
            if key == 0:
                frase = str(i) + "s^" + str((len(num)-x)) + " "
                key = 1
            else:
                if i > 0:
                    texto = texto + "+"
                frase = str(i) + "s^" + str((len(num)-x)) + " "
                
                    
            #print(len(num) - x)
            x = x + 1
            texto = texto + frase 
        #texto para o denominador
        x = len(den)
        print(den)
        i = 0
        while(x>0):
            if(den[i] > 0):
                conteudo = "(" + "s" + " " + "+" + " " + str(den[i]) + ")"
            if(den[i] < 0):
                conteudo = "(" + "s" + " " + str(den[i]) + ")"
            if(den[i] == 0):
                conteudo = "s"             
            if(i==0):
                texto2 = conteudo
            else:
                texto2 = texto2 + conteudo
            i = i + 1
            x = x - 1
        print(texto)   
        #plotagem da linha
        linha = ""
        linha_tb = ""
        for i in texto2:
            linha_tb = "-" + linha_tb
        #plotagem
        i = 50
        while(i > 0):
            linha = "-" + linha
            i = i - 1
        #plotagem
        #print(texto)
        lb_transfi = Label(lb_transf_rac,text = texto,bg = "white",fg = "black",width = 40)
        lb_transfi.grid(row = 1, column = 1,sticky = W)
        lb_transfi1 = Label(lb_transf_rac,text = texto2,bg = "white",fg = "black",width = 40)
        lb_transfi1.grid(row = 3, column = 1,sticky = W)
        lb_transfi2 = Label(lb_transf_rac,text = linha_tb,bg = "white",fg = "black",width = 40)
        lb_transfi2.grid(row = 2, column = 1,sticky = W)
        ###display
        coluna = 3
        #ganho
        display_planta_topo = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_planta_topo.grid(row = 1, column = 3,sticky = W)
        display_planta = Label(lb_display,text = '-----',bg = "white",fg = "black",width = 5)
        display_planta.grid(row = 2, column = 3,sticky = W)
        display_planta1 = Label(lb_display,text = '--'+'|'+str(kain)+'|'+'--',bg = "white",fg = "black",width = 5)
        display_planta1.grid(row = 3, column = 3,sticky = W)
        display_planta2 = Label(lb_display,text = '-----',bg = "white",fg = "black",width = 5)
        display_planta2.grid(row = 4, column = 3,sticky = W)
        display_planta_baixo = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_planta_baixo.grid(row = 5, column = 3,sticky = W)
        #planta
        display_planta_topo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = 35)
        display_planta_topo.grid(row = 1, column = 4,sticky = W)
        display_planta = Label(lb_display,text = texto,bg = "white",fg = "black",width = 35)
        display_planta.grid(row = 2, column = 4,sticky = W)
        display_planta1 = Label(lb_display,text = linha,bg = "white",fg = "black",width = 35)
        display_planta1.grid(row = 3, column = 4,sticky = W)
        display_planta2 = Label(lb_display,text = texto2,bg = "white",fg = "black",width = 35)
        display_planta2.grid(row = 4, column = 4,sticky = W)
        display_planta_baixo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = 35)
        display_planta_baixo.grid(row = 5, column = 4,sticky = W)
        #display realimentaçao
        espaço = 10
        coluna = 3
        display_feed = Label(lb_display,text = linha,bg = "white",fg = "black",width = 35)
        display_feed.grid(row = 6, column = 4,sticky = W)
        display_feed = Label(lb_display,text = linha,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 6, column = 3,sticky = W)
        coluna = 1
        display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 1, column = coluna,sticky = W)
        display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 2, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "(S-)----",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 3, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 4, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 5, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "  |------",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 6, column = coluna,sticky = W)

        coluna = 5
        display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 1, column = coluna,sticky = W)
        display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 2, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "--------|",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 3, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "             |",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 4, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "             |",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 5, column = coluna,sticky = W)
        display_feed = Label(lb_display,text = "--------|",bg = "white",fg = "black",width = 5)
        display_feed.grid(row = 6, column = coluna,sticky = W)
        #print(texto)
        #tranformar na forma
        dencov = []
        if(len(den) == 1):
            dencov.append(1.0)
            dencov.append(den[0])
            G = co.tf(num,dencov)
            print(G)
        if(len(den) == 2):
            dencov.append(1.0)
            dencov.append(den[0] + den[1])
            dencov.append(den[1]*den[0])
            G = co.tf(num,dencov)
            print(G)
        if(len(den) == 3):
            dencov.append(1.0)
            dencov.append(den[0] + den[1] + den[2])
            dencov.append(den[1]*den[0] + den[1]*den[2] + den[0]*den[2])
            dencov.append(den[0]*den[1]*den[2])
            G = co.tf(num,dencov)
            print(G)
        if(len(den) == 4):
            dencov.append(1.0)
            dencov.append(den[0] + den[1] + den[2] + den[3])
            dencov.append(den[1]*den[0] + den[1]*den[2] + den[0]*den[2] + den[3]*den[0] + den[1]*den[3] + den[3]*den[2])
            dencov.append(den[1]*den[2]*den[3] + den[0]*den[2]*den[3] + den[0]*den[1]*den[3] + den[1]*den[2]*den[0])
            dencov.append(den[0]*den[1]*den[2]*den[3])
            G = co.tf(num,dencov)
            print(G)
        #plotagem forma normal
        x = 1
        key = 0
        texto = ""
        for i in num:
            if key == 0:
                frase = str(i) + "s^" + str((len(num)-x)) + " "
                key = 1
            else:
                if i > 0:
                    texto = texto + "+"
                frase = str(i) + "s^" + str((len(num)-x)) + " "
                
                    
            #print(len(num) - x)
            x = x + 1
            texto = texto + frase 
            #texto para o denominador
        x = 1
        key = 0
        texto2 = ""
        for i in dencov:
            if key == 0:
                frase = str(i) + "s^" + str((len(dencov)-x)) + " "
                key = 1
            else:
                if i > 0:
                    texto2 = texto2 + "+"
                frase = str(i) + "s^" + str((len(dencov)-x)) + " "
                if i == 0:
                    frase = "+" + str(i) + "s^" + str((len(dencov)-x)) + " " 
                
            #print(len(num) - x)
            x = x + 1
            texto2 = texto2 + frase
        linha = ""
        linha_tb = ""
        for i in texto2:
            linha_tb = "-" + linha_tb
        #plotagem
        i = 50
        while(i > 0):
            linha = "-" + linha
            i = i - 1
        #plotagem
        lb_transfi = Label(lb_transf,text = texto,bg = "white",fg = "black",width = 40)
        lb_transfi.grid(row = 1, column = 1,sticky = W)
        lb_transfi1 = Label(lb_transf,text = texto2,bg = "white",fg = "black",width = 40)
        lb_transfi1.grid(row = 3, column = 1,sticky = W)
        lb_transfi2 = Label(lb_transf,text = linha,bg = "white",fg = "black",width = 40)
        lb_transfi2.grid(row = 2, column = 1,sticky = W)
        
        polos = co.pole(G)
        zeros = co.zero(G)
        resultado_zero = Label(lb_transf_rac,text = str(zeros),bg = "white",fg = "black",width= 40).grid(row = 7, column = 1,sticky = W)
        resultado_polo = Label(lb_transf_rac,text = str(polos),bg = "white",fg = "black",width= 40).grid(row = 9, column = 1,sticky = W)  
        print(polos)
        print(den)
        Grac = kain*G
        return Grac
        
########################################################################################
def print_file(imagem):
    script_dir = os.path.dirname(__file__)
    rel_path = "../images/"
    abs_file_path = os.path.join(script_dir, rel_path)
    current_file ="image" + str(X) +".png"
    file = open(abs_file_path+current_file,'r')
        
            
        
    
#####################degrau
def degrau(transf):
    t = np.linspace(0,10,1000)
    t1,y1 = co.step_response(transf,t)
    plt.figure(1)
    plt.plot(t1,y1)
    
    plt.grid()
    plt.xlabel("tempo")
    plt.ylabel("amplitude")
    plt.legend()
    plt.show()
######################feedback
def feedback(transf):
    G = co.feedback(transf)
    t = np.linspace(0,10,1000)
    t1,y1 = co.step_response(G,t)
    plt.figure(1)
    plt.plot(t1,y1)
    
    plt.grid()
    plt.xlabel("tempo")
    plt.ylabel("amplitude")
    plt.legend()
    plt.show()
######################Impulso
def impulso(transf):
    #rampa
    t = np.linspace(0,1,1000)
    num = [1.0]
    den = [1.0, 0]
    ent = co.tf(num,den)
    G2 = ent*transf
    print(G2)
    t1,y1 = co.step_response(G2,t)
    plt.figure(1)
    plt.plot(t1,y1)
    
    plt.grid()
    plt.xlabel("tempo")
    plt.ylabel("amplitude")
    plt.legend()
    plt.show()
##################### grafico
def grafico(transf,h):
    if h == 0:
        msg.showwarning("Erro","Entrada não selecionada")
        return 0
    stringy_num = numerador.get()
    stringy_den = denominador.get()
    ccor = random.randrange(0,9)
    print(transf)
    tempo = float(tempo_graf.get())
    string_de_cor = ['#00008B','#8B0000','#008B8B','#006400','#FF7F00','#00FA9A','#CD6889','#9B30FF','#8B5742','#FFC1C1']
    
    if h == 1:
        if len(amp_deg.get()) == 0 or len(tempo_graf.get()) == 0:
            msg.showwarning("Erro","Parâmetros de entrada incorretos")
            return 0
        amplitude = float(amp_deg.get())
        #convertendo numerador
        conv_num = stringy_num.split()
        num = []
        for casa in conv_num:
            num.append(float(casa))
        #convertendo denominador
        conv_den = stringy_den.split()
        den = []
        for casa in conv_den:
            den.append(float(casa))
        tamD = len(den)
        tamN = len(num)
        y = (amplitude*num[0])
    
        t = np.linspace(0,tempo,1000)
        n_transf = amplitude*transf
        G = co.feedback(n_transf,1,-1)
        t1,y1 = co.step_response(G,t)
        t2,y2 = co.step_response(amplitude,t)
        #degrau
        
        
        plt.figure(1)
        plt.plot(t1,y1,c = string_de_cor[ccor], lw = 3., label = 'Saída')
        plt.plot(t2,y2,c = 'green', lw = 3., label = 'Entrada')
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show()
    if h == 2:
        #rampa
        ruido = 0
        if(ruido == 0):
            t = np.linspace(0,tempo,1000)
            num = [1.0]
            den = [1.0, 0]
            ent = co.tf(num,den)
            G2 = ent*transf
            G = co.feedback(G2,1,-1)
            print(G2)
            t1,y1 = co.step_response(G,t)
            t2,y2 = co.step_response(ent,t)
            plt.plot(t1,y1,c = string_de_cor[ccor], lw = 3., label = 'Saída')
            plt.plot(t2,y2,c = 'green', lw = 3., label = 'Entrada')
            plt.grid(True)
            plt.xlabel("tempo")
            plt.ylabel("amplitude")
            plt.legend()
            plt.show()
        
            
    if h == 3:
        ruido = 0
        w = float(freq_sen.get())
        w2 = w*w
        t = np.linspace(0,tempo,1000)
        num = [w]
        den = [1.0, 0, w2]
        ent2 = co.tf(num,den)
        print(ent2)
        n2 = [1.0, 0]
        d2 = [1.0]
        G3 = co.tf(n2,d2)
        G2 = ent2*transf*G3
        G = co.feedback(G2,1,-1)
        if(ruido == 0):
            t1,y1 = co.step_response(G,t)
            t2,y2 = co.step_response(ent2,t)
            plt.plot(t1,y1,c = string_de_cor[ccor], lw = 3., label = 'Saída')
            plt.plot(t2,y2,c = 'green', lw = 3., label = 'Entrada')
            plt.grid(True)
            plt.xlabel("tempo")
            plt.ylabel("amplitude")
            plt.legend()
            plt.show() 

    if h == 4:
        G = co.feedback(transf,1,-1)
        t = np.linspace(0,tempo,1000)
        t1,y1 = co.step_response(G,t)
        plt.figure(1)
        plt.plot(t1,y1)
    
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show()
        
#################################################################################
def avanco_fase(transf,x,a,z,p,k):
    pkc = float(k)
    #err = float(atraso_f.get())
    tempo = float(tempo_graf.get())
    #tempo = 10
    stringy_num = z
    stringy_den = p
    #convertendo numerador
    conv_num = stringy_num.split()
    num = []
    for casa in conv_num:
        num.append(float(casa))
    #convertendo denominador
    conv_den = stringy_den.split()
    den = []
    for casa in conv_den:
        den.append(float(casa))
    
    #plotagem
    x = 1
    key = 0
    texto = str(pkc) + "*" + "| " 
    for i in num:
        if key == 0:
            frase = str(i) + "s^" + str((len(num)-x)) + " "
            key = 1
        else:
            if i > 0:
                texto = texto + "+"
            frase = str(i) + "s^" + str((len(num)-x)) + " "
                
                    
        #print(len(num) - x)
        x = x + 1
        texto = texto + frase 
        #texto para o denominador
    texto = texto + " |"
    x = 1
    key = 0
    texto2 = "| "
    for i in den:
        if key == 0:
            frase = str(i) + "s^" + str((len(den)-x)) + " "
            key = 1
        else:
            if i > 0:
                texto2 = texto2 + "+"
            frase = str(i) + "s^" + str((len(den)-x)) + " "
                
                    
        #print(len(num) - x)
        x = x + 1
        texto2 = texto2 + frase
    #plotagem da linha
    texto2 = texto2 + " |"
    linha = ""
    i = 50
    while(i > 0):
        linha = linha + "-"
        i = i - 1
    #plotagem da linha topo
    linha_tb = ""
    for i in texto2:
        linha_tb = "-" + linha_tb
    widt = 35
    coluna = 2
    print(len(linha_tb))
    display_control_topo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = widt)
    display_control_topo.grid(row = 1, column = coluna,sticky = W)
    display_control = Label(lb_display,text = texto,bg = "white",fg = "black",width = widt)
    display_control.grid(row = 2, column = coluna,sticky = W)
    display_control1 = Label(lb_display,text = linha,bg = "white",fg = "black",width = widt)
    display_control1.grid(row = 3, column = coluna,sticky = W)
    display_control2 = Label(lb_display,text = texto2,bg = "white",fg = "black",width = widt)
    display_control2.grid(row = 4, column = coluna,sticky = W)
    display_control_baixo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = widt)
    display_control_baixo.grid(row = 5, column = coluna,sticky = W)
    #realimentaçao
    espaço = 10
    display_feed = Label(lb_display,text = linha,bg = "white",fg = "black",width = 35)
    display_feed.grid(row = 6, column = coluna,sticky = W)
    coluna = 1
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 1, column = coluna,sticky = W)
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 2, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "(S-)----",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 3, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 4, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 5, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "  |------",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 6, column = coluna,sticky = W)

    coluna = 4
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 1, column = coluna,sticky = W)
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 2, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "------|",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 3, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "          |",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 4, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "          |",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 5, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "------|",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 6, column = coluna,sticky = W)
    if a == 1:
        Gco = pkc*(co.tf(num,den))
        print(Gco)
        A_deg = float(amp_deg.get())
        print(transf)
        G1 = A_deg*Gco*transf
        print(G1)
        transf1 = A_deg*transf
        G = co.feedback(G1,1,-1)
        Ga = co.feedback(transf1,1,-1)
        print(G)
        t = np.linspace(0,tempo,1000)
        t1,y1 = co.step_response(G,t)
        t2,y2 = co.step_response(Ga,t)
        t3,y3 = co.step_response(A_deg,t)
        plt.figure(2)
        plt.plot(t1,y1,c = 'blue', lw = 3., label = 'Compensador')
        plt.plot(t2,y2,c = 'orange', lw = 3., label = 'MF sem Controlador')
        plt.plot(t3,y3,c = 'green', lw = 3., label = 'Entrada')
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show()

    if a == 2:
        Gco = pkc*(co.tf(num,den))
        print(Gco)
            
            
        num = [1.0]
        den = [1.0, 0]
        ent = co.tf(num,den)
        G2 = ent*transf*Gco
        Gt = co.feedback(G2,1,-1)
        Ga = co.feedback(transf,1,-1)
        t = np.linspace(0,tempo,1000)
        t1,y1 = co.step_response(Gt,t)
        t2,y2 = co.step_response(Ga,t)
        plt.figure(2)
        plt.plot(t1,y1,c = 'blue', lw = 3., label = 'Compensador')
        plt.plot(t2,y2,c = 'green', lw = 3., label = 'MF sem Controlador')
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show()
    if a == 3:
        Gco = pkc*(co.tf(num,den))
        print(Gco)
            
        w = float(freq_sen.get())
        w2 = w*w
        Ga = co.feedback(transf,1,-1)
        t = np.linspace(0,tempo,1000)
        num = [w]
        den = [1.0, 0, w2]
        ent2 = co.tf(num,den)
        print(ent2)
        n2 = [1.0, 0]
        d2 = [1.0]
        ent3 = co.tf(n2,d2)
        G2 = ent2*ent3*transf
        Ga = co.feedback(G2,1,-1)
        Gt = ent2*ent3*Gco*transf
        t1,y1 = co.step_response(Gt,t)
        t2,y2 = co.step_response(Ga,t)
        plt.figure(2)
        plt.plot(t1,y1,c = 'blue', lw = 3., label = 'Compensador')
        plt.plot(t2,y2,c = 'green', lw = 3., label = 'MF sem Controlador')
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show()
            
#################################################################################
def pid(transf,x,p,i,k):
    kp = float(p)
    ki = float(i)
    kd = float(k)
    if len(amp_deg.get()) == 0 or len(tempo_graf.get()) == 0:
        msg.showwarning("Erro","Parâmetros de entrada incorretos")
        return 0
    A_deg = float(amp_deg.get())
    tempo = float(tempo_graf.get())
    num = [1.0, ki]
    den = [1.0, kd]
    #plotagem
    x = 1
    key = 0
    texto = str(kp) + "*"+ "| "
    for i in num:
        if key == 0:
            frase = str(i) + "s^" + str((len(num)-x)) + " "
            key = 1
        else:
            if i > 0:
                texto = texto + "+"
            frase = str(i) + "s^" + str((len(num)-x)) + " "
                
                    
        #print(len(num) - x)
        x = x + 1
        texto = texto + frase 
        #texto para o denominador
    texto = texto + " |"
    x = 1
    key = 0
    texto2 = "| "
    for i in den:
        if key == 0:
            frase = str(i) + "s^" + str((len(den)-x)) + " "
            key = 1
        else:
            if i > 0:
                texto2 = texto2 + "+"
            frase = str(i) + "s^" + str((len(den)-x)) + " "
                
                    
        #print(len(num) - x)
        x = x + 1
        texto2 = texto2 + frase
    #plotagem da linha
    texto2 = texto2 + " |"
    linha = ""
    i = 50
    while(i > 0):
        linha = linha + "-"
        i = i - 1
    #plotagem da linha topo
    linha_tb = ""
    for i in texto2:
        linha_tb = "-" + linha_tb
    widt = 25
    coluna = 2
    print(len(linha_tb))
    display_control_topo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = widt)
    display_control_topo.grid(row = 1, column = coluna,sticky = W)
    display_control = Label(lb_display,text = texto,bg = "white",fg = "black",width = widt)
    display_control.grid(row = 2, column = coluna,sticky = W)
    display_control1 = Label(lb_display,text = linha,bg = "white",fg = "black",width = widt)
    display_control1.grid(row = 3, column = coluna,sticky = W)
    display_control2 = Label(lb_display,text = texto2,bg = "white",fg = "black",width = widt)
    display_control2.grid(row = 4, column = coluna,sticky = W)
    display_control_baixo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = widt)
    display_control_baixo.grid(row = 5, column = coluna,sticky = W)
    #realimentaçao
    espaço = 10
    display_feed = Label(lb_display,text = linha,bg = "white",fg = "black",width = 25)
    display_feed.grid(row = 6, column = coluna,sticky = W)
    coluna = 1
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 1, column = coluna,sticky = W)
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 2, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "(S-)----",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 3, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 4, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 5, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "  |------",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 6, column = coluna,sticky = W)

    coluna = 5
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 1, column = coluna,sticky = W)
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 2, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "--------|",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 3, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "             |",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 4, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "             |",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 5, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "--------|",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 6, column = coluna,sticky = W)
    
    if len(gain.get()) == 0:
        kain = 1
    else:
        kain = float(gain.get())
    #proporcional
    nump = [kp]
    denp = [1.0]
    gp = co.tf(nump,denp)
    #integral
    numi = [ki]
    deni = [1.0, 0.0]
    gi = co.tf(numi,deni)
    #derivativo
    numd = [kd, 0.0]
    dend = [1.0]
    gd = co.tf(numd,dend)
    #controlador
    gc = gp + gi + gd
    Gpid = 1*A_deg*gc*transf
    Ga = co.feedback(kain*A_deg*transf,1,-1)
    G = co.feedback(Gpid,1,-1)
    t = np.linspace(0,tempo,100)
    t1,y1 = co.step_response(G,t)
    t2,y2 = co.step_response(Ga,t)
    t3,y3 = co.step_response(A_deg,t)
    plt.figure(3)
    plt.plot(t1,y1,c = 'blue', lw = 3., label = 'PID')
    plt.plot(t2,y2,c = 'orange', lw = 3., label = 'MF sem Controlador')
    plt.plot(t3,y3,c = 'green', lw = 3., label = 'Entrada')
    plt.grid(True)
    plt.xlabel("tempo")
    plt.ylabel("amplitude")
    plt.legend()
    plt.show()
    
#################################################################################
def mapaZP(transf):
    [p,z] = co.pzmap(transf)
    vetor_zero = []
    vetor_polo = []
    if(len(z) < len(p)):
        for i in p:
            print(i)
        plt.figure(1)
        plt.plot(vetor_polo,vetor_zero)
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.show()
    if(len(z) > len(p)):
        for i in p:
            print(i)
        plt.figure(1)
        plt.plot(vetor_polo,vetor_zero)
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.show()
    if(len(z) == len(p)):
        for i in p:
            print(i)
        plt.figure(1)
        plt.plot(vetor_polo,vetor_zero)
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.show()
##############################################
def mapaZP_rac(transf):
    [p,z] = co.pzmap(transf)
    vetor_zero = []
    vetor_polo = []
    if(len(z) < len(p)):
        for i in p:
            print(i)
        plt.figure(1)
        plt.plot(vetor_polo,vetor_zero)
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.show()
    if(len(z) > len(p)):
        for i in p:
            print(i)
        plt.figure(1)
        plt.plot(vetor_polo,vetor_zero)
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.show()
    if(len(z) == len(p)):
        for i in p:
            print(i)
        plt.figure(1)
        plt.plot(vetor_polo,vetor_zero)
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.show()
def tiko(transf,entrada):
    root = Tk()
    root.title('Compensador')
    root.geometry("350x100")
    root.resizable(0,0)
    b = 1
    mostrar_pz_af = Label(root,text = 'Numerador:').grid(row = 6,column = 1,sticky = W)
    mostrar_pq_af = Label(root,text = 'Denominador:').grid(row = 7,column = 1,sticky = W)
    mostrar_pq_af = Label(root,text = 'Ganho(Kc):').grid(row = 5,column = 1,sticky = W)
    atraso_pz = Entry(root,width = 40)
    atraso_pq = Entry(root,width = 40)
    atraso_pkc = Entry(root,width = 10)
    botao_af = Button(root,text = "Calcular",padx = 20,pady = 5,command = lambda: avanco_fase(transf,b,entrada,atraso_pz.get(),atraso_pq.get(),atraso_pkc.get())).grid(row = 8,column = 1)
    
    atraso_pz.grid(row = 6,column = 2)
    atraso_pq.grid(row = 7,column = 2)
    atraso_pkc.grid(row = 5,column = 2)
    root.mainloop()
def pid_fun(transf,x):
    root = Tk()
    root.title('Controlador PID')
    root.geometry("350x100")
    root.resizable(0,0)
    b = 1
    pid_kp = Entry(root,width=20)
    pid_ki = Entry(root,width=20)
    pid_kd = Entry(root,width=20)
    mostrar_pq_af = Label(root,text = 'Ganho Proporcional(Kp):').grid(row = 1,column = 0,sticky = W)
    mostrar_pq_af = Label(root,text = 'Ganho Integral(Kp/Ti):').grid(row = 2,column = 0,sticky = W)
    mostrar_pq_af = Label(root,text = 'Ganho Derivativo(Kp*Td):').grid(row = 3,column = 0,sticky = W)
    botao_pid = Button(root,text = "Executar",padx = 20,pady = 5,command = lambda: pid(transf,b,pid_kp.get(),pid_ki.get(),pid_kd.get())).grid(row = 4,column = 0)#pid
    pid_kp.grid(row = 1,column = 1)
    pid_ki.grid(row = 2,column = 1)
    pid_kd.grid(row = 3,column = 1)
    root.mainloop()
def comparar(transf,entrada):
    if entrada == 0 or len(tempo_graf.get()) == 0 or len(amp_deg.get()) == 0:
        msg.showwarning("Erro","Revise os parâmetros de entrada")
        return 0
    tempo = float(tempo_graf.get())
    if(entrada == 1):
        amplitude = float(amp_deg.get())
        t = np.linspace(0,tempo,1000)
        n_transf = amplitude*transf
        G = co.feedback(n_transf,1,-1)
        t1,y1 = co.step_response(G,t)
        t2,y2 = co.step_response(transf*amplitude,t)
        #degrau
        
        plt.figure(1)
        plt.plot(t1,y1,c = 'blue', lw = 3., label = 'Malha Fechada')
        plt.plot(t2,y2,c = 'green', lw = 3., label = 'Malha Aberta')
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show() 
def c_at_av(transf,entrada):
    if entrada == 0:
        msg.showwarning("Erro","Entrada não selecionada")
        return 0
    root = Tk()
    root.title('Compensador')
    root.geometry("350x300")
    root.resizable(0,0)
    b = 1
    atrasok = Entry(root,width=20)
    atraso_num = Entry(root,width=20)
    atraso_den = Entry(root,width=20)
    avancok = Entry(root,width=20)
    avanco_num = Entry(root,width=20)
    avanco_den = Entry(root,width=20)
    mostrar = Label(root,text = 'Compensador de atraso').grid(row = 1,column = 0,sticky = W)
    mostrar_atrasok = Label(root,text = 'Ganho:').grid(row = 2,column = 0,sticky = W)
    mostrar_atraso_num = Label(root,text = 'Numerador:').grid(row = 3,column = 0,sticky = W)
    mostrar_atraso_den  = Label(root,text = 'Denominador:').grid(row = 4,column = 0,sticky = W)
    mostrar_avanco = Label(root,text = 'Compensador de avanço').grid(row = 5,column = 0,sticky = W)
    mostrar_atrasok = Label(root,text = 'Ganho:').grid(row = 6,column = 0,sticky = W)
    mostrar_atraso_num = Label(root,text = 'Numerador:').grid(row = 7,column = 0,sticky = W)
    mostrar_atraso_den  = Label(root,text = 'Denominador:').grid(row = 8,column = 0,sticky = W)
    botao_pid = Button(root,text = "Executar",padx = 20,pady = 5,command = lambda: comp_at_av(transf,b,entrada,atrasok.get(),atraso_num.get(),atraso_den.get(),avancok.get(),avanco_num.get(),avanco_den.get())).grid(row = 9,column = 0)#atraso
    atrasok.grid(row = 2,column = 1)
    atraso_num.grid(row = 3,column = 1)
    atraso_den.grid(row = 4,column = 1)
    avancok.grid(row = 6,column = 1)
    avanco_num.grid(row = 7,column = 1)
    avanco_den.grid(row = 8,column = 1)
    root.mainloop()
##################################################################################################################
def comp_at_av(transf,x,input,k_at,n_at,d_at,k_av,n_av,d_av):
    if len(gain.get()) == 0:
        kain = 1
    else:
        kain = float(gain.get())
    if len(k_at) == 0 and len(n_at) == 0 and len(d_at) == 0:
        k_at = '1.0'
        n_at = '1.0'
        d_at = '1.0'
    if len(k_av) == 0 and len(n_av) == 0 and len(d_av) == 0:
        k_av = '1.0'
        n_av = '1.0'
        d_av = '1.0'
    atk = float(k_at)
    stringy_num = n_at
    stringy_den = d_at
    #convertendo numerador
    conv_num = stringy_num.split()
    num_at = []
    for casa in conv_num:
        num_at.append(float(casa))
    #convertendo denominador
    conv_den = stringy_den.split()
    den_at = []
    for casa in conv_den:
        den_at.append(float(casa))
    #########avanco
    avk = float(k_av)
    stringy_num = n_av
    stringy_den = d_av
    #convertendo numerador
    conv_num = stringy_num.split()
    num_av = []
    for casa in conv_num:
        num_av.append(float(casa))
    #convertendo denominador
    conv_den = stringy_den.split()
    den_av = []
    for casa in conv_den:
        den_av.append(float(casa))
    Gat = atk*co.tf(num_at,den_at)
    #print(Gat)
    Gav = avk*co.tf(num_av,den_av)
    #print(Gav)
    Gc = Gat*Gav
    print(Gc)
    k = atk*avk
    
    
    print_num = []
    print_den = []

    if len(num_at) == 1 and len(num_av) == 1:
        print_num = [np.round(num_at[0]*num_av[0],3)]
    if len(den_at) == 1 and len(den_av) == 1:
        print_den = [np.round(den_at[0]*den_av[0],3)]
    
    if len(num_at) == 2 and len(num_av) == 2:
        print_num = [np.round(num_at[0]*num_av[0],3),np.round(num_at[0]*num_av[1] + num_at[1]*num_av[0],3),np.round(num_at[1]*num_av[1],3)]
    if len(den_at) == 2 and len(den_av) == 2:
        print_den = [np.round(den_at[0]*den_av[0],3),np.round(den_at[0]*den_av[1] + den_at[1]*den_av[0],3),np.round(den_at[1]*den_av[1],3)]


    if len(num_at) == 1 and len(num_av) == 2:
        print_num = [np.round(num_at[0]*num_av[0],3),np.round(num_at[0]*num_av[1],3)]
    if len(den_at) == 1 and len(den_av) == 2:
        print_den = [np.round(den_at[0]*den_av[0],3),np.round(den_at[0]*den_av[1],3)]

    if len(num_at) == 1 and len(num_av) == 3:
        print_num = [np.round(num_at[0]*num_av[0],3),np.round(num_at[0]*num_av[1],3),np.round(num_at[0]*num_av[2],3)]
    if len(den_at) == 1 and len(den_av) == 3:
        print_den = [np.round(den_at[0]*den_av[0],3),np.round(den_at[0]*den_av[1],3),np.round(den_at[0]*den_av[2],3)]

    if len(num_at) == 2 and len(num_av) == 1:
        print_num = [np.round(num_at[0]*num_av[0],3),np.round(num_at[1]*num_av[0],3)]
    if len(den_at) == 2 and len(den_av) == 1:
        print_den = [np.round(den_at[0]*den_av[0],3),np.round(den_at[1]*den_av[0],3)]

    if len(num_at) == 3 and len(num_av) == 1:
        print_num = [np.round(num_at[0]*num_av[0],3),np.round(num_at[1]*num_av[0],3),np.round(num_at[2]*num_av[0],3)]
    if len(den_at) == 3 and len(den_av) == 1:
        print_den = [np.round(den_at[0]*den_av[0],3),np.round(den_at[1]*den_av[0],3),np.round(den_at[2]*den_av[0],3)]
    print(print_num)
    print(print_den)
    #################plotagem
    x = 1
    key = 0
    print_k = np.round(k,3)
    texto = str(print_k) + "*"+ "| "
    for i in print_num:
        if key == 0:
            frase = str(i) + "s^" + str((len(print_num)-x)) + " "
            key = 1
        else:
            if i > 0:
                texto = texto + "+"
            frase = str(i) + "s^" + str((len(print_num)-x)) + " "
                
                    
        #print(len(num) - x)
        x = x + 1
        texto = texto + frase 
        #texto para o denominador
    texto = texto + " |"
    x = 1
    key = 0
    texto2 = "| "
    for i in print_den:
        if key == 0:
            frase = str(i) + "s^" + str((len(print_den)-x)) + " "
            key = 1
        else:
            if i > 0:
                texto2 = texto2 + "+"
            frase = str(i) + "s^" + str((len(print_den)-x)) + " "
                
                    
        #print(len(num) - x)
        x = x + 1
        texto2 = texto2 + frase

    linha = ""
    i = 50
    while(i > 0):
        linha = linha + "-"
        i = i - 1
    #plotagem da linha topo
    linha_tb = ""
    for i in texto2:
        linha_tb = "-" + linha_tb
    widt = 25
    coluna = 2
    print(len(linha_tb))
    display_control_topo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = widt)
    display_control_topo.grid(row = 1, column = coluna,sticky = W)
    display_control = Label(lb_display,text = texto,bg = "white",fg = "black",width = widt)
    display_control.grid(row = 2, column = coluna,sticky = W)
    display_control1 = Label(lb_display,text = linha,bg = "white",fg = "black",width = widt)
    display_control1.grid(row = 3, column = coluna,sticky = W)
    display_control2 = Label(lb_display,text = texto2,bg = "white",fg = "black",width = widt)
    display_control2.grid(row = 4, column = coluna,sticky = W)
    display_control_baixo = Label(lb_display,text = linha_tb,bg = "white",fg = "black",width = widt)
    display_control_baixo.grid(row = 5, column = coluna,sticky = W)
    #realimentaçao
    espaço = 10
    display_feed = Label(lb_display,text = linha,bg = "white",fg = "black",width = 25)
    display_feed.grid(row = 6, column = coluna,sticky = W)
    coluna = 1
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 1, column = coluna,sticky = W)
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 2, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "(S-)----",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 3, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 4, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "|        ",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 5, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "  |------",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 6, column = coluna,sticky = W)

    coluna = 5
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 1, column = coluna,sticky = W)
    display_feed = Label(lb_display,bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 2, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "------|",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 3, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "          |",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 4, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "          |",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 5, column = coluna,sticky = W)
    display_feed = Label(lb_display,text = "------|",bg = "white",fg = "black",width = 5)
    display_feed.grid(row = 6, column = coluna,sticky = W)
    

    tempo = float(tempo_graf.get())
    if input == 1:
        A_deg = float(amp_deg.get())
        G1 = A_deg*Gc*transf
        transf1 = A_deg*transf
        G = co.feedback(G1,1,-1)
        Ga = kain*co.feedback(transf1,1,-1)
        t = np.linspace(0,tempo,1000)
        t1,y1 = co.step_response(G,t)
        t2,y2 = co.step_response(Ga,t)
        t3,y3 = co.step_response(A_deg,t)
        plt.figure(2)
        plt.plot(t1,y1,c = 'blue', lw = 3., label = 'Compensador')
        plt.plot(t2,y2,c = 'orange', lw = 3., label = 'MF sem Controlador')
        plt.plot(t3,y3,c = 'green', lw = 3., label = 'Entrada')
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show()

    if input == 2:   
        num = [1.0]
        den = [1.0, 0]
        ent = co.tf(num,den)
        G2 = ent*transf*Gc
        Gt = co.feedback(G2,1,-1)
        Ga = co.feedback(transf,1,-1)
        t = np.linspace(0,tempo,1000)
        t1,y1 = co.step_response(Gt,t)
        t2,y2 = co.step_response(Ga,t)
        plt.figure(2)
        plt.plot(t1,y1,c = 'blue', lw = 3., label = 'Compensador')
        plt.plot(t2,y2,c = 'green', lw = 3., label = 'MF sem Controlador')
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show()
    if input == 3:
        w = float(freq_sen.get())
        w2 = w*w
        Ga = co.feedback(transf,1,-1)
        t = np.linspace(0,tempo,1000)
        num = [w]
        den = [1.0, 0, w2]
        ent2 = co.tf(num,den)
        print(ent2)
        n2 = [1.0, 0]
        d2 = [1.0]
        ent3 = co.tf(n2,d2)
        G2 = ent2*ent3*transf
        Ga = co.feedback(G2,1,-1)
        Gt = ent2*ent3*Gc*transf
        t1,y1 = co.step_response(Gt,t)
        t2,y2 = co.step_response(Ga,t)
        plt.figure(2)
        plt.plot(t1,y1,c = 'blue', lw = 3., label = 'Compensador')
        plt.plot(t2,y2,c = 'green', lw = 3., label = 'MF sem Controlador')
        plt.grid(True)
        plt.xlabel("tempo")
        plt.ylabel("amplitude")
        plt.legend()
        plt.show()


#################################################################################
#frame
lb_funTransf = LabelFrame(root,text = "Coeficientes do Sistema Dinâmico",borderwidth = 1,relief = "solid")
lb_funTransf.place(x = 0,y = 0,width = 300,height = 125)

#lb_funTransf_racional = LabelFrame(root,text = "Coeficientes da TF Racional",borderwidth = 1,relief = "solid")
#lb_funTransf_racional.place(x = 310,y = 0,width = 300,height = 100)

lb_entrada = LabelFrame(root,text = "Entrada",borderwidth = 1,relief = "solid")
lb_entrada.place(x = 312,y = 0,width = 300 ,height = 125)

lb_transf = LabelFrame(root,text = "Painel Polinomial",borderwidth = 1,relief = "solid")
lb_transf.place(x = 0,y = 127,width = 300,height = 150)

lb_transf_rac = LabelFrame(root,text = "Painel Racional",borderwidth = 1,relief = "solid")
lb_transf_rac.place(x = 312,y = 127 ,width = 300,height = 150)

lb_control = LabelFrame(root,text = "Controladores",borderwidth = 1,relief = "solid")
lb_control.place(x = 0,y = 295,width = 270,height = 70)

#lb_atraso = LabelFrame(lb_control,text = "Atraso de fase",borderwidth = 1,relief = "solid")
#lb_atraso.place(x = 0,y = 0,width = 300,height = 200)

lb_display = LabelFrame(root,text = "Display",borderwidth = 1,relief = "solid")
lb_display.place(x = 0,y = 390,width = 612,height = 200)

#definir
numerador = Entry(lb_funTransf,width = 20)
denominador = Entry(lb_funTransf,width = 20)
gain = Entry(lb_funTransf,width = 20)
#numerador_rac = Entry(lb_funTransf_racional,width = 20)
#denominador_rac = Entry(lb_funTransf_racional,width = 20)
amp_deg = Entry(lb_entrada,width = 4)
freq_sen = Entry(lb_entrada,width = 4)
tempo_graf = Entry(lb_entrada,width = 2)
#atraso_f = Entry(lb_atraso,width = 3)
#atraso_pz = Entry(lb_atraso,width = 10)
#atraso_pq = Entry(lb_atraso,width = 10)
#atraso_pkc = Entry(lb_atraso,width = 10)
#pid_kp = Entry(lb_pid,width=10)
#pid_ki = Entry(lb_pid,width=10)
#pid_kd = Entry(lb_pid,width=10)
#labels
lb_transfi = Label(lb_transf,bg = "white",fg = "black",width = 35)
lb_transfi.grid(row = 1, column = 1,sticky = W)
lb_transfi1 = Label(lb_transf,bg = "white",fg = "black",width = 35)
lb_transfi1.grid(row = 3, column = 1,sticky = W)
lb_transfi2 = Label(lb_transf,bg = "white",fg = "black",width = 35)
lb_transfi2.grid(row = 2, column = 1,sticky = W)

lb_transfi_rac = Label(lb_transf_rac,bg = "white",fg = "black",width = 35)
lb_transfi_rac.grid(row = 1, column = 1,sticky = W)
lb_transfi1_rac = Label(lb_transf_rac,bg = "white",fg = "black",width = 35)
lb_transfi1_rac.grid(row = 3, column = 1,sticky = W)
lb_transfi2_rac = Label(lb_transf_rac,bg = "white",fg = "black",width = 35)
lb_transfi2_rac.grid(row = 2, column = 1,sticky = W)



mostrar2 = Label(lb_funTransf,text = 'Numerador')
mostrar3 = Label(lb_funTransf,text = 'Denominador')
mostrar4 = Label(lb_funTransf,text = 'Ganho').grid(row = 1,column = 0)
#mostrar4 = Label(lb_funTransf_racional,text = 'Numerador')
#mostrar5 = Label(lb_funTransf_racional,text = 'Denominador')
mostrar_amp_deg = Label(lb_entrada,text = 'Amplitude:')
mostrar_freq_sen = Label(lb_entrada,text = 'Frequência').grid(row = 3,column = 6)
mostrar_tempo = Label(lb_entrada,text = 'Fundo de escala(s):')
mostrar_zero = Label(lb_transf,text ='zero(s):')
mostrar_polo = Label(lb_transf,text ='polo(s):')
mostrar_zero_rac = Label(lb_transf_rac,text ='zero(s):')
mostrar_polo_rac = Label(lb_transf_rac,text ='polo(s):')
#mostrar_erro_af = Label(lb_atraso,text = 'Parametros do Controlador:').grid(row = 2,column = 1,sticky = W)
#mostrar_pz_af = Label(lb_atraso,text = 'Parametro z:').grid(row = 5,column = 1,sticky = W)
#mostrar_pq_af = Label(lb_atraso,text = 'Parametro p:').grid(row = 6,column = 1,sticky = W)
#mostrar_pq_af = Label(lb_atraso,text = 'Parametro Kc:').grid(row = 7,column = 1,sticky = W)
#mostrar_pq_af = Label(lb_pid,text = 'Ganho Proporcional(Kp):').grid(row = 1,column = 0,sticky = W)
#mostrar_pq_af = Label(lb_pid,text = 'Ganho Integral(Ki):').grid(row = 2,column = 0,sticky = W)
#mostrar_pq_af = Label(lb_pid,text = 'Ganho Derivativo(Kd):').grid(row = 3,column = 0,sticky = W)
#radiobuttons
a = IntVar()
b = IntVar()
c = IntVar()
#a.set("1")
#Radiobutton(lb_entrada, text = "Degrau",variable = a,value = 1,command = lambda: degrau(calcular())).grid(row = 1,column = 5)
#Radiobutton(lb_entrada, text = "Impulso",variable = a,value = 2,command = lambda: impulso(calcular())).grid(row = 2,column = 5,columnspan = 2)
#Radiobutton(lb_entrada, text = "Feedback",variable = a,value = 3,command = lambda: feedback(calcular())).grid(row = 3,column = 5,columnspan = 2)
Radiobutton(lb_entrada, text = "Degrau",variable = a,value = 1).grid(row = 1,column = 1)
Radiobutton(lb_entrada, text = "Rampa",variable = a,value = 2).grid(row = 2,column = 1,columnspan = 2)
Radiobutton(lb_entrada, text = "Senoide",variable = a,value = 3).grid(row = 3,column = 1,columnspan = 2)
Radiobutton(lb_funTransf, text = "Polinomial",variable = c,value = 1).grid(row = 4,column = 0)
Radiobutton(lb_funTransf, text = "Racional",variable = c,value = 2).grid(row = 4,column = 1)
#Radiobutton(lb_entrada, text = "feedback",variable = a,value = 4).grid(row = 4,column = 1,columnspan = 2)
#Radiobutton(lb_atraso, text = "Parametro do Erro",variable = b,value = 1).grid(row = 1,column = 0,columnspan = 2)
#Radiobutton(lb_atraso, text = "Parametros do Controlador",variable = b,value = 2).grid(row = 4,column = 1,columnspan = 2)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
#ruido = Checkbutton(lb_entrada,text = "ruido",variable = CheckVar1).grid(row = 5,column = 9)
mapa = Checkbutton(lb_transf,text = "Mapa polos e zeros",variable = CheckVar2,command = lambda: mapaZP(calcular(c.get()))).grid(row = 10,column = 1)
mapa_rac = Checkbutton(lb_transf_rac,text = "Mapa polos e zeros",variable = CheckVar3,command = lambda: mapaZP_rac(calcular(c.get()))).grid(row = 10,column = 1)
print(CheckVar1.get())
print(a.get())
#botoes
botao_calcular = Button(lb_funTransf,text = "Executar",padx = 10,pady = 5,command = lambda: calcular(c.get()))
#botao_teste = Button(lb_control,text = "Compensador",padx = 10,pady = 5,command = lambda: tiko(calcular(c.get()),a.get())).grid(row = 5,column = 3,sticky = W)
botao_teste = Button(lb_control,text = "PID",padx = 10,pady = 5,command = lambda: pid_fun(calcular(c.get()),a.get())).grid(row = 4,column = 4,sticky = W)
botao_comparar = Button(lb_control,text = "MF&MA",padx = 10,pady = 5,command = lambda: comparar(calcular(c.get()),a.get())).grid(row = 4,column = 5,sticky = W)
botao_teste = Button(lb_control,text = "Compensador",padx = 10,pady = 5,command = lambda: c_at_av(calcular(c.get()),a.get())).grid(row = 4,column = 3,sticky = W)
#botao_calcular_rac = Button(lb_funTransf_racional,text = "Executar",padx = 80,pady = 5,command = calcular_rac).grid(row = 3,columnspan = 2,sticky = W)
botao_grafico = Button(lb_entrada,text = "Gráfico",padx = 20,pady = 5,command = lambda: grafico(calcular(c.get()),a.get()))
#botao_af = Button(lb_atraso,text = "Calcular",padx = 20,pady = 5,command = lambda: avanco_fase(calcular(),b.get(),a.get())).grid(row = 8,column = 1)#atraso de fase
#botao_pid = Button(lb_pid,text = "Calcular",padx = 20,pady = 5,command = lambda: pid(calcular(),a.get())).grid(row = 4,column = 0)#pid
#posicao
mostrar2.grid(row = 2, column = 0,sticky = W)
mostrar3.grid(row = 3, column = 0,sticky = W)
#mostrar4.grid(row = 1, column = 0,sticky = W)
#mostrar5.grid(row = 2, column = 0,sticky = W)
mostrar_amp_deg.grid(row = 1,column = 6)
mostrar_tempo.grid(row = 5,column = 6)
mostrar_zero.grid(row = 7,column = 0)
mostrar_polo.grid(row = 9,column = 0)
mostrar_zero_rac.grid(row = 7,column = 0)
mostrar_polo_rac.grid(row = 9,column = 0)
numerador.grid(row = 2, column = 1)
denominador.grid(row = 3, column = 1)
gain.grid(row = 1, column = 1)
#numerador_rac.grid(row = 1, column = 1)
#denominador_rac.grid(row = 2, column = 1)
amp_deg.grid(row = 1,column = 7)
tempo_graf.grid(row = 5, column = 7)
freq_sen.grid(row = 3,column = 7)
botao_calcular.grid(row = 4,column = 2,sticky = W)
botao_grafico.grid(row = 5,column = 1)
#atraso_f.grid(row = 2,column = 2)
#atraso_pz.grid(row = 5,column = 2)
#atraso_pq.grid(row = 6,column = 2)
#atraso_pkc.grid(row = 7,column = 2)
#pid_kp.grid(row = 1,column = 1)
#pid_ki.grid(row = 2,column = 1)
#pid_kd.grid(row = 3,column = 1)
root.mainloop()
