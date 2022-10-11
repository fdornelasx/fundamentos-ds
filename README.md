# MonkeyPox Feelings
Repositório para a disciplina de fundamentos de ciência de dados que contém um projeto de coleta e análise de tweets a respeito da Varíola dos Macacos.

# Professores:
Sergio Serra                  | Jorge Zavaleta
------------------------------|--------------------------------|

[serra@pet-si.ufrrj.br](mailto:serra@pet-si.ufrrj.br) | [zavaleta@pet-si.ufrrj.br](zavaleta@pet-si.ufrrj.br)

# Tema:

MonkeyPox Feelings - Analisando sentimentos em tweets sobre a MonkeyPox

Neste trabalho coletamos mais de 6 mil tweets usando a Twitter Research API a respeito da Varíola dos Macacos (MonkeyPox) e aplicamos técnicas de ranqueamento de palavras e análise de sentimentos.

Este trabalho é o primeiro deste tema no Brasil a disponibilizar uma maneira de coletar tweets que torna possível a reprodutibilidade e continuidade da pesquisa.

# Alunos:


- Eliel Roger, Fillipe Dornelas

# Dependências


#### É necessário a instação das bibliotecas Python listadas abaixo

- pip install pandas
- pip install numpy
- pip install matplotlib
- pip install prov
- pip install mglearn
- python -m spacy download pt_core_news_lg
- pip install ntlk && nltk.download('stopwords') && nltk.download('punkt')

# Como usar


Atualmente o código está adequado para ser executado totalmente no ambiente do Google Colab, devido a facilidade de utilização e interoperabilidade.

coloque todos os arquivos em um diretório no colab chamado "MestradoPPGI/topicos-ds" (ou simplesmente edite o caminho nos dois arquivos .ipynb)

### Passos de execução:

1. Execute o arquivo <i>[MonkeyPox.ipynb](MonkeyPox.ipynb)</i> selecionando as datas que deseja coletar os tweets<br>
1.1 - Devido a limitações na API, não é possível coletar todos os tweets de uma só vez a depender do intervalo de datas.
2. Edite o arquivo <i>teste.json</i> com os tweets para colocá-los todos dentro de apenas um dicionário
3. execute o arquivo <i>[MonkeyPox-Tweets.ipynb](MonkeyPox_Tweets.ipynb)</i> para obter os resultados.


Após as etapas de preparação e execução, o resultado deverá ser 100% igual aos obtidos no artigo.

# Artigo
O artigo pode ser encontrado [neste link](MonkeyPox_Feelings___Analisando_tweets_sobre_MonkeyPox.pdf).

