from bs4 import BeautifulSoup


def filter_content(data, opt_class):
    soup = BeautifulSoup(data, 'lxml')
    dictionary = {}
    for table in soup.find_all('table', attrs={opt_class}):
        if opt_class not in dictionary:
            dictionary[opt_class] = [table]
        else:
            dictionary[opt_class].append(table)
    return dictionary
