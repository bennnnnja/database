class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = open(db_name, "a+")

    def write(self, data): # возможность записи
        self.db_file.write(data)
        self.db_file.write("\n")

    def read_all(self): # возможность чтения
        self.db_file.seek(0)
        return self.db_file.readlines()

    def search(self, key, value): # возможность поиска
        self.db_file.seek(0)
        result = []
        for line in self.db_file:
            if key in line and value in line:
                result.append(line.strip())
        return result

    def update(self, key, value, new_data): # возможность обновления
        lines = self.read_all()
        self.db_file.seek(0)
        self.db_file.truncate(0)
        for line in lines:
            if key in line and value in line:
                line = new_data
            self.db_file.write(line)

    def delete(self, key, value): # возможность удаления
        lines = self.read_all()
        self.db_file.seek(0)
        self.db_file.truncate(0)
        for line in lines:
            if not (key in line and value in line):
                self.db_file.write(line)
