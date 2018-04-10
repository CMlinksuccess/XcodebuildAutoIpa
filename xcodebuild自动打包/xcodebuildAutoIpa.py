# -*- coding: utf-8 -*-
import optparse
import os
import sys
import getpass
import json
import hashlib
import smtplib

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


SDK = "iphoneos"
isupload = "y"
mainPath = mainPath0
targetName = targetName0
ipaPath = ipaPath0
firToken = firToken0


#菜单
def menu_fun():
    global mainPath
    global targetName
    print "\n==========iOS自动打包工具============="
    print "           --Mr.Chen--\n"
    print "     1、一键打ipa包并上传至fir"
    print "     2、自动打ipa包"
    print "     3、上传ipa包到fir"
    print "     4、显示帮助"
    print "     0、退出\n"
    while True:
        sel = raw_input("\n  请选择: ")
        if sel=="1":
            file = mainPath + "/" + targetName + ".xcodeproj"
            if os.path.exists(file):
                #编译
                buildApp()
                #生成ipa文件
                cerateIPA()
                #删除生产的build文件夹
                rmoveFinder()
                isupload = raw_input("  是否将ipa文件上传到fir(y/n,默认y):")
                if isupload=="y" or isupload=="":
                    #上传到fir.im
                    uploadToFir()
                    print("\n  已上传完成..")
            else:
                print "对应目录文件不存在"
        elif sel=="2":
            path = raw_input("拖入.xcodeproj文件生成目录：")
            if isEmpty(path):
                print "目录不能为空"
            else:
                mainPath = getMainPath(path)
                targetName = getTargetName(path,"xcodeproj")
                if isEmpty(targetName):
                    print "目录不正确"
                    continue
                #编译
                buildApp()
                #生成ipa文件
                cerateIPA()
                #删除生产的build文件夹
                rmoveFinder()
                print("\n  打包已完成..")
                mainPath = mainPath0
                targetName = targetName0
        elif sel=="3":
            path = raw_input("拖入.ipa文件生成目录：")
            if isEmpty(path):
                print "目录不能为空"
            else:
                ipaPath = getMainPath(path)
                targetName = getTargetName(path,"ipa")
                if isEmpty(targetName):
                    print "目录不正确"
                    continue
                token = raw_input("请输入API token：")
                if isEmpty(token):
                   print "fir的API token不能为空"
                else:
                    firToken = token
                    #上传到fir.im
                    uploadToFir()
                    print("\n  已上传完成..")
                    
                ipaPath = ipaPath0
                targetName = targetName0
                firToken = firToken0
        elif sel=="4":
            help()
        else:
            exit()
    return

#帮助
def help():
    print("\n  提供iOS自动打包及上传ipa包至fir功能，打包前请将参数设置与项目配置参数保持一致，功能具体选项内容如下：\n  选1:则进入autoIpa.py文件内设置为自己的参数配置，在是否上传fir时将可选\n  选2:按步骤输入路径及打包模式，默认为Debug\n  选3:按步骤提示输入ipa路径及参数，fir账号的token为点击头像菜单中API token生成，即可将ipa包上传至fir\n  选0:退出菜单")
    return

#分解字符串获得mainPath
def getMainPath(path):
    strA = path.split("/")
    arr = strA.pop()
    delimiter = "/"
    name = delimiter.join(strA)
    return name

#分解字符串获得targetNme
def getTargetName(path, suffix):
    strA = path.split("/")
    targetN = strA[-1].split(".")
    name = targetN[0]
    if targetN[-1]== suffix:
        return name
    else:
        return


#判断字符串是否为空
def isEmpty(str):
    if str == None or len(str) == 0:
        return True
    else:
        return False

#查找文件
def scan_files(directory,postfix):
    files_list=[]
    for root, sub_dirs, files in os.walk(directory):
      for special_file in sub_dirs:
        if special_file.endswith(postfix):
            files_list.append(os.path.join(root,special_file))
    return files_list

#编译获取.app文件和dsym
def buildApp():
    global isWorkSpace

    if isWorkSpace:
        os.system("cd %s;xcodebuild archive -workspace %s.xcworkspace -scheme %s -configuration %s -archivePath '%s/build.xcarchive'"%(mainPath,targetName, targetName, model, mainPath))
    else:
        x=os.system("cd %s;xcodebuild archive -scheme %s -configuration %s -archivePath '%s/build.xcarchive'"%(mainPath, targetName, model, mainPath))

    return

#创建ipa
def cerateIPA():
    os.system ("cd %s;rm -r -f %s.ipa"%(mainPath,targetName))
    os.system ("cd %s;xcodebuild -exportArchive -archivePath %s/build.xcarchive -exportPath %s -exportOptionsPlist %s"%(mainPath,mainPath,ipaPath,plistPath))
    return

#删除文件夹
def rmoveFinder():
    if os.path.exists("%s/build.xcarchive"%mainPath):
        os.system("rm -r -f %s/build.xcarchive"%mainPath)
    return

#上传fir
def uploadToFir():
    httpAddress = None
    if os.path.exists("%s/%s.ipa"%(ipaPath,targetName)):
        ret = os.popen("fir p '%s/%s.ipa' -T '%s'"%(ipaPath,targetName,firToken))
        for info in ret.readlines():
            if "Published succeed" in info:
                httpAddress = info
                print httpAddress
                break
    else:
        print "没有找到ipa文件"
    return httpAddress

#主函数
def main():

    menu_fun()
    return

main()
