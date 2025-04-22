import json

# ========================

class RegisterMixin:
    def register(self, name, password, id):
        with open('user.json', 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == name:
                print('Такой юзер уже существует!')
                return
        data.append({
            "id": id,
            "name": name,
            "password": password
        })
        with open('user.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print('Successfully registered')


class LoginMixin:
    def login(self, name, password):
        with open('user.json', 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == name:
                if n['password'] == password:
                    print('Вы успешно залогинились!')
                else:
                    print("Неверный пароль!")
                return
        print('Нет такого юзера в БД')


class ChangePasswordMixin:
    def change_password(self, name, old_password, new_password):
        with open('user.json', 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == name:
                if n['password'] == old_password:
                    n['password'] = new_password
                    print('Password changed successfully!')
                else:
                    print('Старый пароль введен не верно!')
                break
        else:
            print('Нет такого юзера в БД')
            return
        with open('user.json', 'w') as file:
            json.dump(data, file, indent=4)


class ChangeUsernameMixin:
    def change_name(self, old_name, new_name):
        with open('user.json', 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == old_name:
                n['name'] = new_name
                print('Имя успешно изменено!')
                break
        else:
            print('Нет такого юзера в БД')
            return
        with open('user.json', 'w') as file:
            json.dump(data, file, indent=4)


class CheckOwnerMixin:
    def check(self, owner):
        with open("user.json", 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == owner:
                return
        print('Нет такого пользователя!')

# ========================

class User(RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin):
    count = 0

    def __init__(self):
        User.count += 1

    def register(self, name, password):
        self.valitade_password(password)
        return super().register(name, password, User.count)

    def login(self, name, password):
        return super().login(name, password)

    def change_password(self, name, old_password, new_password):
        self.valitade_password(new_password)
        return super().change_password(name, old_password, new_password)

    def change_name(self, old_name, new_name):
        return super().change_name(old_name, new_name)

    @classmethod
    def incounter(cls):
        cls.count += 1

    def valitade_password(self, password):
        if len(password) < 8:
            raise ValueError('Пароль слишком короткий!')
        if not any(i.isdigit() for i in password):
            raise KeyError('Пароль должен состоять из букв и цифр!')
        if not any(i.isalpha() for i in password):
            raise KeyError('Пароль должен состоять из букв и цифр!')

class Post(CheckOwnerMixin):
    def __init__(self, title, description, price, quantity, owner):
        self.check(owner)
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = owner

obj1 = User()
obj1.register('jonh', 'dfwfw211')
obj2 = User()
obj2.register('rick', 'dwfewfwe2')
obj3 = User()
obj3.register('sam', 'wfwefwe43')