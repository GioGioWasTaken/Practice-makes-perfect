from pip._internal.utils.misc import enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


wanted_percentage = int(input('Please enter the minimum discount percentage you are willing to buy games for:'))
steam_tags=["Indie", "Action", "Adventure", "Casual", "Simulation", "RPG", "Strategy", "Singleplayer", "Early Access", "Free to Play", "2D", "3D", "Atmospheric", "Story Rich", "Fantasy", "Multiplayer", "Massively Multiplayer", "Puzzle", "Colorful", "Sports", "Violent", "Pixel Graphics", "Exploration", "Cute", "First-Person", "Racing", "Nudity", "Sexual Content", "Anime", "Funny", "Combat", "Gore", "Sci-fi", "Arcade", "Shooter", "Action-Adventure", "Relaxing", "Horror", "Family Friendly", "Retro", "Open World", "Third Person", "Female Protagonist", "Platformer", "Co-op", "Survival", "Stylized", "Controller", "PvP", "Comedy", "Choices Matter", "Top-Down", "Realistic", "Difficult", "Visual Novel", "Great Soundtrack", "Old School", "FPS", "VR", "Physics", "Dark", "Character Customization", "Online Co-Op", "Cartoony", "Mystery", "PvE", "2D Platformer", "Multiple Endings", "Linear", "Psychological Horror", "Sandbox", "Tactical", "Medieval", "Magic", "Minimalist", "Space", "Futuristic", "Action RPG", "Building", "Shoot 'Em Up", "Point & Click", "Design & Illustration", "Hand-drawn", "Management", "Crafting", "Local Multiplayer", "Cartoon", "Side Scroller", "Utilities", "Procedural Generation", "Drama", "1980s", "Roguelike", "Mature", "Education", "Resource Management", "Puzzle Platformer", "Survival Horror", "Logic", "Dark Fantasy", "3D Platformer", "Choose Your Own Adventure", "Roguelite", "Turn-Based Combat", "Romance", "War", "Hack and Slash", "Turn-Based Strategy", "Zombies", "Tabletop", "Post-apocalyptic", "Emotional", "Turn-Based Tactics", "Replay Value", "Interactive Fiction", "Base Building", "Turn-Based", "Local Co-Op", "JRPG", "Dating Sim", "Hentai", "Nature", "Immersive Sim", "Hidden Object", "Surreal", "Historical", "Party-Based RPG", "1990's", "Stealth", "Narration", "Dungeon Crawler", "Walking Simulator", "Bullet Hell", "Score Attack", "Action Roguelike", "Memes", "Web Publishing", "Military", "Third-Person Shooter", "Cinematic", "Top-Down Shooter", "Aliens", "Robots", "2.5D", "Conversation", "Text-Based", "Cyberpunk", "Team-Based", "LGBTQ+", "Isometric", "Dark Humor", "NSFW", "RTS", "Fast-Paced", "Investigation", "Nonlinear", "Short", "Inventory Management", "Tutorial", "Classic", "Card Game", "Artificial Intelligence", "Animation & Modeling", "Demons", "Abstract", "Economy", "Lore-Rich", "Life Sim", "Driving", "Software", "Clicker", "Thriller", "Psychological", "Perma Death", "Strategy RPG", "Real Time Tactics", "Detective", "Arena Shooter", "Board Game", "Modern", "Movie", "4 Player Local", "Supernatural", "Flight", "Music", "RPGMaker", "Precision Platformer", "Dystopian ", "Psychedelic", "Time Management", "Loot", "Tower Defense", "Soundtrack", "City Builder", "Beautiful", "Tactical RPG", "Experimental", "Fighting", "Destruction", "Moddable", "Beat 'em up", "Metroidvania", "Souls-like", "Wargame", "Alternate History", "Comic Book", "Audio Production", "Video Production", "Level Editor", "Competitive", "Mythology", "Runner", "2D Fighter", "Crime", "Grid-Based Movement", "Parkour", "Game Development", "MMORPG", "Collectathon", "Dark Comedy", "CRPG", "Philosophical", "Class-Based", "World War II", "Idler", "Science", "Gun Customization", "Twin Stick Shooter", "Deckbuilding", "Automobile Sim", "Co-op Campaign", "Rhythm", "Space Sim", "Swordplay", "Card Battler", "Cats", "Grand Strategy", "Vehicular Combat", "Lovecraftian", "Battle Royale", "Character Action Game", "Software Training", "Dragons", "6DOF", "3D Fighter", "3D Vision", "eSports", "Blood", "America", "Noir", "Match 3", "Conspiracy", "Split Screen", "Parody ", "Capitalism", "Addictive", "Bullet Time", "Automation", "Satire", "Colony Sim", "Open World Survival Craft", "Trading", "Illuminati", "Mystery Dungeon", "Quick-Time Events", "Hero Shooter", "Time Manipulation", "Farming Sim", "Voxel", "Dynamic Narration", "Political", "Steampunk", "Gothic", "Creature Collector", "Underground", "Agriculture", "Word Game", "Mechs", "Hunting", "Mining", "Time Travel", "Martial Arts", "Looter Shooter", "Combat Racing", "Photo Editing", "Spectacle fighter", "Mouse only", "Otome", "MOBA", "Dog", "Tanks", "God Game", "Cooking", "Real-Time", "Ninja", "Pirates", "Hacking", "Cult Classic", "Politics", "Remake", "Solitaire", "Episodic", "Epic", "Asynchronous Multiplayer", "Hex Grid", "FMV", "Trading Card Game", "Cold War", "Fishing", "Vampire", "Superhero", "Assassin", "Underwater", "4X", "Faith", "Narrative", "Immersive", "Programming", "Dinosaurs", "Auto Battler", "Sokoban", "Action RTS", "Political Sim", "Heist", "Naval", "Western", "Trains", "Party Game", "Real-Time with Pause", "Party", "Minigames", "Archery", "Diplomacy", "Foreign", "Transportation", "Snow", "Kickstarter", "Naval Combat", "Dungeons & Dragons", "Mod", "Sailing", "Typing", "Sequel", "Transhumanism", "Gambling", "Touch-Friendly", "Villain Protagonist", "GameMaker", "Experience", "Music-Based Procedural Generation", "Sniper", "Mars", "Time Attack", "On-Rails Shooter", "Nostalgia", "Soccer", "Offroad", "360 Video", "World War I", "Escape Room", "Werewolves", "Football", "Horses", "Trivia", "Games Workshop", "Traditional Roguelike", "Roguelike Deckbuilder", "Documentary", "Farming", "Wholesome", "Cozy", "Gaming", "Boxing", "Silent Protagonist", "Chess", "Jet", "Spaceships", "Unforgiving", "Outbreak Sim", "Crowdfunded", "LEGO", "Golf", "Medical Sim", "Motorbike", "Spelling", "Asymmetric VR", "Rome", "Electronic Music", "Roguevania", "Submarine", "Ambient", "Bikes", "TrackIR", "Pinball", "Basketball", "Social Deduction", "Warhammer 40K", "Mini Golf", "Based On A Novel", "Skateboarding", "Vikings", "Wrestling", "Pool", "Instrumental Music", "Intentionally Awkward Controls", "Baseball", "Tennis", "Skating", "Cycling", "Motocross", "Lemmings", "Benchmark", "Bowling", "Jump Scare", "Boss Rush", "Hockey", "Hardware", "Rock Music", "Steam Machine", "8-bit Music", "Electronic", "Well-Written", "ATV", "BMX", "Snowboarding", "Skiing", "Voice Control", "Feature Film", "Job Simulator", "Musou", "Tile-Matching", "Rugby", "Reboot", "Mahjong", "Cricket", "Volleyball", "Snooker", "Shop Keeper", "Coding", "Hobby Sim"]
print(f'Please pick the steam tags you want the game to include, example: {steam_tags[1]}, if any of the tags you inputted are located in a game, it will be printed.\n') #steam tag list
tags_list=str(input('Would you like to see the full tag list? (y=yes/n=no)')) #giving the user the option to see all available tags to sort through
if tags_list=='y':
    print(steam_tags)
