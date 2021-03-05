from tkinter import*
import webbrowser

class Blockbuster:
    def __init__(self, master = None):
        self.widget =  Frame(master)
        self.widget.pack()

        self.title = Label(self.widget, text = "BLOCKBUSTER")
        self.title["font"] = ("Impact", "24")
        self.title["fg"] = ("#000046")
        self.title["highlightthickness"] = ("20")
        self.title["justify"]= ("center")
        self.title.pack()
        
        self.filmC = Frame(master)
        self.filmC["pady"] = 10
        self.filmC["padx"] = 10
        self.filmC.pack()

        self.filmLabel = Label(self.filmC, text="Seu Filme: ")
        self.filmLabel["font"] = ("Calibri", "16")
        self.filmLabel["fg"] = ("#000046")
        self.filmLabel.pack()

        self.film = Entry(self.filmC)
        self.film["width"] = 50
        self.film["font"] = ("Verdana", "10")
        self.film["fg"] = ("#000046")
        self.film["justify"] = "center"
        self.film.pack()

        self.searchC = Frame(master)
        self.searchC["pady"] = 5
        self.searchC.pack()

        self.search = Button(self.searchC)
        self.search["text"] = "Buscar"
        self.search["font"] = ("Verdana", "10", "bold")
        self.search["fg"] = ("#FFFFFF")
        self.search["cursor"] = ("hand2")
        self.search["bg"] = ("#000046")
        self.search["bd"] = 10
        self.search["overrelief"] = "sunken"
        self.search["highlightcolor"] = ("#FFFFFF")
        self.search["width"] = 20
        self.search["compound"] = (LEFT)
        self.search["command"] = self.checkFilm
        self.search.pack()

        self.menseger = Label(self.searchC, text="", font = "Arial")
        self.menseger.pack()

        self.exit = Frame(master)
        self.exit["pady"] = 2
        self.exit.pack()

        self.filmOnTC = Frame(master)
        self.filmOnTC["pady"] = 5
        self.filmOnTC.pack()

        self.filmOnTLabel = Label(self.filmOnTC, text = "Filmes Disponíveis:")
        self.filmOnTLabel["font"] = ("Verdana", "14", "bold")
        self.filmOnTLabel["fg"] = ("#000046")
        self.filmOnTLabel["justify"] = "center"
        self.filmOnTLabel.pack()

        self.filmOnC = Frame(master)
        self.filmOnC["pady"] = 5
        self.filmOnC.pack()

        self.filmOnLabel = Label(self.filmOnC, text = "A Cabana \nDeadpool \nSpirit - O Corcel Indomável \nProjeto Gemini \n\n")
        self.filmOnLabel["font"] = ("Verdana", "12")
        self.filmOnLabel["fg"] = ("#000046")
        self.filmOnLabel["justify"] = "center"
        self.filmOnLabel.pack()

        self.filmNot = Label(self.filmOnC, text = "Mais títulos em breve...")
        self.filmNot["font"] = ("Verdana", "8", "bold", "italic")
        self.filmNot["fg"] = ("#000046")
        self.filmNot["justify"] = "center"
        self.filmNot.pack()

    def checkFilm(self):
        check = self.film.get()
        # check = check.lower()
        if check in ["A Cabana", "Cabana", "A cabana", "a cabana", "cabana", "A CABANA", "CABANA"]:
            self.filmOnLabel["text"] = ""
            self.filmOnTLabel["text"] = ""
            self.filmNot["text"] = ""
            self.image = PhotoImage(file = "img/Cabana.png")
            self.newWindow = Label(root, image = self.image)
            self.newWindow.pack()

            self.text = Label(self.filmOnTC, text = "A Cabana", font = ("Tahoma", "18", "bold"))
            self.text1 = Label(self.filmOnC, text = "Ano: 2017 \nDuração: 2h 13min \nGênero: Drama \nDireção: Stuart Hazeldine", font = ("Calibri", "14"))
            self.text["width"] = 100
            self.text.pack(side = BOTTOM)
            self.text1["width"] = 100
            self.text1.pack(side = BOTTOM)

            self.filmOnLabel["height"] = 0

            self.search["text"] = "Alugar no Telecine Play"
            self.search["width"] = 30
            self.search["command"] = lambda: webbrowser.open("https://www.telecineplay.com.br/")

            self.search = Button(self.exit)
            self.search["text"] = "Sair"
            self.search["font"] = ("Verdana", 8, "bold", "italic")
            self.search["fg"] = ("#FFFFFF")
            self.search["cursor"] = ("hand2")
            self.search["bg"] = ("#000046")
            self.search["width"] = 10
            self.search["command"] = quit
            self.search.pack()

        elif check in ["Deadpool", "deadpool", "DEADPOOL"]:
            self.filmOnLabel["text"] = ""
            self.filmOnTLabel["text"] = ""
            self.filmNot["text"] = ""
            self.image = PhotoImage(file = "img/Deadpool.png")
            self.newWindow = Label(root, image = self.image)
            self.newWindow.image = self.image
            self.newWindow.pack()

            self.text = Label(self.filmOnTC, text = "Deadpool", font = ("Tahoma", "20", "bold"))
            self.text1 = Label(self.filmOnC, text = "Ano: 2016 \nDuração: 1h 48min \nGênero: Ação/Comédia\nDireção: Tim Miller", font = ("Calibri", "14"))
            self.text["width"] = 100
            self.text.pack(side = BOTTOM)
            self.text1["width"] = 100
            self.text1.pack(side = BOTTOM)
            
            self.filmOnLabel["height"] = 0
        
            self.search["text"] = "Alugar"
            self.search["width"] = 30
            self.search["command"] = lambda: webbrowser.open("https://www.telecineplay.com.br/")

            self.search = Button(self.exit)
            self.search["text"] = "Sair"
            self.search["font"] = ("Verdana", "8", "bold", "italic")
            self.search["fg"] = ("#FFFFFF")
            self.search["cursor"] = ("hand2")
            self.search["bg"] = ("#000046")
            self.search["width"] = 10
            self.search["command"] = quit
            self.search.pack()

        elif check in ["Spirit", "spirit", "SPIRIT"]:
            self.filmOnLabel["text"] = ""
            self.filmOnTLabel["text"] = ""
            self.filmNot["text"] = ""
            self.image = PhotoImage(file = "img/Spirit.png")
            self.newWindow = Label(root, image = self.image)
            self.newWindow.image = self.image
            self.newWindow.pack()

            self.text = Label(self.filmOnTC, text = "Spirit - O Corcel Indomável", font = ("Tahoma", "20", "bold"))
            self.text1 = Label(self.filmOnC, text = "Ano: 2002 \nDuração: 1h 23min \nGênero: Animação/Aventura\nDireção: Kelly Asbury, Lorna Cook", font = ("Calibri", "14"))
            self.text["width"] = 100
            self.text.pack(side = BOTTOM)
            self.text1["width"] = 100
            self.text1.pack(side = BOTTOM)
            

            self.filmOnLabel["height"] = 0
        
            self.search["text"] = "Alugar no Looke"
            self.search["width"] = 20
            self.search["command"] = lambda: webbrowser.open("https://www.looke.com.br/")

            self.search = Button(self.exit)
            self.search["text"] = "Sair"
            self.search["font"] = ("Verdana", "8", "bold", "italic")
            self.search["fg"] = ("#FFFFFF")
            self.search["cursor"] = ("hand2")
            self.search["bg"] = ("#000046")
            self.search["width"] = 10
            self.search["command"] = quit
            self.search.pack()

        elif check in ["Projeto Gemini", "Projeto gemini", "projeto Gemini", "projeto gemini", "PROJETO GEMINI"]:
            self.filmOnLabel["text"] = ""
            self.filmOnTLabel["text"] = ""
            self.filmNot["text"] = ""
            self.image = PhotoImage(file = "img/Gemini.png")
            self.newWindow = Label(root, image = self.image)
            self.newWindow.image = self.image
            self.newWindow.pack()

            self.text = Label(self.filmOnTC, text = "Projeto Gemini", font = ("Tahoma", "20", "bold"))
            self.text1 = Label(self.filmOnC, text = "Ano: 2019 \nDuração: 1h 57min \nGênero: Ação/Ficção Científica \nDireção: Ang Lee", font = ("Calibri", "14"))
            self.text["width"] = 100
            self.text.pack(side = BOTTOM)
            self.text1["width"] = 100
            self.text1.pack(side = BOTTOM)

            self.filmOnLabel["height"] = 0
        
            self.search["text"] = "Alugar no Telecine Play"
            self.search["width"] = 30
            self.search["command"] = lambda: webbrowser.open("https://www.telecineplay.com.br/")

            self.search = Button(self.exit)
            self.search["text"] = "Sair"
            self.search["font"] = ("Verdana", "8", "bold", "italic")
            self.search["fg"] = ("#FFFFFF")
            self.search["cursor"] = ("hand2")
            self.search["bg"] = ("#000046")
            self.search["width"] = 10
            self.search["command"] = quit
            self.search.pack()

        else:
            self.filmOnLabel["text"] = ""
            self.filmOnTLabel["text"] = "" 
            self.filmNot["text"] = ""
            self.newWindow = Label(text = "Digite um filme da lista... \nClique em 'Sair' para reiniciar o programa", font = ("Verdana", "10"), fg = "#000046")
            self.newWindow.pack()

            self.search["text"] = "Sair"
            self.search["command"] = quit

root = Tk()
root.title("Blockbuster")
root.geometry("900x700") 
Blockbuster(root)
root.mainloop()