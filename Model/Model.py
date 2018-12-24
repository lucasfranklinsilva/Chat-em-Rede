import pymysql
import sys
sys.path.insert(0, '../')
import Global

class My_DB(object):

    __instance   = None
    __host       = None
    __user       = None
    __password   = None
    __database   = None
    __session    = None
    __connection = None

    def __init__(self, host='localhost', user='root', password='', database=''):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    ## End def __init__

    def __open(self):
        try:
            self.__connection = pymysql.connect(self.__host, self.__user, self.__password, self.__database)
            self.__session = self.__connection.cursor(pymysql.cursors.DictCursor)

        except pymysql.DatabaseError as e:
            print
            "Error %d: %s" % (e.args[0], e.args[1])

    ## End def __open

    def __close(self):
        self.__session.close()
        self.__connection.close()

    ## End def __close

    def select(self, table, where=None, sort=None, *args, **kwargs):

        query = 'SELECT '
        keys = args
        values = tuple(kwargs.values())
        l = len(keys) - 1

        for i, key in enumerate(keys):
            query += "`"+key+"`"
            if i < l:
                query += ","
        ## End for keys

        if len(keys) == 0:
            query += '* '

        query += 'FROM %s' % table

        if where:
            query += " WHERE %s" % where
        ## End if where

        if sort:
            query += " ORDER BY %s" % sort

        self.__open()

        if self.__session.execute(query, values) > 0:
            Global.print_query(query)
            result = self.__session.fetchall()
            self.__close()
            return result
        else:
            self.__close()
            return False
    ## End def select


    def insert(self, table, *args, **kwargs):
        values = None
        query = "INSERT INTO %s " % table
        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query += "(" + ",".join(["`%s`"] * len(keys)) % tuple(keys) + ") VALUES (" + ",".join(
                ["%s"] * len(values)) + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"] * len(values)) + ")"

        Global.print_query(query)

        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()
        self.__close()
        return self.__session.lastrowid
    ## End def insert

    def update(self, table, where=None, *args, **kwargs):
        query = "UPDATE %s SET " % table
        keys = kwargs.keys()
        values = tuple(kwargs.values()) + tuple(args)
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += "`" + key + "` = %s"
            if i < l:
                query += ","
            ## End if i less than 1
        ## End for keys
        query += " WHERE %s" % where

        Global.print_query(query)
        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()

        # Obtain rows affected
        update_rows = self.__session.rowcount
        self.__close()

        return update_rows
    ## End function update

    def delete(self, table, where=None, *args):
        query = "DELETE FROM %s" % table
        if where:
            query += ' WHERE %s' % where

        values = tuple(args)

        Global.print_query(query)
        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()

        # Obtain rows affected
        delete_rows = self.__session.rowcount
        self.__close()

        return delete_rows
    ## End def delete

    def select_advanced(self, sql, *args):

        od = OrderedDict(args)
        query  = sql
        values = tuple(od.values())
        Global.print_query(query)
        self.__open()
        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        result = [item for item in self.__session.fetchall()]

        self.__close()
        return result

    def sql_query(self, sql):

        query = sql

        self.__open()
        Global.print_query(query)
        self.__session.execute(query)

        result = [item for item in self.__session.fetchall()]

        self.__close()

        return result


# def main():
#     BD = My_DB('127.0.0.1', 'lufs', '1234', 'bd_teste')
#     print(BD.select('tbl', None, 'campo'))
#     #print(BD.insert('tbl',campo='lufs'))
#     #print(BD.update('tbl','id = 26', campo='LuFr'))
#     #print(BD.delete('tbl','id = 26'))
#
# main()

# Instructions
#
# >>Insert
# obj.insert('car', car_make='ford', car_model='escort', car_year='2005')
#
# >>Update
# conditional_query = 'car_make = %s'
# obj.update('car_table', conditional_query, 'nissan', car_model='escort', car_year='2005')
#
# >>Delete
# conditional_query = 'car_make = %s'
# obj.delete('car', conditional_query, 'nissan')
#
# >>Select_Advanced
# sql_query = 'SELECT C.cylinder FROM car C WHERE C.car_make = %s AND C.car_model = %s'
# obj.select_advanced(sql_query, ('car_make', 'nissan'), ('car_model', 'altima'))
#
# >>Sql_Query
# Free sql query method, can execute any sql comand


