from bs4 import BeautifulSoup
import requests # Request specific information from a website

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_='clearfix job-bx wht-shd-bx') # Bring the first match of this li with this class name
# print(job)

