import json
from ticketing.common.decorators.dec_debug import debug
#config_file = json.loads('config.json')

class Config:
    @debug
    def __init__(self):
        self.database_location = '/home/miki/dev/ticketing/database/ticketing.db'
        self.database_directory = '/home/miki/dev/ticketing/database/'
        self.database_init_file = '/home/miki/dev/ticketing/database/init.sql'
        self.database_defaults = '/home/miki/dev/ticketing/database/default.sql'
        self.adminuser = 'miki'
        self.admin_password = '263b24b397a06a3f727f1e75b44970d9d1f3e9b7d113f115b2531f361fe1da6d426bb0c7283be6d07e81060206de4697d8b6f675dae1eb7acd6fc936493f48fd0d85d0b062711eeb2ab2df55f374590fff25726d510eabd3b11d0d724a9c5b81'
        self.setup_complete = False

    @debug
    def save_config(self):
        payload = json.dumps(config.__dict__, indent=4)
        with open('/home/miki/dev/ticketing/config.json', 'w') as f:
            f.write(payload)

    @debug
    def load_config(self):
        try:
            payload = ''
            with open('/home/miki/dev/ticketing/config.json', 'r') as f:
                payload = json.load(f)
            for k in payload:
                for kk in self.__dict__:
                    if k == kk:
                        self.__dict__[k] = payload[kk]
        except Exception as e:
            pass


config = Config()