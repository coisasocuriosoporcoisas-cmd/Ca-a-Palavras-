#O CÓDIGO A SEGUIR POSSUE ALGUNS ERROS CONSIDERÁVEIS, COMO A QUESTÃO DA CENTRALIZAÇÃO QUANDO SAIMOS DA TELA PADRÃO PARA A TELA CHEIA. e possue poucas matrizes, só preciso comenta cada um


import tkinter as tk
def matrix():
      return {"matrix1": {
            "matriz": [
                ["A","B","C","D","B","A","Q","G"],
                ["J","A","V","A","R","H","J","K"],
                ["A","U","Y","W","M","Y","T","J"],
                ["B","U","Q","S","S","O","O","L"],
                ["F","O","R","T","R","A","N","J"],
                ["U","U","I","Q","M","R","Q","Y"],
                ["X","Y","T","H","W","N","A","Z"],
                ["P","Y","T","H","O","N","W","S"]
            ],
            "palavras": {
                "PYTHON": [
                    "É A LINGUAGEM MAIS SIMPLES DENTRE TODAS AS DEMAIS.",
                    "SUA FORMA DE EXIBIR ALGO NA TELA É FEITA ATRAVÉS DA FUNÇÃO PRINT()",
                    "É ÓTIMA PARA ANALISE DE DADOS E INTELIGÊNCIA ARTIFICIAL."
                ],
                "JAVA": [
                    "É A LINGUGEM QUE RODA EM VÁRIOS DISPOSITIVOS DIFERENTES.",
                    "ERA A LINGUAGEM DOMINANTE NAS APLICAÇÃOES DOS PRIMEIROS SHARTPHONES.",
                    "ERA A LINGUAGEM FREBRE NOS ANOS 90 E INICIO DOS ANOS 2000."
                ],
                "FORTRAN":[
                      "A PRIMEIRA LINGUAGEM DE PROGRAMAÇÃO DE ALTO NÍVEL.",
                      "FOI CRIADA PELA IBM, UMAS DAS MAIORES EMPRESAS DE TECNOLOGIA DO MUNDO EM 1950.",
                      "POSSUI FOCO NA ÁREA CIENTÍFICA E DE ENGENHARIA."
                      
                ]
            }
        },
    
      "matrix2":{
            "matriz": [
                ["Y","S","E","I","U","A","Q","G"],
                ["T","S","I","U","R","H","J","K"],
                ["G","D","Y","W","O","L","B","J"],
                ["Ç","U","Q","S","M","O","O","L"],
                ["P","Z","W","V","R","R","E","J"],
                ["U","U","R","A","M","R","Q","Y"],
                ["M","J","Q","E","V","N","A","Z"],
                ["L","K","T","I","O","N","W","S"]
            ],
          "palavras": {
                  "SSD": [
                        "TIPO DE ARMAZENAMENTO MAIS RÁPIDO E MODERNO.",
                        "UTILIZA MEMÓRIA FLASH PARA ARMAZENAR DADOS.",
                        "NÃO POSSUI PARTES MÓVEIS, AO CONTRÁRIO DOS HDs."
                  ],
                  "ROM": [
                        "TIPO DE MEMÓRIA QUE ARMAZENA DADOS DE FORMA PERMANENTE.",
                        "SEU CONTEÚDO NÃO PODE SER MODIFICADO FACILMENTE.",
                        "UTILIZADA PARA ARMAZENAR FIRMWARES E SOFTWARES EMBUTIDOS."

                  ],
                  "RAM":[
                        "TIPO DE MEMÓRIA VOLÁTIL UTILIZADA PELO COMPUTADOR PARA ARMAZENAR DADOS TEMPORÁRIOS.",
                        "QUANTO MAIS DELA UM COMPUTADOR POSSUI, MAIS RÁPIDO ELE PODE EXECUTAR TAREFAS.",
                        "SEU CONTEÚDO É PERDIDO QUANDO O COMPUTADOR É DESLIGADO."
                  ]
          }
    } 

    }
def gera_matrix():
      import random
      matrixes= matrix()
      nome_matrix= random.choice(list(matrixes.keys()))
      return nome_matrix, matrixes[nome_matrix]

