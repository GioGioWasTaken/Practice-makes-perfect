#Goal: Sort through steam sales and find all games that have 70% discound and above. Than make a txt file that contains:
# The game's link, the amount discounted, and the current price.
# Possible feature: Erase games with specific game tags, i.e. adventure, role-play, etc.
# Possible feature2: Update the list once every x minutes/hours/days.....
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
#insert input taker here, take wanted percentage as int and sort through html info
driver=webdriver.Chrome() #set up webdriver, bs cannot scarpe dynmic(?) pages by itself.
url_selenium=driver.get('https://store.steampowered.com/specials')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll to the bottom so it loads everything, please attempt to make it scroll to "show more" in future versions
WebDriverWait(driver,10 ).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'salepreviewwidgets_SaleItemBrowserRow_y9MSd'))) #wait so it loads everything
html_loaded=driver.page_source #only than take the page source
soup=BeautifulSoup(html_loaded,'lxml') #use bs to sort through elements now that we have them
sales=soup.find_all('div',class_='salepreviewwidgets_SaleItemBrowserRow_y9MSd')
for sale in sales:
    #insert press button here
    game_link=sale.find('div',class_='salepreviewwidgets_StoreSaleWidgetHalfLeft_2Va3O').find('a').get('href')
    print(f'The game on Steam: {game_link}')
    #sale_percentage
    #sale_price