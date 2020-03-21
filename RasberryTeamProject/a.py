import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 로그파일 불러오기
df = pd.read_csv("tempHumid-2020-03-18.log",
                    names=['Datetime', 'etc'],
                    header=None, index_col='Datetime')
        
        # 인덱스를 datetimeindex로 바꾸기
df.index = pd.to_datetime(df.index)

        # etc 컬럼 나누기
df[['etc1', 'etc2', 'etc3', 'Temp', 'Humidity']] = \
        df['etc'].str.split(' ', n=5, expand=True)

        # Temp 컬럼에서 숫자만 빼오기, str->numeric
df['Temp'] = df['Temp'].str.slice(start=5, stop=-1)
df['Temp'] = df['Temp'].apply(pd.to_numeric)

# datetimeindex를 float타입으로
idx_float = mpl.dates.date2num(df.index.to_pydatetime())

# print(df['Temp'])
# xx = df.index.df['Temp']
# data_dict = {df['Temp']:idx_float}
# print(data_dict)
# a = df['Temp'].max()
# print(a)
print(df)
# print(idx_float)