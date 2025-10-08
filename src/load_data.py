import pandas as pd

def load_iris_csv(path='../data/datasets-uci-iris.csv'):
    return pd.read_csv(path, header=None,
                       names=['sepal_length','sepal_width','petal_length','petal_width','target'])

if __name__ == "__main__":
    df = load_iris_csv()
    print(df.head())
