from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content) # Printing the content of html_file 

    soup = BeautifulSoup(content, 'lxml') # Specifying the content we want to scrape with the lxml parsing method
    # print(soup.prettify()) # Printing the html code in a prettier way

    courses_html_tags = soup.find_all('h5') 
    # print(courses_html_tags) # Print all the h5 tags in a list

    for course in courses_html_tags:
        print(course.text) # Printing the content of each h5 tag, that represents the course name

    