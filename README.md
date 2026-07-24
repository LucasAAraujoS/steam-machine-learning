# Classificação de Sucesso de Jogos Virtuais na Steam

## 1. Título e Objetivo do Projeto
* **Título:** Classificação de Sucesso de Jogos Virtuais na Steam
* **Objetivo:** Prever se um jogo publicado na plataforma Steam obterá sucesso de público e engajamento mínimo antes ou logo após seu lançamento, utilizando apenas atributos intrínsecos e estruturais do produto (como preço, plataformas suportadas, gêneros, categorias, número de conquistas, ano de lançamento, publicadoras e desenvolvedoras).

---

## 2. Integrantes
* João Pedro Costa Cruz
* João Vitor Souza Tavares
* Lucas Antônio Araújo Santos

---

## 3. Fonte dos Dados
**Dataset Original:** [Kaggle - Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset)

---

## 4. Tipo da Tarefa
* **Tarefa:** Classificação Binária ($Y \in \{0, 1\}$)
  * `1` = Sucesso (Taxa de Aprovação $\ge 80\%$ e $\ge 100$ avaliações no total)
  * `0` = Não Sucesso (Caso contrário)
* **Justificativa:** O problema foi estruturado como uma tarefa de classificação categórica e discreta para auxiliar a tomada de decisão (como publicadoras de jogos) em avaliações de risco, permitindo mapear taxas de falsos positivos e falsos negativos por meio de matrizes de confusão.

---

## 5. Organização dos Arquivos
```text
├── README.md                          # Documentação completa e instruções do projeto
├── dataset/
│   ├── dataset_ia.py                  # Script Python utilizado no tratamento e limpeza inicial dos dados
│   └── steam_games_clean.csv          # Base de dados tratada e filtrada utilizada nos experimentos
└── notebook/
    └── steam_machine_learning.ipynb   # Notebook principal com a análise exploratória, pré-processamento e modelos
```
* **Carregamento de Dados:** O notebook carrega o dataset diretamente a partir de uma URL pública configurada em seu código, sem depender de upload manual de arquivos locais.

---

## 6. Instruções para Abrir e Executar no Google Colab
1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Clique em **Arquivo > Abrir notebook > GitHub** (*File > Open notebook > GitHub*).
3. Insira a URL do repositório no GitHub e selecione o arquivo `steam_machine_learning.ipynb`.
4. Vá em **Ambiente de execução > Executar tudo** (*Runtime > Run all*).
5. O notebook executará todas as células de forma automatizada, carregando o dataset via web e utilizando bibliotecas nativas do Colab (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`).

---

## 7. Modelos Utilizados e Hiperparâmetros
Em conformidade com as diretrizes do capítulo de classificação, foram utilizados e otimizados via `GridSearchCV` (`cv=5`, métrica de otimização `f1_macro` devido ao desbalanceamento de ~9:1) os seguintes modelos:

* **Baseline (`DummyClassifier`):** Estratégia `most_frequent` (prevê sempre a classe majoritária `0`).
* **SGDClassifier:** Otimizado explorando combinações de `loss` (`'hinge'`, `'log_loss'`, `'modified_huber'`), `penalty` (`'l2'`, `'l1'`, `'elasticnet'`) e `alpha` (`0.0001`, `0.001`, `0.01`, `0.1`).
* **RandomForestClassifier:** Otimizado explorando combinações de `n_estimators` (`100`, `200`), `max_depth` (`10`, `20`, `None`) e `min_samples_split` (`2`, `5`).

---

## 8. Principais Resultados

### Desempenho no Conjunto de Teste (25.171 jogos)
| Modelo | Acurácia | F1-Score (Classe 0 - Não Sucesso) | F1-Score (Classe 1 - Sucesso) | F1-Macro | Modelo Escolhido |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Baseline (Dummy)** | 89,56% | 0,94 | 0,00 | 0,47 | Não |
| **SGDClassifier** | ~89,0% | ~0,94 | 0,31 | ~0,63 | Não |
| **RandomForestClassifier** | **92,1%** | **0,96** | **0,48** | **0,72** | **Sim (Final)** |

### Justificativa da Escolha e Resumo da Avaliação
* **Modelo Escolhido:** `RandomForestClassifier`.
* **Desempenho:** Apresentou o melhor F1-Score (0,48) para a classe minoritária ("Sucesso") e uma **Precisão de 71%**.
* **Pontos Fortes:** Demonstrou capacidade superior para modelar relações não-lineares complexas entre os 158 atributos preditivos.
* **Erros e Limitações:** Apresenta um volume considerável de falsos negativos (recall limitado na classe "Sucesso"), reflexo direto do forte desbalanceamento de classes do dataset original (~89,56% Não Sucesso vs ~10,44% Sucesso).

---

## 9. Divisão das Contribuições
* **Etapa preparatória (Obtenção do dataset e eliminação de dados desnecessários):** Lucas Antônio Araújo Santos
* **Etapa 1 (Análise Exploratória e Definição do Alvo):** João Pedro Costa Cruz
* **Etapa 2 (Pré-processamento e Separação dos Dados):** Lucas Antônio Araújo Santos
* **Etapa 3 (Modelagem e Validação):** João Vitor Souza Tavares
* **Etapa 4 (Avaliação e Discussão Crítica):** João Vitor Souza Tavares
* **Etapa 5 (Vídeo e Ajustes Finais no GitHub):** Todos contribuíram.

---

## 10. Link do Vídeo de Apresentação
* **Vídeo:** https://youtu.be/PAIYdE4YiXc

---

## 11. Declaração de Uso de Ferramentas de Inteligência Artificial
* **Ferramenta utilizada:** Claude (Anthropic) / ChatGPT (OpenAI).
* **Finalidade:** Apoio na estruturação sintática de trechos de código em Python/scikit-learn, formatação da documentação em Markdown e auxílio na interpretação das métricas.
* **Forma de Verificação:** Todo o código gerado, lógica de negócio, transformações do pipeline e análises críticas dos resultados foram testados, verificados e revisados manualmente pelos integrantes do grupo.
