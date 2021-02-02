from ticketing.common.config import config
import sqlite3
from ticketing.common.decorators.dec_debug import debug
import os


class Database:
    @debug
    def __init__(self):
        self.db_file = config.database_location
        self.conn = None
        self.curr = None
        self.create_connection()
        self.create_cursor()
        self.test_connection()
        self.validate_database()

    @debug
    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Exception as e:
            print(e)

    @debug
    def create_cursor(self):
        try:
            self.curr = self.conn.cursor()
        except Exception as e:
            print(e)

    @debug
    def test_connection(self):
        try:
            self.curr.execute('select id from users where username == 1;')
            res = self.curr.fetchall()
        except Exception as e:
            print(e.__dict__)

    @debug
    def validate_database(self):
        try:
            tables = ['tickets','description','short_description','work_notes','users','password']
            path = os.path.join(config.database_directory, 'validate.sql')
            for table in tables:
                res = self.curr.execute("SELECT name FROM sqlite_master WHERE type='table' and name!='sqlite_sequence';").fetchall()
            result_set = [] 
            for r in res:
                result_set.append(r[0])

            if len(result_set) == len(tables):
                for i in result_set:
                    if i in result_set:
                        for ii in tables:
                            if ii not in result_set:
                                raise NotImplementedError
                    else:
                        raise NotImplementedError
            else:
                raise NotImplementedError

        except NotImplementedError as e:
            print(f'somethings fishy with {e}')

        except Exception as e:
            print(e)
        print('database validated')
    
    @debug
    def add_user(self, name, username, email=None, roles=None):
        try:
            self.curr.execute('INSERT INTO users VALUES (?, ?, ?, ?)', name, username, email, roles)
            user = self.curr.execute('SELECT id FROM users where username=?', username).fetchone()
            print(user)
            print('useradded?????')
        except Exception as e:
            print(e)


database = Database()