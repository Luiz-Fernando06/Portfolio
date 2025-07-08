# Importação das bibliotecas necessárias
import pandas as pd
from sklearn.preprocessing import LabelEncoder               # Para transformar variáveis categóricas em numéricas

# Importando a base de dados
medico_df = pd.read_csv('/content/medico_db_atualizado.csv')

# Visualizando a primeira e a última linha do DataFrame
medico_df.head(1)
medico_df.tail(1)

# Verificando o formato (linhas e colunas)
medico_df.shape

# Informações sobre os tipos de dados e colunas
medico_df.info()

# Verificando valores nulos
medico_df.isnull().sum()

# Removendo linhas com valores nulos
medico_df = medico_df.dropna()
medico_df.shape
medico_df.isnull().sum()

# Reiniciando o índice após remoção
medico_df = medico_df.reset_index(drop=True)
medico_df.head(1)

# Visualizando a tabela após o tratamento
medico_df.head(3)

# Removendo colunas irrelevantes ou sensíveis
medico_df = medico_df.drop([
    'idcadmed', 'Idguia', 'nroguia', 'paciente', 'titular',
    'matricula', 'Senha', 'cirurgiao', 'crm_cirurgiao'
], axis=1)
medico_df.head(1)

# Convertendo colunas de data/hora para tipo datetime
medico_df.dt_cirurg = pd.to_datetime(medico_df.dt_cirurg, errors='coerce')
medico_df.data_cadastro = pd.to_datetime(medico_df.data_cadastro, errors='coerce')
medico_df.hora_inicio = pd.to_datetime(medico_df.hora_inicio, errors='coerce')
medico_df.hora_fim = pd.to_datetime(medico_df.hora_fim, errors='coerce')
medico_df.info()

# Extraindo informações úteis das datas
medico_df['ano_cirurg'] = medico_df['dt_cirurg'].dt.year
medico_df['mes_cirurg'] = medico_df['dt_cirurg'].dt.month
medico_df['dia_semana_cirurg'] = medico_df['dt_cirurg'].dt.weekday

medico_df['ano_cadastro'] = medico_df['data_cadastro'].dt.year
medico_df['mes_cadastro'] = medico_df['data_cadastro'].dt.month
medico_df['dia_semana_cadastro'] = medico_df['data_cadastro'].dt.weekday

# Extraindo apenas as horas das colunas de horário
medico_df['hora_inicio_hora'] = medico_df['hora_inicio'].dt.hour
medico_df['hora_fim_hora'] = medico_df['hora_fim'].dt.hour

# Removendo linhas que ficaram com valores nulos após conversão
medico_df = medico_df.dropna(subset=[
    'ano_cirurg', 'mes_cirurg', 'dia_semana_cirurg',
    'ano_cadastro', 'mes_cadastro', 'dia_semana_cadastro',
    'hora_inicio_hora', 'hora_fim_hora'
])

medico_df.head(5)

# Eliminando colunas de data originais, agora substituídas por colunas numéricas
medico_df = medico_df.drop(['dt_cirurg', 'data_cadastro', 'hora_inicio', 'hora_fim'], axis=1)
medico_df.head(1)

# Verificando o tipo das colunas (resta apenas 1 categórica: tipo_cirurgia)
medico_df.info()

# Convertendo a coluna categórica tipo_cirurgia para valores numéricos
modelo = LabelEncoder()
medico_df['tipo_cirurgia'] = modelo.fit_transform(medico_df['tipo_cirurgia'])
medico_df.head(10)

# Salvando o dataset tratado como um novo CSV
medico_df.to_csv('medico_db_TotalemnteTratado.csv', index=False)

# Recarregando o CSV para verificação final
medico_csv = pd.read_csv('/content/medico_db_TotalemnteTratado.csv')
medico_csv.head(1)
