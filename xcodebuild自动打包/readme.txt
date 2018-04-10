自动打包xcodebuildAutoIpa  v1.0.

外部文件： 
     1、xcodebuildAutoIpa.py
 
使用步骤：

    1、修改OptionsPlist.plist、xcodebuildAutoIpa.py为自己的配置内容。具体内容参考文件内参数说明
    2、打开终端cd到项目根目录，执行python xcodebuildAutoIpa.py

注意： 使用前确保终端安装了xcodebuild，没有请执行xcode-select --install，报错问度娘
      没有配置证书参数，需在打包前在项目中设置好
      项目不使用cocoapods