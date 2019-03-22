import json
import urllib.request
import itchat

api_url = "http://www.tuling123.com/v1/kb/match"


def get_response(_info):
    req = {
        "reqType": 0,  # 输入类型，0代表文本

        "perception":  # 输入信息
        {
            "inputText":  # 文本信息，必须
            {
                "text": _info  # 为函数传入的参数，即好友发送过来的消息
            },


            "selfInfo":  # 客户端属性
            {
                "location":  # 地理位置信息
                {
                    "city": "北京",
                    "province": "北京",
                    "street": "海淀区"
                }
            }
        },


        "userInfo":  # 用户参数
        {
            "apiKey": "xxxxxxxxx"
        }
    }
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    http_post = urllib.request.Request(api_url, data=req, headers={
                                       'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    response_dic = json.loads(response_str)
    return response_dic['results'][0]['values']['text']


# isGroupChat为false表示忽略群聊
@itchat.msg_register(itchat.content.TEXT, isGroupChat=False)
def text_reply(msg):
    return get_response(msg["Text"])


if __name__ == '__main__':
    # hotReload = True, 保持在线，下次运行代码可自动登录
    itchat.auto_login(hotReload=True)
    itchat.run()
