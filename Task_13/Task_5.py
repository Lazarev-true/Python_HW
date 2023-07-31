# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта. Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
#
# Метод входа в систему – требует указать имя и id пользователя.
# Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта.
# Если в списке его нет, то вызывается исключение доступа.
# Если пользователь присутствует в списке пользователей проекта, то пользователь, который входит получает его уровень доступа и становится администратором.
#
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.

# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера

import json
from Task_4 import User
from exceptions import NotAllowedError, LevelError, AdminNotFoundError

class Project:
    def __init__(self):
        self.user_dict = {}
        self.admin = None
    
    @classmethod
    def fill_project_users(cls):
        with open('users.json', 'r', encoding='utf-8') as j:
            file = json.load(j)
            user_list = []
            for key in file:
                for user in file[key].items():
                    user_list.append(User(user[1], int(user[0]), int(key)))
            return cls.from_list(user_list)
            
    @classmethod
    def from_list(cls, user_list):
        project = cls()
        for user in user_list:
            project.user_dict[user.id_] = user
        return project
    
    def enter(self, name, id_):
        User(name, id_)
        try:
            self.admin = self.user_dict[id_]
        except KeyError:
            raise NotAllowedError(name, id_)
            
    def add_user(self, name, id_, level):
        if self.admin is None:
            raise AdminNotFoundError
        if level > self.admin.level:
            raise LevelError(level, self.admin.level)
        user = User(name, id_, level)
        self.user_dict[id_] = user
        
    def del_user(self, name, id_, level):
        if self.admin is None:
            raise AdminNotFoundError
        if level > self.admin.level:
            raise LevelError(level, self.admin.level)
        try:
            del self.user_dict[id_]
        except KeyError:
            print('Ошибка удаления! Такого пользователя  нет в списке!')
            
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        user_list = list(self.user_dict.values())
        temp = {k: {} for k in range(1, 6)}
        for user in user_list:
            temp[user.level].update({user.id_: user.name})
        with open(f'file_users.json', 'w', encoding='utf-8') as f:
            json.dump(temp, f, ensure_ascii=False, indent=4)
            
with Project.fill_project_users() as p:
    print(list(p.user_dict.values()))
    p.enter('Илья', 765)
    print(p.admin)
    