# -------------------------------
# Social Bot Version 1 (Corrected)
# -------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
import os


class Social_bot:
    def __init__(self):
        # URLs
        self.login_page = "https://www.facebook.com/"
        self.page_ref = "https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Fpages%2F%3Fcategory%3Dyour_pages%26amp%253Bref%3Dbookmarks"

        # Path to chromedriver
        self.chromium_path = os.path.abspath("chromedriver.exe")

        # Browser session
        self.browser_session = None
        self.browser_visit = 0
        self.login = 0

        # Default time delay (seconds)
        self.time_pattern = 5

        # Facebook login XPaths
        self.user_xpath = "//input[@id='email']"
        self.pass_xpath = "//input[@id='pass']"

        # Credentials
        self.user = None
        self.password = None

        # Logout XPaths
        self.logout_fb = [
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]/i[1]",
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]",
            "//div[@class='oajrlxb2 s1i5eluu gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329']//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 c4xchbtz by2jbhx6']"
        ]

        # Facebook post XPaths
        self.fb_posting = [
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]",
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]",
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[4]/div[1]"
        ]

        self.fb_page_partial = None
        self.textContents = None

    def initiate_chrome(self):
        if self.browser_session is None:
            # FIXED: Modern way to load Chrome driver
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.browser_session = webdriver.Chrome(options=options)
            return 1
        return -1

    def close_session(self):
        if self.browser_session:
            self.browser_session.quit()
            self.browser_session = None
            return 1
        return -1

    def page_load(self, path=None):
        if self.browser_session is None:
            return -1
        url = path if path else self.login_page
        self.browser_session.get(url)
        self.browser_visit += 1
        return 1

    def reverse_visit(self, back_v=None):
        if self.browser_visit is None:
            return -1
        if back_v is None:
            for _ in range(self.browser_visit):
                self.browser_session.back()
            self.browser_visit = 0
        else:
            for _ in range(back_v):
                self.browser_session.back()
                self.browser_visit -= 1  # FIXED: Corrected "- ="
        return 1

    def do_login(self, user_name=None, user_pass=None):
        if self.browser_session is None or self.login == 1:
            return -1

        # FIXED: Corrected condition (was inverted)
        if user_name is not None and user_pass is not None:
            self.user = user_name
            self.password = user_pass

        try:
            self.browser_session.find_element(By.XPATH, self.user_xpath).send_keys(self.user)
            self.browser_session.find_element(By.XPATH, self.pass_xpath).send_keys(self.password)
            self.browser_session.find_element(By.XPATH, self.pass_xpath).send_keys(Keys.ENTER)
            self.browser_visit += 1
            self.login = 1
            return 1
        except Exception as e:
            print("Login failed:", e)
            return -1

    def do_logout(self):
        if self.browser_session is None or self.login == 0:
            return -1
        try:
            for path in self.logout_fb:
                self.browser_session.find_element(By.XPATH, path).click()
                self.time_patterns()
            return 1
        except Exception as e:
            print("Logout failed:", e)
            return -1

    def time_patterns(self, tp=None):
        if tp is not None:
            self.time_pattern = tp
        time.sleep(self.time_pattern)
        return 1

    def page_navigation_partial(self, pg_name):
        if self.browser_session is None:
            return -1
        try:
            # FIXED: removed syntax error in previous version
            self.browser_session.find_element(By.PARTIAL_LINK_TEXT, pg_name).click()
            self.browser_visit += 1
            return 1
        except Exception as e:
            print("Navigation failed:", e)
            return -1

    def page_posting(self):
        if self.browser_session is None:
            return -1
        try:
            self.browser_session.find_element(By.XPATH, self.fb_posting[0]).click()
            self.time_patterns()
            self.browser_session.find_element(By.XPATH, self.fb_posting[1]).send_keys(Keys.ENTER, self.textContents)
            self.time_patterns()
            self.browser_session.find_element(By.XPATH, self.fb_posting[2]).click()
            self.time_patterns()
            self.reverse_visit(1)
            return 1
        except Exception as e:
            print("Posting failed:", e)
            return -1

    def credential_loads_using_json(self):
        try:
            with open("credentials_load.json", "r") as filePointer:
                contents = json.load(filePointer)
            self.fb_page_partial = contents["Page Names"]
            self.user = contents["Email Address"]
            self.password = contents["Password"]
            return 1
        except Exception as e:
            print("Error loading credentials:", e)
            return -1

    def text_posting_content_load(self):
        try:
            with open("PostingContents.txt", "r", encoding="utf-8") as filePointer:
                self.textContents = filePointer.read()
            return 1
        except Exception as e:
            print("Error loading post text:", e)
            return -1


def soc_bot():
    bot = Social_bot()
    bot.initiate_chrome()
    bot.credential_loads_using_json()
    bot.text_posting_content_load()
    bot.page_load()
    bot.do_login()

    ask_to_block_notif = input(
        "[+] Perform these tasks:\n1. Accept 2FA if required.\n"
        "2. Once FB Page loads, block notifications.\n"
        "Press Y when done to continue posting: "
    )

    if ask_to_block_notif.strip().upper() == "Y":
        bot.page_load(bot.page_ref)
        bot.time_patterns()

        for link in bot.fb_page_partial:
            bot.page_navigation_partial(link)
            bot.time_patterns()
            bot.page_posting()
            print(f"[+] Posting done on {link}")

        bot.do_logout()
        bot.close_session()
        print("[+] Posting Work Done!")
        return 1
    else:
        bot.close_session()
        return -1


if __name__ == "__main__":
    print("SOCIAL BOT SCRIPT INITIATED")
    soc_bot()
