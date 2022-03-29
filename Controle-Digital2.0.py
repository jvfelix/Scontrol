from scipy import signal
import math
import random
import numpy as np
import control as co
from control import *
from control.matlab import *
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg
from numpy.polynomial import polynomial as P
import warnings
warnings.filterwarnings("ignore")
root = Tk()
root.title('Control 1.0')
root.geometry("850x400")


def polinomial (c):
    if c==1:
        stringy_ganp = ganho_planta.get()
        stringy_nump = numerador_planta.get()
        stringy_denp = denominador_planta.get()

        stringy_ganc = ganho_controlador.get()
        stringy_numc = numerador_controlador.get()
        stringy_denc = denominador_controlador.get()

        stringy_perio = periodo.get()
        #convertendo numerador
        conv_nump = stringy_nump.split()
        nump = []
        conv_numc = stringy_numc.split()
        numc = []
        for casa in conv_nump:
            nump.append(float(casa))

        for casa in conv_numc:
            numc.append(float(casa))
            
        #convertendo denominador
        conv_denp = stringy_denp.split()
        denp = []
        for casa in conv_denp:
            denp.append(float(casa))

        conv_denc = stringy_denc.split()
        denc = []
        for casa in conv_denc:
            denc.append(float(casa))
        #convertendo ganho
        conv_ganp = stringy_ganp.split()
        ganp = []
        for casa in conv_ganp:
            ganp.append(float(casa))

        conv_ganc = stringy_ganc.split()
        ganc = []
        for casa in conv_ganc:
            ganc.append(float(casa))

        if len(numc)==0:
            numc=[1]
        if len(denc)==0:
            denc=[1]
        if len(ganc)==0:
            ganc=[1]
        if len(ganp)==0:
            ganp=[1]

        if len(nump) > len(denp):
            msg.showwarning("Control Error","O numerador não pode ter mais coeficientes que o denominador")
            return 0
        if len(numc) > len(denc):
            msg.showwarning("Control Error","O numerador não pode ter mais coeficientes que o denominador")
            return 0
        
        dt=float(stringy_perio)
        
        B = signal.dlti(signal.convolve(nump,ganp),denp,dt=float(stringy_perio))

        #C = signal.cont2discrete(B,dt,"zoh")
       
      
        D = signal.dlti(signal.convolve(numc,ganc),denc,dt=float(stringy_perio))
      
        
        G = signal.dlti(signal.convolve(B.num,D.num),signal.convolve(B.den,D.den),dt=float(stringy_perio))
                                                                                                                                                        
       
    if c==2:
        stringy_ganp = ganho_planta.get()
        stringy_nump = numerador_planta.get()
        stringy_denp = denominador_planta.get()

        stringy_ganc = ganho_controlador.get()
        stringy_numc = numerador_controlador.get()
        stringy_denc = denominador_controlador.get()

        stringy_perio = periodo.get()
        #convertendo numerador
        conv_nump = stringy_nump.split()
        nump = []
        conv_numc = stringy_numc.split()
        numc = []
        for casa in conv_nump:
            nump.append(float(casa))

        for casa in conv_numc:
            numc.append(float(casa))
            
        #convertendo denominador
        conv_denp = stringy_denp.split()
        denp = []
        for casa in conv_denp:
            denp.append(float(casa))

        conv_denc = stringy_denc.split()
        denc = []
        for casa in conv_denc:
            denc.append(float(casa))
        #convertendo ganho
        conv_ganp = stringy_ganp.split()
        ganp = []
        for casa in conv_ganp:
            ganp.append(float(casa))

        conv_ganc = stringy_ganc.split()
        ganc = []
        for casa in conv_ganc:
            ganc.append(float(casa))


        
        dt=float(stringy_perio)
        
        if len(numc)==0:
            d_num=[1]
        else:
            d_num=np.poly(numc)
            
        if len(nump)==0:
            b_num=[1]
            
        else:
            b_num=np.poly(nump)
            
            
        if len(denc)==0:
            
            d_den=[1]
        else:
            d_den=np.poly(denc)

        if len(denp)==0:
            b_den=[1]
        else:
            b_den=np.poly(denp)
            
        if len(ganc)==0:
            ganc=[1]

            
        if len(ganp)==0:
            ganp=[1]



        if len(nump) > len(denp):
            msg.showwarning("Control Error","O numerador não pode ter mais coeficientes que o denominador")
            return 0
        if len(numc) > len(denc):
            msg.showwarning("Control Error","O numerador não pode ter mais coeficientes que o denominador")
            return 0

        B = signal.dlti(signal.convolve(b_num,ganp), b_den,dt=float(stringy_perio))
        
        
        D = signal.dlti(signal.convolve(d_num,ganc),d_den,dt=float(stringy_perio))
        

        G = signal.dlti(signal.convolve(B.num,D.num),signal.convolve(B.den,D.den),dt=float(stringy_perio))
        #print(G)


        #texto para o numerador
    x = 1
    key = 0
    texto = ""
    for i in G.num:
      
        if key == 0:
              if len(G.num)-x> 0:
                frase = str(round(i,5)) + " z^" + str((len(G.num)-x)) + " "
              else:
                if i==0:
                    frase = " "
                else:
                    frase= str(round(i,5))
                    
              key = 1
        else:
             if i > 0:
                texto = texto + "+"
             if len(G.num)-x> 0:
                frase = str(round(i,5)) + " z^" + str((len(G.num)-x)) + " "
             else:
                if i==0:
                    frase = " "
                else:
                    frase= str(round(i,5))
        #print(len(nump) - x)
        x = x + 1
        texto = texto + frase 
        #texto para o denominador
    x = 1
    key = 0
    texto2 = ""
    for i in G.den:
        if key == 0:
             if len(G.den)-x> 0:
                frase = str(round(i,5)) + " z^" + str((len(G.den)-x)) + " "
             else:
                if i==0:
                    frase = " "
                else:
                    frase= str(round(i,5))
             key = 1
        else:
            if i > 0:
                texto2 = texto2 + "+"
            if len(G.den)-x> 0:
                frase = str(round(i,5)) + " z^" + str((len(G.den)-x)) + " "
            else:
                if i==0:
                    frase = " "
                else:
                    frase= str(round(i,5))
                
        #print(len(nump) - x)
        x = x + 1
        texto2 = texto2 + frase
    #plotagem da linha
    linha = ""
    for i in texto2:
        linha = "-" + linha
    #plotagem
    #print(len(G.den))
    lb_transfp = Label(lb_transf,text = texto,bg = "white",fg = "black",width = 50)
    lb_transfp.grid(row = 1, column = 1,sticky = W)
    lb_transfp1 = Label(lb_transf,text = texto2,bg = "white",fg = "black",width = 50)
    lb_transfp1.grid(row = 3, column = 1,sticky = W)
    lb_transfp2 = Label(lb_transf,text = linha,bg = "white",fg = "black",width = 50)
    lb_transfp2.grid(row = 2, column = 1,sticky = W)
    #print(texto)

    zeros_num = np.roots(G.num)
    zeros_den = np.roots(G.den)
    
    x = 1
    key = 0
    texto = ""

    if len(zeros_num) > 0:
        
        for i in zeros_num:
            
           
            if key == 0:
                if i<0:
                      frase = str(G.num[0])+ "*(" + " z+" + str(-1*np.round(i,5)) + ")"
                      key = 1
                
                else:
                      frase = str(G.num[0])+"*(" + " z-" + str(np.round(i,5)) + ")"
                      key = 1
                 
            else:
                 if i > 0:
                    texto = texto + ""
                 if len(zeros_num)-x> 0:
                        if i<0:
                          frase = "(" + " z+" + str(-1*np.round(i,5)) + ")"
                        else:
                          frase = "(" + " z-" + str(np.round(i,5)) + ")"
                   
                 else:
                    if i==0:
                        frase = ""
                    else:
                        if i<0:
                          frase = "(" + " z+" + str(-1*np.round(i,5)) + ")"
                        else:
                          frase = "(" + " z-" + str(np.round(i,5)) + ")"
            #print(len(nump) - x)

            texto = texto + frase 
            #texto para o numerador
   
            
    if len(zeros_num) == 0:
            frase = str(G.num[0])
            texto = texto + frase
            
            
        
    key = 0
    texto2 = ""
    for i in zeros_den:
        if key == 0:
            if i<0:
                  frase = "(" + " z+" + str(-1*np.round(i,5)) + ")"
                  key = 1
            else:
                  frase = "(" + " z-" + str(np.round(i,5)) + ")"
                  key = 1
        else:
             if i > 0:
                texto = texto + ""
             if len(zeros_den)-x> 0:
                if i<0:
                   frase = "(" + " z+" + str(-1*np.round(i,5)) + ")"
                else:
                   frase = "(" + " z-" + str(np.round(i,5)) + ")"
                 
             else:
                if i==0:
                    frase = ""
                else:
                    if i<0:
                       frase = "(" + " z+" + str(-1*np.round(i,5)) + ")"
                    else:
                       frase = "(" + " z-" + str(np.round(i,5)) + ")"
                       
        #print(len(nump) - x)
        
        texto2 = texto2 + frase
    #plotagem da linha
    linha = ""
    for i in texto2:
        linha = "-" + linha

    lb_transfr = Label(lb_transf2,text = texto,bg = "white",fg = "black",width = 50)
    lb_transfr.grid(row = 1, column = 1,sticky = W)
    lb_transfr1 = Label(lb_transf2,text = texto2,bg = "white",fg = "black",width = 50)
    lb_transfr1.grid(row = 3, column = 1,sticky = W)
    lb_transfr2 = Label(lb_transf2,text = linha,bg = "white",fg = "black",width = 50)
    lb_transfr2.grid(row = 2, column = 1,sticky = W)



                                                                                                                                                        
    return G 
