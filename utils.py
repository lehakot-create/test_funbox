import re


def url_parser(url_list: list):
    """
    Вытаскиваем доменное имя
    url_list список урлов
    :return: list
    """
    new_list = []
    for el in url_list:
        url = re.findall('([\w\-\.]+)', el)
        new_list.append(url[1] if url[0] == 'http' or url[0] == 'https' else url[0])
    return new_list
