import pandas as pd 

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("climbs.csv")


#pd.read_sql_query("select * from airlines where id=19847;", conn)