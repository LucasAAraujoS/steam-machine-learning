import pandas as pd

# Arquivo csv original do dataset
nome_arquivo_original = "games.csv" 

print("Lendo o arquivo original completo...")

# Definição manual das colunas para corrigir o erro de cabeçalho do arquivo original
nomes_das_colunas = [
    'AppID', 'Name', 'Release date', 'Estimated owners', 'Peak CCU', 
    'Required age', 'Price', 'Discount', 'DLC count', 'About the game', 
    'Supported languages', 'Full audio languages', 'Reviews', 'Header image', 
    'Website', 'Support url', 'Support email', 'Windows', 'Mac', 'Linux', 
    'Metacritic score', 'Metacritic url', 'User score', 'Positive', 'Negative', 
    'Score rank', 'Achievements', 'Recommendations', 'Notes', 
    'Average playtime forever', 'Average playtime two weeks', 
    'Median playtime forever', 'Median playtime two weeks', 
    'Developers', 'Publishers', 'Categories', 'Genres', 'Tags', 
    'Screenshots', 'Movies'
]

# Leitura do arquivo completo ignorando o cabeçalho quebrado original (header=0)
df_completo = pd.read_csv(
    nome_arquivo_original, 
    names=nomes_das_colunas, 
    header=0, 
    low_memory=False
)

# Seleção das colunas de interesse
colunas_filtradas = [
    'Name', 'Release date', 'Estimated owners', 'Price', 
    'Windows', 'Mac', 'Linux', 'Positive', 'Negative', 'Achievements', 
    'Developers', 'Publishers', 'Categories', 'Genres'
]

df_reduzido = df_completo[colunas_filtradas]

# Criação do arquivo pré-processado
nome_saida = "steam_games_clean.csv"
df_reduzido.to_csv(nome_saida, index=False, sep=';')

print(f"\nProcessamento concluído com sucesso!")