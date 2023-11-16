import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

un_val = data['whoAmI'].unique()
one_hot = pd.DataFrame()

for value in un_val:
    one_hot[value] = (data['whoAmI'] == value).astype(int)
print(one_hot)