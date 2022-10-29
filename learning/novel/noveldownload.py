""" 打开chrome浏览器 """

# 从selenium模块中导入driver类
import time

from selenium import webdriver


def wait(delay):
    time.sleep(delay)
    pass


def waitZ(delay):
    driver.implicitly_wait(delay)
    # time.sleep(delay)
    pass


# 将Chrome类实例化
driver = webdriver.Chrome()

# 窗口最大化
driver.maximize_window()

# 等待时间（秒）
time.sleep(3)

# 访问目标主页
driver.get('https://www.qishuta.la/')

wait(3)
# 获取到页面标题
title = driver.title
if '奇书网' in title:
    print('页面打开成功')
else:
    print('页面打开失败')
names = {0: '玄幻奇幻',
         1: '武侠仙侠',
         2: '女频言情',
         3: '现代都市',
         4: '历史军事',
         5: '游戏竞技',
         6: '科幻灵异',
         7: '美文同人',
         8: '剧本教程',
         9: '名著杂志'
         }
index = 'https://www.qishuta.la/'
for i in names:
    driver.get('https://www.qishuta.la/')
    waitZ(3)
    tmp = index
    tmp = tmp + "soft/sort0" + str(i + 1)+'/'
    print(tmp)
    driver.get(tmp)
    waitZ(3)

# 关闭浏览器，释放进程
driver.quit()
