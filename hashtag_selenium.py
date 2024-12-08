from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time  # importanto a biblioteca de tempo

# webdriver ferramenta que o SELENIUM usa para controlar navegador

# Chrome / firefox (navegadores recomendados)

# abrir o navegador
# o ".Chrome" é selecionando o navegador chrome para abrir
navegador = webdriver.Chrome()

# acessar um site
# get para puxar , importante passar o inicio htpps://
navegador.get("https://www.hashtagtreinamentos.com/")

# colocar o navegador tela cheia
navegador.maximize_window()  # documentação, para o navegador esta em tela cheia


# sempre que quiser selecionar apenas 1 elemento na tela utilizar find_element
# sempre que quiser selecionar mais de 1 elemento na tela utilizar find_elements

# ele precisa de 2 informações para funcionar
botao_verde = navegador.find_element("class name", "botao-verde")
# 1° caracteristica do elemento(id, clase, texto, nome xpath)
# sempre utilizar o console para identificar essas caracteristicas
# colocar dentro dos ()
# nisso, eu posso atribuir uma variavel


# se eu quiser clicar nesse botão
botao_verde.click()
# obs = as vezes vai ter a mesma classe para outros elementos

# encontrar varios elementos
# é uma lista com todos os botao dessa classe header__titulo
lista_botoes = navegador.find_elements("class name", "header__titulo")

for botao in lista_botoes:  # pecorrer essa lista
    if "Assinatura" in botao.text:  # para clicar no botao do text assinatura. ".text é o paramentro de elemento de qualquer site"
        botao.click()  # se tiver esse texto eu coloco pra cliccar
        break  # caso tenha ele vai parar , ai usa o break


# selecionar um aba
# vai dar a lista com todas as abas começando com indice 0
abas = navegador.window_handles
navegador.switch_to.window(abas[1])


# navegar para um site diferente
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

# escrever em um campo/formulario
# sempre mais facil usar id do que class, se tiver id priorizar id
""" campo_nome = navegador.find_element("id", "firstname")
campo_nome.send_keys("mateus") # ou 
campo_nome = navegador.find_element("id", "firstname").sendkeys("mateus")"""

navegador.find_element("id", "firstname").send_keys("Mateus")
navegador.find_element("id", "email").send_keys("mateuslucena1996@hotmail.com")
navegador.find_element("id", "phone").send_keys("2199999999")

botao_quero_clicar = navegador.find_element("id", "_form_2475_submit")


# dar scoll (colocar elemento na tela)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",
                         botao_quero_clicar)

# opcao 1 - espera direta
# time.sleep(3)

# opcao 2 = espera dinamica
""" from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC """

espera = WebDriverWait(navegador, 10)  # esperar condicao por 10 segundos

# o elemento tem que ta visivel na tela
botao_quero_clicar.click()
# espera dinamica e inteligente
espera.until(EC.element_to_be_clickable(botao_quero_clicar))


time.sleep(10)  # codigo para delay na pagina
