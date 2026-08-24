'''
Como existe apenas 1 sensor de clima para 22 inversores 
de energia, o cruzamento pela coluna DATE_TIME 
(o comando pd.merge no script) garante que a 
temperatura e a irradiação das 14:00, por exemplo, 
sejam replicadas e associadas perfeitamente aos 22 
registros de geração de energia daquele exato minuto. 
É isso que consolida a matriz final para os cálculos 
numéricos.
'''
import pandas as pd

# 1. Leitura dos arquivos: Focando nos dados da Plant_1
df_gen = pd.read_csv('Plant_1_Generation_Data.csv')
df_weather = pd.read_csv('Plant_1_Weather_Sensor_Data.csv')

# Padronização: Convertendo a coluna DATE_TIME para datetime em ambos os DataFrames
df_gen['DATE_TIME'] = pd.to_datetime(df_gen['DATE_TIME'], format='%d-%m-%Y %H:%M')
df_weather['DATE_TIME'] = pd.to_datetime(df_weather['DATE_TIME'], format='%Y-%m-%d %H:%M:%S')

# 2. Merge: Cruzando clima e potência no mesmo instante por meio da coluna DATE_TIME
df_merged = pd.merge(df_weather, df_gen, on='DATE_TIME', how='inner')

# 3 e 4. Remova textos/datas e fixe a coluna alvo: 
# Mantendo apenas as variáveis independentes de clima e o target DC_POWER para a direita
colunas_numericas = ['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION', 'DC_POWER']

# 5. Remoção de valores nulos: Mantendo apenas as linhas com dados completos
df_final = df_merged[colunas_numericas].dropna()

# Salva o arquivo final limpo na mesma pasta
df_final.to_csv('dataset_regressao_limpo.csv', index=False)
print("Limpeza concluída! Arquivo gerado com sucesso.")