janela = tk.Tk()
janela.title("Caça-Palavras")
janela.geometry("1080x1080")
janela.config(bg="black")
texto= tk.Label(janela,text="CAÇA-PALAVRAS", font=("Arial",50), bg="Blue", fg="white", borderwidth=4, relief="raised")
texto.pack(pady=5)
#chamadas das funções.
nome_matrix, jogo = gera_matrix()
matrix_sorteada = jogo["matriz"]
palavras = list(jogo["palavras"].keys())
indice_palavra= 0
palavra_atual = palavras[indice_palavra]
dicas = jogo["palavras"][palavra_atual]
indice_palavra= 0
indice_dicas=0

#parte VISUAL DAS DICAS.
#___________________RETÂNGULOS________________
Canvas_quadri= tk.Canvas(janela, bg="orange",width="2050", height="350",highlightthickness=0)
Canvas_quadri.pack(side="bottom",pady=15)
Canvas_nv_quadrado= tk.Canvas(Canvas_quadri, bg="#FFFFFF",width="1950", height="300",highlightthickness=0)
Canvas_nv_quadrado.pack(pady=20)
#funções dedicadas aos butões
def atualizar_tela_dicas():
    """Função única para desenhar o texto da dica no Canvas"""
    Canvas_nv_quadrado.delete("dicas") 
    largura = Canvas_nv_quadrado.winfo_width()
    altura = Canvas_nv_quadrado.winfo_height()
    if largura <= 1: largura = 1950
    if altura <= 1: altura = 300
    Canvas_nv_quadrado.create_text(
        largura // 2,
        altura // 2,      
        text=dicas[indice_dicas],
        font=("open sans", 16, "bold"), 
        anchor="center",
        fill="black",
        width=largura * 0.8, 
        tag="dicas"
    )
def mostra_dicas_uma_a_uma():
    global indice_dicas
    if indice_dicas < len(dicas) - 1:
        indice_dicas += 1
        atualizar_tela_dicas()
def voltar_dica():
    global indice_dicas 
    if indice_dicas > 0:
        indice_dicas -= 1
        atualizar_tela_dicas()
def avancar_palavra():
    global indice_palavra, palavra_atual, dicas, indice_dicas

    indice_palavra += 1
    
    if indice_palavra >= len(palavras):
        print("TODAS AS PALAVRAS ENCONTRADAS!")
        Canvas_nv_quadrado.delete("dicas")
        Canvas_nv_quadrado.create_text(
            Canvas_nv_quadrado.winfo_width() // 2,
            Canvas_nv_quadrado.winfo_height() // 2,
            text="\t JOGO FINALIZADO! ",
            font=("open sans", 22, "bold"),
            fill="black",
            tag="dicas"
        )
        return
    palavra_atual = palavras[indice_palavra]
    dicas = jogo["palavras"][palavra_atual]
    indice_dicas = 0
    mostra_dicas_uma_a_uma()
#função para o butão voltar aqui é a lógica.
def voltar_dica():
      global indice_dicas 
      if indice_dicas <= 0:
            return 
      indice_dicas -=1
      mostra_dicas_uma_a_uma()
      Canvas_nv_quadrado.delete("dicas")
      #largura = Canvas_nv_quadrado.winfo_width()
      #altura = Canvas_nv_quadrado.winfo_height()

      Canvas_nv_quadrado.create_text(
        largura = 20 ,
        altura = 34,
        text=dicas[indice_dicas], font =("open sans",10, "bold" ),anchor="center", fill="black", tag="dicas")
def novo_jogo():
    global matrix_sorteada, jogo, palavras, palavra_atual, dicas, indice_palavra, indice_dicas     
    nome, jogo = gera_matrix() 
    matrix_sorteada = jogo["matriz"]
    palavras = list(jogo["palavras"].keys())
    indice_palavra = 0
    palavra_atual = palavras[indice_palavra]
    dicas = jogo["palavras"][palavra_atual]
    indice_dicas = 0
    desenhar_grade()        
    atualizar_tela_dicas()  
    print(f"Novo jogo carregado: {nome}")
#função para configura o posiciobamneto do butão.
def posicionar_botao(event=None):
    Canvas_nv_quadrado.delete("botao")
    largura = Canvas_nv_quadrado.winfo_width()
    altura = Canvas_nv_quadrado.winfo_height()
    Canvas_nv_quadrado.create_text(
        largura // 2, 30, 
        text="DICAS", font=("open sans", 12, "bold"), fill="gray", tag="botao"
    )
    Canvas_nv_quadrado.create_window(
        largura * 0.1, altura * 0.5, 
        window=butao_volta, anchor="center", tag="botao"
    )
    Canvas_nv_quadrado.create_window(
        largura * 0.9, altura * 0.5, 
        window=butao_seg, anchor="center", tag="botao"
    )
    Canvas_nv_quadrado.create_window(
        largura * 0.5, altura * 0.85, 
        window=butão_gerar_caca, anchor="center", tag="botao"
    )
