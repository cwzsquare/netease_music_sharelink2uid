from urllib.parse import unquote_plus
from base64 import b64decode
from Crypto.Cipher import AES
key = 'y6oV5go8h5Vg31dSetYA3V1dZ2JGG3WF' # from c.smail

url = input("any sharelink from netease music:\n")


# 解析完成uct参数
a = url.split('&')
uct =""
for i in a:
    if "uct" in i:
        uct = i[4:]
uct = unquote_plus(uct)

# base64解密
uct = b64decode(uct)

# aes解密
aes = AES.new(key.encode(), AES.MODE_ECB)
uid = aes.decrypt(uct).decode()

print(f"belongs to https://music.163.com/#/user/home?id={uid}")
