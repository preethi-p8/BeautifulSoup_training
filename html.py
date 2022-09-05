from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())  #- whole content

    tags = soup.find('h5')   #- first h5 tag

    tags = soup.find_all('h5')
    print(tags)

    for i in tags:
        print(i.text)

    course_cards = soup.find_all('div',class_='card')
    
    for i in course_cards:

        print(i)
        print(i.h5)

        course_name = i.h5.text
        course_price = i.a.text

        print(course_name)
        print(course_price)
        
        #extracting only the price

        course_name = i.h5.text
        course_price = i.a.text.split()[-1]

        # print(course_name)
        # print(course_price)

        print(f'{course_name} costs {course_price}')