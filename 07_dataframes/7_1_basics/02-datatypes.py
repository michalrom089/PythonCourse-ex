from datetime import datetime
import pandas as pd

if __name__ == '__main__':
    data = {
        'apples': [0, 1, 2, 3],
        'oranges': ['1', '2', '3', '4'],
        'date': [datetime.now()] * 4
    }

    df = pd.DataFrame(data=data)

    print(df['apples'].dtype)
    print(df['oranges'].dtype)
    print(df['date'].dtype)

    # casting
    # df['oranges'] = df['oranges'].astype(int)
    # print(df['oranges'].dtype)
