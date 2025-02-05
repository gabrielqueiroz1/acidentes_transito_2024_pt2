#%%
import pandas as pd

data = pd.read_csv("../dados/datatran2024.csv", encoding="latin-1", sep=";")

data
# %%

df = pd.DataFrame(data)
df

#%%
#converti o id para inteiro por ser uma boa prática no sentido de ocupar menos memória e desempenho
df['id'] = df['id'].astype(int)
df['id'].dtype
# %%
#convertendo para o tipo datetime
df['data_inversa'] = pd.to_datetime(df['data_inversa'])

#%%
#contando valores distintos = 659
#como temos muitos valores, vou diminuir a categoria utilizando apenas a primeira parte e generalizando
df['tracado_via'].nunique()
df['tracado_via'].value_counts()
#%%
def primeira_parte(nome_col:str):
    if nome_col[2] == ":":
        return nome_col.split(":")[0]
    else:
        return nome_col.split(";")[0]

#%%
#quero criar uma coluna apenas com as horas
df['hora_fixa'] = df['horario'].apply(primeira_parte)

#comparando os dois
df[['horario', 'hora_fixa']]

# %%

df['tracado_via'] = df['tracado_via'].apply(primeira_parte)

#%%
#contando os novos valores = 12
df['tracado_via'].nunique()
df['tracado_via'].value_counts()
