import pandas as pd

def funkcja1():
    data = {'Kolumna1':[1,2,3,4,5],'Kolumna2':[10,20,30,40,50]}
    df = pd.DataFrame(data)
    print(df)
    
if __name__ == '__main__':
    funkcja1()
