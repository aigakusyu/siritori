import pandas as pd
import urllib.request
from io import StringIO

url = "https://raw.githubusercontent.com/aigakusyu/siritori/master/sample_command/s_hyou1.csv"

#csvを読み込む関数
def read_csv(url):
    print(url)
    res = urllib.request.urlopen(url)
    res = res.read().decode("utf-8")
    df = pd.read_csv(StringIO( res) )
    return df

#実行
read_csv(url)
