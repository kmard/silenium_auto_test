# https://api.chucknorris.io/

import requests

url ='https://api.chucknorris.io/jokes/random'

class Test_new_joke:
    """
    create new joke
    """
    def __init__(self):
        pass

    def create_new_joke(self):
        """
        create new joke
        :return:
        """
        result = requests.get(url)
        result.encoding = 'utf-8'
        # print('state cod :'+str(result.status_code))
        if result.status_code == 200:
            print('Its all right')
        else:
            print('Error connecting')

        # assert 200 == result.status_code, 'Wrong state code'
        print(result.text)
        check = result.json()
        # check_info = check.get('categories')
        # assert check_info == [], 'error1'
        # check_info_value = check.get('value')
        # print(check_info_value)


random_joke = Test_new_joke()
random_joke.create_new_joke()

