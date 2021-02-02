from ticketing.common.config import config
from ticketing.common.db.database import database
from ticketing.common.decorators.dec_debug import debug

@debug
def setup_app():
    if not config.setup_complete:
        try:
            with open(config.database_defaults) as f:
                database.curr.executescript(f.read())
            config.setup_complete = True
        except Exception as e:
            print(e)
        