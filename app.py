import csv
from bs4 import BeautifulSoup
import requests
# open the file in read mode

urls = []
with open('app/bayutblog.csv','r') as urlFile:
    csv_reader = csv.DictReader(urlFile)
    with open('app/bayutBlogcontent.csv','w') as new_file:
        fieldnsmes = ['title','description']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnsmes)
        csv_writer.writeheader()
        for line in csv_reader :
            url = line

            print(url)

            response = requests.get(url['url'])
            html = response.text
            soup = BeautifulSoup(html,'lxml')
            try:
                title = soup.find('div',class_='post_header post_header_single').h1.text

                # descriptionList = []
                descriptionList = soup.find('div',class_="entry-content blog_post_text blog_post_description clearfix").find_all('p')
                description = ""
                for p in descriptionList:
                    description += p.text

                csv_writer.writerow({
                    'title':title,
                    "description":description
                })
            except:
                print("Error***")




    

