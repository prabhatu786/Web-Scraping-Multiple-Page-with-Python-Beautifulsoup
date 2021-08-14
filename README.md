# Web-Scraping-Multiple-Page-with-Python-Beautifulsoup
 I will scrape Cryptocurrency Data. I use Python, Beautiful Soup, the Requests Library and Pandas Dataframe. The results will be stored inside an Excel File.
 
# website link:'https://www.coingecko.com/en'
 
![Screenshot 2021-08-14 180609](https://user-images.githubusercontent.com/59795901/129446689-a003ccb9-3bb4-42c1-afb8-35edabdbb043.png)

# step_1: 
## First i will imports all necessary library such as:

pandas 

BeautifulSoup

requests 

# step_2: 
## After importing all Liabrary .I will going to store website link in website vairiable
check HTTP Request
website='https://www.coingecko.com/en'
 
response= rt.get(website)
 
response.status_code
 
## If Status Code shown 200 Value That means it indicates that the request has succeeded. A 200 response is cacheable by default. The meaning of a success depends on the HTTP request method: GET : The resource has been fetched and is transmitted in the message body.
 
# step3:
## In step 3 i will make soup object . With help BeautifulSoup liabrary we can scrap all HTML Parser. Using soup object  i'm going to scrap all Necessary target data  such as give Below:
# target Necessary data
#Name

#Price

#1h Change

#24h change

#7d Change

#24h volume

#supply


# step4:

## In this step we are going to put everything inside the loops and do pagination to Get all Results from Multiple pages.

![Screenshot 2021-08-14 180838](https://user-images.githubusercontent.com/59795901/129447538-eb9b337f-470c-483c-9b2c-6462b977f62d.png)

# step5:
## Now we are going to use pandas laibrary to creat Dataframe and store all dataframe in  the excel.





