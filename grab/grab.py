import requests
from bs4 import BeautifulSoup


def get_urls(url, opt_class=False):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    link_list = []
    if not opt_class:
        for link in soup.find_all('a'):
            href = link.get('href')
            if href not in link_list:
                link_list.append(href)
    else:
        for link in soup.find_all('a', attrs={opt_class}):
            href = link.get('href')
            if href not in link_list:
                link_list.append(href)
    return link_list


def get_text(url, bs=True):
    r = requests.get(url)
    data = r.text
    if not bs:
        return data
    else:
        soup = BeautifulSoup(data, 'lxml')
        return soup.get_text()


def dump_content(data, file):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(data)


def load_content(file):
    with open(file, 'r', encoding='UTF-8') as f:
        return '\n'.join(f.readlines())
