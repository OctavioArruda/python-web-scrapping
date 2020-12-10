from bs4 import BeautifulSoup
import time
import requests # Request specific information from a website

print('Put some skill that you\'re not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx') # Bring the first match of this li with this class name
    # print(jobs)

    # printing all the first page jobs (the title, job name)
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text

        # Only show jobs posted a few days ago
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            job_key_skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            # Filtering for jobs that does not require the unfamiliar skill
            if unfamiliar_skill not in job_key_skills:
                with open(f'job-posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {job_key_skills.strip()} \n')
                    f.write(f'More info: {more_info} \n')

                print(f'File {index}.txt created.')

if __name__ == '__main__':
    while True:
        find_jobs()
        # The program runs every 10 minutes
        time_wait = 10
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)