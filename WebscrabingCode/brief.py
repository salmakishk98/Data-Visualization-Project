from requests_html import HTMLSession
session = HTMLSession()
url = session.get("https://cats.com/cat-Breeds")
url.html.render(sleep=2)

products=url.html.xpath("/html/body/div[1]/div/div/article/div/div[4]",first=True)

    
    

for product in products.absolute_links:
        url=session.get(product)
        name=url.html.find("header.entry-header",first=True).text
        data=url.html.find("div.breed-data-items",first=True).text
        # descrption=url.html.find("div.breed-about-left ",first=True).text
        #Temperament =url.html.find("div.breed-data-item-value",first=True).text
        
        print(name)
        print("\n")
        print(data)
        print("\n")
        
        
    