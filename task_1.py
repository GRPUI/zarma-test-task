import requests


def get_data(link: str) -> str:
    try:
        response = requests.get(link)
        return response.text
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return ''


def save_data(data: str) -> None:
    with open('data.json', 'w') as file:
        file.write(data)


if __name__ == '__main__':
    data = get_data('https://jsonplaceholder.typicode.com/posts')
    save_data(data)
