from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=electrical+engineering&txtLocation=').text
soup=BeautifulSoup(html_text,"lxml")
jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
print('This list was made out of the site "timesjobs.com"')
for job in jobs:
 company_name=job.find('h3',class_="joblist-comp-name").text.replace(' ','').replace('(MoreJobs)','*Check the site for more job opportunities in this company')
 skills=job.find('span',class_="srp-skills").text.replace('  ,',',')
 date_published=job.find('span',class_="sim-posted").span.text
 more_info=job.header.h2.a['href']
 if 'few' in date_published:
     print(f'''Company name:{company_name.strip()}\nRequired skills:{skills.strip()}\nThis job offer was posted recently\nrMore info:{more_info}
   ''')
     print('')
