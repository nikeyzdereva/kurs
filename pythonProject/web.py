import requests

url = input("Введите URL для получения кода состояния: ")
try:
    response = requests.get(url)
    print(f"Код состояния сайта {url}: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Ошибка при подключении к сайту: {e}")



