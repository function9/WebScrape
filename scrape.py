import requests
from bs4 import BeautifulSoup
from csv import writer
#requesting information from random blog (I had to go to the first page where they didn't use emojis)
response = requests.get('https://blog.disqus.com/page/3')
#creating the BeautifulSoup object used to parsing
soup = BeautifulSoup(response.text, 'html.parser')
#creating a list of all post items on the blog
posts = soup.find_all(class_='post-item')
#creating csv file with 3 collumns
with open('blog.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Paragraph']
    csv_writer.writerow(headers)
    #for each post find corresponding information and write it
    for post in posts:
        #finding title within the a tag
        title = post.find(class_='post-header').find('a').text
        #finding link within the href of the a tag
        link = post.find('a')['href']
        #finding post information withing the p tag
        paragraph = post.find(class_='post-body clearfix').find('p').text
        #writing to csv file
        csv_writer.writerow([title, link, paragraph])