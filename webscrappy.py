from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import DataFrame,Series
url="https://www.imdb.com/chart/top"
response=requests.get(url)
soup=BeautifulSoup(response.content,"lxml")
print(soup)