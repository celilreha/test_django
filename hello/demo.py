"""import time
import random
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import pickle
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.support.ui import Select
class M():
    named_tuple = time.localtime()
    time_string = time.strftime("%Y%m%d_%H%M%S", named_tuple)
    file_name="test_logs/test_log_"+time_string+".txt"
    with open(file_name, "a") as file_object:
        file_object.write("Test started\n")
    #file = open("test_logs/test_log_"+time_string+".txt", "a")
    #file = open("test_log_"+time_string+".txt", "a")
    #file = open("test_logs/test.txt", "a")
    none_list=['','N/A','0','00','?','None','? None','-1']
    all_links=[]    #
    start_time = time.time()
    live_server_url='https://www.hyperiser.com'
    selenium = WebDriver(executable_path='D:\Hyperiser\geckodriver.exe')
    selenium.implicitly_wait(10)
    selenium.get(live_server_url)
    '''username_input = selenium.find_element_by_name("username")
    username_input.send_keys('celilreha')
    password_input = selenium.find_element_by_name("password")
    password_input.send_keys('')
    selenium.find_element_by_xpath('//button[@id="send"]').click()
    self.selenium.find_elements_by_xpath('//span[text()="Accept Cookies"]')[0].click()
    pickle.dump( self.selenium.get_cookies() , open("cookies.pkl","wb"))'''
    selenium.maximize_window()
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        selenium.add_cookie(cookie)
    selenium.find_elements_by_xpath('//span[text()="Accept Cookies"]')[0].click()
    @classmethod
    def tearDownClass(cls):
        #print('file is closed')
        #cls.file.close()
        cls.selenium.quit()
    def test_000_add_list(self):
        self.selenium.get(self.live_server_url+'/influencerlists')
        self.selenium.find_element(By.LINK_TEXT,'View List').click()
        self.delete_from_list()
        self.delete_list()
        list_name='test_cre'
        self.selenium.get('https://www.hyperiser.com/discover/instagram')
        cards=self.selenium.find_elements(By.CLASS_NAME,'profile-instagram')
        self.click_add_list_button(cards[random.randint(0,len(cards)-1)],'instagram',list_name)
        self.selenium.get('https://www.hyperiser.com/discover/twitch')
        cards=self.selenium.find_elements(By.CLASS_NAME,'profile-twitch')
        self.click_add_list_button(cards[random.randint(0,len(cards)-1)],'twitch',list_name)
        self.selenium.get('https://www.hyperiser.com/discover/tiktok')
        cards=self.selenium.find_elements(By.CLASS_NAME,'profile-tiktok')
        self.click_add_list_button(cards[random.randint(0,len(cards)-1)],'tiktok',list_name)
        self.selenium.get('https://www.hyperiser.com/discover/youtube')
        cards=self.selenium.find_elements(By.CLASS_NAME,'profile-youtube')
        self.click_add_list_button(cards[random.randint(0,len(cards)-1)],'youtube',list_name)
        self.selenium.get('https://www.hyperiser.com/discover/clubhouse')
        cards=self.selenium.find_elements(By.CLASS_NAME,'profile-clubhouse')
        self.click_add_list_button(cards[random.randint(0,len(cards)-1)],'clubhouse',list_name)
        self.selenium.get('https://www.hyperiser.com/podcast')
        cards=self.selenium.find_elements(By.CLASS_NAME,'profile-instagram')
        self.click_add_list_button(cards[random.randint(0,len(cards)-1)],'instagram',list_name)
        self.selenium.get(self.live_server_url+'/influencerlists')
        list_name='test_cre'
        current_url = self.selenium.current_url
        search_box=self.selenium.find_element(By.ID,'influencerSearchInput')
        for i in 'gac':
            search_box.send_keys(i)
            time.sleep(0.3)
        search_box.send_keys(Keys.ENTER)
        WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
        time.sleep(2)
        WebDriverWait(self.selenium,30).until(EC.visibility_of_element_located((By.CLASS_NAME,'profile-instagram')))
        cards=self.selenium.find_elements(By.CLASS_NAME,'profile-instagram')
        rand_indexes=random.sample(range(0,len(cards)-1),2)
        self.click_add_list_button(cards[rand_indexes[0]],'instagram',list_name)"""