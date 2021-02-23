'''
This module provides an ability to navigate through json object.

It has 3 functions:

1) make_json(user, friends_number, bearer_token)

Return json object of friend of given user.
user - username of Twitter user
friends_number - number of friends to show
bearer token - bearer token which twitter users with
    developer accounts havew

2) navigate(obj, depth = 0)

The function that do all navigation through json object.

3) main()

Main function. It starts the whole program of navigation
'''
import requests


def make_json(user, friends_number, bearer_token):
    '''
    Return json object of friend of given user.
    user - username of Twitter user
    friends_number - number of friends to get
    bearer token - bearer token which twitter users with
     developer accounts havew
    '''
    base_url = "https://api.twitter.com/"
    search_url = f"{base_url}1.1/friends/list.json"
    search_headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    search_params = {
        'screen_name': user,
        'count': friends_number
    }
    response = requests.get(search_url, headers=search_headers,\
                            params=search_params)
    json_response = response.json()
    return json_response


def navigate(obj, depth = 0):
    '''
    The function that do all navigation through json object.
    '''
    while True:
        if isinstance(obj, dict):
            if depth != 0:
                print("This is dictionary. Enter a key index \
from list below or -1 to return back, -2 to end a program: ")
            else:
                print("This is dictionary. Enter a key index \
from list below or -2 to end a program: ")
            keys = list(obj.keys())
            for i in range(len(keys)):
                if i == len(keys) - 1:
                    print(f'{i}) {keys[i]}')
                    break
                print(f'{i}) {keys[i]}   ', end='')
            ind = int(input('Key index: '))
            if ind == -2:
                print("Do you want to end a program?")
                print("0) Yes   1) No")
                if int(input("Choose an option: ")) == 0:
                    return 0
            elif ind == -1:
                return 1
            else:
                if not navigate(obj[keys[ind]], 1):
                    return 0
        elif isinstance(obj, list):
            print("This is list. Do you want to display the entire list?")
            print("0) Yes   1) No")
            display = int(input('Choose an option: '))
            if display == 1:
                pass
            else:
                for i in range(len(obj)):
                    if i == len(obj) - 1:
                        print(f'{i}) {obj[i]}')
                        break
                    print(f'{i}) {obj[i]}   ', end='')
            print(f'Enter an index in range from 0 to {len(obj)-1} or -1 \
to return back, -2 to end a program')
            ind = int(input("Enter an index: "))
            if ind == -2:
                print("Do you want to end a program?")
                print("0) Yes   1) No")
                if int(input("Choose an option: ")) == 0:
                    return 0
            elif ind == -1:
                return 1
            else:
                if not navigate(obj[ind], 1):
                    return 0
        else:
            obj_type = str(type(obj)).split('\'')[1]
            print(f'This is {obj_type}. Do you want to display it?')
            print('0) Yes   1) No')
            if int(input('Choose an option: ')) == 0:
                print('\n' ,obj, '\n')
            print('This is the end of the file.')
            print('Enter -1 to return back or -2 to end a program')
            if int(input('>>> ')) == -1:
                return 1
            return 0


def main():
    '''
    Main function. It starts the whole program of navigation
    '''
    user = input('Enter username: ')
    friend_number = int(input('Enter number of friends to get: '))
    bearer_token = input('Enter bearer token: ')
    friends_json = make_json(user, friend_number, bearer_token)
    navigate(friends_json)


if __name__ == "__main__":
    main()
