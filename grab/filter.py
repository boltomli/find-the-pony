from bs4 import BeautifulSoup


def filter_content(data, elem, opt_class):
    soup = BeautifulSoup(data, 'lxml')
    dictionary = {}
    for e in soup.find_all(elem, attrs={opt_class}):
        if opt_class not in dictionary:
            dictionary[opt_class] = [e]
        else:
            dictionary[opt_class].append(e)
    return dictionary
