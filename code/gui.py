import tkinter as tk
from PIL import ImageTk, Image
import threading
from spinFuncs import *

def object_destroy(obj):
    obj.destroy()

class My_gui:

    def __init__(self):
        self.balancer = 0
        self.root = tk.Tk()
        self.menubar = tk.Menu(self.root)
        self.root.title('Slots')
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.image = Image.open('images/Welcome.png')
        self.newImg = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.root, image=self.newImg)
        self.image_label.place(x=0, y=0)
        self.start = tk.Button(self.root, text="Start Game", font=("Arial", 18), bg='Yellow', fg='purple', relief='groove', height=2, bd=10, command=self.clear)
        self.start.pack(side=tk.BOTTOM)
        self.root.mainloop()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.balancer == 0:
            self.leader()
            self.balancer+=1
        elif self.balancer == 1:
            self.bets()
            self.balancer+=1
        else:
            pass
    
    def replace(self):
        self.label = tk.Label(self.root, text="")
        self.image = Image.open('images/tall_slot_machine_500x500.png')
        self.newImg = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.root, image=self.newImg)
        self.image_label.place(x=0, y=0)
        self.betLabel = tk.Label(self.root, text=f"Total Bet: {self.total}")
        self.betLabel.place(x=5, y=15)
        self.lineLabel = tk.Label(self.root, text=f"Lines: {self.lines+1}")
        self.lineLabel.place(x=5, y=45)
        self.currentBalance = tk.Label(self.root, text=f"Current Balance: {self.balance}", wraplength=125)
        self.currentBalance.place(x=5, y=75)
        self.spinner = tk.Button(self.root, text="SPIN", font=('Arial', 16), command=self.spin)
        self.spinner.place(x=217, y=350)
        self.leave = tk.Button(self.root, text="Leave", font=('Arial', 16), command=self.leaver)
        self.leave.place(x=400, y=450)


    def leader(self):
        self.balance = 0
        self.lines = 1
        self.bet = 0
        self.message = 'What would you like to deposit?'
        self.alabel = tk.Label(self.root, text=self.message, font=('Arial', 18))
        self.alabel.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=2, font=('Arial', 16))
        self.textbox.bind("<KeyPress>")
        self.textbox.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text="Enter", font=('Arial', 16), command=self.show)
        self.button.pack(padx=10, pady=10)

    def show(self):
        try:
            self.myMessage = int(self.textbox.get('1.0', tk.END))
            self.balance = self.myMessage
            self.clear()
        except:
            self.newMsg = tk.Label(self.root, text="That is not a number, please enter a number", font=('Arial', 16))
            self.newMsg.pack(padx=10, pady=10)

    def bets(self):
        self.newMsg = tk.Label(self.root, text="Input the amount you want to bet on each line, then the number of lines you want to bet on.", wraplength=450, font=('Arial', 16))
        self.newMsg.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=2, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.option = tk.IntVar()

        self.radio1 = tk.Radiobutton(self.frame, text="1 Line", variable=self.option, value=0)
        self.radio2 = tk.Radiobutton(self.frame, text="2 Lines", variable=self.option, value=1)
        self.radio3 = tk.Radiobutton(self.frame, text="3 Lines", variable=self.option, value=2)

        self.radio1.pack(side=tk.LEFT, padx=3)
        self.radio2.pack(side=tk.LEFT, padx=3)
        self.radio3.pack(side=tk.LEFT, padx=3)

        self.alabel = tk.Button(self.root, text='submit', font=('Arial', 16), command=self.setter)
        self.alabel.pack(padx=10, pady=10)

    def setter(self):
        try:
            self.bet = (self.textbox.get('1.0', tk.END)).rstrip()
            self.bet = int(self.bet)
        except:
            self.newMsg = tk.Label(self.root, text="The bet you entered is not a number, please enter a number", wraplength=450, font=('Arial', 16))
            self.newMsg.pack(padx=10, pady=10)

        self.lines = self.option.get()
        self.total = self.bet*(self.lines+1)
        if self.total > self.balance:
            self.newMsg = tk.Label(self.root, text=f"You bet ${self.bet} on {self.lines+1} lines. That is ${(self.total)-(self.balance)} more than your balance", wraplength=450, font=('Arial', 16))
            self.newMsg.pack(padx=10, pady=10)
        else:
            self.clear()
            self.replace()


    def spin(self):
        if self.balance >= self.total:
            self.balance-=self.total
            self.replace()
            self.spun = get_slots_spin()
            self.row_one = '\n'.join(self.spun[0])
            self.row_two = '\n'.join(self.spun[1])
            self.row_three = '\n'.join(self.spun[2])
            self.numLabel = tk.Label(self.root, text=self.row_one)
            self.numLabel.place(x=193, y=183)
            self.numLabel2 = tk.Label(self.root, text=self.row_two)
            self.numLabel2.place(x=246, y=183)
            self.numLabel3 = tk.Label(self.root, text=self.row_three)
            self.numLabel3.place(x=299, y=183)
            self.winnings = check_slots(self.spun, self.lines+1, self.bet)
            self.balance+=self.winnings

    def leaver(self):
        self.clear()
        self.last = tk.Label(self.root, text=f"You ended with ${self.balance}, come again soon!", font=('Arial', 54), wraplength=400)
        self.last.pack(padx=40)
        self.ender = threading.Timer(5, self.end)
        self.ender.start()

    def end(self):
        self.root.destroy()


