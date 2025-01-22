# import pandas as pd
# from pandas import Series

# data = {
# 	'Name' : ['Mercedes', 'BMW', 'Porshe', 'Wolkswagen', 'Toyota'],
# 	'Model' : ['Merin black', 'BMW X3', 'Razor 4', 'Lightly xy5', 'Jeps12'],
# 	'Year' : ['2023', '2024', '2020', '2021', '2019'],
# 	'Price' : [12000, 34000, 43000, 31000, 26500],
# 	'Speed' : ['220 km/s','250 km/s','320 km/s','240 km/s','200 km/s',]
# }


# df=pd.DataFrame(data)

# print(df['Name'])

# def convert_speed_to_int(speed_column):
#     return speed_column.str.extract('(\\d+)').astype(int)




# a = input('Birinchi avtomobil nomini kiriting: ')
# b = input('Ikkinchi avtomobil nomini kiriting: ')


# if a in df['Name'].values:
# 	print(df[df['Name'] == a])
# else:
# 	print("Bunday avtomobil yo'q !")


# df['Speed'] = convert_speed_to_int(df['Speed'])


import numpy as np

arr1 = np.arange(0, 11, 3)

print(arr1)

np1 = np.random.randint(80,size=100)
print(np1)

npsort = np.sort(np1)

print(npsort)

np2 = np.where(npsort == 44)

print(np2)
# print("--------------------------------")

# np3 = np.array(["Oq", "Qora", "Ko'k", "Qizil", "Yashil", "Sariq", "Och malla", "Och jigarrang"])
# print(np3)

# np4 = np.where(np3 == "Ko'k")

# print(np4)
# print(np4[0])

# print('----------------------------')

# npsort = np.sort(np3)

# print(npsort)

# filtered = [item for item in np3 if item.startswith("O")]
# print(filtered)

import random
import string
import numpy as np
from faker import Faker

# Tasodifiy so'z yaratish
def random_word(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# 5 ta tasodifiy so'z yaratish
words = [random_word(8) for _ in range(20)]
print(words)

np1 = np.sort(words)

print(np1)
fk = Faker()
matn = [fk.word() for _ in range(20)]

print(matn)

npbir = np.sort(matn)

print(npbir)

