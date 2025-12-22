# Valores da Apple
import pandas as pd

dicionario = pd.DataFrame({
    "empresas": ["Apple", 'Vale', 'Petrobras', 'Weg'],
    "cotacao" : [150.20, 75.40, 32.00, 58.30],
    "volume": [1000, 1200, 1100, 1300],
    
})

dicionario.columns = ['empresas', 'precos', 'volume']


valores_apple = dicionario[dicionario['empresas'] == 'Apple']

print(valores_apple)