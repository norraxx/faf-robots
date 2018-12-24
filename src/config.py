# -*- coding: utf-8 -*-

__all__ = ('ENVIRONMENT', 'DB_CONF')


ENVIRONMENT = "dev"

DB_CONFS = {
    'prod': {
        'host': '127.0.0.1',
        'user': 'root',
        'passwd': 'banana',
        'db': 'faf-db'
    },
    'dev': {
        'host': '127.0.0.1',
        'user': 'root',
        'passwd': 'banana',
        'db': 'faf-dump'
    }
}

DB_CONF = DB_CONFS[ENVIRONMENT]

REPLAY_DIRS = {
    'prod': "/content/faf/vault/replay_vault/",
    'dev': "/home/konstantin/var/faf-robots/replays/"
}

REPLAY_DIR = REPLAY_DIRS[ENVIRONMENT]

