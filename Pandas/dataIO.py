import numpy as np
import pandas as pd


def incrementIter(param):
    incrementIter.i += 1
    print()
    print(str(incrementIter.i) + ' -------- ' + str(param) + ' -------- ')


incrementIter.i = 0

# 1. CSV
incrementIter('CSV')
df = pd.read_csv('example.csv')
print(df)
df.to_csv('csv_output', index=False)
print(pd.read_csv('csv_output'))

# 2. Excel
incrementIter('Excel')
df = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1', index_col=0)
print(df)
df.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')

# 3. HTML
incrementIter('HTML')
# reads data from the table tag, returns list of table
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
df2 = df[0].copy()
print(df[0])
# write to xlsx
df[0].to_excel('table.xlsx', sheet_name='Sheet1', index=0)

# 4. SQL
incrementIter('SQL')
from sqlalchemy import create_engine

cnx = create_engine('mysql+pymysql://root:@localhost:3306/notice_board').connect()
sql = 'select * from notices'
df = pd.read_sql(sql, cnx)
print(df)
df2.to_sql('delete_table', con = cnx)
