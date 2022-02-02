import sqlite3


class DB:

    __connection = None

    def __init__(self, db_file):
        self.db_file = db_file

    @property
    def connection(self):
        if not self.__connection:
            self.__create_connection()
        return self.__connection

    def __create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            self.__connection = sqlite3.connect(self.db_file)
        except:
            print('unable to connect to db')
    
    def __close_connection(self):
        if self.__connection:
            self.__connection.close()

    def create_table(self):
        if not self.__connection:
            self.__create_connection()
        table = '''CREATE TABLE IF NOT EXISTS inventory (
            name TEXT NOT NULL,
            price TEXT,
            photo BLOB NOT NULL
        );'''
        cursor = self.__connection.cursor()
        cursor.execute(table)

    def convert_to_binary_data(self, filename):
        #Convert digital data to binary format
        with open(filename, 'rb') as file:
            data = file.read()
        return data

    def insert(self, name, price, path):
        if not self.__connection:
            self.__create_connection()
        self.create_table()
        cursor = self.__connection.cursor()
        sqlite_insert_blob_query = """INSERT INTO inventory
                                  (name, price, photo) VALUES (?, ?, ?)"""
        photo = self.convert_to_binary_data(path)
        # Convert data into tuple format
        data_tuple = (name, price, photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        self.__connection.commit()
        cursor.close()
        self.__connection.close()
        return "Inventory added successfully into a table"
