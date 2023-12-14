import tkinter as tk

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Transição")

        # Criação de dois frames
        self.frame1 = tk.Frame(root)
        self.frame2 = tk.Frame(root)

        # Configuração inicial
        self.mostrar_frame(self.frame1)

        # Adiciona widgets aos frames
        self.configurar_frame1()
        self.configurar_frame2()

    def mostrar_frame(self, frame):
        """Mostra o frame desejado e esconde os outros."""
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def configurar_frame1(self):
        label1 = tk.Label(self.frame1, text="Frame 1")
        label1.pack(pady=20)

        # Adicione widgets ou configurações específicas para o Frame 1

        # Adiciona um botão para transição para o Frame 2
        botao_transicao = tk.Button(self.frame1, text="Ir para Frame 2", command=lambda: self.mostrar_frame(self.frame2))
        botao_transicao.pack()

    def configurar_frame2(self):
        label2 = tk.Label(self.frame2, text="Frame 2")
        label2.pack(pady=20)

        # Adicione widgets ou configurações específicas para o Frame 2

        # Adiciona um botão para transição para o Frame 1
        botao_transicao = tk.Button(self.frame2, text="Ir para Frame 1", command=lambda: self.mostrar_frame(self.frame1))
        botao_transicao.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.geometry("400x300")
    root.mainloop()
