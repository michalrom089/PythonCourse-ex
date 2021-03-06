import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('07_dataframes/7_1_basics/seed.csv')

    df_agg = df.groupby('externalID').agg({
        'totalAct': 'sum',
        'totalInAdh': 'mean'
    })

    print(df_agg)