wanted_tags=str(input('(please seperate each tag with a comma, no spaces required.):')) #taking the wanted tags from the user
wanted_tags_list=wanted_tags.split(',')
game_tags_list=[]


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    chrome_options=chrome_options)  # set up webdriver, bs cannot scarpe dynmic(?) pages by itself.
url_selenium = driver.get('https://store.steampowered.com/specials')
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);")  # scroll to the bottom so it loads everything, please attempt to make it scroll to "show more" in future versions
print(url_selenium)
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, 'salepreviewwidgets_SaleItemBrowserRow_y9MSd')))  # wait so it loads everything
html_loaded = driver.page_source  # only than take the page source
soup = BeautifulSoup(html_loaded, 'lxml')  # use bs to sort through elements now that we have them
g = 0  # will be used to determine the offset of the steam page
o = 396  # will be used to have something(that i can change at a given time) to match g with

def take_stats():
    global sales
    WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, 'salepreviewwidgets_SaleItemBrowserRow_y9MSd')))
    sales = driver.find_elements(By.CLASS_NAME,'salepreviewwidgets_SaleItemBrowserRow_y9MSd')
    for sale in sales:
        game_link = sale.find_element(By.CLASS_NAME,'salepreviewwidgets_StoreSaleWidgetHalfLeft_2Va3O').find_element(By.TAG_NAME,'a').get_attribute('href')
        sale_percentage=sale.find_element(By.CLASS_NAME,'salepreviewwidgets_StoreSaleDiscountBox_2fpFv').text
        game_name=sale.find_element(By.CLASS_NAME,'salepreviewwidgets_StoreSaleWidgetTitle_3jI46').text
        game_price = sale.find_element(By.CLASS_NAME,'salepreviewwidgets_StoreOriginalPrice_1EKGZ').text
        game_price_discounted = sale.find_element(By.CLASS_NAME, 'salepreviewwidgets_StoreSalePriceBox_Wh0L8').text
        game_tags = sale.find_element(By.CLASS_NAME, 'salepreviewwidgets_StoreSaleWidgetTags_3OSJs').find_elements(By.TAG_NAME, 'a') #finding tags
        for game_tag in game_tags:
            global game_tags_list
            game_tags_list.append(game_tag.text)
        game_tags_list_before=list(filter(None,game_tags_list)) #removes all the '' , and creates a new variable so we can reset the core one, because for some reason all the games' tags got added to the same list??
        game_tags_list.clear() #resets the first list, the second one still has the text
        byepercents = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                       '0']  # get rid of % and - so i can compare the percent of sale_percent with the user set wanted_percentage variable.
        newlist = []
        i = 0
        for letter in sale_percentage:
            if sale_percentage[i] in byepercents:
                newlist.append(letter)
            i = i + 1
        sale_percentage = int(newlist[0] + newlist[1])
        if sale_percentage >= wanted_percentage:
            for wanted_tag in wanted_tags_list:
                if wanted_tag in game_tags_list_before:
                  print(f' ⌜———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————⌝\n│"{game_name}" is {sale_percentage}% off. The original price is {game_price} and the current price is {game_price_discounted}│ \n│The game on Steam: {game_link}.│\n The tags of the game are: {game_tags_list_before}\n ⌞_______________________________________________________________________________________________________________________⌟\n')
                  game_tags_list.clear()
                else:
                    game_tags_list.clear()
        else:
            game_tags_list.clear()


def show_more1():
    global g, sales
    show_more = driver.find_element(By.CLASS_NAME, 'saleitembrowser_ShowContentsContainer_3IRkb').find_element(
        By.TAG_NAME, 'button')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'saleitembrowser_ShowContentsContainer_3IRkb')))
    show_more.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    g = g + 13
    WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, 'salepreviewwidgets_SaleItemBrowserRow_y9MSd')))
    print(f'The approximated offset is:{g}')


def show_more_all():
    global o, html_loaded, soup, url_selenium
    while g < o:
        driver.implicitly_wait(50)
        show_more1()
    else:
        take_stats()
        url_selenium = driver.get(
            f'https://store.steampowered.com/specials?offset={g}')  # an attempt to change the url to the g offset, after testing might change to {g-13}/{g+13} too tired to tell which as of now
        html_loaded = driver.page_source
        soup = BeautifulSoup(html_loaded, 'lxml')
        o = o + 396  # I want the process to be repeated 10 times.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


while g < 3968:
    show_more_all()
