#encoding=utf-8
from selenium import webdriver
import unittest, time
from PIL import Image


class ImageCompare(object):
    '''
    本类实现了对两张图片通过像素比对的算法，获取文件的像素个数大小
    然后使用循环的方式将两张图片的所有项目进行一一对比，
    并计算比对结果的相似度的百分比
    '''
    def make_regalur_image(self, img, size=(256, 256)):
        # 将图片尺寸强制重置为指定的size大小
        # 然后再将其转换成RGB值
        return img.resize(size).convert('RGB')

    def split_image(self, img, part_size=(64, 64)):
        # 将图片按给定大小切分
        w, h = img.size
        pw, ph = part_size
        assert w % pw == h % ph == 0
        return [img.crop((i, j, i + pw, j + ph)).copy() \
                for i in xrange(0, w, pw) for j in xrange(0, h, ph)]

    def hist_similar(self, lh, rh):
        # 统计切分后每部分图片的相似度频率曲线
        assert len(lh) == len(rh)
        return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) \
                   for l, r in zip(lh, rh)) / len(lh)

    def calc_similar(self, li, ri):
        # 计算两张图片的相似度
        return sum(self.hist_similar(l.histogram(), r.histogram())\
            for l, r in zip(self.split_image(li), self.split_image(ri))) / 16.0

    def calc_similar_by_path(self, lf, rf):
        li, ri = self.make_regalur_image(Image.open(lf)), \
                 self.make_regalur_image(Image.open(rf))
        return self.calc_similar(li, ri)


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.IC = ImageCompare()
        # 启动Firefox浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_ImageComparison(self):
        #url = "http://doc.outofmemory.cn/python/webpy-cookbook/"
        url = "http://www.sohu.com

"
		# 访问搜狗首页
        self.driver.get(url)
        time.sleep(3)
        # 截取第一次访问搜狗首页的图片，并保存在本地
        self.driver.save_screenshot("e:\\sogou1.png")
        self.driver.get(url)
        time.sleep(3)
        # 截取第二次访问搜狗首页的图片，并保存在本地
        self.driver.save_screenshot("e:\\sogou2.png")
        # 打印两张截图比对后相似度，100表示完全匹配
        print self.IC.calc_similar_by_path('e:\\sogou1.png','e:\\sogou2.png') * 100

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()