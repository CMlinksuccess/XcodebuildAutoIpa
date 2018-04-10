# XcodebuildAutoIpa
iOS自动打包ipa及上传fir的python脚本
<br>
<br>
### 使用方法：
```Python
#=======================设置参数区==========================
#主路径
mainPath0 = "/Users/mac/Desktop/自动打包/Demo"
targetName0 = "Demo"
#输出.ipa文件路径
ipaPath0 = "/Users/mac/Desktop/自动打包/ipa"
#Debug\Release
model = "Debug"
#fir账号的API token
firToken0 = "29cxxxxxxxxxdaxxxxxxxxx1fxxx"
#配置的OptionsPlist路径
plistPath = "/Users/mac/Desktop/自动打包/OptionsPlist.plist"
'''
    OptionsPlist.plist必改参数:
        teamID:    证书的团队名
        method:    打包方式值：app-store, ad-hoc, enterprise, development
        buildleID: 项目buildle identifier
'''
isWorkSpace = False
#=========================================================
```

效果图.<br>
![](https://github.com/CMlinksuccess/XcodebuildAutoIpa/blob/master/xcodebuild%E8%87%AA%E5%8A%A8%E6%89%93%E5%8C%85/raw/image1.png)
