import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    data = {
        'apples': [312, 2234, 32, 524],
        'date': [datetime(2019, 10, 1), datetime(2019, 10, 2), datetime(2019, 10, 3), datetime(2019, 10, 4)]
    }
    df = pd.DataFrame(data=data)

    print("===\naxis=0\n===")

    df.apply(
        lambda val: print(val.max()), axis=0
    )

    print("===\naxis=1\n===")

    df.apply(
        lambda val: print(f"apples: {val['apples']} | date: {val['date']}"), axis=1
    )
