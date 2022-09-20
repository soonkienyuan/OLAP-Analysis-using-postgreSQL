import pandas as pd
import os
dataset_rel_pth = ".\\data"
csv_file_nm_li = os.listdir(dataset_rel_pth)
rm_file_ext = lambda nm: nm.split('.')[0].replace(".csv", "")

dfs = {file_nm:pd.read_csv(f"{dataset_rel_pth}\\{file_nm}")
	   for file_nm in csv_file_nm_li}

for df_nm in dfs:
	# PostgreSQL doesn't like capitals or spaces
	df = dfs[df_nm]
	df.rename(lambda c: c.lower(), axis = 'columns',inplace=True)


# loading dfs to psql
from sqlalchemy import create_engine

psql_usr_nm = 'postgres'
psswrd = 'humanright'
host_nm = 'localhost'
db_nm = 'dota2_db'

engine = create_engine(f'postgresql://postgres:{psswrd}@{host_nm}:5432/{db_nm}')


for df_nm in dfs:
	print(df_nm)
	df = dfs[df_nm]
	df.to_sql(df_nm, engine, if_exists='replace') # it is a slow process
	