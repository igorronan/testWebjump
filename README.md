# Teste Automatizado Webjump

Teste Automatizado WebJump - Analista de QA


## Preparando Ambiente

* Python 3
        - https://www.python.org/downloads/


* Google Chrome
        - https://www.google.pt/intl/pt-PT/chrome/

        Verificar a versão do Chrome e realizar o downalod do ChromeDriver compatível
        Versão chrome: Menu > Ajuda > Sobre o Google Chrome 

* ChromeDriver (Manter na mesma pasta do app)
        - https://chromedriver.chromium.org/downloads
        deve ser copiado para a raiz da pasta do projeto


* Instalação
    ```sh
        source venv/Scripts/activate
        pip install -r requirements.txt
    ```

## Cenários possiveis

1) Crie um cenário onde clicamos nos botões "One", "Two, e "Four", depois verifique a ausência dos mesmos.

2) Dentro da mesma página, clique nos botões "One", "Two" e "Four" que encontram-se dentro do painel "IFRAME BUTTONS" e valide a não-presença dos mesmos.

3) No cenário final, iremos preencher o campo "YourFirstName" com um texto qualquer. Clique no botão "One", cheque a opção "OptionThree", selecione a opção "ExampleTwo" dentro da select box, e valide a presença da imagem do logo do "Selenium Webdriver".

4) Documente as versões das ferramentas utilizadas (O.S, Ruby, Firefox, Geckodriver, Chromedriver, etc.) e crie um step-by-step informando como configurar e utilizar esse ambiente, levando em conta a possibilidade de alguma pessoa iniciante dar continuidade em um projeto feito por você.


## Utilização

No prompt de comando:
```sh
    python3 Controller.py
```

## Saidas
```sh
    - 2022-04-22 16:11:40.722693 [SUCCESS]: btn_one Clique ok
    - 2022-04-22 16:11:40.749694 [SUCCESS]: Elemento btn_one ok
    - 2022-04-22 16:11:41.798162 [SUCCESS]: btn_two Clique ok
    - 2022-04-22 16:11:41.813189 [SUCCESS]: Elemento btn_two ok
    - 2022-04-22 16:11:42.854514 [SUCCESS]: btn_link Clique ok
    - 2022-04-22 16:11:42.870250 [SUCCESS]: Elemento btn_link ok
    - 2022-04-22 16:11:43.879686 [SUCCESS]: Frame Alterado 0
    - 2022-04-22 16:11:44.934936 [SUCCESS]: btn_one Clique ok
    - 2022-04-22 16:11:44.956549 [SUCCESS]: Elemento btn_one ok
    - 2022-04-22 16:11:46.018494 [SUCCESS]: btn_two Clique ok
    - 2022-04-22 16:11:46.041121 [SUCCESS]: Elemento btn_two ok
    - 2022-04-22 16:11:47.101543 [SUCCESS]: btn_link Clique ok
    - 2022-04-22 16:11:47.129793 [SUCCESS]: Elemento btn_link ok
    - 2022-04-22 16:11:48.143081 [SUCCESS]: Frame Alterado None
    - 2022-04-22 16:11:49.200880 [SUCCESS]: reset_buttons Clique ok
    - 2022-04-22 16:11:49.281376 [SUCCESS]: Texto de teste enviado ao item first_name
    - 2022-04-22 16:11:50.321064 [SUCCESS]: btn_one Clique ok
    - 2022-04-22 16:11:51.376917 [SUCCESS]: opt_three Clique ok
    - 2022-04-22 16:11:51.452262 [SUCCESS]: option_two selecionado
    - 2022-04-22 16:11:51.472935 [SUCCESS]: Imagem encontrada e Visivel

    - FIM DE PROCESSAMENTO
    - SUCCESS:              20
    - ERROR:                0
    - DURATION:             0:00:12.820959
```