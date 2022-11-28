import requests
import datetime 
from requests_html import HTML
import pandas as pd


year = datetime.datetime.now().year


#this is supposed to give a status of the program. another in 200> range is successful. 400> range is failure
#r.status_code

def url_to_file(url, filename="world.html", save = False): #creates a function with two arg
    r = requests.get(url) #requests used to get the url
    
    if r.status_code == 200: #if the url is gotten successfully (200  => code), then:
        
        html_text = r.text #storing all the html text
        if save: 
            with open(f"world-{year}.html", 'w', encoding='utf-8') as f: 
                f.write(html_text) #writing a new file with all the html code
        return html_text 
    return ""

url = "https://www.boxofficemojo.com/year/world/2020/"

html_text = url_to_file(url)
r_html = HTML(html=html_text) 

table_class  = ".imdb-scroll-table" #html class for table

r_table = r_html.find(table_class) #finding the html types

table_data = []
header_names = []

if len(r_table) == 1:
    #print(r_table[0].text) #gives us all the text data that is in the html class
    parsed_table = r_table[0] #1
    rows = parsed_table.find("tr") #finds the table rows
    header_row = rows[0]#assume first row is a header row
    header_cols = header_row.find('th')
   # header_names = [x.text for x in header_cols] #advanced way to write a for loop

    
    for row in rows[1:]: #loops through all the rows om this loop
       # print(row.text)
        cols = row.find("td")
        row_data = []

        for i, col in enumerate(cols):
        #    print(i,col.text,'\n\n')
            row_data.append(col.text)
        table_data.append(row_data)
#print(header_names)
#print(table_data[0])

df = pd.DataFrame(table_data, columns=header_names)
df.to_csv("cleaned_data.csv")


#now im amount to make some changes in this shit 
