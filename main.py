import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_all_links(content, only_https=False):
    soup = BeautifulSoup(content, 'lxml')
    links = []
    for link in soup.findAll('a'):
        value = link.get('href')
        if only_https and 'https' in value:
            links.append(value)
        elif not only_https:
            links.append(value)
    return links


def get_response_attrs_dict(url):
    try:
        response = requests.get(url)
        return response.__dict__
    except Exception as e:
        raise Exception(f"Not a valid url or connection aborted.\n Detailed information: {e}")


def is_word_present_in_website(word, content):
    return word in str(content)


def do_exercise_task():
    url = input("Enter URL: ")
    search_word = input("Enter search word (or pass enter to skip it): ")

    search_option = False if search_word == '' else True

    attrs_dict = get_response_attrs_dict(url)
    attrs_dict['All links'] = scrape_all_links(content=attrs_dict['_content'], only_https=True)

    if search_option:
        attrs_dict[f'Is the website contains the word "{search_word}"'] = is_word_present_in_website(search_word,
                                                                                                     attrs_dict[
                                                                                                         '_content'])
    pd.set_option('display.max_colwidth', 80)
    df = pd.DataFrame(attrs_dict.items())
    print(df)


if __name__ == '__main__':
    do_exercise_task()
