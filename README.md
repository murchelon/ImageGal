# ImageGal
 Project created to train/learn about the stack: Vue.js, Phyton, Flask, DevOps-Amazon
 The application is an Image Gallery where you can uploads images to it. An thumbnail version of it is created and the metadata is saved in a database.
 You are able to see the images in a list or grid format and you can download the original with full resolution.
 You also can search for a particular image.


## LIVE TEST:


## FEATURES:

- Upload image
- Thumbnail generation
- Save metadata in a database
- Vue.js to create a reactive front-end
- Responsive front-end, using a free Bootstrap theme
- Javascript and CSS to resize the image and get it's size. width and height, on the client side before upload
- Image preview before upload


## STACK USED:

- Bootstrap
- Markdown (Readme.md)
- Git
- Python
- Flask
- Jinja
- Vue.js
- AWS Aurora
- AWS BeanStalk
- JavaScript
- jQuery (cames with Bootstrap)
- Photoshop
- SQL


## LIBRARYS/TEMPLATES USED:

Bootstrap theme for the Image Gallery:
https://startbootstrap.com/previews/freelancer/


## INSTALLATION IN A DESKTOP:


## INSTALLATION IN AWS WITH BEANSTOCK:


## INSTALLATION IN AWS USING A DOCKER CONTAINER:


## Step-by=step of all the actions I did, while creating this project:


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
        :: Command: python -m flask run (to start a web server)
        :: Install Axios: npm install --save axios
        :: Install Pillow: pip3 install pillow
        :: Save Requirements: pip3 freeze > requirements.txt
        









Original Text:

Teste

Objetivo:

Demonstrar capacidade no desenvolvimento de aplicações web.
Tecnologias:

● Frontend: Vue.js<BR>
● Backend: Python e Flask<BR>
● Banco de Dados: MySQL / Aurora (Amazon)<BR>
● DevOps: Amazon<BR>

As tecnologias acima são as desejadas, mas caso não conheça alguma das tecnologias acima, substitua por tecnologias equivalentes.

Projeto:
Desenvolver uma aplicação para cadastro e galeria de imagens.Cadastro
Você deverá desenvolver um módulo de cadastro de imagens, onde seja possível adicionar
imagens com os seguintes dados:

● Uma Imagem de grande resolução<BR>
● Descrição da imagem<BR>

Além disso, ao fazer o upload da imagem, outras informações devem ser adicionadas a base de dados, essas informações devem ser extraidas do próprio arquivo de Imagem:

● Dimensão da Imagem<BR>
● Formato (PNG, JPEG e etc)<BR>
● Versão Thumbnail<BR>


Galeria<BR>
Criar um visualizador(browser) das imagens cadastradas. As imagens devem estar disponiveis
para busca e/ou filtragem em ao menos dois modos de visualização, lista e grade.

● A escolha de utilizar a busca e/ou filtragem fica a seu critério, é obrigatório ao menos
uma forma. A diferença está em que a busca consiste numa forma livre de entrada dos
critérios e o filtro é pré-estabelecido com base nos dados das imagens cadastradas.<BR>
● As imagens exibidas no visualizador devem ser as versões em miniatura das imagens
originais, a dimensão dessas miniaturas fica a seu critério.<BR>
● Ao clicar na imagem no visualizador, deverá ser mostrado uma caixa de diálogo ou um
pop-up com mais informações e os botões para editar e baixar a imagem original.<BR>
● (Opcional) Ordenação das imagens nos modos lista e grade.<BR>

Observações<BR>
● Escrever um arquivo README explicando como instalar e usa a aplicação.<BR>
● Desenvolver em um repositório Git, e ao final enviar acesso ao repositorio ou o
repositorio zipado contendo o histórico de alterações.<BR>
● Caso utilize a base MySQL na amazon, certifique que uma aplicação local consiga rodar
acessando a base remotamente, ou desenvolva utilizando SQLite por exemplo.<BR>
● Você não precisa hospedar a aplicação, mas fique a vontade para demonstrar o seu
conhecimento caso desejar.<BR>









