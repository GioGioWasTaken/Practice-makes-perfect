from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
#insert input taker here, take wanted percentage as int and sort through html info
wanted_percentage=int(input('Please enter the minimum discount percentage you are willing to buy games for:'))
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(chrome_options=chrome_options) #set up webdriver, bs cannot scarpe dynmic(?) pages by itself.
url_selenium=driver.get('https://store.steampowered.com/specials')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll to the bottom so it loads everything, please attempt to make it scroll to "show more" in future versions

WebDriverWait(driver,10 ).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'salepreviewwidgets_SaleItemBrowserRow_y9MSd'))) #wait so it loads everything
html_loaded=driver.page_source #only than take the page source
soup=BeautifulSoup(html_loaded,'lxml') #use bs to sort through elements now that we have them
sales=soup.find_all('div',class_='salepreviewwidgets_SaleItemBrowserRow_y9MSd')

g=0 #will be used to determine the offset of the steam page
o=396#will be used to have something(that i can change at a given time) to match g with
def take_stats():
 for sale in sales:
     game_link=sale.find('div',class_='salepreviewwidgets_StoreSaleWidgetHalfLeft_2Va3O').find('a').get('href')
     sale_percentage=sale.find('div',class_='salepreviewwidgets_StoreSaleDiscountBox_2fpFv').text
     game_name=sale.find('div',class_='salepreviewwidgets_StoreSaleWidgetTitle_3jI46').text
     game_price=sale.find('div',class_='salepreviewwidgets_StoreOriginalPrice_1EKGZ').text
     game_price_discounted=sale.find('div',class_='salepreviewwidgets_StoreSalePriceBox_Wh0L8').text
     byepercents=['1','2','3','4','5','6','7','8','9','0']
     newlist=[]
     i = 0
     for letter in sale_percentage:
         if sale_percentage[i] in byepercents:
             newlist.append(letter)
         i=i+1
     sale_percentage=int(newlist[0]+newlist[1])
     if sale_percentage>=wanted_percentage:
      print(f' ⌜———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————⌝\n│"{game_name}" is {sale_percentage}% off. The original price is {game_price} and the current price is {game_price_discounted}│ \n│The game on Steam: {game_link}.│\n ⌞_______________________________________________________________________________________________________________________⌟\n')
def show_more1():
    global g
    show_more=driver.find_element(By.CLASS_NAME, 'saleitembrowser_ShowContentsContainer_3IRkb').find_element(By.TAG_NAME,'button')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 20).until(
     EC.presence_of_element_located((By.CLASS_NAME,'saleitembrowser_ShowContentsContainer_3IRkb')))
    show_more.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    g=g+13
    print(g)
def show_more_all():
    global o
    while g<o:
        driver.implicitly_wait(50)
        show_more1()
    else:
        take_stats()
        time.sleep(30) # check if it takes stats before redirecting
        url_selenium = driver.get(f'https://store.steampowered.com/specials?offset={g}') #an attempt to change the url to the g offset, after testing might change to {g-13}/{g+13} too tired to tell which as of now
        html_loaded = driver.page_source
        soup = BeautifulSoup(html_loaded, 'lxml')
        time.sleep(120) #testing
        o=o+396# I want the process to be repeated 10 times.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while g<3968:
 show_more_all()