#####################degrau
def degrau(transf,tempo):
    Amp_deg = float(amplitude.get())  
    time = np.linspace(0,int(np.amax(tempo)*10),int(np.amax(tempo)*10)+1)*transf.dt
    K=Amp_deg*transf
    t1,y1 = co.step_response(K,tempo)
    #print(np.amax(tempo))
  
    t,y = co.step_response(K,time)
    
    n_max = np.amax(y)
    n_pos= np.argmax(y)*transf.dt


    
    
    
    #entrada degrau
    t2,y2 = co.step_response(Amp_deg,tempo)

    #erro de 5%
    t3,y3 = co.step_response(Amp_deg*0.95,tempo)
    t4,y4 = co.step_response(Amp_deg*1.05,tempo)
    
    cont=0
    valor_estaby = 0
    valor_estabx = 0

    for i in range(len(y)):
        
        if abs(y[i]-y[len(y)-1])<=0.05*y[len(y)-1] and cont==0:
            valor_estaby = y[i]
            valor_estabx = t[i]
        
            for j in range(i,len(y)):
                if abs(y[j]-y[len(y)-1])<=0.05*y[len(y)-1]:
                    cont=1
                else:
                    cont=0
                    break

    if n_max <= valor_estaby:
        n_max=0
        n_pos=0

                
    ccor_entrada = random.randrange(0,9)
    ccor_saida = random.randrange(0,9)
    cont=cont+1
    
    #print(valor_estabx.itemsize)
    
    
    string_de_cor = ['#00008B','#8B0000','#008B8B','#006400','#FF7F00','#00FA9A','#CD6889','#9B30FF','#8B5742','#FFC1C1']            
        
        
    plt.figure(1)
       # plt.subplot(2,1,1)

    plt.plot(t2, (y2),'k-o',c = string_de_cor[ccor_entrada],label='Entrada')
    plt.plot(t1, (y1),'k-o',c = string_de_cor[ccor_saida],label='Saída')

    
    plt.plot(t1,y1,c = string_de_cor[ccor_saida])
    
 
    if math.isnan(n_pos)==False and n_pos <= np.amax(tempo):
         plt.text(n_pos+0.1, n_max, "Tpico="+str(n_pos)+" T", fontsize=13, horizontalalignment='left')
         plt.plot(n_pos, n_max,'o',color='black')


    if  math.isnan(valor_estabx)== False and valor_estabx <= np.amax(tempo)  :
         plt.text(valor_estabx+0.1, valor_estaby, "Test="+str(valor_estabx)+" T", fontsize=13, horizontalalignment='left')
         plt.plot(valor_estabx, valor_estaby,'o',color='cyan')
         #plt.step(t3, np.squeeze(y3),'k--',color='black')
         #plt.step(t4, np.squeeze(y4),'k--',color='black')
    plt.grid(True)
    plt.xlabel("T")
    plt.ylabel("amplitude")

    plt.legend(loc='lower right')
    
    plt.show()
    


