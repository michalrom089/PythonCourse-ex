import pandas as pd

if __name__ == '__main__':
    data = {
        'apples': [0, 1, 2, 3],
        'oranges': ['1', '2', '3', '4']
    }

    df = pd.DataFrame(data=data)

    print(df)
