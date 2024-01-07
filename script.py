import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlsplit


def create_short_link(long_url, token, url):
    address = "/v4/shorten"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"long_url": f"{long_url}",
               "domain": "bit.ly"}
    response = requests.post(f"{url}{address}", headers=headers, json=payload)
    response.raise_for_status()
    short_link = response.json()['link']
    return short_link


def count_clicks(token, url, link):
    address = "/v4/bitlinks/"
    end_point = "/clicks/summary"
    bitlink = urlsplit(link)
    headers = {"Authorization": f"Bearer {token}", "unit": "day", "units": "-1"}
    response = requests.get(f"{url}{address}{bitlink[1]}{bitlink[2]}{end_point}", headers=headers)
    response.raise_for_status()
    return f"Всего кликов за день: {response.json()['total_clicks']}"


def check_bitlink(token, url, link_to_check):
    end_point = urlsplit(link_to_check)
    address = "/v4/bitlinks/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{url}{address}{end_point[1]}{end_point[2]}", headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    url = 'https://api-ssl.bitly.com'
    link_to_check = input("Введите ссылку: \n")
    if check_bitlink(link_to_check=link_to_check, token=token, url=url):
        try:
            print(count_clicks(token, link=link_to_check, url=url))
        except requests.exceptions.HTTPError as error:
            exit(print(error))
    else:
        try:
            print(create_short_link(long_url=link_to_check, token=token, url=url))
        except requests.exceptions.HTTPError as error:
            exit(print(error))


if __name__ == "__main__":
    main()
