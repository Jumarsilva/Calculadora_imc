from tkinter import *

class Aplication:
    def __init__(self):
        self.root = root
        self.cor_base = '#ffffff'
        self.cor_bg = '#8892B3'
        self.cor_1 = "#000000"
        self.e_peso = float(0)
        self.e_altura = 0
        self.imc = 0
        self.l_resultado_texto = 0   
        self.tela()
        self.frames_da_tela()
        self.widget()
        root.mainloop()
    
    def tela(self):
        self.root.title('Calculadora de IMC')
        #isso serve para colocar um fundo de tela
        self.root.configure(background=self.cor_base)
        self.root.geometry('295x230')
        #isso serve para deixar a tela responsiva e fixar um tamanho maximo.
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=900)
        #self.root.minsize(width=200, height=200)
        

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, width=295, height=50, bg=self.cor_base, pady=0, padx=0, relief='flat')
        self.frame_1.grid(row=0, column=0, sticky=NSEW)
        
        self.frame_2 = Frame(self.root, width=295, height=180, bg=self.cor_base, pady=0, padx=0, relief='flat')
        self.frame_2.grid(row=1, column=0, sticky=NSEW)
        #estudar depois sobre o place
        #self.frame_1.place(relx='0.1', rely='0.1', relwidth='0.8', relheight='0.5')
        #self.frame_2 = Frame(self.root)
        #self.frame_2.place(relx='0.1', rely='0.7', relwidth='0.8', relheight='0.3')
    
    def widget(self):
        #configurando o frame cima
        app_name = Label(self.frame_1, text=" Calculadora de IMC", width=23, height=1, padx=0, relief="flat", anchor="center", font=('Ivy 16 bold'), bg=self.cor_base, fg=self.cor_1)

        app_name.place(x=0, y=0)

        app_linha = Label(self.frame_1, text="", width=400, height=1, padx=0, relief="flat", anchor="center", font=('Ivy 1  '), bg=self.cor_bg, fg=self.cor_1)

        app_linha.place(x=0, y=35)


        #configurando o frame baixo

        #info do peso
        l_peso = Label(self.frame_2, text="Insira um peso", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=self.cor_base, fg=self.cor_1)
        l_peso.grid(row=0, column=0, sticky=NSEW, padx=3, pady=10)
        self.e_peso = Entry(self.frame_2, width=5, relief="solid", font=('Ivy 10 bold'), justify='center')
        self.e_peso.grid(row=0, column=1, sticky=NSEW, padx=3, pady=10)


        #info da altura
        l_altura = Label(self.frame_2, text="Insira sua altura:", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=self.cor_base, fg=self.cor_1)
        l_altura.grid(row=1, column=0, sticky=NSEW, padx=3, pady=10)
        self.e_altura = Entry(self.frame_2, width=5, relief="solid", font=('Ivy 10 bold'), justify='center')
        self.e_altura.grid(row=1, column=1, sticky=NSEW, padx=3, pady=10)

        #resultado
        self.l_resultado = Label(self.frame_2, text="---", width=5, height=1, padx=6, pady=12, relief="flat", anchor="center", font=('Ivy 24 bold'), bg=self.cor_bg, fg=self.cor_base)
        self.l_resultado.place(x=175, y=10)

        self.l_resultado_texto = Label(self.frame_2, text="O seu IMC é ---", width=37, height=1, pady=0, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=self.cor_base)
        self.l_resultado_texto.place(x=0, y=100)

        #configurando o botão

        b_calcular = Button(self.frame_2, text="Calcular", width=34, height=1, overrelief=SOLID, relief="raised", anchor="center", font=('Ivy 10 bold'), bg=self.cor_bg, fg=self.cor_base, command=self.calcular)
        b_calcular.grid(row=4, column=0, sticky=NSEW, padx=5, pady=60, columnspan=40)


    def avaliacao(self,imc):
        if imc < 18.5:
            resultado = f'Voce está abaixo do peso'
        elif imc >= 18.5 and imc <24.9:
            resultado = f'Voce está com o peso normal'
        elif imc >= 25 and imc <29.9:
            resultado = f'Voce está com sobrepeso'
        elif imc >= 30 and imc <34.9:
            resultado = f'Voce está com o Obesidade Grau I'
        elif imc >= 35 and imc <39.9:
            resultado = f'Voce está com o Obesidade Grau II'
        else:
            resultado = f'Voce está com Obesidade Grau III ou Mórbida'
        return resultado

    def calcular(self):
        self.peso = float(self.e_peso.get())
        self.altura = float(self.e_altura.get())
        self.imc = (self.peso/((self.altura*self.altura)))
        dados = self.avaliacao(self.imc)
        self.l_resultado_texto['text'] = dados
        self.l_resultado['text'] = f'{self.imc:.2f}'
        
              
        

root = Tk()
Aplication()