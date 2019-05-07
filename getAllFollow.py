from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(3)

girisYap=browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
girisYap.click()
time.sleep(3)

username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")

username.send_keys("KULLANICI ADINI BURAYA YAZIN")
password.send_keys("ŞİFREYİ BURAYA YAZIN")

loginButton=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button")
loginButton.click()
time.sleep(3)

skip=browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]")
skip.click()
time.sleep(3)

profileButton=browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
profileButton.click()
time.sleep(3)

followingButton=browser.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[3]/a")
followingButton.click()
time.sleep(3)

jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
followersList = []

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")



for follower in followers:
    
    followersList.append(follower.text)
    
with open("following.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")

browser.close()