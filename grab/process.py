from bs4 import BeautifulSoup


def find_content(data, elem, opt_class=None):
    '''Find content by optional class name.'''
    soup = BeautifulSoup(data, 'lxml')
    if opt_class:
        results = soup.find_all(elem, attrs={opt_class})
    else:
        results = soup.find_all(elem)
        for result in results:
            results.remove(result)
            results.append(BeautifulSoup.get_text(result))
    return results
