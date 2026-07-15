# Projeto Final: Aprendizado de Máquina

Previsão de Sucesso de Jogos na Plataforma Steam

## 1. Identificação do Grupo e Dataset

### Título do Projeto: Classificação de Sucesso de Jogos Virtuais na Steam

### Integrantes:
* João Pedro Costa Cruz
* João Vitor Souza Tavares
* Lucas Antônio Araújo Santos

Fonte dos dados original: https://www.kaggle.com/datasets/fronkongames/steam-games-dataset

## 2. Descrição do Problema e Contextualização

A indústria de jogos eletrônicos consolidou-se como um dos setores de entretenimento mais lucrativos do mundo. No ecossistema de computadores, a plataforma Steam atua como a principal vitrine e canal de distribuição global para desenvolvedores independentes (indies) e grandes publicadoras (AAA).

Diante de milhares de títulos lançados anualmente, um dos maiores desafios para desenvolvedores e investidores é prever o potencial de aceitação de um jogo antes ou logo após seu lançamento. A análise preditiva baseada em atributos de mercado e estruturais do jogo ajuda a reduzir o risco financeiro e a traçar estratégias de desenvolvimento de produto mais assertivas.

Neste projeto, em vez de tratarmos o sucesso de forma puramente contínua (como faturamento bruto estimado), estabelecemos uma métrica de sucesso híbrida baseada em qualidade de recepção (crítica do público) e engajamento/visibilidade mínima (volume de reviews).

## 3. Definição Técnica da Tarefa de Aprendizado

### A. O Atributo-Alvo (Success)

O atributo-alvo, batizado como Success, é uma variável binária categórica ($Y \in \{0, 1\}$), em que:

$Y = 1$ representa um jogo de "Sucesso" (altamente aclamado pela comunidade e com relevância mínima de mercado).

$Y = 0$ representa um jogo de "Não Sucesso" (baixa aceitação ou volume de interação insignificante).

A regra de negócio que rege a criação deste atributo-alvo combina duas variáveis fundamentais do dataset: as avaliações positivas (Positive) e as avaliações negativas (Negative).

Sejam:

$R_{pos}$ o número de avaliações positivas do jogo.

$R_{neg}$ o número de avaliações negativas do jogo.

$R_{total} = R_{pos} + R_{neg}$ o volume total de avaliações obtidas.

$A = \frac{R_{pos}}{R_{total}}$ a taxa de aprovação da comunidade ($A \in [0, 1]$).

Matematicamente, a função que mapeia o sucesso do jogo $i$ é definida por:

$$Success_i = \begin{cases} 1, & \text{se } A_i \ge 0.80 \quad \text{e} \quad R_{total, i} \ge 100 \\\ 0, & \text{caso contrário} \end{cases}$$

Justificativa dos Limiares:

Taxa de Aprovação ($\ge 80\%$): Equivalente à classificação oficial "Muito Positivo" ou "Extremamente Positivo" na plataforma Steam, garantindo que o título de "Sucesso" seja reservado para jogos de excelente qualidade percebida.

Volume Mínimo ($\ge 100$ avaliações): Funciona como um filtro de relevância e significância estatística. Evita o viés de falsos positivos, como jogos recém-lançados que possuem pouquíssimas avaliações (ex: 5 avaliações, todas positivas, o que resultaria em $100\%$ de aprovação sem relevância estatística ou de mercado).

### B. Justificativa do Tipo de Tarefa: Classificação

O problema foi estruturado como uma tarefa de Classificação porque o nosso objetivo final é mapear os dados de entrada para uma decisão categórica e discreta (Sucesso vs. Não Sucesso). Isso permite que tomadores de decisão (como publicadoras de jogos) façam avaliações qualitativas e utilizem métricas de diagnóstico de erro cruciais para minimizar os riscos de investimento.

### C. Atributos Preditivos

Os atributos preditivos são as variáveis que os modelos de classificação utilizarão para aprender o comportamento de um jogo de sucesso. Foram selecionados atributos puramente intrínsecos e estruturais, evitando dados coletados após a consolidação do sucesso (evitando o vazamento de dados). São eles:

* Price (Numérico Contínuo): O valor monetário do jogo em seu lançamento. Ajuda a identificar a sensibilidade ao preço.

* Release date (Temporal): Data de publicação. Permite extrair sazonalidades (mês de lançamento, ano) e entender o impacto do tempo no mercado.

* Achievements (Numérico Inteiro): Quantidade de conquistas desbloqueáveis que o jogo oferece.

* Windows, Mac, Linux (Booleanos): Indicadores de compatibilidade com os diferentes sistemas operacionais do mercado (portabilidade).

* Developers e Publishers (Categóricos): Desenvolvedoras e publicadoras responsáveis.

* Categories (Categórico/Multi-valor): Recursos técnicos do jogo (ex: Single-player, Multi-player, Coop, Compatibilidade com Controle, Steam Cloud).

* Genres (Categórico/Multi-valor): Gêneros que caracterizam a jogabilidade (ex: Action, Adventure, Indie, RPG, Strategy).
