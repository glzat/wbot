from datetime import datetime
from random import choice
from time import sleep
from webbrowser import open as openwp


def answer(text):
    print("wbot：", end="")
    if "你好" in text:
        print(choice(["你好啊，主人！", "嗨，主人！"]))
    elif "你是谁" in text or "名字" in text:
        print("我是wbot，你的小助手")
    elif "你会" in text:
        print("我可以帮你查询时间、查询日期、搜索内容等等，具体可以查看我的源代码")
    elif "日期" in text or "几月几日" in text or "几月几号" in text:
        now = datetime.now()
        date = now.strftime("%Y年%m月%d日")
        weekday = now.weekday()
        ls = ["一", "二", "三", "四", "五", "六", "日"]
        print(f"今天是 {date}，星期{ls[weekday]}")
    elif "时间" in text or "几点" in text:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"现在是 {time}")
    elif "搜索" in text:
        try:
            c = input("""1. 百度
      2. 必应
      请输入你要使用的搜索引擎：""")
            w = input("      请输入你要查询的内容：")
        except KeyboardInterrupt:
            print()
            s = choice(["下次再见！", "期待下次见面！"])
            print(f"wbot：{s}")
            sleep(1)
            exit()
        if c == "1":
            openwp(f"https://www.baidu.com/s?wd={w}")
        elif c == "2":
            openwp(f"https://cn.bing.com/search?q={w}")
        else:
            print("输入错误！")
            sleep(1)
    elif "谢谢" in text or "谢谢了" in text:
        print("不用谢，主人！")
    elif "再见" in text or "拜拜" in text:
        print(choice(["下次再见！", "期待下次见面！"]))
        sleep(1)
        exit()
    else:
        print("我暂时还不会呢")


print("欢迎使用 wbot 智能机器人！")
while True:
    try:
        text = input("你：")
    except KeyboardInterrupt:
        print()
        s = choice(["下次再见！", "期待下次见面！"])
        print(f"wbot：{s}")
        sleep(1)
        exit()
    answer(text)