######################feedback
def feedback(transf,x):

    M= co.tf(transf.num,transf.den,transf.dt)
    stringy_amostras = amostras.get()
    K = co.feedback(M,1,-1)
    n=int(stringy_amostras)
    tempo = np.linspace(0,n-1,n)*transf.dt
    print(K)


    if x==1:
        degrau(K,tempo)
    if x==2:
        impulso(K,tempo)

######################feedback
def sem_feedback(transf,x):
    M= co.tf(transf.num,transf.den,transf.dt)
    stringy_amostras = amostras.get()
    n=int(stringy_amostras)
    tempo = np.linspace(0,n-1,n)*transf.dt
    
    #t1,y1 = co.step_response(K,tempo)
    #n_max = np.amax(y1)
    #n_pos= np.argmax(y1)*K.dt

    if x==1:
        degrau(M,tempo)
    if x==2:
        impulso(M,tempo)
######################Impulso
def impulso(transf,tempo):
    Amp_imp = float(amplitude.get())  
    time = np.linspace(0,int(np.amax(tempo)*10),int(np.amax(tempo)*10)+1)*transf.dt
    K=transf*Amp_imp
    t1,y1 = co.impulse_response(K,tempo)
    t,y =  co.impulse_response(K,time)

        #entrada impulse
    t2,y2 = co.impulse_response(Amp_imp,tempo)
    
    n_max = float(np.amax(y))
    n_pos= float(np.argmax(y)*transf.dt)

    if n_max <= 0:
        n_max=0
        n_pos=0
        
    cont=0
    valor_estaby = 0
    valor_estabx = 0

    for i in range(len(y)):
        
        if abs(y[i]-y[len(y)-1])<=0.05*y[len(y)-1] and cont==0:
            valor_estaby = float(y[i])
            valor_estabx = float(t[i])
            
            for j in range(i,len(y)):
                if abs(y[j]-y[len(y)-1])<=0.05*y[len(y)-1]:
                    cont=1
                else:
                    cont=0
                    break
    plt.figure(1)
       # plt.subplot(2,1,1)
    

    #if n_max!=0 and n_pos!=0:
    #     plt.text(n_pos+0.1, n_max, "Tpico="+str(n_pos)+" T", fontsize=13, horizontalalignment='left')
    #     plt.plot(n_pos, n_max,'o',color='black')

    #if valor_estabx !=0 and valor_estaby !=0 :
     #    plt.text(valor_estabx+0.1, valor_estaby, "Test="+str(valor_estabx)+" T", fontsize=13, horizontalalignment='left')
     #    plt.plot(valor_estabx, valor_estaby,'o',color='black')
     #    plt.step(t3, np.squeeze(y3),'k--',color='black')
     #    plt.step(t4, np.squeeze(y4),'k--',color='black')


    ccor_entrada = random.randrange(0,9)
    ccor_saida = random.randrange(0,9)
    cont=cont+1
    string_de_cor = ['#00008B','#8B0000','#008B8B','#006400','#FF7F00','#00FA9A','#CD6889','#9B30FF','#8B5742','#FFC1C1']            
        
        
    plt.figure(1)
       # plt.subplot(2,1,1)

    plt.plot(t2, (y2),'k-o',c = string_de_cor[ccor_entrada],label='Entrada')
    plt.plot(t1, (y1),'k-o',c = string_de_cor[ccor_saida],label='Saída')

    
    plt.plot(t1,y1,c = string_de_cor[ccor_saida])
    
 
         #plt.step(t3, np.squeeze(y3),'k--',color='black')
         #plt.step(t4, np.squeeze(y4),'k--',color='black')
    plt.grid(True)
    plt.xlabel("T")
    plt.ylabel("amplitude")

    plt.legend(loc='lower right')
    
    plt.show()
    


