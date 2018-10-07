import requests

# id для примера:
# 423982232
#   9297520

# класс "пользователь вконтакте":
class UserVk:

    def __init__(self, user_id):
        # old token:
        #'35036f7d9a3921b072136088a92ef266d5af073bc599203289863b6ef63553ea26d17d4442bd59abdabd5'

        self.PARAMS = {'access_token': '080c84a0d6ef03a2dfd8fbd7bf9f000f8dc773672135fdbd8731c3563ae4ce0ab57ab2f4165dbb2eda2c7',
                       'v': '5.85'}
        self.id = user_id

    def __query_vk__(self, items, url):
        response = requests.get(url.format(items), self.PARAMS).json()
        if response.get('error'):
            return response['error']
        else:
            return response['response']

    def get_friends(self):
        url = 'https://api.vk.com/method/friends.get?user_id={}&fields=domain'
        friend_list = self.__query_vk__(self.id, url)
        if friend_list.get('items'):
            return friend_list['items']
        elif friend_list.get('error_msg'):
            return friend_list['error_msg']
        else:
            return list()


#ввод данных:
def check_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def input_id():
    while True:
        id = input('Введите id vk пользователя:')
        if not check_int(id):
            print('Введите целочисленный id')
        else:
            break
    return id


user1 = UserVk(input_id())
user2 = UserVk(input_id())
friend_list1 = user1.get_friends()
friend_list2 = user2.get_friends()

# списки айдишников:
friend_ids1 = (list(map(lambda f: f['id'], friend_list1)))
friend_ids2 = (list(map(lambda f: f['id'], friend_list2)))

# общие айдишники:
common_friends_list = list(set(friend_ids1) & set(friend_ids2))
common_friends_dict = [{'id': item['id'], 'address': 'https://vk.com/' + item['domain']} for item in friend_list1 if item['id'] in common_friends_list]

print(f'Итого: {len(common_friends_dict)} общих друзей\n'
      f'Список общих друзей id = {user1.id} и id = {user2.id}\n', common_friends_dict)








