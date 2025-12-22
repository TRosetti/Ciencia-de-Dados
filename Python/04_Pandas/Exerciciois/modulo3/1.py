# Crie um DataFrame que as colunas tenham informações ficticias de cotações, volumes e data de cada dado. Utilize pd.date_range para criar a coluna de datas

import pandas as pd

datas = pd.date_range(start="01/01/2025", end="30/04/2025", freq="ME")



dados = {
    "Apple": [150.20, 155.40, 152.00, 158.30],
    "Vale": [70.50, 72.10, 68.90, 71.00],
    "Volume": [1000, 1200, 1100, 1300]
}


dataframe = pd.DataFrame(dados, index=datas)

print(dataframe)
