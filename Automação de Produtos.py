
import pandas as pd
import time as tm
import pyautogui as pg  

Link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
Email = "emailfake@gmail.com"
Senha = "SenhaFake"
pg.PAUSE = 1

#abrir o navegador 
pg.press("win")
pg.write("opera gx")
pg.press("enter")
tm.sleep(3)

#abrir o sistema pelo link
pg.write(Link)
pg.press("enter")
tm.sleep(5)

#fazer login
pg.click(x=1506, y=368)
pg.write(Email)
pg.press("tab")
pg.write(Senha)
pg.press("tab")
pg.press("enter")
tm.sleep(5)

#importar a base de dados
tabela = pd.read_csv(r"C:\Users\Pichau\OneDrive\Área de Trabalho\Cursos\Curso Hastag Programação\Python\Automacao\Exercicios\Produtos.csv")
print(tabela)

#lopp da automacao
for linha in tabela.index:
    #cadastrar o primeiro produto
    #codigo do produto
    pg.click(x=1343, y=267)
    codigo = tabela.loc[linha, "codigo"]
    pg.write(codigo)
    pg.press("tab")

    #marca do produto
    marca = tabela.loc[linha, "marca"]
    pg.write(marca)
    pg.press("tab")

    #tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pg.write(tipo)
    pg.press("tab")

    #categoria do produto
    categoria = tabela.loc[linha, "categoria"]
    pg.write(str(categoria))
    pg.press("tab")

    #preco do produto
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pg.write(preco_unitario)
    pg.press("tab")

    #custo do produto
    custo = str(tabela.loc[linha, "custo"])
    pg.write(custo)
    pg.press("tab")

    #obs do produto
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pg.write(str(tabela.loc[linha, "obs"]))
    pg.press("tab")

    #enviar o produto
    pg.press("enter")