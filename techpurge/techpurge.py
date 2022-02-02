import os
from .db import DB

class TechPurge:

    __db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tech_purge.db'))

    def add(self, name, price, path):
        path = os.path.abspath(os.path.expanduser(os.path.expandvars(path)))
        if not os.path.exists(path):
            raise ('Unable to add path - does not exist')
        return DB(self.__db_path).insert(name, price, path)
