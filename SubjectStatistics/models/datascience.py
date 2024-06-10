# ライブラリ
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# データの前処理
# 科目処理
def subject_data(df):
    print("以下が科目の処理になります。")
    # 科目ごとのデータフレーム
    df_subject = df.copy()

    # 重複を排除してユニークな科目名と学生番号の組み合わせを取得
    df_unique = df[['科目名', '学生番号']].drop_duplicates()

    # 科目名ごとに履修者数をカウント
    student_count = df_unique.groupby('科目名').count().reset_index()
    student_count.rename(columns={"学生番号": "履修者数"}, inplace=True)

    # インデックスに設定
    student_count.set_index("科目名", inplace=True)

    # 成績ごとにカウント
    grade_count = df_subject.groupby(["科目名", "GP"]).size().unstack(fill_value=0)
    grade_count.columns = ["D", "C", "B", "A", "S"]
    df_subject = pd.concat([student_count, grade_count], axis=1)
    df_subject.head()
    print(df_subject.head())



# 学生処理
def student_data(df):
    pass
