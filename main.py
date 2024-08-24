import pandas as pd 

data  = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_3401680.csv",skiprows=4)
print(data.head(5))
print(data.columns)