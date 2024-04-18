from bs4 import BeautifulSoup
import requests
import random
from lxml import html
import csv
urlmain='https://www.imdb.com/search/title/?title_type=feature&release_date=2022-01-01,2023-07-31'
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
]
columns = ['Name','link', 'rating','genres','directors','popularity of director','writers','popularity of writer','cast','popularity of cast','story']
data = []
def popularity(urlforrank):
    html_text1 = requests.get(urlforrank, headers={'User-Agent': random.choice(user_agent_list)})
    soup1=BeautifulSoup(html_text1.text,'lxml')
    rank=soup1.find('span','sc-d462a8ef-6 hOuQwM starmeter-current-rank')
    if rank:
        rank=rank.text
        rank=rank.replace('Top','').strip()
        rank=rank.replace(',','')
        if rank=='See rank':
            rank=0
        rank=int(rank)
    #print(rank)
        return rank
def final_ans(url):
        #print(index)
        #index+=1
        #print(url)
        html_text = requests.get(url, headers={'User-Agent': random.choice(user_agent_list)})
        soup=BeautifulSoup(html_text.text,'lxml')
        movie=soup.find('span',class_='sc-afe43def-1 fDTGTb').text
        print(movie)
        rating=soup.find('span',class_='sc-bde20123-1 iZlgcd')
        if rating:
            rating=rating.text
            rating=int(rating.replace('.',''))/10
        else:
            rating='N/A'
        #print(rating)
        story=soup.find('span',class_='sc-466bb6c-2 eVLpWt')
        if story:
            story=story.text
        #print(story)
        genres1=soup.find('div',class_='ipc-chip-list__scroller')
        g=[]
        if genres1:
            genres=genres1.find_all('a',class_='ipc-chip ipc-chip--on-baseAlt')
            for genre in genres:
                if genre:
                    genre=genre.text
                    g.append(genre)
                    #print(genre)
        cast=soup.find_all('div',class_='sc-bfec09a1-7 dpBDvu')
        z=[]
        z1=[]
        for i in cast:
            c=i.a.text
            #print(c)
            ca=i.a.get("href")
            ca=ca[0:16]
            ca='https://www.imdb.com'+ca
            popofcast=popularity(ca)
            z1.append(popofcast)
            #print(ca)
            z.append(c)
        directors=soup.find_all('li',class_='ipc-metadata-list__item')
        directors=directors[0:1]
        x=[]
        x1=[]
        for k in directors:
            l=k.find_all('li', class_='ipc-inline-list__item')
            for m in l:
                d=m.text
                x.append(d)
                #print(d)
                da=m.a.get('href')
                da=da[0:16]
                da='https://www.imdb.com'+da
                popofdirector=popularity(da)
                x1.append(popofdirector)
                    #print(da)
        writers1=soup.find_all('li',class_='ipc-metadata-list__item')
        writers1=writers1[1:2]
        y=[]
        y1=[]
        for k in writers1:
            l=k.find_all('li', class_='ipc-inline-list__item')
            for m in l:
                w=m.text
                    #print(w)
                wa=m.a.get('href')
                y.append(w)
                wa=wa[0:16]
                wa='https://www.imdb.com'+wa
                popofwriter=popularity(wa)
                y1.append(popofwriter)
                    #print(wa)
        data.append([[movie],[url],[rating],g,x,x1,y,y1,z,z1,[story]])
###############
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.read_csv('/home/sasidharreddy/study/OELP/features.csv',delimiter='\t')

def get_link(i):
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        url = 'https://www.imdb.com/'
        driver.get(url)
        search = driver.find_element(By.ID,'suggestion-search')
        submit = driver.find_element(By.ID,'suggestion-search-button')
        search.send_keys(i)
        submit.click()
        try:
            link = driver.find_element(By.XPATH,"//a[@class='ipc-metadata-list-summary-item__t']").get_attribute('href')
            driver.get(link)
            link = link.split('?')
            link = link[0]
            driver.quit()
            return link
        except:
            driver.quit()
            return None
    except:
        driver.quit()
        return None
####
index=1
####
for i in range(50):
            ###############
    print(index)
    i=df['title'][index]
    url = get_link(i)
    final_ans(url)
    index+=1
file_name = 'example.csv'

with open(file_name, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header (column names)
    csv_writer.writerow(columns)

    # Write the data rows
    csv_writer.writerows(data)