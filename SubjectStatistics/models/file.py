import pandas as pd

class File():
    pass

class ReadFile(File):
    # CSVファイルのパスを指定
    file_path = r"C:\Users\User\PycharmProjects\GraduationResearch\CsvFiles\data.csv"

    # CSVファイルをデータフレームとして読み込む
    df = pd.read_csv(file_path)

    # データフレームを表示する
    print(df)

class ProcessingFile(File):
    pass

class WriteFile(File):
    pass