Canvas_nv_quadrado.bind("<Configure>", posicionar_botao)
#butões 
butao_seg= tk.Button( Canvas_nv_quadrado,text=" |>", font=("open sans",50, "bold"),bg="#3E8199", fg="white", command=avancar_palavra)
butao_volta= tk.Button(Canvas_nv_quadrado,text=" <| ",font=("open sans", 50,"bold"),bg="#005F81", fg= "white", command=voltar_dica)
butão_gerar_caca= tk.Button(Canvas_nv_quadrado,text="NOVO\nCaça-Palavras",font=("open sans", 20,"bold"),bg="#FFE600", fg= "#000000",command= novo_jogo)
# ================= CAÇA-PALAVRAS =================

TAM_CELULA = 53.5
arrastando = False
selecionadas = []
posicoes = []
#LÓGICA INTERATIVA DA MATRIX COM CADA UM DOS ELEMNETOS, QUANDO PASSAMOS O MOUSE OS ELEMNTOS ALTERAM SEU CONTÉUDO VISUAL.
Canvas_matrix = tk.Canvas(
    janela, bg="green", width=420, height=420, highlightthickness=0
)
Canvas_matrix.pack(pady=20)

def eh_adjacente(p1, p2):
    l1, c1 = p1
    l2, c2 = p2
    return abs(l1 - l2) <= 1 and abs(c1 - c2) <= 1
def adicionar_letra(linha, coluna):
    pos = (linha, coluna)
    if pos in posicoes:
        return
    if posicoes and not eh_adjacente(posicoes[-1], pos):
        return
    selecionadas.append(matrix_sorteada[linha][coluna])
    posicoes.append(pos)

    Canvas_matrix.itemconfig(celulas[pos], fill="#00FF22")
def iniciar_selecao(event):
    global arrastando, selecionadas, posicoes

    arrastando = True
    selecionadas = []
    posicoes = []

    linha = int(event.y // TAM_CELULA)
    coluna = int(event.x // TAM_CELULA)

    if 0 <= linha < 8 and 0 <= coluna < 8:
        adicionar_letra(linha, coluna)

def arrastar(event):
    if not arrastando:
        return
    linha = int(event.y // TAM_CELULA)
    coluna = int(event.x // TAM_CELULA)
    if 0 <= linha < 8 and 0 <= coluna < 8:
        adicionar_letra(linha, coluna)
def finalizar_selecao(event):
    global arrastando
    arrastando = False
    palavra_formada = "".join(selecionadas) 
    if palavra_formada == palavra_atual:
        print("Acertou:", palavra_atual)    
        avancar_palavra()         
    else:     
        for pos in posicoes:
            Canvas_matrix.itemconfig(celulas[pos], fill="white")

# ================= DESENHO DA MATRIZ =================
celulas = {}
def desenhar_grade():
  Canvas_matrix.delete("all") 
  for linha in range(8):
        for coluna in range(8):
            x1 = coluna * TAM_CELULA
            y1 = linha * TAM_CELULA
            x2 = x1 + TAM_CELULA
            y2 = y1 + TAM_CELULA

            rect = Canvas_matrix.create_rectangle(
                x1, y1, x2, y2, fill="#EED600", outline="#000000"
            )
            
            Canvas_matrix.create_text(
                x1 + TAM_CELULA / 2,
                y1 + TAM_CELULA / 2,
               
                text=matrix_sorteada[linha][coluna],
                font=("open sans", 30),
                fill = "#421B1B"
            )

            celulas[(linha, coluna)] = rect
# ================= BINDS CORRETOS =================

Canvas_matrix.bind("<Button-1>", iniciar_selecao)
Canvas_matrix.bind("<B1-Motion>", arrastar)
Canvas_matrix.bind("<ButtonRelease-1>", finalizar_selecao)



desenhar_grade()
janela.update()
atualizar_tela_dicas()
janela.mainloop()
              
              
              
              