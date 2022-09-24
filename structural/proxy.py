class DB:
    def work(self):
        print('You are a admin user, so you can work with database.')

    def get_all_data(self):
        print('All data...')


class Proxy:
    _admin_password = "secret_password"

    def check_admin(self, password):
        if password == self._admin_password:
            database = DB()
            database.work()
            return database
        print('You are not a admin user!')


if __name__ == '__main__':
    p = Proxy()
    database = p.check_admin('secret_password')
    database.get_all_data()
