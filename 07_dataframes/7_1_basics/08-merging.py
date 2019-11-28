import pandas as pd

if __name__ == '__main__':
    data1 = {
        'id': [1, 2, 6, 7],
        'apples': [312, 2234, 32, 524]
    }
    data2 = {
        'idx': [2, 3, 4, 6],
        'bananas': [31, 34, 122, 44]
    }

    df1 = pd.DataFrame(data=data1)
    df2 = pd.DataFrame(data=data2)

    df_merged = df1.merge(df2, left_on='id', right_on='idx')

    print(df_merged)
