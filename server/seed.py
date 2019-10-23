import pandas as pd 

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
#allClimbsCSV = pd.read_csv("climbs.csv")

df = pd.read_csv("climbs.csv")

#def csv_to_db ():

    #return csv.to_sql(name='Climbs', con=db, if_exists='append')


'''DataFrame.to_sql(self, name, con, schema=None, if_exists='fail', index=True, 
    index_label=None, chunksize=None, dtype=None, method=None)[source]

Write records stored in a DataFrame to a SQL database.

Databases supported by SQLAlchemy [1] are supported. Tables can be newly created, appended to, or overwritten.

#pd.read_sql_query("select * from airlines where id=19847;", conn)'''