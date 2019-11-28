import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    data = {
        'apples': [312, 2234, 32, 524],
        'date': [datetime(2019, 10, 1), datetime(2019, 10, 2), datetime(2019, 10, 3), datetime(2019, 10, 4)]
    }
    df = pd.DataFrame(data=data)
    # formatting dates
    print(df)
    print('===\nFormatting\n===')

    df['date'] = df['date'].apply(
        lambda val: val.strftime("%d-%b-%Y")
    )

    print(df)
