#encoding=utf-8
import traceback

from PageObject.add_address import *


def add_address(driver,name,mobile,address,index_provience,index_city,index_area,is_default):
    try:
        driver.get("https://ke.youdao.com/user/address/")
        time.sleep(2)
        ad = AddressPage(driver)
        ad.addaddresselement().click()
        time.sleep(5)
        Select(ad.province()).select_by_index(index_provience)
        Select(ad.city()).select_by_index(index_city)
        Select(ad.area()).select_by_index(index_area)
        time.sleep(2)
        ad.address().send_keys(address)
        time.sleep(2)
        ad.name().send_keys(name)
        time.sleep(2)
        ad.mobile().send_keys(mobile)
        if is_default== "True":
            ad.defaultbutton().click()
        ad.submitbutton().click()
        time.sleep(5)
        info("add_address successfully!")
    except Exception,e:
        traceback.print_exc()
        error("add_address fail")



if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
    login(driver, "huihuitestecho@163.com", "Firewood612")
    add_address(driver,"jingyu","15899999999","test",1,1,4,True)
    driver.quit()