

# ## imports

import pandas as pd 
from bs4 import  BeautifulSoup
import requests as rt


# ## HTTP Request
# store website in vairiable
website='https://www.coingecko.com/en'
response= rt.get(website)
response.status_code
soup= BeautifulSoup(response.content,'html.parser') 
results= soup.find('table',{'class':'table-scrollable'}).find('tbody').find_all('tr')
len(result)
# ##target Necessary data
# Name
# Price
# 1h Change
# 24h change
# 7d Change
# 24h volume
# supply

# name
result[0].find('a',{'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()
# price
result[0].find('td',{'class':'td-price'}).get_text().strip()
#1h Change
result[0].find('td',{'class':'td-change1h'}).get_text().strip()
# 24h change
result[0].find('td',{'class':'td-change24h'}).get_text().strip()
# 7d change
result[0].find('td',{'class':'td-change7d'}).get_text().strip()
# 24h volume
result[0].find('td',{'class':'td-liquidity_score'}).get_text().strip()
# market capture
result[0].find('td',{'class':'td-market_cap'}).get_text().strip()
# # put everything inside the loops
# empty list
Name = []
Price= []
Change_1h= []
change_24h= []
change_7d= []
volume_24h= []
market_capture= []

for result in results:
    #nmae
    try:
        Name.append(result.find('a',{'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    except:
        Name.append('n/a')
    #price
    try:
        Price.append(result.find('td',{'class':'td-price'}).get_text().strip())
    except:
        Price.append('n/a')

    #Change_1h
    try:
        Change_1h.append(result.find('td',{'class':'td-change1h'}).get_text().strip())
    except:
        Change_1h.append('n/a')

    #change_24h
    try:
        change_24h.append(result.find('td',{'class':'td-change24h'}).get_text().strip())
    except:
        change_24h.append('n/a')

    # change_7d
    try:
        change_7d.append(result.find('td',{'class':'td-change7d'}).get_text().strip())
    except:
        change_7d.append('n/a')
        
    # volume_24h
    try:
        volume_24h.append(result.find('td',{'class':'td-liquidity_score'}).get_text().strip())
    except:
        volume_24h.append('n/a')

     # Market_Capture
    try:
        market_capture.append(result.find('td',{'class':'td-market_cap'}).get_text().strip())
    except:
        market_capture.append('n/a')



# # Create pandas dataframe
crypto_df=pd.DataFrame({'coin':Name ,'price':Price, "Change_1h":Change_1h, "change_24h":change_24h ,
            'change_7d':change_7d , 'volume_24h':volume_24h , ' market_capture': market_capture})
crypto_df
# # Part-2 pagination -Get 1000 Results
Name = []
Price= []
Change_1h= []
change_24h= []
change_7d= []
volume_24h= []
market_capture= []

for i in range(1,87):
    #website
    website='https://www.coingecko.com/en?page='+str(i)
    response= rt.get(website)
    soup= BeautifulSoup(response.content,'html.parser') 
    for result in results:
        #nmae
        try:
            Name.append(result.find('a',{'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
        except:
            Name.append('n/a')
        #price
        try:
            Price.append(result.find('td',{'class':'td-price'}).get_text().strip())
        except:
            Price.append('n/a')

        #Change_1h
        try:
            Change_1h.append(result.find('td',{'class':'td-change1h'}).get_text().strip())
        except:
            Change_1h.append('n/a')

        #change_24h
        try:
            change_24h.append(result.find('td',{'class':'td-change24h'}).get_text().strip())
        except:
            change_24h.append('n/a')

        # change_7d
        try:
            change_7d.append(result.find('td',{'class':'td-change7d'}).get_text().strip())
        except:
            change_7d.append('n/a')

        # volume_24h
        try:
            volume_24h.append(result.find('td',{'class':'td-liquidity_score'}).get_text().strip())
        except:
            volume_24h.append('n/a')

         # Market_Capture
        try:
            market_capture.append(result.find('td',{'class':'td-market_cap'}).get_text().strip())
        except:
            market_capture.append('n/a')


crypto_df=pd.DataFrame({'coin':Name ,'price':Price, "Change_1h":Change_1h, "change_24h":change_24h ,
            'change_7d':change_7d , 'volume_24h':volume_24h , ' market_capture': market_capture})
print(crypto_df)


# #  output in Excel
crypto_df.to_excel('crypto_data.xlsx',index=False)




