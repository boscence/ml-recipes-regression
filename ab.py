import pandas as pd

#aa = pd.read_parquet("data/sample.parquet")
aa = pd.read_csv("data/taxi-fares.csv")
print(aa.dtypes)