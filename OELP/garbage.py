def movie_data(urlofmovie):
    html_text1 = requests.get(urlofmovie, headers={'User-Agent': random.choice(user_agent_list)})
    soup1=BeautifulSoup(html_text1.text,'lxml')
    IMDb_rating=soup1.find('span','sc-bde20123-1 iZlgcd').text
    print(IMDb_rating)
    genres=soup1.find('div','ipc-chip-list--baseAlt ipc-chip-list')
    genre1=genres.find_all('a','ipc-chip ipc-chip--on-baseAlt')
    genre=[]
    for a in genre1:
        genre.append(a.text)
    print(genre)



url2='https://www.imdb.com'+url1+'reviews?ref_=tt_urv'
print(url2)
html_text2 = requests.get(url2, headers={'User-Agent': random.choice(user_agent_list)})
soup2=BeautifulSoup(html_text2.text,'lxml')
usernames=soup2.find_all('div',class_='display-name-date')
usernames=usernames[:1]
for name in usernames:
    user=name.a.get('href')
    user=user[0:17]
    url3='https://www.imdb.com/'+user+'reviews?sort=helpfulnessScore&dir=desc&ratingFilter=0'
    html_text3 = requests.get(url3, headers={'User-Agent': random.choice(user_agent_list)})
    soup3=BeautifulSoup(html_text3.text,'lxml')
    moviecontents=soup3.find_all('div',class_='lister-item-content')
    moviecontents=moviecontents[:1]
    for moviecontent in moviecontents:
        moviename=moviecontent.find('div',class_='lister-item-header').a.text
        print(moviename)
        rating=moviecontent.find('div',class_='ipl-ratings-bar')
        if rating:
            rating=moviecontent.find('div',class_='ipl-ratings-bar').text.strip()
            rating=rating.split("/")[0]
            print(rating)
        user_review=moviecontent.find('div',class_='text show-more__control')
        if user_review:
            user_review=moviecontent.find('div',class_='text show-more__control').text.strip()
            print(user_review)
        helpfulness=moviecontent.find('div',class_='actions text-muted').text.strip()
        helpfulness=list(helpfulness.split(" "))
        helpful=helpfulness[0]
        print(helpful)
        reach=helpfulness[3]
        print(reach)
        urlofmovie=moviecontent.find('div',class_='lister-item-header').a.get('href')
        urlofmovie='https://www.imdb.com'+urlofmovie
        movie_data(urlofmovie)
        print(urlofmovie)
    print(url3)