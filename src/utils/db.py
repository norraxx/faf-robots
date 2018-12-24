from MySQLdb import _mysql

from config import DB_CONF

__all__ = ('db_con',)


db_con = _mysql.connect(**DB_CONF)
