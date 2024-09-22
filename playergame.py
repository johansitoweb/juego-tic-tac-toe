import tkinter as tk  
from tkinter import messagebox  

class TicTacToe:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Tic Tac Toe")  
        self.root.configure(bg='black')  
        
        self.current_player = "X"  
        self.board = [" " for _ in range(9)]  
        self.buttons = [None for _ in range(9)]  

        self.create_buttons()  
    
    def create_buttons(self):  
        for i in range(9):  
            button = tk.Button(self.root, text=" ", font=('Arial', 40), bg='black', fg='white',  
                               command=lambda i=i: self.make_move(i))  
            button.grid(row=i // 3, column=i % 3, sticky='nsew', ipadx=20)  
            self.buttons[i] = button  
        
        for i in range(3):  
            self.root.grid_rowconfigure(i, weight=1)  
            self.root.grid_columnconfigure(i, weight=1)  

    def make_move(self, index):  
        if self.board[index] == " " and self.check_winner() is None:  
            self.board[index] = self.current_player  
            self.buttons[index].config(text=self.current_player)  
            winner = self.check_winner()  
            if winner:  
                messagebox.showinfo("¡Ganador!", f"¡El jugador {winner} ha ganado!")  
                self.reset_game()  
            elif " " not in self.board:  
                messagebox.showinfo("¡Empate!", "El juego ha terminado en empate.")  
                self.reset_game()  
            else:  
                self.current_player = "O" if self.current_player == "X" else "X"  

    def check_winner(self):  
        winning_combinations = [  
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas  
            (0, 4, 8), (2, 4, 6)               # diagonales  
        ]  
        
        for combo in winning_combinations:  
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":  
                return self.board[combo[0]]  
        return None  

    def reset_game(self):  
        self.current_player = "X"  
        self.board = [" " for _ in range(9)]  
        for button in self.buttons:  
            button.config(text=" ")  

if __name__ == "__main__":  
    root = tk.Tk()  
    game = TicTacToe(root)  
    root.mainloop()