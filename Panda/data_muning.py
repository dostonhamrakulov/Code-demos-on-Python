import pandas as pd
 
country= pd.read_csv("/home/doston/Downloads/datamein.csv",index_col=0)
 
country.to_html('edu.html')
