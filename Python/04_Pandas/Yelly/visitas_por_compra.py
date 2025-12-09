import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados (substitua os nomes dos arquivos)
df_mkt = pd.read_csv('clientes_marketing.csv', encoding='utf-8', sep=',')
df_nao_mkt = pd.read_csv('clientes_nao_marketing.csv', encoding='utf-8', sep=',')

# 2. Criar uma coluna de identificação para segmentação
df_mkt['Segmento'] = 'Marketing'
df_nao_mkt['Segmento'] = 'Nao-Marketing'

# 3. Concatenar (juntar) os dois DataFrames em um só
df_total = pd.concat([df_mkt, df_nao_mkt], ignore_index=True)

# 4. Visualizar as primeiras linhas para confirmar o carregamento
print(df_total.head())


# Mantenha o nome da coluna original ou renomeie para simplificar:
df_total = df_total.rename(columns={'Número de sessões': 'Visitas'})

# 1. Tratar valores ausentes (NaNs) na coluna 'Visitas'
# Se houver algum cliente convertido sem número de visitas, o valor pode ser NaN.
# É seguro preencher com 0, ou remover se for um erro de exportação.
df_total['Visitas'] = df_total['Visitas'].fillna(0) 

# 2. Garantir que a coluna 'Visitas' seja do tipo inteiro
df_total['Visitas'] = df_total['Visitas'].astype(int)

# 3. Verificação (opcional):
print(df_total.info())


# Agrupar pelo 'Segmento' e calcular a média da coluna 'Visitas'
media_por_segmento = df_total.groupby('Segmento')['Visitas'].mean().round(2)

print("\n--- Média de Visitas até a Compra ---")
print(media_por_segmento)
# Exemplo de saída:
# Segmento
# Marketing        3.54
# Nao-Marketing    6.12

# Bônus: Visão estatística mais completa:
estatisticas_por_segmento = df_total.groupby('Segmento')['Visitas'].describe()

print("\n--- Estatísticas Detalhadas ---")
print(estatisticas_por_segmento)
# A coluna 'std' (desvio padrão) mostrará a dispersão (variabilidade) das visitas.



# Configuração para melhor visualização
sns.set_style("whitegrid")

# 1. Gráfico de Barras da Média de Visitas
plt.figure(figsize=(8, 5))
media_por_segmento.plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title('Média de Visitas Necessárias para Conversão por Segmento')
plt.ylabel('Média de Visitas (Sessões)')
plt.xticks(rotation=0) # Mantém os rótulos horizontais
plt.show()

# 2. Histograma da Distribuição de Visitas
# Mostra a frequência de visitas (e.g., quantos clientes converteram com 1 visita, 2, 3, etc.)
plt.figure(figsize=(10, 6))
sns.histplot(data=df_total, x='Visitas', hue='Segmento', bins=20, kde=True, palette='viridis')
plt.title('Distribuição de Visitas até a Conversão')
plt.xlabel('Número de Visitas (Sessões)')
plt.ylabel('Frequência (Contagem de Clientes)')
plt.xlim(0, df_total['Visitas'].quantile(0.95)) # Limita o eixo X para tirar outliers
plt.show()