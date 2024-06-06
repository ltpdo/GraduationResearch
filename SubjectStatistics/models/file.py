import pandas as pd

class File(object):
    file_path = r"C:\Users\User\PycharmProjects\GraduationResearch\CsvFiles\data.csv"
    def __init__(self):
        self.filepath = File.file_path

class ReadFile(File):
    def __init__(self):
        super().__init__()

    def read(self):
        with open(self.filepath, 'r', encoding="utf-8") as file:
            self.content = file.read()
        return self.content

    def display_file(self):
        if self.content is None:
            self.read()
        df = pd.read_csv(self.filepath)
        print(df.head())

class ProcessingFile(File):
    pass

class WriteFile(File):
    pass