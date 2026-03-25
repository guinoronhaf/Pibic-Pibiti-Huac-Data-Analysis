# Análise de dados para projeto de pesquisa PIBIC-PIBITI

## Sumário

- [Recursos utilizados](#recursos-utilizados)
- [Organização de diretórios](#organização-de-diretórios)
- [Executando código](#executando-código)
- [Contribuidores](#contribuidores)

Este repositório é composto por _scripts_ Python focados em produzir dados estatísticos e gráficos relacionados ao projeto de pesquisa de título:

 - **PIBIC**: Plano de Trabalho para Concepção e Avaliação de uma Ferramenta de Inteligência Artificial para a Geração de Laudos de Citologia Oncótica.

 - **PIBITI**: Desenvolvimento de um Sistema de Geração Automática de Laudos Médicos por Reconhecimento de Voz e Processamento de Linguagem Natural.

 Tais dados compoõem os estudos realizados sobretudo durante a primeira etapa de realização do projeto, na qual foram colhidas repostas de médicos especialistas, residentes e técnicos de Radiologia do Hospital Universitário Alcides Carneiro (HUAC/UFCG).

## Recursos utilizados

Visando promover geração e análise eficientes das informações obtidas, várias bibliotecas de _Python_ foram utilizadas para promover melhor tratamento dos dados em questão, a saber:


| Biblioteca/Módulo | Modo de instalação | Tarefa desempenhada |
|----------|----------|----------|
| [pandas](https://pandas.pydata.org/) | Instalador _pip_   | Análise, tratamento e agrupamento de dados |
| [matplotlib](https://matplotlib.org/) |  Instalador _pip_   | Geração de gráficos personalizados mediante integração com _pandas_.   |
| [scipy](https://scipy.org/) |  Instalador _pip_   | Análise estatística mediante algoritmos de computação científica. |


Na definição de parâmetro menores, especialmente para geração de gráficos, a biblioteca `numpy` foi utilizada.

## Organização de diretórios

Do ponto de vista de estrutura de diretórios, a organização dos módulos e arquivos pode ser visualizada da seguinte forma:

```diff
.
└── Pibic-Pibiti-Huac-Data-Analysis
    ├── data
    │   ├── csv_files
    │   └── graphs
    ├── src
    │   ├── aux
    │   ├── plot
    │   ├── stats
    │   └── main.py
    ├── .gitignore
    ├── README.md
    └── requirements.txt
```

### Diretório `data`

Em primeiro plano, no diretório `csv_files`, estão localizados os arquivos _csv_ associados às respostas obtidas após aplicação do questionário entre os profissionais do HUAC.

Adicionalmente, o diretório `graphs` contém os gráficos gerados após obtenção, análise e tratamento dos dados.

### Diretório `src`

Os _scripts_ responsáveis pela geração dos gráficos, importação dos módulos e continuidade das métricas estatísticas estão localizados aqui.

Ademais, um arquivo `main.py` atua como inicializador da aplicação, invocando funções e módulos _python_.

### Arquivo `requirements.txt`

Durante a organização do conjunto de dependências utilizadas no processo de geração, tratamento e análise dos dados, foi utilizado um **ambiente virtual** python (popularmente conhecido como _venv_) para isolar o espaço do repositório para as dependências utilizadas.

Dessa forma, visando promover a portabilidade e manutenabilidade do código, optou-se por fixar as versões (e nomenclaturas) das dependências utilizadas em um arquivo adequado.

Nesse sentido, fixa-se dependências e versões utilizando o comando:

```bash
pip freeze > ./requirements.txt
```

E atualiza-se as mesmas a partir de:

```bash
pip install -r ./requirements.txt
```

## Executando código

Para gerar gráficos e análises estatíscas personalizadas, siga o passo a passo:

1) Clone este repositório.

```bash
git clone https://github.com/guinoronhaf/Pibic-Pibiti-Huac-Data-Analysis.git
```

2) Navegue até o diretório raiz.

```bash
cd ./Pibic-Pibiti-Huac-Data-Analysis
```

3) Crie um novo ambiente virtual e carregue-o.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4) Atualize as dependências necessárias.

```bash
pip install -r ./requirements.txt
```

5) Execute o arquivo principal.

```bash
pytho3 -m src.main
```

---

## Contribuidores

 - [Guilherme Fragoso](https://github.com/guinoronhaf)
 - [João Ventura](https://github.com/joaoneto9)

---

Repositório componente de projeto de pesquisa associado a Unidade Acadêmica de Sistemas e Computação da Universidade Federal de Campina Grande (UASC/UFCG). A orientação do projeto é do Professor Dr. [Tiago Massoni](https://github.com/tiagomassoni).
