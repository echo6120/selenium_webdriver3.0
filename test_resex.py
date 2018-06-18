def test_resex(self):
        url = "https://ke.youdao.com/user/account/"
        # 访问自定义网页
        self.driver.get(url)
        sexradiofemail = self.driver.find_element_by_id("sex0")
        sexradiofemail.click()
        time.sleep(5)
        self.assertTrue(sexradiofemail.is_selected(),u"女同学未被选中哦")
        if sexradiofemail.is_selected():
            sexradiomail = self.driver.find_element_by_id("sex1")
            sexradiomail.click()
            time.sleep(5)
            self.assertFalse(sexradiofemail.is_selected())