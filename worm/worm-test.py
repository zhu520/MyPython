from selenium import webdriver
import time

browser = webdriver.Chrome()
'''
#百度搜索
browser.get('http://www.baidu.com')

elem_id = browser.find_element_by_id('kw')
elem_name = browser.find_element_by_name('wd')
elem_cls = browser.find_element_by_class_name("s_ipt")
elem_btn = browser.find_element_by_id("su")

elem_id.send_keys("python")
elem_btn.click()
'''
'''
#获取糗事百科笑话
browser.get('https://www.qiushibaike.com/text/')
main_content = browser.find_element_by_id("content-left")
content = main_content.find_elements_by_class_name("content")

for c in content:
    try:
        print(c.text)
    except:
        pass
'''
#豆瓣图书TOP25
browser.get('https://book.douban.com/top250')
for i in range(10):
    title = browser.find_element_by_xpath("//div[@id='content']//h1").text
    print(title)
    book_list = browser.find_elements_by_xpath("//tr[@class='item']")
    for ele in book_list:
        print(ele.text + "\n")
    print("------------第%s页------------" % (i + 1))

    #下一页
    next_page = browser.find_element_by_class_name("next").click()
    time.sleep(5)
    print("\n")

browser.quit()
#browser.close() #存在命令行窗口未关闭

