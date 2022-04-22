from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime


class Controller:
    def __init__(self, url ,tempo):
        self.url = url
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s=Service('./chromedriver.exe')
        self.driver = webdriver.Chrome(options=options,service=s)
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.tempoespera = tempo
        self.success = 0
        self.error = 0
        self.start = datetime.now()
        self.end = datetime.now()
        time.sleep(self.tempoespera)

    def log(self, msg, tipo):
        if tipo == 1:
            t = '[SUCCESS]'
            self.success +=1
        else:
            t = '[ERROR]'
            self.error +=1
        print(F" - {datetime.now()} {t}: {msg}")

    def resumo(self):
        self.end = datetime.now()
        total = self.end-self.start
        print(f" ")
        print(f" - FIM DE PROCESSAMENTO")
        print(f" - SUCCESS: \t\t {self.success}")
        print(f" - ERROR: \t\t {self.error}")
        print(f" - DURATION: \t\t {total}")

    def valida(self, id):
        driver = self.driver
        try:
            saida = driver.find_element(By.ID, id).text
            if not saida:
                self.log(F"Elemento {id} ok",1)
                return True
            self.log(F"{id} ainda permanece na pagina",0)
            return False
        except:
            self.log(F"Erro ao validar item {id} ",0)
            return False
        

    def image(self, path):
        driver = self.driver
        try:
            imagem = driver.find_element(By.XPATH,path)
            if imagem.is_displayed():
                self.log(F"Imagem encontrada e Visivel",1)
                return True
            self.log(F"Imagem encontrada mas não visivel",0)
            return False
        except:
            self.log(F"Erro ao encontrar imagem",0)
            return False


    def troca_iframe(self,id):
        try:
            driver = self.driver
            driver.switch_to.frame(id)
            time.sleep(self.tempoespera)
            self.log(F"Frame Alterado {id} ",1)
            return True
        except:
            self.log(F"Erro Frame {id}",0)
            return False
    
    def clique(self, id):
        try:
            driver = self.driver
            botao_enviar =  driver.find_element(By.ID, id)
            botao_enviar.click()
            time.sleep(self.tempoespera)
            self.log(F"{id} Clique ok",1)
            return True
        except:
            self.log(F"Erro clique {id} ",0)
            return False

    def preencher(self, id, dado):
        try:
            driver = self.driver
            preenche = driver.find_element(By.ID, id)
            preenche.clear()
            preenche.send_keys(dado)
            self.log(F"{dado} enviado ao item {id} ",1)
            return True
        except:
            self.log(F"Erro ao preencher {id} ",0)
            return False

    def selecionar(self, id, opcao):
        try:
            driver = self.driver
            select = Select(driver.find_element(By.ID,id))
            select.select_by_value(opcao)
            self.log(F"{opcao} selecionado",1)
            return True
        except:
            self.log(F"Erro ao selecionar {id} ",0)
            return False

    def fechar(self):
        self.resumo()
        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":
    bot = Controller('https://wj-qa-automation-test.github.io/qa-test/',1)
    butons = ["btn_one","btn_two","btn_link"]

    '''
    1) Crie um cenário onde clicamos nos botões "One", "Two, e "Four", 
    depois verifique a ausência dos mesmos.

    2) Dentro da mesma página, clique nos botões "One", "Two" e "Four" 
    que encontram-se dentro do painel "IFRAME BUTTONS" e 
    valide a não-presença dos mesmos.
    '''

    for i in range(2):
        for item in butons:
            bot.clique(item)
            bot.valida(item)
        bot.troca_iframe(0)
    bot.troca_iframe(None)



    '''
    3) No cenário final, iremos preencher o campo "YourFirstName" com um texto qualquer. 
    Clique no botão "One", cheque a opção "OptionThree", 
    selecione a opção "ExampleTwo" dentro da select box, 
    e valide a presença da imagem do logo do "Selenium Webdriver".
    '''
    bot.clique('reset_buttons')
    bot.preencher('first_name','Texto de teste')
    bot.clique('btn_one')
    bot.clique('opt_three')
    bot.selecionar('select_box','option_two')
    bot.image("//div[@id='panel_body_three']//img[@alt='selenium']")

    bot.fechar()
