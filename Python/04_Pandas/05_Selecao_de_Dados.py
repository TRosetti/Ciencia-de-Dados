import pandas as pd 

df_cambio = pd.DataFrame({
        "moeda": ['dolar/real', 'libra/real'] * 4,
        "price": [5.24,  4.15, 5.26, 4.23, 5.55, 4.02, 5.76, 3.98],
        "derivativo": list(["DOLFT3", "LIBFT3"]) * 4    
    },
    index=sorted(list(pd.date_range('1/5/2014', periods=4)) * 2)
)

print(df_cambio) 
