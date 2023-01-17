# %%
import pandas as pd
# %%
# import data
df = pd.read_csv('Churn_Modelling.csv')
df
# %%
# Count number of people from France
french = df.loc[df['Geography'] == 'France']
len(french)
# %%
# Any other questions?