####################################################################################
################### frame ##################
lb_funTransf_c = LabelFrame(root,text = "Coeficientes do Controlador",borderwidth = 1,relief = "solid")
lb_funTransf_c.place(x = 0,y = 0,width = 420,height = 150)

lb_funTransf = LabelFrame(root,text = "Coeficientes do Sistema Dinâmico",borderwidth = 1,relief = "solid")
lb_funTransf.place(x = 421,y = 0,width = 420,height = 150)

lb_sistema = LabelFrame(root,text = "Sistema",borderwidth = 1,relief = "solid")
lb_sistema.place(x = 553,y = 151,width = 275,height = 100)

lb_sistema_g = LabelFrame(root,text = "Dados Gerais do Sistema",borderwidth = 1,relief = "solid")
lb_sistema_g.place(x =0,y = 151,width = 275,height = 100)

lb_entrada = LabelFrame(root,text = "Entrada",borderwidth = 1,relief = "solid")
lb_entrada.place(x = 277,y = 151,width = 275,height = 100)

lb_transf = LabelFrame(root,text = "Função de Transferência (Polinomial)",borderwidth = 1,relief = "solid")
lb_transf.place(x = 0,y = 251,width = 425,height = 100)

lb_transf2 = LabelFrame(root,text = "Função de Transferência (Racional)",borderwidth = 1,relief = "solid")
lb_transf2.place(x = 425,y = 251,width = 424,height = 100)

