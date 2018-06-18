    def test_reinfo(self):
        url = "https://ke.youdao.com/user/account/"
        # 访问自定义网页
        self.driver.get(url)
        try:
            # 创建一个显示等待对象
            wait = WebDriverWait(self.driver, 10, 0.2)
            nicknameelement = wait.until(EC.visibility_of_element_located((By.ID, 'account-nickname')))
        except TimeoutException, e:
            # 捕获TimeoutException异常
            print traceback.print_exc()
        except NoSuchElementException, e:
            # 捕获NoSuchElementException异常
            print traceback.print_exc()
        except Exception, e:
            # 捕获其他异常
            print traceback.print_exc()
        else:
            nicknameelement.click()
            nicknameelement.clear()
            rename = u"小仙女"+str(random.randint(1,1000))
            nicknameelement.send_keys(rename)
                # 找到页面上ID属性值为“filesubmit”的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("submit-btn")
                # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            time.sleep(5)
            comfirmtext = self.driver.find_element_by_xpath('//h2[text()="保存成功"]')
                # *[@id="dialog-alert"]/div/table/tbody/tr/td[2]/div[1]/h2
            self.assertTrue(comfirmtext, "没有上传成功的弹框")
            comfirmbutton = self.driver.find_element_by_xpath("//div[@class='box-content']/div[@class='tac']/input[@class='g-btn-green finish box-ok']")
            comfirmbutton.click()
            time.sleep(5)
            try:
                renickname=self.driver.find_element_by_xpath("//dl[@class='input clear-fix']/dd/input")
                self.assertEqual(renickname.get_attribute("value"),rename,u"昵称竟然没有更新成功啊")
            except Exception,e:
                print e