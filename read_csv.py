#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv

with open("s_hyou1.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダを読み飛ばす
    for row in reader:     # 1 行ずつ文字列のリストとして読み込む
        print(",".join(row))
