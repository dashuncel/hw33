import requests
import pprint

# 423982232
#   9297520

TOKEN = '35036f7d9a3921b072136088a92ef266d5af073bc599203289863b6ef63553ea26d17d4442bd59abdabd5'
params = {'access_token': TOKEN,
          'v': '5.85'
          }

def chk_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def inputId():
    while True:
        id = input('Введите id vk пользователя:')
        if not chk_int(id):
            print('Введите целочисленный id')
        else:
            break
    return id

def get_freinds(id):
    url = 'https://api.vk.com/method/friends.get'
    user_params = {'user_id': id, 'fields': 'domain'}
    user_params.update(params)
    response = requests.get(url, user_params).json()
    if response.get('error'):
        return response['error']

    return response['response']['items']


id1 = inputId()
id2 = inputId()

friend_list1 = get_freinds(id1)
friend_list2 = get_freinds(id2)

# списки айдишников:
friend_ids1 = (list(map(lambda f: f['id'], friend_list1)))
friend_ids2 = (list(map(lambda f: f['id'], friend_list2)))

# общие айдишники:
common_friends_list = list(set(friend_ids1) & set(friend_ids2))

common_friends_dict = [{'id': item['id'], 'address': 'https://vk.com/' + item['domain']} for item in friend_list1 if item['id'] in common_friends_list]
print(f'Список общих друзей {id1} и {id2}\n', common_friends_dict)








