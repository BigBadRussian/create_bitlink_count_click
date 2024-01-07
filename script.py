import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlsplit


def create_short_link(long_url, token):
    url = 'https://api-ssl.bitly.com'
    address = "/v4/shorten"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"long_url": long_url}
    response = requests.post(f"{url}{address}", headers=headers, json=payload)
    response.raise_for_status()
    short_link = response.json()['link']
    return short_link


def count_clicks(token, link):
    url = 'https://api-ssl.bitly.com'
    address = "/v4/bitlinks/"
    bitlink_par = "/clicks/summary"
    bitlink = urlsplit(link)
    headers = {"Authorization": f"Bearer {token}"}
    params = {"unit": "day", "units": "-1"}
    response = requests.get(f"{url}{address}{bitlink.netloc}{bitlink.path}{bitlink_par}",
                            headers=headers, params=params)
    response.raise_for_status()
    return f"Всего кликов за всё время: {response.json()['total_clicks']}"


def check_bitlink(token, link_to_check):
    url = 'https://api-ssl.bitly.com'
    link_to_check = urlsplit(link_to_check)
    address = "/v4/bitlinks/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{url}{address}{link_to_check.netloc}{link_to_check.path}", headers=headers)
    return response.ok


def main():
    load_dotenv()
    token_bitly = os.getenv("TOKEN_BITLY")
    link_to_check = input("Введите ссылку: \n")
    if check_bitlink(link_to_check=link_to_check, token=token_bitly):
        try:
            print(count_clicks(token, link=link_to_check))
        except requests.exceptions.HTTPError as error:
            exit(print(error))
    else:
        try:
            print(f"Ваш битлинк:{create_short_link(long_url=link_to_check, token=token_bitly)}")
        except requests.exceptions.HTTPError as error:
            exit(print(error))


if __name__ == "__main__":
    main()
