import pandas as pd
import numpy as np

#slide 37
print("slide 37")
ser = pd.Series([2, 4, 6, 8])
print(ser)
arr_price = np.array([76.3, 23.1, 102.4])
arr_symbol = np.array(['FPT', 'ACB', 'VNM'])
ser = pd.Series(arr_price, index=arr_symbol)
print(ser)
dic = {'FPT':76.3, 'ACB':23.1, 'VNM':102.4}
ser = pd.Series(dic)
print(ser)

#slide 38
print("slide 38")
print(ser['ACB'])
print(ser[2])
print(ser[1:])
print(ser[['FPT', 'VNM']])

#slide 39
print("slide 39")
print(ser.size)
print(len(ser))
print(ser.values)
print(ser.index)
print(ser.axes)

#slide 40
print("slide 40")
dic = {'FPT':76.3, 'ACB':23.1, 'VNM':102.4,
       'AGH': 7.8, 'FLC':3.5, 'HTC':24.2}
ser = pd.Series(dic)
print(ser)
print(ser.head(3))
print(ser.tail(2))

#slide 41
print("slide 41")
print(ser.mean())
print(ser.std())
print(ser.describe())

#slide 42
print("slide 42")
ser['FPT'] = 81
ser[2] = 106
print(ser)

#slide 43
print("slide 43")
print(ser.drop(ser.index[[0, 2]]))
print(ser.drop(['FLC', 'AGH']))

#slide 44
print("slide 44")
print(ser + 2)
print(ser.map(lambda x:x*2))

#slide 45
print("slide 45")
list_sample = [['PNJ', 180.1, 182], ['VIB', 22.3, 21.2], ['VIC', 46.2, 45.6], ['VNM', 150, 146.1]]
df = pd.DataFrame(list_sample, columns=['Symbol', 'Open', 'Close'])
print(df)