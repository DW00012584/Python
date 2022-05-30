# -*- coding: utf-8 -*-
import urllib.request

# 取得したいサイトURL
url = "https://www.yahoo.co.jp/"

# サイトデータをオブジェクトとして取得
response = urllib.request.urlopen(url)

# 取得データを読み込む
encodeData = response.read()

# 表示
print(encodeData)