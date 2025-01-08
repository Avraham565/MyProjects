import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import random


def main():

    main_dir= input("enter dir main: ")

    initinal_url= input("enter initinal url: ")

    depth = int(input("enter depth"))
    assert depth >= 0 , "depth is not positive"

    width = int(input("enter width"))
    assert width > 0 , "width is not positive"

    crawl(main_dir,initinal_url,depth,width)

def get_Soup_by_url(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup if response.status_code == 200 else None
    

def get_image_from_soup(soup):
    num_of_photos_desired= 10
    src_images = []
    images = soup.find_all("img",class_ = 'mw-file-element')
    filtered_images = [
    img for img in images
    if int(img.get('width')) > 40 and int(img.get('height')) > 40
        ]
    for img in filtered_images:
        src_image= "https:" + img['src']
        src_images.append(src_image)
    src_images = random.sample(src_images,min(num_of_photos_desired,len(src_images)))
    return src_images

def open_folder_for_img(dir_main, soup):
    page_dir = os.path.join(dir_main,soup.find('title').text.strip())
    os.makedirs(page_dir,exist_ok=True)
    return page_dir
    
def get_links_from_soup(soup,width):
    links = soup.find_all("a", href=True)
    wikipedia_links = []
    for link in links:
        href = link['href']
        if href.startswith('/wiki/') and not ':' in href: 
            full_url = f"https://en.wikipedia.org{href}"
            wikipedia_links.append(full_url)
    wikipedia_links = random.sample(wikipedia_links,min(width,len(wikipedia_links)))
    return wikipedia_links


def save_image(src, path):
    image_name = os.path.basename(urlparse(src).path)
    path = os.path.join(path, image_name)
    img = requests.get(src).content
    with open(path, 'wb') as file:
        file.write(img)

    




def crawl( main_dir, initinal_url, depth, width, visited=None ):
    if depth == 0:
        return

    visited = set() if not visited else visited
    if initinal_url in visited:
        return
    visited.add(initinal_url)

    soup = get_Soup_by_url(initinal_url)
    if not soup:
        print(f"{initinal_url} not found")
        return
    src_images = get_image_from_soup(soup)
    page_dir = open_folder_for_img(main_dir, soup)
    for src in src_images:
        save_image(src, page_dir)

    links = get_links_from_soup(soup, width)
    for link in links:
        crawl(main_dir,link,depth-1,width,visited)



    
    





if __name__ == "__main__":
    main()