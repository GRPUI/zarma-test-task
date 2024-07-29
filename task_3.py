import pandas as pd
from faker import Faker


def create_data_csv() -> None:
    fake = Faker()
    data = {
        'product_id': [i for i in range(1, 101)],
        'product_name': [fake.name() for _ in range(100)],
    }
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)


def create_data_json() -> None:
    fake = Faker()
    data = {
        'product_id': [i for i in range(1, 101)],
        'sale_id': [fake.random_number() for _ in range(1, 101)],
        'amount': [fake.random_number() for _ in range(1, 101)],
    }
    df = pd.DataFrame(data)
    df.to_json('data.json', orient='records')


def get_data_csv() -> pd.DataFrame:
    data = pd.read_csv('data.csv')
    return data


def get_data_json() -> pd.DataFrame:
    data = pd.read_json('data.json')
    return data


def merge_data() -> pd.DataFrame:
    data_csv = get_data_csv()
    data_json = get_data_json()
    data = pd.merge(data_csv, data_json, on='product_id')
    return data


if __name__ == '__main__':
    create_data_csv()
    create_data_json()
    print(merge_data())

