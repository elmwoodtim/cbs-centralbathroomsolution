def get_resorts():
    import requests
    from bs4 import BeautifulSoup
    url = "https://www.cheapcaribbean.com/deals/vacation-packages.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    resorts = soup.find_all('div',class_="resort-result-container")
    results = list()
    for resort in resorts:
        location = resort.get('gadestination')
        url = "https://www.cheapcaribbean.com"+resort.find('a').get('href')
        description = resort.get('garesort')
        price= resort.find('span',class_='from-price').get_text().strip()[:-1]
        next_soup = BeautifulSoup(requests.get(url).content,'lxml')
        try:
            rating = next_soup.find('meta',{'itemprop':'ratingValue'}).get('content')
        except:
            rating = 'None'
        results.append((location,url,description,price,rating))
    return results
