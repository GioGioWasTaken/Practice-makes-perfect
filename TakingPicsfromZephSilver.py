from bs4 import BeautifulSoup
import requests
html_text=requests.get('https://myanimelist.net/profile/ZephSilver') #image stealing source :)
session = requests.Session()
soup=BeautifulSoup(html_text.text,'html.parser')
profile_description=soup.find('div',class_='profile-about-user js-truncate-inner')
images=profile_description.find_all('img',class_='userimg') #finding the location of all images in profile desc
for image in images:
    image_source=image.parent.get('href') #looping through all the images' parents, in order to get the link attached to each image.
    if image.parent.name=='a':
        print('************************************************************************************************************') #prettifing purposes
        print(f'Image link:{image["src"]}')
        print('')
        shorturl=session.head(image_source,allow_redirects=True) #unshortens the goo.gl urls that were grabbed
        print(f'Image Source: {shorturl.url}')
        print('************************************************************************************************************')
        print('')