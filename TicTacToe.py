from tkinter import *
import random

class TicTacToe:
    winBoard = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
    def __init__(self, board):
        self.mainFrame = Frame(board)
        self.mainFrame.pack()

        self.board = Canvas(self.mainFrame, width=300, height=300, bg = "gray")
        self.board.pack(fill="both")

        self.single = Button(self.mainFrame, text="Single Player", command=self.sgPlayer, height=3, fg="white", bg="gray")
        self.single.pack(fill="both", expand=True, side=LEFT)

        self.double = Button(self.mainFrame, text="Double Player", command=self.dbPlayer, height=3, fg="white", bg="gray")
        self.double.pack(fill="both", expand=True, side=RIGHT)
        
        
    def drawBoard(self):
        self.board.create_rectangle(0, 0, 300, 300)
        self.board.create_rectangle(0, 200, 300, 100)
        self.board.create_rectangle(200, 0, 100, 300)
        self.board.pack()

    def sgPlayer(self):
        self.players = 1
        self.moves = [1,2,3,4,5,6,7,8,9]
        self.start()

    def dbPlayer(self):
        self.players = 2
        self.start()
        
    def start(self):
        self.board.delete(ALL)
        self.drawBoard()
        self.board1 = []
        self.board2 = []
        self.turn = 0
        self.board.bind("<Button-1>", self.draw)
                      
    def draw(self, event):
        x = (event.x // 100)
        y = (event.y // 100)
        if self.turn % 2 == 0:
            if self.board.find_enclosed(x * 100, y * 100, (x + 1) * 100, (y + 1) * 100) == ():
                self.board.create_line(x * 100 + 15, y * 100 + 15, x * 100 + 85, y * 100 + 85, width=4, fill="white")
                self.board.create_line(x * 100 + 85, y * 100 + 15, x * 100 + 15, y * 100 + 85, width=4, fill="white")

                if y == 0:
                    i = x + 1
                elif y == 1:
                    i = x + 4
                else:
                    i = x + 7
                    
                self.board1.append(i)
                if self.players == 1:
                    self.moves.remove(i)
                self.turn += 1
                
            if self.players == 1 and self.turn % 2 == 1:
                self.checkWin()
                self.computer()
                self.turn += 1
                        
        elif self.players == 2:
            if self.board.find_enclosed(x * 100, y * 100, (x + 1) * 100, (y + 1) * 100) == ():
                self.board.create_oval(x * 100 + 15, y * 100 + 15, x * 100 + 85, y * 100 + 85, width=4, outline="white")
                if y == 0:
                    self.board2.append(x + 1)
                elif y == 1:
                    self.board2.append(x + 4)
                else:
                    self.board2.append(x + 7)
                self.turn += 1
    
        self.checkWin()
    
    def computer(self):
        for x in range(len(self.winBoard)):
            if len(set(self.winBoard[x]) & set(self.board2)) == 2:
                i = list(set(self.winBoard[x]) ^ (set(self.winBoard[x]) & set(self.board2)))[0]
                if i in self.moves:
                    self.drawCircle(i)
                    self.moves.remove(i)
                    self.board2.append(i)
                    return
        
        for y in range(len(self.winBoard)):
            if len(set(self.winBoard[y]) & set(self.board1)) == 2:
                i = list(set(self.winBoard[y]) ^ (set(self.winBoard[y]) & set(self.board1)))[0]
                if i in self.moves:
                    self.drawCircle(i)
                    self.moves.remove(i)
                    self.board2.append(i)
                    return

        if not self.moves == []:
            i = random.sample(self.moves, 1)[0]
            self.drawCircle(i)
            self.moves.remove(i)
            self.board2.append(i)

    def drawCircle(self, sq):
        if sq in range(1, 4):
            sq -= 1
            self.board.create_oval(sq * 100 + 15, 15, sq * 100 + 85, 85, width=4, outline="white")
        elif sq in range(4, 7):
            sq -= 4
            self.board.create_oval(sq * 100 + 15, 115, sq * 100 + 85, 185, width=4, outline="white")
        else:
            sq -= 7
            self.board.create_oval(sq * 100 + 15, 215, sq * 100 + 85, 285, width=4, outline="white")

    def checkWin(self):
        for i in range(len(self.winBoard)):
            if len(set(self.winBoard[i]) & set(self.board1)) == 3:
                self.endGame("Player 1 wins!")
            if len(set(self.winBoard[i]) & set(self.board2)) == 3:
                self.endGame("Player 2 wins!" if self.players == 2 else "Computer wins!")
        if self.turn == 9:
            self.endGame("It's a tie!")
        
    def endGame(self, txt):
        self.moves = []
        self.board.unbind("<ButtonPress-1>")

        self.popup = Toplevel()
        self.popup.geometry("100x54+%d+%d" % (x-50, y-27))

        self.popup.title("Winner!")
        
        self.msg = Message(self.popup, text=txt, width=100)
        self.msg.pack()

        self.btn = Button(self.popup, text="Close", command=self.popup.destroy)
        self.btn.pack()

    
root = Tk()
root.title("PythonTTT")

welcome = Label(root, text = "Welcome to our Tic Tac Toe game!", fg = "white", bg="gray")
welcome.pack(fill=X)

x = root.winfo_screenwidth() / 2 
y = root.winfo_screenheight() / 2 

root.geometry("+%d+%d" % (x - 150, y - 150))

game = TicTacToe(root)
root.mainloop()
