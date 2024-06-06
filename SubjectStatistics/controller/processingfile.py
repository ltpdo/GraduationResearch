import tkinter as tk

from SubjectStatistics.models import file
from SubjectStatistics.models.upload import UploadFile


def processing_file():
    # ファイルのアップロード
    root = tk.Tk()
    upload_app = UploadFile(root)
    while not upload_app.upload_file_path:
        root.update()

    # ファイルの読み込み
    read_file = file.ReadFile()
    read_file.read()
    read_file.display_file()
