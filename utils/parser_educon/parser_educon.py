import requests
from bs4 import BeautifulSoup as BS


def valid(login: str, password: str) -> bool:
    s = requests.session()
    auth_html = s.get("https://educon2.tyuiu.ru/login/index.php")
    auth_bs = BS(auth_html.content, "html.parser")
    token = auth_bs.select("input[name=logintoken]")[0]['value']
    url = 'https://educon2.tyuiu.ru/login/index.php'

    payload = {
        "logintoken": token,
        "returnUrl": '/',
        "username": f"{login}",
        "password": f"{password}",
        "rememberusername": 1
    }
    answ = s.post(url, data=payload)
    answ_bs = BS(answ.content, "html.parser")
    objects = answ_bs.findAll('div', class_="loginerrors")
    if objects:
        return False
    else:
        return True