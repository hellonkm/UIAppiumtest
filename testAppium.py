#!/usr/bin/python
# -*- coding=utf-8 -*-
#encoding=utf-8
from os import sys
sys.path.append("..")
from imp import reload
reload(sys)

from androguard.core.bytecodes.apk import APK
from appium import webdriver

class testWeb(object):

    def action(self,platformName,platformVersion,deviceName,app):
            # desired_caps = {'platformName': 'Android', 'platformVersion': '9', 'deviceName': '835c6ae1', 
        #         'app': r'C:\Python37\crm_6.74.0_246_debug_auto.apk', 
        #         'automationName': 'flutter','appPackage': 'com.ibaibu.crmflutter'}
        #app = r'C:\Python37\crm_6.74.0_246_debug_auto.apk'
        try:
            if platformName == 'ios':
                desired_caps = {
                                'platformName': platformName, 'platformVersion':platformVersion, 'deviceName': deviceName, 
                                'bundleId':'bundleId','udid':'udid',
                                'app': '...ipa',"skipServerInstallation": True}
            else:    
                appPackage = APK(app, False, "r").get_package()
                appActivity = APK(app, False, "r").get_main_activity()
                desired_caps = {
                                'platformName': platformName, 'platformVersion':platformVersion, 'deviceName': '835c6ae1', 
                                'appPackage':appPackage,'appActivity':appActivity,
                                'automationName': 'flutter',"skipServerInstallation": True}
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        except Exception  as e:
            return ({"code":1001,"msg":"fail","data":e}) 
        return ({"code":200,"msg":"success"})   

    def basicAppium(self,type):
        '''
            type:1 退出  type：2 后退
            type:3 屏幕截图 type:4 获取页面源码
            type:5 设置超时 type:6 设置隐式等待超时时间
        '''
        try:
            if type == 1 :
                self.driver.quit()
            elif type== 2:
                self.driver.back()
            elif type == 3:
                screenshotBase64 = self.driver.get_screenshot_as_base64()
            elif type == 4:            
                source = self.driver.page_source        
            elif type == 5:
                self.driver.set_page_load_timeout(5000)
            elif type == 6:
                self.driver.implicitly_wait(5)    
        except Exception  as e:
            return ({"code":1001,"msg":"fail","data":e}) 
        return ({"code":200,"msg":"success"})

    def elementAppium(self,type,data):

        '''
        type:1 元素查找
        type:2  元素组查找
        
        '''
        try:
            if type == 1:
                self.driver.find_element_by_accessibility_id(data)
            elif type == 2:
                self.driver.find_elements_by_accessibility_id(data)
        except Exception  as e:
            return ({"code":1001,"msg":"fail","data":e}) 
        return ({"code":200,"msg":"success"})                    