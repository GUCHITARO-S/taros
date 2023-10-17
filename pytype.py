from datetime import datetime
import os
import sys
import csv
import time
import random
import PySimpleGUI as sg

flag = 0
font = ("meiryo", 16)
font1 = ("meiryo", 12)


def type_index():
    """起動時の画面"""
    global flag
    day = datetime.now()
    today = f"{day.month}月{day.day}日 "
    today_time = day.strftime("%H:%M")
    layout = [
            [sg.Text(today+today_time,
                     font=font, size=(20, 1),
                     justification="center")],
            [sg.Text("        "),
             sg.Button("スタート", key="-START-", focus=True, bind_return_key=True),
             sg.Button("おわり", key="-END-", bind_return_key=True)],
        ]

    window = sg.Window("タイピング", layout, size=(250, 100))
    while True:
        event, value = window.read()
        if event in [sg.WIN_CLOSED, "-END-"]:
            break
        if flag == 1:
            window.close()
            main()
        if event == "-START-":
            flag = 1
            main()
            window.close()


def main():
    count = 0
    ans_word = ""
    ans_time = ""
    total_time = 0
    count = 0
    words = []
    files = ["csvs/typing.csv", "csvs/typing1.csv", "csvs/typing2.csv", "csvs/anime.csv", "csvs/hard.csv"]
    file = random.choice(files)
    sc_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(sc_dir, file)

    while True:
        with open(csv_file_path, encoding="utf-8") as f:
            reader = csv.reader(f, skipinitialspace="True")
            for row in reader:
                words += row

        random.shuffle(words)
        gen_words = iter(words)
        pop_word = next(gen_words)
        layout = [
            [sg.Text(pop_word, key="-T1-", font=font, justification="center")],
            [sg.Input(key="-I1-", font=font, border_width=3),
             sg.Button("終了", key="-END-")],
            [sg.Text(key="-O1-", s=(60, 20), font=font1),
             sg.Text(key="-O2-", s=(15, 20), font=font1)],
        ]
        window = sg.Window("タイピングNOW", layout, size=(800, 600),
                           return_keyboard_events=True)
        start = time.perf_counter()
        while count < 20:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                sys.exit()
            elif event == "-END-":
                break

            try:
                if pop_word.rstrip() == value["-I1-"]:
                    count += 1
                    end = time.perf_counter()
                    total_time += end - start
                    ans_word += value["-I1-"] + "\n"
                    ans_time += f"問{count} -> {end - start:.2f}秒\n"
                    pop_word = next(gen_words)
                    window["-I1-"].update("")
                    window["-T1-"].update(pop_word)
                    window["-O1-"].update(ans_word)
                    window["-O2-"].update(ans_time)
                    start = time.perf_counter()
            except StopIteration:
                layout = [
                    [sg.Text(f"入力時間合計：{int(total_time // 60)}分"
                             f"{int(total_time % 60)}秒 -> 問題数：{count}",
                             font=("meiryo", 20))],
                    [sg.Text(f"{ans_word}", s=(60, 20), font=font1),
                     sg.Text(f"{ans_time}", s=(15, 20), font=font1)],
                    [sg.Button("トップに戻る", key="-B1-", bind_return_key=True)],
                ]
                window2 = sg.Window("result", layout, size=(800, 600))
                while True:
                    event, value = window2.read()
                    if event == sg.WIN_CLOSED:
                        sys.exit()
                    if event == "-B1-":
                        window.close()
                        window2.close()
                        type_index()
            else:
                continue
        layout = [
                [sg.Text(f"合計入力時間：{int(total_time // 60)}分"
                         f"{int(total_time % 60)}秒 -> 問題数：{count}",
                         font=("meiryo", 20), justification="center")],
                [sg.Text(f"{ans_word}", s=(60, 20), font=font1),
                 sg.Text(f"{ans_time}", s=(15, 20), font=font1)],
                [sg.Button("トップに戻る", key="-B1-", bind_return_key=True)],
            ]

        window2 = sg.Window("result", layout, size=(800, 600),
                            return_keyboard_events=True)

        while True:
            event, value = window2.read()
            if event == sg.WIN_CLOSED:
                sys.exit()
            if event == "-B1-":
                window.close()
                window2.close()
                type_index()
            else:
                continue


if __name__ == "__main__":
    type_index()
