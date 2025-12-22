#  Crie uma série de números
import numpy as np
import pandas as pd 

serie_numeros = pd.Series(np.random.randint(1, 100, size=10))
print("Série de Números:")
print(serie_numeros)