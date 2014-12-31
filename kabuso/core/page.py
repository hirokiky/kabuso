import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from core.schema import RequestPageSchema


def request_page(url):
    def return_default():
        return {
            'page_url': url,
            'title': url,
            'description': '',
            'summary_image_url': '',
        }

    try:
        res = requests.get(url, timeout=0.5)
    except RequestException:
        return return_default()

    soup = BeautifulSoup(res.text)

    og_url_soup = soup.find('meta', {'property': 'og:url'})
    if og_url_soup:
        page_url = og_url_soup['content']
    else:
        page_url = url

    og_title_soup = soup.find('meta', {'property': 'og:title'})
    if og_title_soup:
        title = og_title_soup['content']
    elif soup.title.text:
        title = soup.title.text
    else:
        title = ''

    og_description_soup = soup.find('meta', {'property': 'og:description'})
    if og_description_soup:
        description = og_description_soup['content']
    elif soup.body.text:
        description = soup.body.text[:100]
    else:
        description = ''

    og_image_soup = soup.find('meta', {'property': 'og:image'})
    if og_image_soup:
        image_url = og_image_soup['content']
    else:
        image_url = None

    schema = RequestPageSchema({
        'page_url': page_url,
        'title': title[:255],
        'summary_image_url': image_url,
        'description': description[:4095],
    })

    if not schema.is_valid():
        return return_default()

    return schema.cleaned_data
