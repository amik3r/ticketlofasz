from flask import Flask
from flask_restful import Api
from ticketing.resources.index import Index
from ticketing.resources.tickets import Tickets
from ticketing.common.db.database import database
from ticketing.common.config import config
import ticketing.common.setup as setup_app
from ticketing.common.decorators.dec_debug import debug


@debug
def setup_app():
    try:
        setup_app.setup_app()
        config.setup_complete = True
        config.save_config()
    except Exception as e:
        print(e)
    print(config.setup_complete)

@debug
def add_user():
    database.add_user('MIkkk', 'asdasd', 'asd@asdasd.hu', '00000000')

app = Flask(__name__)
api = Api(app)
api.add_resource(Index, '/')
api.add_resource(Tickets, '/tickets')

if __name__ == '__main__':
    config.load_config()
    add_user()
    if config.setup_complete:
        pass
    else:
        setup_app()
    app.run()