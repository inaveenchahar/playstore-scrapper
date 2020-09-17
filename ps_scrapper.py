from bs4 import BeautifulSoup
import textwrap
import requests
from re import sub


while True:
    try:
        playstore_url = input("PlayStore app url or press Ctrl+C to exit: ")
        if playstore_url == '':
            break
        playstore_url = playstore_url.replace(' ', '')  # remove spaces from url

        r = requests.get(playstore_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        upper_class = soup.find('div', {'class': 'WpDbMd'})
        # Game Name
        game_name = soup.find('h1', {'class': 'AHFaub'}).text

        # Game Manufacturer Name
        manufacturer_name = soup.find('a', {'class': 'hrTbp'}).text

        # Game Genre
        genre = soup.findAll('a', {'class': 'hrTbp'})[1].text

        # Additional Information
        upper_additional = upper_class.findAll('div', {'class': 'W4P4ne'})[-1]
        middle_additional = upper_additional.findAll('div', {'class': 'hAyfc'})
        lst = []
        for abc in middle_additional[:5]:
            tags = abc.find('div', {'class': 'BgcNfc'}).text
            main_data = abc.find('span').text
            lst.append(tags + ' - ' + main_data)

        # Game Rating
        middle_class_rating = upper_class.findAll('div', {'class': 'W4P4ne'})[1]
        lower_class_rating = middle_class_rating.find('div', {'class': 'K9wGie'})
        final_rating = lower_class_rating.find('div').attrs['aria-label']

        # Game Reviews
        middle_reviews = lower_class_rating.find('span', {'class': 'EymY4b'})
        total_reviews = middle_reviews.findAll('span')[1].text

        # Game Description
        middle_class_des = upper_class.findAll('div', {'class': 'W4P4ne'})[0]
        lower_class_des = middle_class_des.find('meta').attrs['content']

        # whats new
        whats_new_upper = upper_class.findAll('div', {'class': 'W4P4ne'})[-1]
        # whats_new_final = middle_class_des.find('content').text

        # file storing
        straight_line = '-' * 100
        new_line = '\n'
        name = sub('[ :]', '-', (game_name + '.txt').lower())
        with open(name, 'w+', encoding='UTF-8') as f:
            f.write(straight_line)
            f.write(new_line)
            f.write(("Game Name - " + game_name))
            f.write(new_line)
            f.write(straight_line)
            f.write(new_line)
            f.write(("A product of - " + manufacturer_name))
            f.write(new_line)
            f.write(straight_line)
            f.write(new_line)
            f.write(("Genre - " + genre))
            f.write(new_line)
            f.write(straight_line)
            for item in lst:
                f.write(new_line)
                f.write(item)
                f.write(new_line)
                f.write(straight_line)
            f.write(new_line)
            f.write(("PlayStore Rating - " + final_rating))
            f.write(new_line)
            f.write(straight_line)
            f.write(new_line)
            f.write(("Total Review - " + total_reviews))
            f.write(new_line)
            f.write(straight_line)
            f.write(new_line)
            f.write(textwrap.fill(("Game Description - " + '\n' + lower_class_des), 100))
            f.write(new_line)
            f.write(straight_line)
            f.close()
    except requests.exceptions.MissingSchema or requests.exceptions.InvalidSchema:
        print("Enter correct playstore app url")
    except AttributeError:
        print("Make sure you have typed google play store url")