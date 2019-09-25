# 导入模块
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)
print("机器人已启动")

# 设置好友消息自动回复
@bot.register(Friend, TEXT)
def auto_accept_friends(msg):
    print("获取到好友消息", msg.text)
    if msg.text == "在吗":
        msg.chat.send("呵呵")
    elif msg.text == "0":
        msg.chat.send("回复1获取更多内容")
    elif msg.text == "1":
        msg.chat.send("邀请你进入某个群")
        group_select=bot.groups().search("test")[0]
        group_select.add_members(msg.chat, use_invitation=True)
# 获取简单的好友统计
# friends_total=bot.friends().stats_text()
# print(friends_total)

# 获取微信好友总数
# wx_friends=bot.friends()
# print("获取到的微信好友数据为", len(wx_friends), wx_friends[1])
# friend_now=wx_friends[1]
# print("名称",friend_now.name)
# print("头像",friend_now.get_avatar())
# print("性别sex 1为男性,2为女性",friend_now.sex)
# print("地区 省份-城市",friend_now.province,friend_now.city)
# print("个性签名",friend_now.signature)

# # 获取微信群的总数
# wx_groups=bot.groups()
# print("获取到的微信群数据为", len(wx_groups),wx_groups)
#
# # 获取微信公众号的总数
# wx_mps=bot.mps()
# print("获取到的微信公众号数据为", len(wx_mps),wx_mps)

# 仅仅堵塞线程
bot.join()

