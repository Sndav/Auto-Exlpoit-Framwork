from auto_exp.lib.core.database.core import D_Mysql
from auto_exp.config.config import config
import hashlib,uuid


class D_Action:
    config = config()
    table = "data"

    def __init__(self):
        self.DB = D_Mysql(self.config.MySQL_user, self.config.MySQL_password,
                          self.config.MySQL_host, self.config.MySQL_port, self.config.MySQL_db)

    def get_id(self):
        return self.__md5(uuid.uuid1())

    def __md5(self, data):
        t = hashlib.md5("data")
        return t.hexdigest()

    def insert_data(self, taskid, data):
        taskid = self.__md5(taskid)
        data = {
            "taskid": "'" + taskid + "'",
            "data": "'" + data + "'"
        }
        self.DB.db_insert(self.table, data)

    def update_data(self, taskid, data):
        taskid = self.__md5(taskid)
        data = {"data": "'" + data + "'", }
        where = "taskid = '" + taskid + "'"
        self.DB.db_update(self.table, data, where)

    def get_data(self, taskid):
        taskid = self.__md5(taskid)
        where = "taskid = '" + taskid + "'"
        rec = self.DB.db_select(self.table, ['data'], where)
if __name__ == "__main__":
    pass