################### definir ##################

ganho_controlador = Entry(lb_funTransf_c,width = 20)
numerador_controlador = Entry(lb_funTransf_c,width = 20)
denominador_controlador = Entry(lb_funTransf_c,width = 20)

ganho_planta = Entry(lb_funTransf,width = 20)
numerador_planta = Entry(lb_funTransf,width = 20)
denominador_planta = Entry(lb_funTransf,width = 20)



periodo = Entry(lb_sistema_g,width = 5)
amostras = Entry(lb_sistema_g,width = 5)

amplitude = Entry(lb_entrada,width = 5)

################## labels ######################
mostrar0 = Label(lb_funTransf_c,text = 'Ganho')
mostrar1 = Label(lb_funTransf_c,text = 'Numerador')
mostrar2 = Label(lb_funTransf_c,text = 'Denominador')
mostrar3 = Label(lb_funTransf,text = 'Ganho')
mostrar4 = Label(lb_funTransf,text = 'Numerador')
mostrar5 = Label(lb_funTransf,text = 'Denominador')

# Características do Projeto
mostrar6 = Label(lb_sistema_g,text = 'Período de amostragem')
mostrar7 = Label(lb_sistema_g,text = 'Número total de amostras')

mostrar8= Label(lb_entrada,text = 'Amplitude')
####################################################



################## radiobuttons ######################

c= IntVar()
c.set("0")
Radiobutton(lb_funTransf_c, text = "Polinomial",variable = c,value = 1).grid(row = 3,column = 0)
Radiobutton(lb_funTransf_c, text = "Racional",variable = c,value = 2).grid(row = 3,column = 1,columnspan = 2)


b = IntVar()
b.set("0")

Radiobutton(lb_entrada, text = "Degrau",variable = b,value = 1).grid(row = 1,column = 7)
Radiobutton(lb_entrada, text = "Impulso",variable = b,value = 2).grid(row = 2,column = 7,columnspan = 2)

a = IntVar()
a.set("0")
Radiobutton(lb_sistema, text = "Feedback",variable = a,value = 1,command = lambda: feedback(polinomial(c.get()),b.get())).grid(row = 1,column = 5)
Radiobutton(lb_sistema, text = "Sem Feedback",variable = a,value = 2,command = lambda: sem_feedback(polinomial(c.get()),b.get())).grid(row = 2,column = 5,columnspan = 2)


################## botões ##################
botao_calcular = Button(lb_sistema_g,text = "Executar",padx = 60,pady = 4,command = lambda: polinomial(c.get()))
botao_calcular.grid(row = 4, column = 0,sticky = W)

################## posicao ##################


mostrar6.grid(row = 1, column = 0,sticky = W)
mostrar7.grid(row = 2, column = 0,sticky = W)
periodo.grid(row = 1, column = 1)
amostras.grid(row = 2, column = 1)

mostrar8.grid(row = 1, column = 0,sticky = W)
amplitude.grid(row = 1,column=1)

botao_calcular.grid(columnspan = 2,sticky = W)

mostrar0.grid(row = 0, column = 0,sticky = W)
mostrar1.grid(row = 1, column = 0,sticky = W)
mostrar2.grid(row = 2, column = 0,sticky = W)

ganho_controlador.grid(row = 0, column = 1)
numerador_controlador.grid(row = 1, column = 1)
denominador_controlador.grid(row = 2, column = 1)

mostrar3.grid(row = 0, column = 0,sticky = W)
mostrar4.grid(row = 1, column = 0,sticky = W)
mostrar5.grid(row = 2, column = 0,sticky = W)

ganho_planta.grid(row = 0, column = 1)
numerador_planta.grid(row = 1, column = 1)
denominador_planta.grid(row = 2, column = 1)

root.mainloop()
