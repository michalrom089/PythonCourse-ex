import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('07_dataframes/7_1_basics/seed.csv')

    df_agg = df.groupby('externalID').agg({
        'totalAct': 'sum',
        'totalInAdh': 'mean'
    })

    print(df_agg.iloc[1])  # index based
    print(df_agg.loc['Alexander.Keturi@staples-solutions.com'])  # label based

    df_agg.reset_index(inplace=True)

    print(df_agg.iloc[1])  # index based
    print(df_agg.loc['Alexander.Keturi@staples-solutions.com'])  # will raise an exception (index reset)
