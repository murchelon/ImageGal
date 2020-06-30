# ImageGal
 Project created to train/learn about the stack: Vue.js, Phyton, Flask, DevOps-Amazon






---

# LIVE TEST:


# FEATURES:

- Image Gallery




# STACK USED:

- Bootstrap
- Markdown (Readme.md)
- Git
- Python
- Flask
- Vue.js
- AWS Aurora
- AWS BeanStalk
- Vanilla JavaScript
- jQuery (cames with Bootstrap)
- Photoshop
- SQL


# LIBRARYS/TEMPLATES USED:

Bootstrap theme for the Image Gallery:
https://startbootstrap.com/previews/freelancer/

# INSTALLATION IN A DESKTOP:


# INSTALLATION IN AWS WITH BEANSTOCK:


# INSTALLATION IN AWS USING A DOCKER CONTAINER:


# Step-by=step of all the actions I did, while creating this project:


1 - Install in the dev machine:

    - Github Desktop
    - Node.JS
    - Python 3.7
    - VSCode
        :: Install: Vetur

    - Vue Cli (not sure if needed)
        :: Install: npm install -g @vue/cli
        :: Install: npm install -g @vue/cli-init
        :: Create project: vue create imagegal
        :: Create init: vue init webpack imagegal
        :: ok the above tasks were needed only to Vue Server Side (routes). Just used the folder structure created
        
    - Python Virtual Env (for later deploy with AWS BeanStock)
        :: Install virtualenv: pip3 install virtualenv
        :: Create Virtual Env: virtualenv virt
        :: Run script: /virt/scripts/activate.bat
        :: Save Requirements: pip3 freeze > requirements.txt
        :: Command: SET FLASK_APP=app.py (in the .py folder)
        :: Command: python -m flask run (to start a web server)
        :: Install Axios: npm install --save axios
        


1 - Create an Aurora Database in AWS

2 - Download Bootstrap theme and customize for my needs
2 - Install Vue Cli in 








LINKS:
https://cli.vuejs.org/
https://www.youtube.com/watch?v=VqnJwh6E9ak


Original Text:

Teste

Objetivo
Demonstrar capacidade no desenvolvimento de aplicações web.
Tecnologias
● Frontend: Vue.js
● Backend: Python e Flask
● Banco de Dados: MySQL / Aurora (Amazon)
● DevOps: Amazon

As tecnologias acima são as desejadas, mas caso não conheça alguma das
tecnologias acima, substitua por tecnologias equivalentes.
Projeto
Desenvolver uma aplicação para cadastro e galeria de imagens.
Cadastro
Você deverá desenvolver um módulo de cadastro de imagens, onde seja possível adicionar
imagens com os seguintes dados:
● Uma Imagem de grande resolução
● Descrição da imagem
Além disso, ao fazer o upload da imagem, outras informações devem ser adicionadas a base
de dados, essas informações devem ser extraidas do próprio arquivo de imagem:
● Dimensão da Imagem
● Formato (PNG, JPEG e etc)
● Versão Thumbnail


Galeria
Criar um visualizador(browser) das imagens cadastradas. As imagens devem estar disponiveis
para busca e/ou filtragem em ao menos dois modos de visualização, lista e grade.
● A escolha de utilizar a busca e/ou filtragem fica a seu critério, é obrigatório ao menos
uma forma. A diferença está em que a busca consiste numa forma livre de entrada dos
critérios e o filtro é pré-estabelecido com base nos dados das imagens cadastradas.
● As imagens exibidas no visualizador devem ser as versões em miniatura das imagens
originais, a dimensão dessas miniaturas fica a seu critério.
● Ao clicar na imagem no visualizador, deverá ser mostrado uma caixa de diálogo ou um
pop-up com mais informações e os botões para editar e baixar a imagem original.
● (Opcional) Ordenação das imagens nos modos lista e grade.

Observações
● Escrever um arquivo README explicando como instalar e usa a aplicação.
● Desenvolver em um repositório Git, e ao final enviar acesso ao repositorio ou o
repositorio zipado contendo o histórico de alterações.
● Caso utilize a base MySQL na amazon, certifique que uma aplicação local consiga rodar
acessando a base remotamente, ou desenvolva utilizando SQLite por exemplo.
● Você não precisa hospedar a aplicação, mas fique a vontade para demonstrar o seu
conhecimento caso desejar.









