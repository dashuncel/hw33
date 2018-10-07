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
        response = requests.get(url.format(*items), self.PARAMS).json()
        if response.get('error'):
            return response['error']
        else:
            return response['response']

    def get_mutual_friends(self, target_id):
        # target_id -  айди пользователя с кем спмотрим общих друзей
        url = 'https://api.vk.com/method/friends.getMutual?source_uid={}&target_uid={}'
        common_friends = self.__query_vk__((self.id, target_id), url)
        return common_friends

    def get_users_info(self, target_ids, info):
        # target_ids - список, айдишники пользователей
        # info - строка, допинформация, которую надо получить
        target_ids = ','.join(str(x) for x in target_ids)
        url = 'https://api.vk.com/method/users.get?user_ids={}&fields={}'
        user_info = self.__query_vk__((target_ids, info), url)
        return user_info


#ввод данных:
def check_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def input_id(text):
    while True:
        id = input(text)
        if not check_int(id):
            print('Введите целочисленный id')
        else:
            break
    return id


user1 = UserVk(input_id('Введите id vk исходного пользователя:'))
user2 = input_id('Введите id vk пользователя, с которым будем сравнивать:')
common_list = user1.get_mutual_friends(user2)
domain_list = user1.get_users_info(common_list, 'domain')

print(f'Итого:{len(domain_list)} общих друзей\n')
for usr in domain_list:
    print('https://vk.com/' + usr['domain'])

