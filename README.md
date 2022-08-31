# netease_music_sharelink2uid
从网易云音乐的分享链接中获取分享者的用户信息 | Find NetEase CloudMusic User
## 为啥要做？
启发自v2ex的一篇[通过网易云音乐分享链接找到分享用户主页](https://www.v2ex.com/t/876017)，发现作者建了一个站[Find NetEase CloudMusic User](https://findneteasecloudmusicuser.nclgclub.com/)，但是解析不是用纯js，直接和后端交互的……真不符合开放精神。

**个人没啥解析需求。**
## 真正的启发者
https://ahxxm.com/173.moew/  ~~还是看看远方的smali逆向吧家人们~~。（关键其实就是逆向apk拿到一个key参数）

## 开发？
本来是想直接挂个静态网页，用前端js直接全给解析了的，这样稍微能看点js的人也能直接开源拿到全部解析过程；但今晚太晚了，明天再说（js加密库经验匮乏）；但是睡前拿python水水还是不占时间的，就先发布一个python3版本。

py依赖的话，就`pycryptodome`麻烦点得装，其余都自带。

## 结语
请用自由软件打破封闭与可能的隐私威胁。
