# This project pulls base stat from the Ark Wiki and
# stores it in a text file.

# Import libraries
import requests
from bs4 import BeautifulSoup
import os
import sys
import pandas as pd

# Set url to Ark Wiki Base Stats page
url = 'https://ark.gamepedia.com/Base_Creature_Statistics'

# Connect to URL
response = requests.get(url)

# Check to make sure request goes through
print(response)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Get Header information
listHeader = []
listHeader.append("Creature")
header = soup.find_all("table")[0].find_all("tr")[1].find_all("th")
for items in header:
    try:
        listHeader.append(items.get_text())
    except:
        continue

# Get data for all fields
data = []
baseStatData = soup.find_all("table")[0].find_all("tr")[2:]
for element in baseStatData:
    subData = []
    for subElement in element:
        try:
            subData.append(subElement.get_text())
        except:
            continue
    data.append(subData)

# Store data into DataFrame and convert to CSV
dataFrame = pd.DataFrame(data = data, columns = listHeader)
dataFrame.to_csv('ArkBaseStats.csv')
