# INE5421

<h3 align="center">Universidade Federal de Santa Catarina</h3>
<h3 align="center">Departamento de Informática</h3>
<h3 align="center">Ciência da Computação</h3>
<h3 align="center">Florianópolis, 2019-1</h3>

<br></br>

<h2 align="center">Manipulação de Linguagens Regulares e Linguagens Livres de Contexto</h2>
<br></br>

<p align="right">Alunos: Arthur Pickcius</p>
<p align="right">Francisco Vicenzi</p>
<p align="right">João Felipe Uller</p>




### Objetivo do Trabalho

O objetivo deste trabalho é a implementação dos algoritmos relacionados a manipulaçãode Linguagens Regulares e Livres de Contexto. Tais algoritmossão úteis na implementa-ção de Geradores de Analisadores Léxicos e Sintáticos ou dospróprios analisadores.

### Definição do Trabalho

Elaborar uma aplicação, com interface gráfica para facilitar a iteração, para manipular Autômatos Finitos, Gramáticas Regulares, Expressões Regulares e Gramáticas Livres de Contexto e Autômatos de Pilha. A aplicação deve suportar:

    (a) Leitura, gravação e edição de AF, GR e ER.
    (b) Conversão de AFND (com e sem ε) para AFD.
    (✓) Conversão de AFD para GR e de GR para AFND.
    (✓) Reconhecimento de sentenças em AF.
    (e) Minimização de AFD.
    (f) União e interseção de AFD.
    (g) Conversão de ER para AFD (usando o algoritmo baseado em árvore sintática - LivroAho - seção 3.9).
    (h) Leitura, gravação e edição de GLC.
    (i) Transformação de GLC para uma GLC na forma normal de Chomsky.
    (j) Eliminação de recursão a esquerda(k) Fatoração(l) Reconhecimento de sentenças em AP (teorema GLC↔AP)

### Formato de Entrega

    Dia 02/05 - entrega da parte 1 - itens (a), (b), (c) e (d) da Definição do Trabalho
    Dia 30/05 - entrega da parte 2 - itens (e), (f), (g) e (h) da Definição do Trabalho
    Dia 20/06 - entrega da parte 3 - itens (i), (j), (k) e (l) da Definição do Trabalho


### Ferramentas utilizadas
O presente trabalho foi realizado na linguagem Python, utilizando, para a interface gráfica, a biblioteca Qt. É possível instalá-la utlizando o seguinte comando:
```
pip install PySide2
```

#### Para transformação de um objeto UI em seu codigo py
pyuic5 -o ./UI/src/<name>AUX.py  ./UI/Design/<name>.ui  #depois pega esse arquivo aux gerado e copia a definicao da janela para o arquivo correto

### Modelagem e Estrutura de Dados
O programa é orientado a objetos, em que cada modelo estudado (AF, GR, ER) consiste em uma classe. Para construir as transições e produções, utilizamos dicionários e listas.

### Utilização e exemplos
O programa apresenta interface bem intuitiva, permitindo a leitura, gravação e edição de AFs, GRs e ERs. Sendo assim, é possível manipular uma instância por vez.
<br></br>
Os exemplos apresentados foram retirados das listas de exerícios, nomeados no formato ```<L:lista_E:exercicio_T:letra>```. Para manipulação, basta carregar o arquivo desejado, disponível na pasta ``` examples ```, pelo menu ```File->Open```.

#### Autômatos Finitos
Para criar um novo automato basta ir no menu ```File->new```, e aparecerá uma janela perguntando os símbolos do alfabeto. Os símbolos devem ser inseridos separados por vírgulas E.g. ```a,b,c``` .
Os estados e transições podem ser inseridos utilizando os botões da barra lateral.

As operações de determinização e conversão podem ser encontradas no menu ```Convert```.

#### Gramáticas Regulares


#### Expressões Regulares