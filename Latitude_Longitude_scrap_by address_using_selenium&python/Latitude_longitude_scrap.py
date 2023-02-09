import re
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
df = pd.read_csv(r'C:\Users\KARTHIM\Downloads\Address.csv')
print(df.columns)
link2 = df['links2'].tolist()
Address=df['Address'].tolist()
zipcode=df['zipcode'].tolist()
state=df['state'].tolist()
result = []
for i, url in enumerate(link2):
    driver = webdriver.Chrome()
    driver.get(url)
    print(url)
    soup = driver.page_source
    if soup:
        soup = BeautifulSoup(soup, "html.parser")
    else:
        print("soup is None, skipping this iteration")
        continue
    match = re.findall(r'window\.APP_INITIALIZATION_STATE=[\s\[\d\.\,\-]+', str(soup))
    s3 = ''.join(match)
    y_cordinate=s3.split(',')[1]
    x_coordinate=s3.split(',')[2]
    print(y_cordinate)
    print(x_coordinate)
    print(match)
    result.append({

        'Address':Address[i],
        'state': state[i],
       'zipcode': zipcode[i],
       'x_coordinate': x_coordinate,
       'y_cordinate': y_cordinate
                })
    df_result = pd.DataFrame(result)
    df_result.to_csv('output.csv', index=False)
