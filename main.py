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

    # Searching for the "Python for beginners" course then grabbing it's price
    course_cards = soup.find_all('div', class_='card') # Grab all the div's with the card class

    for course in course_cards:
        # print(course.h5)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] # Spliting by blank spaces and grabbing the last part

        # print(course_name)
        # print(course_price)
        
        print(f'{course_name} costs {course_price}') # Displaying a very nice info about each of the courses


    