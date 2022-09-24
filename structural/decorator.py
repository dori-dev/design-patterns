class Article:
    def show(self):
        print('All Articles....')


class Login:
    def check_login(self, username, password) -> bool:
        if username == 'admin' and password == '1234':
            return True
        return False


def outer_login(func):
    def inner_login(*args, **kwargs):
        username = input('Username: ')
        password = input('Password: ')
        login = Login()
        is_login = login.check_login(username, password)
        if is_login:
            func(*args, **kwargs)
        else:
            print('Wrong Username or Password!')
    return inner_login


@outer_login
def show_all_articles():
    articles = Article()
    articles.show()


if __name__ == '__main__':
    show_all_articles()
