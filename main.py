import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import setting
import chromedriver_binary

options = Options()
# turn on to execute in headless mode
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


# answer lists
"""
For Q16. Type ONLY
0: Do Nothing (ex.text field, disabled input)
1-4: normal questions
10: etc
"""
ans_lines = [
    [10, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0]
]


def clickElement(questionNo=0, answer=0):
    try:
        driver.find_element_by_xpath(
            f"//*[@id=\"answer_choice\"]/div[1]/dl/dd[{questionNo + 1}]/ul/li[{answer}]/label/input").click()
    except:
        driver.find_element_by_xpath(
            f"//*[@id=\"answer_choice\"]/div[1]/dl/dd[{questionNo + 1}]/ul[2]/li[{answer}]/label/input").click()


def isElementSet(questionNo=0, answer=0):
    try:
        driver.find_element_by_xpath(
            f"//*[@id=\"answer_choice\"]/div[1]/dl/dd[{questionNo + 1}]/ul/li[{answer}]/label/input").is_selected()
    except:
        driver.find_element_by_xpath(
            f"//*[@id=\"answer_choice\"]/div[1]/dl/dd[{questionNo + 1}]/ul[2]/li[{answer}]/label/input").is_selected()


# NEED TO WAIT FOR A FEW SOCONDS UNTIL PAGES ARE READY
try:
    # log in with EPS-ID
    driver.get("https://www.k.kyoto-u.ac.jp/student/la/top")
    time.sleep(1)
    driver.find_element_by_id("username").send_keys(setting.ID)
    driver.find_element_by_id("password").send_keys(setting.PASS)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)

    # survey top page
    driver.get("https://enq.gakusei.kyoto-u.ac.jp/user/top.php")
    time.sleep(1)

    # accept sending attribution
    driver.find_element_by_xpath("/html/body/div/div/form/p[2]/input[2]").click()
    time.sleep(1)

    # go to survey list
    driver.get("https://enq.gakusei.kyoto-u.ac.jp/user/unanswer_list.php")
    time.sleep(1)

    # get lecName list and lecID
    try:
        for i in range(20):
            lecName = driver.find_element_by_xpath(f"//*[@id=\"contents\"]/dl/dt[{i + 1}]").text
            print(f"講義名:{lecName} -> {i + 1}")
    except:
        pass

    # wait for user to designate lecID
    lecNum = input("Type in ID (02 for 2): ")

    # click on survey
    driver.find_element_by_xpath(f"//*[@id=\"q0{lecNum}_answer\"]").click()
    time.sleep(1)

    # check if survey is type Q16.
    title = driver.find_element_by_xpath("//*[@id=\"answer_choice\"]/ul[1]/li[2]").text
    if title != "第1～5問/全16問":
        print("Too many questions!!!")
        driver.quit()

    # ------START------
    # for page 1 to 3
    for page, ans_line in enumerate(ans_lines):
        for q, ans in enumerate(ans_line):
            if ans != 0 and not isElementSet(q, ans):
                clickElement(q, ans)
            else:
                pass
        driver.find_element_by_xpath("//*[@id=\">\"]").click()
        time.sleep(2)

    # page 4
    if not driver.find_element_by_xpath("//*[@id=\"answer_choice\"]/div[1]/dl/dd/ul/li[1]/label/input").is_selected():
        driver.find_element_by_xpath("//*[@id=\"answer_choice\"]/div[1]/dl/dd/ul/li[1]/label/input").click()

    driver.find_element_by_xpath("//*[@id=\"answer_check\"]").click()
    # ------END------

    # ---disable final submission by default--- #
    # driver.find_element_by_xpath("//*[@id=\"answer_fin\"]")

except:
    traceback.print_exc()
finally:
    print("end")
    # driver.quit()
