import requests
from bs4 import BeautifulSoup


def get_unsplash_images_from_url(url):
    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    soup = BeautifulSoup(response.content, 'html.parser')

    img_tags = soup.find_all('img', src=lambda x: x and x.startswith("https://images.unsplash.com/photo"))

    return [img['src'] for img in img_tags]


images = get_unsplash_images_from_url('https://unsplash.com/s/photos/mountains-forest?orientation=landscape&license=free' )
print(images)
print(len(images))