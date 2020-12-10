from bs4 import BeautifulSoup
import requests # Request specific information from a website

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx') # Bring the first match of this li with this class name
# print(jobs)

# printing all the first page jobs (the title, job name)
for job in jobs:
    published_date = job.find('span', class_='sim-posted').text

    # Only show jobs posted a few days ago
    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        job_key_skills = job.find('span', class_='srp-skills').text.replace(' ', '')

        # Printing the beautiful and formatted info about each job on the first page
        print(f'''
        Company name: {company_name}
        Required skills: {job_key_skills}
        ''')


