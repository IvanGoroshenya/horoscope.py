import requests
from bs4 import BeautifulSoup



def aries():
    url = f"https://horo.mail.ru/prediction/aries/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def taurus():
    url = f"https://horo.mail.ru/prediction/taurus/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def gemini():
    url = f"https://horo.mail.ru/prediction/gemini/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def cancer():
    url = f"https://horo.mail.ru/prediction/cancer/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def leo():
    url = f"https://horo.mail.ru/prediction/leo/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def virgo():
    url = f"https://horo.mail.ru/prediction/virgo/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def libra():
    url = f"https://horo.mail.ru/prediction/libra/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def scorpio():
    url = f"https://horo.mail.ru/prediction/scorpio/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def sagittarius():
    url = f"https://horo.mail.ru/prediction/sagittarius/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def capricorn():
    url = f"https://horo.mail.ru/prediction/capricorn/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def aquarius():
    url = f"https://horo.mail.ru/prediction/aquarius/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data

def pisces():
    url = f"https://horo.mail.ru/prediction/pisces/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='article__item article__item_alignment_left article__item_html').text
    return data









