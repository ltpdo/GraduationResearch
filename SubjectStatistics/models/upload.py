import os.path
import tkinter as tk
from tkinter import filedialog
import shutil


class UploadFile(object):
    def __init__(self, master):
        print("CSVファイルアップローダーにCSVファイルをアップロードしてください。")
        self.master = master
        master.title("CSVファイルアップローダー")

        self.label = tk.Label(master, text="CSVファイルをアップロードしてください。")
        self.label.pack()

        self.upload_button = tk.Button(master, text="ファイルを選択", command=self.upload)
        self.upload_button.pack()

        self.upload_file_path = None

    def upload(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                if self.is_csv_file(file_path):
                    destination_folder = r"C:\Users\User\PycharmProjects\GraduationResearch\CsvFiles\\"
                    shutil.copy(file_path, destination_folder)
                    self.label.config(text="CSVファイルがアップロードされました。")
                    print("CSVファイルがアップロードされました。")
                    self.upload_file_path = file_path
                else:
                    self.label.config(text="CSVファイルを選択してください。")
            except shutil.SameFileError as e:
                self.label.config(text="エラー: 既にアップロードされているファイルです。")


    def is_csv_file(self, file_path):
        filename, file_extension = os.path.splitext(file_path)
        return file_path.lower().endswith('.csv')
