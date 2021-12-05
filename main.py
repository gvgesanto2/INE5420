from tkinter import *
from tkinter import ttk

###CORES###
CorJanela = "#D3D3D3"
Preto = "#000"
Branco = "#fff"
Verde = "#00FF00"
Azul = "#0000FF"
Vermelho = "#FF0000"
Amarelo = "#FFFF00"
ListCores = ["Preto","Verde","Azul","Vermelho","Amarelo"]
#############



class objeto:
    def __init__(self, x, y,tam,cor):
        self.x = x
        self.y = y
        self.tam = tam
        self.cor = cor




class ponto(objeto):
    def __init__(self, x, y,tam,cor):
        super().__init__( x,y,tam,cor)
    def desenha(self):
        cv.create_oval(self.x, self.y, self.x+self.tam, self.y+self.tam, fill=self.cor)


class quadrado(objeto):
    def __init__(self, x, y, tam,cor):
        super().__init__( x,y,tam,cor)
    def desenha(self):
        cv.create_line(self.x,self.y,self.x+self.tam,self.y,fill=self.cor)
        cv.create_line(self.x+self.tam,self.y,self.x+self.tam,self.y+self.tam,fill=self.cor)
        cv.create_line(self.x+self.tam,self.y+self.tam, self.x, self.y + self.tam,fill=self.cor)
        cv.create_line(self.x, self.y, self.x, self.y+self.tam,fill=self.cor)

class linha(objeto):
    def __init__(self, x, y, tam,cor):
        super().__init__( x,y,tam,cor)
    def desenha(self):
        cv.create_line(self.x, self.y, self.x + self.tam,self.y,fill=self.cor)

class viewport:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.zoom=1

    def zoomout(self):
        if self.zoom>0.1:
            self.zoom-=0.1
            self.draw()


    def zoomin(self):
        if self.zoom<2:
            self.zoom+=0.1
            self.draw()

    def dir(self):
        if self.x<=8980:
            self.x+=20
            self.draw()

    def esq(self):
        if self.x>=20:
            self.x-=20
            self.draw()

    def baixo(self):
        if self.y<=4480:
            self.y += 20
            self.draw()

    def cima(self):
        if self.y>=20:
            self.y-=20
            self.draw()

    def draw(self):
        cv.delete("all")
        for i in range(len(ListTipo)):
            tipo = ListTipo[i]
            x = Listx[i]
            y=Listy[i]
            tam = ListTam[i]
            cor = Listcor[i]
            x -= self.x
            y -= self.y
            x *= self.zoom
            y *= self.zoom
            tam*=self.zoom
            obj = tipo(x,y,tam,cor)
            obj.desenha()


def CriarPolig(tipo,x,y,tam,cor):
    ListTipo.append(tipo)
    Listx.append(x)
    Listy.append(y)
    ListTam.append(tam)
    Listcor.append(cor)

def transf():
    Janelaaux=Tk()
    Objeto = lb_Objetos.get(ACTIVE)-1

    Janelaaux.title("Transformações")
    Janelaaux.geometry("800x600")
    Janelaaux.configure(background=CorJanela)

    def apply():
        Listx[Objeto] = int(Entryx.get())
        Listy[Objeto] = int(Entryy.get())
        ListTam[Objeto] = int(Entrytam.get())
        corstr = CBcor.get()
        cor=""
        if corstr=="Amarelo":
            cor=Amarelo
        elif corstr=="Vermelho":
            cor=Vermelho
        elif corstr=="Azul":
            cor=Azul
        elif corstr=="Verde":
            cor=Verde
        else:
            cor=Preto

        Listcor[Objeto] = cor
        vp.draw()



    Labeltipo = Label(Janelaaux,text="Tipo").place(x=0,y=0,width=90,height=25)
    Texttipo = Text(Janelaaux)
    Texttipo.insert(END,ListTipo[Objeto])
    Texttipo.place(x=100,y=0,width=250,height=25)

    Labelx = Label(Janelaaux, text="Coordenada x").place(x=0, y=25, width=90,height=25)

    Entryx = Entry(Janelaaux)
    Entryx.insert(END, Listx[Objeto])
    Entryx.place(x=100, y=25, width=250, height=25)

    Labely = Label(Janelaaux, text="Coordenada y").place(x=0, y=50, width=90,height=25)
    Entryy = Entry(Janelaaux)
    Entryy.insert(END, Listy[Objeto])
    Entryy.place(x=100, y=50, width=250, height=25)

    Labeltam = Label(Janelaaux, text="Tamanho").place(x=0, y=75, width=90,height=25)
    Entrytam = Entry(Janelaaux)
    Entrytam.insert(END, ListTam[Objeto])
    Entrytam.place(x=100, y=75, width=250, height=25)

    labelcor = Label(Janelaaux, text="Cor").place(x=0, y=100, width=90,height=25)
    CBcor = ttk.Combobox(Janelaaux,values = ListCores)
    CBcor.set("Esccolha uma cor")
    CBcor.place(x=100, y=100, width=250, height=25)


    btnapply = Button(Janelaaux,text="aplicar",command=apply).place(x=600,y=500)
    Janelaaux.mainloop()




ListTipo = []
Listx = []
Listy = []
ListTam = []
Listcor = []

CriarPolig(quadrado,5000,2570,50,Azul)
CriarPolig(ponto,5900,2510,5,Amarelo)
CriarPolig(linha,5300,2820,150,Preto)
CriarPolig(quadrado,5100,2890,100,Vermelho)
CriarPolig(linha,5400,2800,300,Vermelho)
CriarPolig(quadrado,5500,2700,200,Preto)
CriarPolig(ponto,5300,2700,20,Preto)




Janela = Tk()



Janela.title("Tarefa1")
Janela.geometry("1500x750")
Janela.configure(background=CorJanela)

label1 = Label(Janela,text = "Menu de Funções", background = CorJanela).place(x=0,y=10,width=150,height=30)
label2 = Label(Janela,text = "Objetos",background = CorJanela).place(x=0,y=40,width=150,height=30)
label3 = Label(Janela,text = "Viewport", background = CorJanela).place(x=200,y=10,width=150,height=30)



#nobj = 0
lb_Objetos = Listbox(Janela)
for i in range(1,len(ListTipo)):
    lb_Objetos.insert(END,i)
#for Objetos in Listnome:
#    lb_Objetos.insert(END,Objetos)
lb_Objetos.place(x=10,y=70,width=150,height= 200)

cv=Canvas(Janela,width=1000,height=500,bg=Branco)
cv.place(x=250,y=70)

vp = viewport(5000,2500)
vp.draw()

##BOTOES##
tamBot = 30
btnTransf = Button(Janela,text="Transformações",command=transf).place(x=10,y=280,heigh=tamBot,width=4*tamBot)
btnDir = Button(Janela,text="ᐅ",command = vp.dir).place(x=70,y=400,height=tamBot,width=tamBot)
btnEsq = Button(Janela,text="ᐊ",command = vp.esq).place(x=10,y=400,height=tamBot,width=tamBot)
btnBaixo = Button(Janela,text="ᐁ",command = vp.baixo).place(x=40,y=400,height=tamBot,width=tamBot)
btnCima = Button(Janela,text="ᐃ",command = vp.cima).place(x=40,y=370,height=tamBot,width=tamBot)
btnCima = Button(Janela,text="+",command = vp.zoomin).place(x=10,y=370,height=tamBot,width=tamBot)
btnCima = Button(Janela,text="-",command = vp.zoomout).place(x=70,y=370,height=tamBot,width=tamBot)
#####

Janela.mainloop()