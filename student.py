from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time

from selenium.webdriver.chrome.options import Options


url = "http://p.istudy.ga:8081/student/login.html"

#登录
def login(login_url):
    browser = webdriver.Chrome()
    email = 'student13'
    passwd_1 = 123456
    #登录
    browser.implicitly_wait(8)   #打开窗口
    browser.get(url)
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/form[1]/div[2]/div/input").clear()
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/form[1]/div[3]/div/input").clear()
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/form[1]/div[2]/div/input").send_keys(email)
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/form[1]/div[3]/div/input").send_keys(passwd_1)
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/form[1]/div[4]/button").click()
    time.sleep(10)


#截图
def take_screenshot(url, save_fn):
    
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 900)
    browser.get("http://p.istudy.ga:8081/student/course_elective.html") # Load page
    browser.find_element_by_xpath("//*[@id='grade_table_length']/label/select").click()
    browser.find_element_by_xpath("//*[@id='grade_table_length']/label/select/option[4]").click()
    
    
    time.sleep(5)
    browser.execute_script("""
        (function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);

            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }

            setTimeout(f, 1000);
        })();
    """)

    # for i in range(30):
    #     if "scroll-done" in browser.title:
    #         break
    #     time.sleep(10)

    browser.save_screenshot(save_fn)
    browser.close()

if __name__ == "__main__":

    take_screenshot(url,'A001')




