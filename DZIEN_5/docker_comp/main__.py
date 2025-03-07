import pandas as pd
import numpy as np


def funckja3():
    data = {'Kolumna1': [1, 2, 3, 4, 5], 'Kolumna2': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)
    print(df)
    arr = np.array(df['Kolumna2'])
    srednia = np.mean(arr)
    
    df['Srednia'] = srednia
    print(df)

if __name__ == '__main__':
    funckja3()
