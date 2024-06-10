import pandas as pd

from SubjectStatistics.models.datascience import subject_data
from SubjectStatistics.models.datascience import student_data


class File(object):
    # ファイルの保存場所
    directory_path = r"C:\Users\User\PycharmProjects\GraduationResearch\CsvFiles\\"
    file_name = "履修成績データ2021.csv"
    file_path = directory_path + file_name

    def __init__(self):
        self.filepath = File.file_path
        self.df = None


class ReadFile(File):
    def __init__(self):
        super().__init__()
        self.content = None

    # ファイルの読み込み
    def read(self):
        with open(self.filepath, 'r', encoding="utf-8") as file:
            self.content = file.read()
        return self.content

    # df を取得するメソッド
    def get_df(self):
        if self.df is None:
            self.read()
            self.df = pd.read_csv(self.filepath)
        return self.df

    def display_file(self):
        print("CSVファイルを表示します。")
        df = self.get_df()
        print(df.head())


class ProcessingFile(File):
    def __init__(self):
        super().__init__()
        self.reader = ReadFile()

    def show_operation(self):
        if input_operation():
            print("科目が選択されました。")
            df = self.reader.get_df()
            subject_data(df)
        else:
            print("学生が選択されました。")
            df = self.reader.get_df()
            student_data(df)


class WriteFile(File):
    pass


# 操作の入力の関数
def input_operation():
    while True:
        choice = input("科目ごとに分けるなら'1'\n学生ごとに分けるなら'2'\n入力: ").lower()
        if choice in ["1", "１"]:

            return True
        elif choice in ["2", "２"]:
            return False
        else:
            pass
