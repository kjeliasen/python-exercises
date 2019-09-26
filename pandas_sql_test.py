import pandas as pd
from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'

df = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)



print(df)