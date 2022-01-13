import time
import random
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import pickle
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class BaseTest(LiveServerTestCase):
    def make_cookie(self):
        live_server_url = 'https://www.hyperiser.com'
        self.selenium = WebDriver(executable_path='D:\Hyperiser\chromedriver.exe')
        self.selenium.implicitly_wait(10)
        self.selenium.get(live_server_url)
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('celilreha')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('Celil14789')
        self.selenium.find_element_by_xpath('//button[@id="send"]').click()
        self.selenium.find_elements_by_xpath('//span[text()="Accept Cookies"]')[0].click()
        pickle.dump(self.selenium.get_cookies(), open("cookies.pkl", "wb"))
        # selenium.maximize_window()
        # cookies = pickle.load(open("cookies.pkl", "rb"))
        # for cookie in cookies:
        #    selenium.add_cookie(cookie)


class MySeleniumTests(LiveServerTestCase):
    named_tuple = time.localtime()
    time_string = time.strftime("%Y%m%d_%H%M%S", named_tuple)
    file_name = "test_logs/test_log_"+time_string+".txt"
    with open(file_name, "a") as file_object:
        file_object.write("Test started\n")
    # file = open("test_logs/test_log_"+time_string+".txt", "a")
    # file = open("test_log_"+time_string+".txt", "a")
    # file = open("test_logs/test.txt", "a")
    none_list = ['', 'N/A', '0', '00', '?', 'None', '? None', '-1']
    all_links = []    #
    start_time = time.time()
    live_server_url = 'https://www.hyperiser.com'
    selenium = WebDriver(executable_path='D:\Hyperiser\chromedriver.exe')
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
        # print('file is closed')
        # cls.file.close()
        cls.selenium.quit()

    def test_000_add_list(self):
        '''
        asfasf
        asfasfasf
        asfas
        fas
        fasf'''
        self.selenium.get(self.live_server_url+'/influencerlists')
        self.selenium.find_element(By.LINK_TEXT, 'View List').click()
        self.delete_from_list()
        self.delete_list()
        list_name = 'test_cre'
        self.selenium.get('https://www.hyperiser.com/discover/instagram')
        cards = self.selenium.find_elements(By.CLASS_NAME, 'profile-instagram')
        self.click_add_list_button(cards[random.randint(0, len(cards)-1)], 'instagram', list_name)
        self.selenium.get('https://www.hyperiser.com/discover/twitch')
        cards = self.selenium.find_elements(By.CLASS_NAME, 'profile-twitch')
        self.click_add_list_button(cards[random.randint(0, len(cards)-1)], 'twitch', list_name)
        self.selenium.get('https://www.hyperiser.com/discover/tiktok')
        cards = self.selenium.find_elements(By.CLASS_NAME, 'profile-tiktok')
        self.click_add_list_button(cards[random.randint(0, len(cards)-1)], 'tiktok', list_name)
        self.selenium.get('https://www.hyperiser.com/discover/youtube')
        cards = self.selenium.find_elements(By.CLASS_NAME, 'profile-youtube')
        self.click_add_list_button(cards[random.randint(0, len(cards)-1)], 'youtube', list_name)
        self.selenium.get('https://www.hyperiser.com/discover/clubhouse')
        cards = self.selenium.find_elements(By.CLASS_NAME, 'profile-clubhouse')
        self.click_add_list_button(cards[random.randint(0, len(cards)-1)], 'clubhouse', list_name)
        self.selenium.get('https://www.hyperiser.com/podcast')
        cards = self.selenium.find_elements(By.CLASS_NAME, 'profile-instagram')
        self.click_add_list_button(cards[random.randint(0, len(cards)-1)], 'instagram', list_name)
        self.selenium.get(self.live_server_url+'/influencerlists')
        list_name = 'test_cre'
        current_url = self.selenium.current_url
        search_box = self.selenium.find_element(By.ID, 'influencerSearchInput')
        for i in 'gac':
            search_box.send_keys(i)
            time.sleep(0.3)
        search_box.send_keys(Keys.ENTER)
        WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
        time.sleep(2)
        WebDriverWait(self.selenium, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'profile-instagram')))
        cards = self.selenium.find_elements(By.CLASS_NAME, 'profile-instagram')
        rand_indexes = random.sample(range(0, len(cards)-1), 2)
        self.click_add_list_button(cards[rand_indexes[0]], 'instagram', list_name)
    '''def test_00_sector_analysis(self):
        self.file_open_write('sector analysis method started\n')
        self.selenium.get(self.live_server_url+'/sector_analysis')
        form=self.selenium.find_element_by_id('sectorAnalysisForm')
        form.find_element(By.XPATH, '//button[@data-id="sectors"]').click()
        sectors=form.find_element(By.XPATH, '//button[@data-id="sectors"]/following-sibling::div').find_elements(By.TAG_NAME,'li')
        sectors[random.randint(1,len(sectors)-1)].click()
        form.find_element(By.XPATH,'//button[@data-id="brandsInput"]').click()
        brands=form.find_element(By.XPATH,'//button[@data-id="brandsInput"]/following-sibling::div').find_elements(By.TAG_NAME,'li')
        brands[random.randint(0,len(brands)-1)].click()
        form.find_element(By.XPATH,'//a[text()="Next"]').click()
        WebDriverWait(self.selenium,5).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="START SCAN"]'))).click()
        self.file_open_write('sector analysis started\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))'''
    def test_01_competition_analysis(self):
        self.file_open_write('competetion analysis method started\n')
        self.selenium.get(self.live_server_url+'/competition_analysis')
        form=self.selenium.find_element_by_id('rakipAnaliziForm')
        form.find_element(By.XPATH,'//button[@data-id="users_lists"]').click()
        form.find_elements(By.TAG_NAME,'li')[0].click()
        form.find_element(By.XPATH,'//a[text()="Next"]').click()
        WebDriverWait(self.selenium,5).until(EC.visibility_of_element_located((By.XPATH, '//button[@data-id="sectors"]'))).click()
        sectors=form.find_element(By.XPATH, '//button[@data-id="sectors"]/following-sibling::div').find_elements(By.TAG_NAME,'li')
        sectors[random.randint(0,len(sectors)-1)].click()
        form.find_element(By.XPATH,'//button[@data-id="brandsInput"]').click()
        brands=form.find_element(By.XPATH,'//button[@data-id="brandsInput"]/following-sibling::div').find_elements(By.TAG_NAME,'li')
        brands[random.randint(1,len(brands)-1)].click()
        form.find_element(By.XPATH,'//a[text()="Next"]').click()
        WebDriverWait(self.selenium,5).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="START SCAN"]'))).click()
        self.file_open_write('competetion analysis started\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_02_dashboard_all_hrefs(self):
        self.file_open_write('all links control started\n')
        self.selenium.get(self.live_server_url)
        self.check_404_or_500()
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/discover/tiktok')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/discover/twitch')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/discover/youtube')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/discover/clubhouse')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/podcast')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/competition_analysis')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/targeted_analysis')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/cross_analysis')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/post_analysis')
        self.get_all_links_on_page()
        self.selenium.get(self.live_server_url+'/sector_analysis')
        self.get_all_links_on_page()
        for dict in self.all_links:
            r=requests.get(dict['link'])
            print('{0} {1} {2}'.format('status code: ',r.status_code,dict))
            try:
                self.assertEqual(r.status_code,200)
                self.file_open_write('{0} {1} {2}\n'.format('status code: ',r.status_code,dict))
            except AssertionError as e:
                self.file_open_write('{0} {1} {2}\n'.format('status code: ',r.status_code,dict))       
        self.file_open_write('all links controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_03_discover_instagram_page_picture(self):
        self.file_open_write('discover instagram page profile picture control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.check_404_or_500()
        '''instagram_cards=self.selenium.find_elements(By.CLASS_NAME,'profile-instagram')
        next_btn=self.selenium.find_element(By.ID,'goNextBtn')
        prev_btn=self.selenium.find_element(By.ID,'goPrevBtn')
        wait_count=0
        while(wait_count<30 and len_inf_card<=len(instagram_profiles)):
            instagram_profiles=self.browser.find_by_css('.profile-instagram')
            time.sleep(0.1)
            wait_count=wait_count+1
        for card in instagram_cards:
            img_url=card.find_element(By.CLASS_NAME,'card-image-instagram').value_of_css_property('background-image')
            if('http' not in img_url):
                self.file_open_write('{0} {1} \n'.format(card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text,' has no picture'))'''
        self.get_card_details('instagram')
        self.file_open_write('discover instagram page profile picture controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_040_filter_discover_instagram_no_category_no_label(self):
        self.file_open_write('discover instagram page no category no label filter control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.selenium.find_element(By.ID,'filters').click()
        current_url = self.selenium.current_url
        self.selenium.find_element(By.CLASS_NAME,'influencer_filter_btn').click()
        WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
        time.sleep(3)
        self.get_card_details('instagram')
        self.file_open_write('discover instagram page no category no label filter controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_041_filter_discover_instagram_one_category(self):
        self.file_open_write('discover instagram page one category filter control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.selenium.find_element(By.ID,'filters').click()
        selected_categories=self.get_select_categories(1)
        current_url = self.selenium.current_url
        self.selenium.find_element(By.CLASS_NAME,'influencer_filter_btn').click()
        WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
        time.sleep(3)
        instagram_cards=self.get_card_details('instagram')
        self.file_open_write('{0} {1}\n'.format('Selected category is',selected_categories))
        for card in instagram_cards:
            user=card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text
            card_categories=card.find_element(By.CLASS_NAME,'card-cats').text.split('/')
            for i in range(len(card_categories)): card_categories[i]=card_categories[i].strip()
            is_cat_exist=False
            for cat in selected_categories:
                if cat in card_categories:
                    is_cat_exist=True
                    break
            if is_cat_exist is False:
                self.file_open_write('{0} {1} {2}\n'.format(selected_categories,'Category not exist',user))
        self.file_open_write('discover instagram page one category filter controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_042_filter_discover_instagram_one_label(self):
        self.file_open_write('discover instagram page one label filter control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.selenium.find_element(By.ID,'filters').click()
        selected_labels=self.get_select_labels(1)
        current_url = self.selenium.current_url
        self.selenium.find_element(By.CLASS_NAME,'influencer_filter_btn').click()
        WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
        time.sleep(3)
        instagram_cards=self.get_card_details('instagram')
        self.file_open_write('{0} {1}\n'.format('Selected label is',selected_labels))
        for card in instagram_cards:
            user=card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text
            card_labels=card.find_element(By.CLASS_NAME,'card-labels').text.split('/')
            for i in range(len(card_labels)): card_labels[i]=card_labels[i].strip()
            is_label_exist=False
            for lab in selected_labels:
                if lab in card_labels:
                    is_label_exist=True
                    break
            if is_label_exist is False:
                self.file_open_write('{0} {1} {2}\n'.format(selected_labels,'Labels not exist',user))
        self.file_open_write('discover instagram page one label filter controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_043_filter_discover_instagram_one_category_one_label(self):
        self.file_open_write('discover instagram page one category one label filter control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.selenium.find_element(By.ID,'filters').click()
        selected_categories=self.get_select_categories(1)
        selected_labels=self.get_select_labels(1)
        current_url = self.selenium.current_url
        self.selenium.find_element(By.CLASS_NAME,'influencer_filter_btn').click()
        WebDriverWait(self.selenium, 60).until(EC.url_changes(current_url))
        time.sleep(3)
        instagram_cards=self.get_card_details('instagram')
        self.file_open_write('{0} {1} {2} {3}\n'.format('Selected category is',selected_categories,'Selected label is'),selected_labels)
        for card in instagram_cards:
            user=card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text
            card_categories=card.find_element(By.CLASS_NAME,'card-cats').text.split('/')
            card_labels=card.find_element(By.CLASS_NAME,'card-labels').text.split('/')
            for i in range(len(card_categories)): card_categories[i]=card_categories[i].strip()
            for i in range(len(card_labels)): card_labels[i]=card_labels[i].strip()
            is_cat_exist=False
            for cat in selected_categories:
                if cat in card_categories:
                    is_cat_exist=True
                    break
            is_label_exist=False
            for lab in selected_labels:
                if lab in card_labels:
                    is_label_exist=True
                    break
            if is_label_exist is False and is_cat_exist is False:
                if is_label_exist is False:
                    self.file_open_write('{0} {1} {2}\n'.format(selected_labels,'Labels not exist',user))
                if is_cat_exist is False:
                    self.file_open_write('{0} {1} {2}\n'.format(selected_categories,'Category not exist',user))
        self.file_open_write('discover instagram page one category one label filter controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_044_filter_discover_instagram_multi_category(self):
        self.file_open_write('discover instagram page multi category filter control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.selenium.find_element(By.ID,'filters').click()
        selected_categories=self.get_select_categories(random.randint(2,5))
        current_url = self.selenium.current_url
        self.selenium.find_element(By.CLASS_NAME,'influencer_filter_btn').click()
        WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
        time.sleep(3)
        instagram_cards=self.get_card_details('instagram')
        self.file_open_write('{0} {1}\n'.format('Selected categories are',selected_categories))
        for card in instagram_cards:
            user=card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text
            card_categories=card.find_element(By.CLASS_NAME,'card-cats').text.split('/')
            for i in range(len(card_categories)): card_categories[i]=card_categories[i].strip()
            is_cat_exist=False
            for cat in selected_categories:
                if cat in card_categories:
                    is_cat_exist=True
                    break
            if is_cat_exist is False:
                self.file_open_write('{0} {1} {2}\n'.format(selected_categories,'Category not exist',user))
        self.file_open_write('discover instagram page multi category filter controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_045_filter_discover_instagram_multi_label(self):
        self.file_open_write('discover instagram page multi label filter control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.selenium.find_element(By.ID,'filters').click()
        selected_labels=self.get_select_labels(random.randint(2,5))
        current_url = self.selenium.current_url
        self.selenium.find_element(By.CLASS_NAME,'influencer_filter_btn').click()
        WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
        time.sleep(3)
        instagram_cards=self.get_card_details('instagram')
        self.file_open_write('{0} {1}\n'.format('Selected labels are',selected_labels))
        for card in instagram_cards:
            user=card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text
            card_labels=card.find_element(By.CLASS_NAME,'card-labels').text.split('/')
            for i in range(len(card_labels)): card_labels[i]=card_labels[i].strip()
            is_label_exist=False
            for lab in selected_labels:
                if lab in card_labels:
                    is_label_exist=True
                    break
            if is_label_exist is False:
                self.file_open_write('{0} {1} {2}\n'.format(selected_labels,'Labels not exist',user))
        self.file_open_write('discover instagram page filter controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_046_filter_discover_instagram_multi_category_multi_label(self):
        self.file_open_write('discover instagram page filter control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.selenium.find_element(By.ID,'filters').click()
        selected_categories=self.get_select_categories(random.randint(2,5))
        selected_labels=self.get_select_labels(random.randint(2,5))
        current_url = self.selenium.current_url
        self.selenium.find_element(By.CLASS_NAME,'influencer_filter_btn').click()
        WebDriverWait(self.selenium, 60).until(EC.url_changes(current_url))
        time.sleep(3)
        instagram_cards=self.get_card_details('instagram')
        self.file_open_write('{0} {1} {2} {3}\n'.format('Selected categories are',selected_categories,'Selected labels are',selected_labels))
        for card in instagram_cards:
            user=card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text
            card_categories=card.find_element(By.CLASS_NAME,'card-cats').text.split('/')
            card_labels=card.find_element(By.CLASS_NAME,'card-labels').text.split('/')
            for i in range(len(card_categories)): card_categories[i]=card_categories[i].strip()
            for i in range(len(card_labels)): card_labels[i]=card_labels[i].strip()
            is_cat_exist=False
            for cat in selected_categories:
                if cat in card_categories:
                    is_cat_exist=True
                    break
            is_label_exist=False
            for lab in selected_labels:
                if lab in card_labels:
                    is_label_exist=True
                    break
            if is_label_exist is False and is_cat_exist is False:
                if is_label_exist is False:
                    self.file_open_write('{0} {1} {2}\n'.format(selected_labels,'Labels not exist',user))
                if is_cat_exist is False:
                    self.file_open_write('{0} {1} {2}\n'.format(selected_categories,'Category not exist',user))
        self.file_open_write('discover instagram page filter controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_05_discover_instagram_sorts(self):
        self.file_open_write('discover instagram page sort control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.make_sorts('instagram')
        self.file_open_write('discover instagram page sort controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_060_discover_instagram(self):
        self.file_open_write('discover instagram page control started\n')
        self.selenium.get(self.live_server_url+'/discover/instagram')
        self.get_card_details('instagram')
        self.file_open_write('discover instagram page controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_061_discover_tiktok(self):
        self.file_open_write('discover tiktok page control started\n')
        self.selenium.get(self.live_server_url+'/discover/tiktok')
        self.get_card_details('tiktok')
        self.file_open_write('discover tiktok page controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_062_discover_youtube(self):
        self.file_open_write('discover youtube page control started\n')
        self.get_card_details('youtube')
        self.file_open_write('discover youtube page controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_063_discover_twitch(self):
        self.file_open_write('discover twitch page control started\n')
        self.selenium.get(self.live_server_url+'/discover/twitch')
        self.get_card_details('twitch')
        self.file_open_write('discover twitch page controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_064_discover_clubhouse(self):
        self.file_open_write('discover clubhouse page control started\n')
        self.selenium.get(self.live_server_url+'/discover/clubhouse')
        self.get_card_details('clubhouse')
        self.file_open_write('discover clubhouse page controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_065_discover_podcast(self):
        self.file_open_write('discover podcast page control started\n')
        self.selenium.get(self.live_server_url+'/podcast')
        podcast_cards=self.selenium.find_elements(By.CLASS_NAME,'podcast-card')
        for card in podcast_cards:
            description=card.find_element(By.CLASS_NAME,'podcast-description').text
            caption=card.find_element(By.CLASS_NAME,'podcast-caption').text
            tags=card.find_element(By.CLASS_NAME,'podcast-tags').find_elements(By.TAG_NAME,'span')
            user=card.find_element(By.CLASS_NAME,'podcast-publisher').text[3:]
            links=card.find_elements(By.TAG_NAME,'a')
            if(description == ''):
                self.file_open_write('{0} {1} {2}\n'.format(user,' Description: ',description))
            if(caption == ''):
                self.file_open_write('{0} {1} {2}\n'.format(user,' Caption: ',caption))
            if(len(tags) < 1):
                self.file_open_write('{0} {1} {2}\n'.format(user,' No tag: ',tags))
            img_url=card.find_element(By.TAG_NAME,'img').get_attribute('src')
            try:
                r=requests.get(img_url)
                if r.status_code != 200:
                    self.file_open_write('{0} {1} \n'.format(user,r.status_code))
            except Exception as e:
                self.file_open_write('{0} podcast img error: {1}\n'.format(user,e))
                print(e)
            links_set=set()
            for link in links:
                link=link.get_attribute('href')
                links_set.add(link)
            for link in links_set:    
                try:
                    r=requests.get(link)
                    if r.status_code != 200:
                        self.file_open_write('{0} podcast link is not valid. Response status code: {1} {2}\n'.format(user,r.status_code,link))
                    else:
                        self.file_open_write('{0} podcast link status code: {1} {2}\n'.format(user,r.status_code,link))
                except Exception as e:
                    self.file_open_write('{0} podcast link error: {1}\n'.format(user,e))
                    print(e)
        self.get_card_details('instagram')
        self.file_open_write('discover podcast page controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_11_dashboard_story_count(self):
        self.file_open_write('dashboard story count control started\n')
        self.selenium.get(self.live_server_url)
        self.check_404_or_500()
        stories=self.selenium.find_element(By.CLASS_NAME,'story-slider').find_elements(By.CLASS_NAME,'story-contain')#.find_elements(By.TAG_NAME,'div')
        try:
            self.assertGreater(len(stories),2)
        except AssertionError as e:
            self.file_open_write('{0} {1}'.format(e,'\n'))
        self.file_open_write('{0} {1} \n'.format(len(stories),' stories found dashboard'))
        self.file_open_write('dashboard story count controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_12_dashboard_influencer_top_lists(self):
        self.file_open_write('dashboard top lists control started\n')
        self.selenium.get(self.live_server_url)
        self.check_404_or_500()
        inf_lists=self.selenium.find_elements(By.CLASS_NAME,'influencer-lists')
        new_infs=inf_lists[0].find_elements(By.TAG_NAME,'a')
        er_top=inf_lists[1].find_elements(By.TAG_NAME,'a')
        follower_top=inf_lists[2].find_elements(By.TAG_NAME,'a')
        try:
            self.assertEqual(len(new_infs),10)
            self.assertEqual(len(er_top),5)
            self.assertEqual(len(follower_top),5)
        except AssertionError as e:
            self.file_open_write('{0} {1} \n'.format(e,'\n'))
        for a in new_infs:
            img_url=a.find_element(By.CLASS_NAME,'influencer-image').value_of_css_property('background-image')
            #flw=a.find_element(By.CLASS_NAME,'influencer-value').text
            user=a.find_element(By.CLASS_NAME,'influencer-abouts').find_element(By.TAG_NAME,'p').text
            if('http' not in img_url):
                self.file_open_write('{0} {1} \n'.format(user,' has no picture'))
        for a in er_top:
            img_url=a.find_element(By.CLASS_NAME,'influencer-image').value_of_css_property('background-image')
            er_value=a.find_element(By.CLASS_NAME,'influencer-value').text
            user=a.find_element(By.CLASS_NAME,'influencer-abouts').find_element(By.TAG_NAME,'p').text
            if(er_value in self.none_list):
                self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',er_value))
            else:
                try:
                    f_er_value=float(er_value.split('%')[0])
                    if f_er_value<100 and f_er_value>0:
                        print(user,'ER is proper',er_value)
                        self.file_open_write('{0} {1} {2}\n'.format(user,'ER is proper',er_value))
                    else:
                        print(user,'ER is not proper',er_value)
                        self.file_open_write('{0} {1} {2}\n'.format(user,'ER is not proper',er_value))
                except Exception as e:
                    print(user,' ER error: ',e)
                    self.file_open_write(' {0} ER error: {1} {2}\n'.format(user,e,er_value))
            if('http' not in img_url):
                self.file_open_write('{0} {1}\n'.format(a.find_element(By.CLASS_NAME,'influencer-abouts').find_element(By.TAG_NAME,'p').text,' has no picture'))
        for a in follower_top:
            img_url=a.find_element(By.CLASS_NAME,'influencer-image').value_of_css_property('background-image')
            flw=a.find_element(By.CLASS_NAME,'influencer-value').text
            user=a.find_element(By.CLASS_NAME,'influencer-abouts').find_element(By.TAG_NAME,'p').text
            if('http' not in img_url):
                self.file_open_write('{0} {1} \n'.format(a.find_element(By.CLASS_NAME,'influencer-abouts').find_element(By.TAG_NAME,'p').text,' has no picture'))
        self.file_open_write('dashboard top lists controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_13_search_box(self):
        self.file_open_write('search box control started\n')
        self.selenium.get(self.live_server_url)
        self.check_404_or_500()
        search_keys_results=[
            {'key':'gace','results':['larissaburak','tolgacebeciphotography','tolgacevikofficial','gacemerburak']},
            {'key':'asda','results':['muhammedbasdag','sevgitasdanofficial']},
            {'key':'elvin','results':['elvin_odabasipekiyi','elvinaydogdu','elvin']},
        
        ]
        for skr in search_keys_results:
            search_box=self.selenium.find_element(By.ID,'influencerSearchInput')
            for i in skr['key']:
                search_box.send_keys(i)
                time.sleep(0.3)
            time.sleep(2)
            influencer_results=self.selenium.find_element(By.ID,'influencer_results').find_elements(By.TAG_NAME,'li')
            for inf_res in influencer_results:
                img_url=inf_res.find_element(By.CLASS_NAME,'item-photos').value_of_css_property('background-image')
                username=inf_res.find_element(By.CLASS_NAME,'influencer_result_item_username').text[1:]
                if('http' not in img_url):
                    self.file_open_write('{0} {1} \n'.format(username,' user div has no picture'))
                if username in skr['results']:
                    self.file_open_write('{0} {1} \n'.format(username,' user div is exist'))
                else:
                    self.file_open_write('{0} {1} \n'.format(username,' user div is not exist'))
            search_box.submit()
            self.check_404_or_500()
            inf_result_page=WebDriverWait(self.selenium,5).until(EC.visibility_of_element_located((By.ID,'table_results_wrapper'))).find_elements(By.CLASS_NAME,'profile-instagram')
            for inf_res in inf_result_page:
                username=inf_res.find_element(By.CLASS_NAME,'card-spot-instagram').text.split(' ')[1][1:]
                img_url=inf_res.find_element(By.CLASS_NAME,'card-image-instagram').value_of_css_property('background-image')
                if('http' not in img_url):
                    self.file_open_write('{0} {1} \n'.format(username,' user card has no picture'))
                if username in skr['results']:
                    self.file_open_write('{0} {1}\n'.format(username,' user card is exist'))
                else:
                    self.file_open_write('{0} {1} \n'.format(username,' user card is not exist'))
            try:
                self.assertEqual(len(inf_result_page),len(influencer_results))
            except AssertionError as e:
                self.file_open_write('{0} {1} \n'.format(e,'\n'))
        self.file_open_write('search box controlled\n')
    '''def test_14_inf_card_and_detail(self):
        self.selenium.get(self.live_server_url)
        self.check_404_or_500()
        skr={'key':'ekink','result':'ekinkollama'}
        search_box=self.selenium.find_element(By.ID,'influencerSearchInput')
        for i in skr['key']:
            search_box.send_keys(i)
            time.sleep(0.3)
        search_box.submit()
        self.check_404_or_500()
        card=WebDriverWait(self.selenium,30).until(EC.visibility_of_element_located((By.ID,'table_results_wrapper'))).find_element(By.CLASS_NAME,'profile-instagram')
        username=card.find_element(By.CLASS_NAME,'card-spot-instagram').text.split(' ')[1][1:]
        img_url=card.find_element(By.CLASS_NAME,'card-image-instagram').value_of_css_property('background-image')
        hs_value=card.find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[1].text
        er_value=card.find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[2].text
        postf_value=card.find_element(By.CLASS_NAME,'card-parameter-instagram').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[0].text
        avg_reach_value=card.find_element(By.CLASS_NAME,'card-parameter-instagram').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[1].text
        avg_eng_value=card.find_element(By.CLASS_NAME,'card-parameter-instagram').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[2].text
        storyf_value=card.find_element(By.CLASS_NAME,'card-parameter-instagram').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[3].text
        user=card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text
        if(hs_value in self.none_list ):
            self.file_open_write('{0} {1} {2}\n'.format(user,' HS: ',hs_value))
        else:
            try:
                f_hs_value=float(hs_value)
                if f_hs_value<=10 and f_hs_value>0:
                    print(user,'HS is proper',hs_value)
                    self.file_open_write('{0} {1} {2}\n'.format(user,'HS is proper',hs_value))
                else:
                    print(user,'HS is not proper',hs_value)
                    self.file_open_write('{0} {1} {2}\n'.format(user,'HS is not proper',hs_value))
            except Exception as e:
                print(user,' HS error: ',e)
                self.file_open_write(' {0} Hs error: {1} {2}\n'.format(user,e,hs_value))
        if(er_value in self.none_list):
            self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',er_value))
        else:
            try:
                f_er_value=float(er_value.split('%')[0])
                if f_er_value<100 and f_er_value>0:
                    print(user,'ER is proper',er_value)
                    self.file_open_write('{0} {1} {2}\n'.format(user,'ER is proper',er_value))
                else:
                    print(user,'ER is not proper',er_value)
                    self.file_open_write('{0} {1} {2}\n'.format(user,'ER is not proper',er_value))
            except Exception as e:
                print(user,' ER error: ',e)
                self.file_open_write(' {0} ER error: {1} {2}\n'.format(user,e,er_value))
        if(postf_value in self.none_list):
            self.file_open_write('{0} {1} {2}\n'.format(user,' Post F: ',postf_value))
        if(avg_reach_value in self.none_list):
            self.file_open_write('{0} {1} {2}\n'.format(user,' Avg Reach: ',avg_reach_value))
        if(avg_eng_value in self.none_list):
            self.file_open_write('{0} {1} {2}\n'.format(user,' Avg Eng: ',avg_eng_value))
        if(storyf_value in self.none_list):
            self.file_open_write('{0} {1} {2}\n'.format(user,' Story F: ',storyf_value))
        img_url=card.find_element(By.CLASS_NAME,'card-image-instagram').value_of_css_property('background-image')
        if('http' not in img_url):
            self.file_open_write('{0} {1}\n'.format(user,' has no picture'))
        if username in skr['result']:
            self.file_open_write('{0} {1}\n'.format(username,' user card is exist'))
        else:
            self.file_open_write('{0} {1} \n'.format(username,' user card is not exist'))
        
        #search_box.send_keys(Keys.ENTER)'''
    def test_15_cross_analysis(self):
        self.selenium.get(self.live_server_url+'/cross_analysis')
        select_list=Select(self.selenium.find_element(By.ID,'cross_lists'))
        select_list.select_by_index(0)
        self.selenium.find_element(By.ID,'crossAnalysisForm').find_element(By.TAG_NAME,'button').click()
        table=WebDriverWait(self.selenium,30).until(EC.visibility_of_element_located((By.TAG_NAME,'table'))).get_attribute('innerHTML')
        try:
            self.assertIsNotNone(table)
        except AssertionError as e:
            self.file_open_write('{0} {1} \n'.format(e,'\n'))
        self.file_open_write('cross analysis controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time)) 
    def test_16_targeted_analysis(self):
        self.selenium.get(self.live_server_url+'/targeted_analysis')
        self.selenium.find_element(By.CLASS_NAME,'targetedForm').find_elements(By.TAG_NAME,'li')[5].click()
        self.selenium.find_element(By.XPATH,'//button[text()="START SCAN"]').click()
        WebDriverWait(self.selenium,30).until(EC.visibility_of_element_located((By.CLASS_NAME,'profile-instagram')))
        cards=self.selenium.find_elements(By.CLASS_NAME,'profile-instagram')
        for card in cards:
            hs_value=card.find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[1].text
            er_value=card.find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[2].text
            postf_value=card.find_element(By.CLASS_NAME,'card-parameter-instagram').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[0].text
            avg_reach_value=card.find_element(By.CLASS_NAME,'card-parameter-instagram').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[1].text
            avg_eng_value=card.find_element(By.CLASS_NAME,'card-parameter-instagram').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[2].text
            user=card.find_element(By.CLASS_NAME,'card-spot-instagram').find_element(By.TAG_NAME,'a').text
            if(hs_value in self.none_list ):
                self.file_open_write('{0} {1} {2}\n'.format(user,' HS: ',hs_value))
            else:
                try:
                    f_hs_value=float(hs_value)
                    if f_hs_value<=10 and f_hs_value>0:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'HS is proper',hs_value))
                    else:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'HS is not proper',hs_value))
                except Exception as e:
                    self.file_open_write(' {0} Hs error: {1} {2}\n'.format(user,e,hs_value))
            if(er_value in self.none_list):
                self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',er_value))
            else:
                try:
                    f_er_value=float(er_value.split('%')[0])
                    if f_er_value<100 and f_er_value>0:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'ER is proper',er_value))
                    else:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'ER is not proper',er_value))
                except Exception as e:
                    self.file_open_write(' {0} ER error: {1} {2}\n'.format(user,e,er_value))
            if(postf_value in self.none_list):
                self.file_open_write('{0} {1} {2}\n'.format(user,' Post F: ',postf_value))
            if(avg_reach_value in self.none_list):
                self.file_open_write('{0} {1} {2}\n'.format(user,' Avg Reach: ',avg_reach_value))
            if(avg_eng_value in self.none_list):
                self.file_open_write('{0} {1} {2}\n'.format(user,' Avg Eng: ',avg_eng_value))
            img_url=card.find_element(By.CLASS_NAME,'card-image-instagram').value_of_css_property('background-image')
            if('http' not in img_url):
                self.file_open_write('{0} {1}\n'.format(user,' has no picture'))
        self.file_open_write('target analysis controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def test_17_post_analysis(self):
        self.selenium.get(self.live_server_url+'/post_analysis')
        count=0
        while count<5:
            user=self.selenium.find_element(By.CLASS_NAME,'post-analysis-influencer-abouts').find_element(By.TAG_NAME,'p').text
            user_url=self.selenium.find_element(By.CLASS_NAME,'post-analysis-influencer-abouts').find_element(By.TAG_NAME,'a').get_attribute('href')
            img_url=self.selenium.find_element(By.CLASS_NAME,'post-analysis-influencer-image').value_of_css_property('background-image')
            self.file_open_write('{0} {1} \n'.format(user,' post analysis'))
            r=requests.get(user_url)
            if r.status_code==200:
                self.file_open_write('user response is 200\n')
            else:
                self.file_open_write('{0} {1} \n'.format('user has no response. response code: ',r.status_code))
                continue
            if('http' not in img_url):
                self.file_open_write('{0} {1} \n'.format(user,' has no picture'))
            stories=WebDriverWait(self.selenium,60).until(EC.visibility_of_element_located((By.CLASS_NAME,'story-slider'))).find_elements(By.CLASS_NAME,'story-contain')
            if len(stories) > 0:
                self.file_open_write('{0} {1} \n'.format('Stories found',len(stories)))
                count=5
                try:
                    self.assertGreater(len(stories),0)
                except AssertionError as e:
                    self.file_open_write('{0} {1} \n'.format(e,'\n'))
            else:    
                alert=self.selenium.find_element(By.CLASS_NAME,'story-slider').find_element(By.CLASS_NAME,'alert')
                if alert:
                    self.file_open_write('{0} {1} \n'.format(alert.text,'\n'))
                count+=1
                if count == 4:
                    self.selenium.get(self.live_server_url+'/post_analysis?influencer=735')
                else:
                    self.file_open_write('{0} {1} \n'.format(count,'page refreshed'))
                    self.selenium.refresh()
                
        WebDriverWait(self.selenium,180).until(EC.visibility_of_element_located((By.CLASS_NAME,'post-container-detail')))
        posts=self.selenium.find_elements(By.CLASS_NAME,'post-container-detail')
        if len(posts)>0:
            self.file_open_write('{0} {1} {2}\n'.format('Posts found',len(posts),'\n'))
            try:
                self.assertGreater(len(posts),0)
            except AssertionError as e:
                self.file_open_write('{0} {1} \n'.format(e,'\n'))
        for post in posts:
            info=post.find_element(By.CLASS_NAME,'profile-post-like-comment').text.split(' ')
            like=info[0]
            comment=info[1][0:len(info[1])-2]
            er_value=info[2]
            reach=info[3]
            if like in self.none_list:
                self.file_open_write('{0} {1} \n'.format('like '+like))
            if comment in self.none_list:
                self.file_open_write('{0} {1} \n'.format('comment '+comment))
            if(er_value in self.none_list):
                self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',er_value))
            else:
                try:
                    f_er_value=float(er_value.split('%')[0])
                    if f_er_value<100 and f_er_value>0:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'ER is proper',er_value))
                    else:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'ER is not proper',er_value))
                except Exception as e:
                    self.file_open_write(' {0} ER error: {1} {2}\n'.format(user,e,er_value))
            if reach in self.none_list:
                self.file_open_write('{0} {1} \n'.format('reach '+reach))
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time)) 
    def test_18_competetion_analysis_results(self):
        self.selenium.get(self.live_server_url+'/competition_analysis')
        self.check_404_or_500()
        is_elem_present=False
        time_count=0
        while(is_elem_present is False):
            try:
                first_row_match=self.selenium.find_elements(By.CLASS_NAME,'competitor-row')[1].find_element(By.CLASS_NAME,'match')
                is_elem_present=True
            except NoSuchElementException:
                time.sleep(30)
                is_elem_present=False
                self.selenium.refresh()
                time_count+=1
                self.file_open_write('{0} {1} \n'.format(time_count,'page refreshed'))
            if(time_count>30):
                self.file_open_write('Competetion analysis 15 min Timeout\n')
                return False
        
        url=first_row_match.find_element(By.TAG_NAME,'a').get_attribute('href')
        response=requests.get(url)
        self.file_open_write('{0} {1} \n'.format(url,response.status_code))
        try:
            self.assertEqual(response.status_code,200)
        except AssertionError as e:
            self.file_open_write('{0} {1} \n'.format(e,'\n'))
        self.file_open_write('competetion analysis controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))      
    def test_19_sector_analysis_results(self):
        self.selenium.get(self.live_server_url+'/sector_analysis')
        self.check_404_or_500()
        is_elem_present=False
        time_count=0
        while(is_elem_present is False):
            try:
                first_row_match=self.selenium.find_elements(By.CLASS_NAME,'competitor-row')[1].find_element(By.CLASS_NAME,'match')
                is_elem_present=True
            except NoSuchElementException:
                time.sleep(30)
                is_elem_present=False
                self.selenium.refresh()
                time_count+=1
                self.file_open_write('{0} {1} \n'.format(time_count,'page refreshed'))
            if(time_count>30):
                self.file_open_write('Sector analysis 15 min Timeout\n')
                return False
        try:
            url=first_row_match.find_element(By.TAG_NAME,'span').find_element(By.TAG_NAME,'a').get_attribute('href')
            response=requests.get(url)
            self.file_open_write('{0} {1} \n'.format(url,response.status_code))
            self.assertEqual(response.status_code,200)
        except NoSuchElementException:
            self.file_open_write('Sector analysis No Matches\n')
        except AssertionError as e:
            self.file_open_write('{0} {1} \n'.format(e,'\n'))
        self.file_open_write('sector analysis controlled\n')
        self.file_open_write("{:0.3f} seconds\n".format(time.time()-self.start_time))
    def get_select_categories(self,count):
        self.selenium.find_element(By.XPATH,'//button[@data-id="categories"]').click()
        categories=self.selenium.find_element(By.XPATH,'//button[@data-id="categories"]/following-sibling::div').find_elements(By.TAG_NAME,'li')
        random_categories_indexes=random.sample(range(0,len(categories) ), count)
        selected_categories=[]
        for r in random_categories_indexes:
            categories[r].click()
            selected_categories.append(categories[r].text)
        return selected_categories
    def get_select_labels(self,count):
        self.selenium.find_element(By.XPATH,'//button[@data-id="labels"]').click()
        labels=self.selenium.find_element(By.XPATH,'//button[@data-id="labels"]/following-sibling::div').find_elements(By.TAG_NAME,'li')
        random_labels_indexes=random.sample(range(0,len(labels) ), count)
        selected_labels=[]
        for r in random_labels_indexes:
            labels[r].click()
            selected_labels.append(labels[r].text)
        return selected_labels
    def check_404_or_500(self):
        try:
            blank_page=self.selenium.find_element(By.CLASS_NAME,'blank-page-images')
            img_url=blank_page.value_of_css_property('background-image')
            if('images/404.' in img_url):
                self.file_open_write('404 page not found\n')
                self.assertEqual(0,1)
            if('images/500.' in img_url):
                self.file_open_write('500 response\n')
                self.assertEqual(0,1)
        except NoSuchElementException:
            self.file_open_write('There is no 404 & 500\n')
            return True
        except AssertionError as e:
            self.file_open_write('{0} {1} \n'.format(e,'\n'))
    def get_all_links_on_page(self):
        elems=self.selenium.find_elements_by_tag_name('a')
        current_url = self.selenium.current_url
        hrefs=set()
        for elem in elems:
            href=elem.get_attribute("href")
            if href is not None:
                if 'www.hyperiser.com' in href:
                    hrefs.add(href)
        for href in hrefs:
            index=-1
            for i,link in enumerate(self.all_links):
                if href in link['link']:
                    index = i
                    break
            if index != -1: #daha önce link listeye eklenmiş
                self.all_links[index]['pages'].add(current_url)
            else:
                my_dict = {#yeni bir link eklemek için
                    'link': href,
                    'pages': {current_url}
                }
                self.all_links.append(my_dict)
    def get_card_details(self,platform):
        WebDriverWait(self.selenium,30).until(EC.visibility_of_element_located((By.CLASS_NAME,('profile-'+platform))))
        cards=self.selenium.find_elements(By.CLASS_NAME,('profile-'+platform))
        for card in cards:
            hs_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[1].text
            user=card.find_element(By.CLASS_NAME,'card-spot-'+platform).find_element(By.TAG_NAME,'a').text
            user_url=card.find_element(By.CLASS_NAME,'card-spot-'+platform).find_element(By.TAG_NAME,'a').get_attribute('href')
            img_url=card.find_element(By.CLASS_NAME,'card-image-'+platform).value_of_css_property('background-image')
            try:
                r=requests.get(user_url)
                if r.status_code==200:
                    self.file_open_write('{0} {1} \n'.format(user,'response code: 200'))
                else:
                    self.file_open_write('{0} {1} {2}\n'.format(user,'has no response. response code: ',r.status_code))
                    continue
            except Exception as e:
                print(e)
                self.file_open_write('{0} Error: {1} {2}\n'.format(user,e,user_url))
            if('http' not in img_url):
                self.file_open_write('{0} {1}\n'.format(user,' has no picture'))
            else:
                img_url=img_url[5:len(img_url)-2]
                try:
                    r=requests.get(img_url)
                    if r.status_code != 200:
                        self.file_open_write('{0} {1} {2}\n'.format(user,r.status_code,' has no picture'))
                except Exception as e:
                    self.file_open_write('{0} Error: {1} {2}\n'.format(user,e,' has no picture'))
            if(hs_value in self.none_list ):
                self.file_open_write('{0} {1} {2}\n'.format(user,' Error HS: ',hs_value))
            else:
                try:
                    f_hs_value=float(hs_value)
                    if f_hs_value<=10 and f_hs_value>0:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'HS is proper',hs_value))
                    else:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'HS is not proper',hs_value))
                except Exception as e:
                    self.file_open_write(' {0} Hs error: {1} {2}\n'.format(user,e,hs_value))
            if platform=='instagram':
                flw_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[0].text
                er_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[2].text
                if flw_value in self.none_list:
                    self.file_open_write('{0} {1} {2}\n'.format(user,' Follower Count: ',flw_value))
                else:
                    if ('K' in flw_value or 'M' in flw_value) is False:
                        self.file_open_write('{0} {1} {2}\n'.format(user,'follower lower than 1K:',flw_value))
                if(er_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',er_value))
                else:
                    try:
                        f_er_value=float(er_value.split('%')[0])
                        if f_er_value<100 and f_er_value>0:
                            self.file_open_write('{0} {1} {2}\n'.format(user,'ER is proper',er_value))
                        else:
                            self.file_open_write('{0} {1} {2}\n'.format(user,'ER is not proper',er_value))
                    except Exception as e:
                        self.file_open_write(' {0} ER error: {1} {2}\n'.format(user,e,er_value))
                postf_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[0].text
                if(postf_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' Post F: ',postf_value))
                avg_reach_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[1].text
                if(avg_reach_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' Avg Reach: ',avg_reach_value))
                avg_eng_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[2].text
                if(avg_eng_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' Avg Eng: ',avg_eng_value))
                try:
                    storyf_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[3].text
                    if(storyf_value in self.none_list):
                        self.file_open_write('{0} {1} {2}\n'.format(user,'Story F:',storyf_value))
                except Exception as e:
                    self.file_open_write('{0} there is no story freq. div\n'.format(user))
            elif platform == 'tiktok':
                flw_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[0].text
                er_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[2].text
                if flw_value in self.none_list:
                    self.file_open_write('{0} {1} {2}\n'.format(user,' Follower Count: ',flw_value))
                if(er_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',er_value))
                else:
                    try:
                        f_er_value=float(er_value.split('%')[0])
                        if f_er_value<100 and f_er_value>0:
                            self.file_open_write('{0} {1} {2}\n'.format(user,'ER is proper',er_value))
                        else:
                            self.file_open_write('{0} {1} {2}\n'.format(user,'ER is not proper',er_value))
                    except Exception as e:
                        self.file_open_write(' {0} ER error: {1} {2}\n'.format(user,e,er_value))
                avg_views_value=card.find_element(By.CLASS_NAME,'card-parameter-tiktok').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[0].text
                if(avg_views_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_views_value: ',avg_views_value))
                avg_likes_value=card.find_element(By.CLASS_NAME,'card-parameter-tiktok').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[1].text
                if(avg_likes_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_likes_value: ',avg_likes_value))
                avg_comments_value=card.find_element(By.CLASS_NAME,'card-parameter-tiktok').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[2].text
                if(avg_comments_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_comments_value: ',avg_comments_value))
                avg_shares_value=card.find_element(By.CLASS_NAME,'card-parameter-tiktok').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[3].text
                if( avg_shares_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_shares_value: ',avg_shares_value))
            elif platform == 'youtube':
                sub_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[0].text
                er_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[2].text
                if sub_value in self.none_list:
                    self.file_open_write('{0} {1} {2}\n'.format(user,' Subscriber Count: ',sub_value))
                if(er_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',er_value))
                else:
                    try:
                        f_er_value=float(er_value.split('%')[0])
                        if f_er_value<100 and f_er_value>0:
                            self.file_open_write('{0} {1} {2}\n'.format(user,'ER is proper',er_value))
                        else:
                            self.file_open_write('{0} {1} {2}\n'.format(user,'ER is not proper',er_value))
                    except Exception as e:
                        self.file_open_write(' {0} ER error: {1} {2}\n'.format(user,e,er_value))
                avg_views_value=card.find_element(By.CLASS_NAME,'card-parameter-twitch').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[0].text
                peak_views_value=card.find_element(By.CLASS_NAME,'card-parameter-twitch').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[1].text
                hours_stream_value=card.find_element(By.CLASS_NAME,'card-parameter-twitch').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[2].text
                hours_watch_value=card.find_element(By.CLASS_NAME,'card-parameter-twitch').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[3].text
                if(avg_views_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_views_value: ',avg_views_value))
                if(peak_views_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_likes_value: ',peak_views_value))
                if(hours_stream_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_comments_value: ',hours_stream_value))
                if(hours_watch_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_shares_value: ',hours_watch_value))
            elif platform == 'twitch':
                flw_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[0].text
                view_count=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[2].text
                if flw_value in self.none_list:
                    self.file_open_write('{0} {1} {2}\n'.format(user,' Follower Count: ',flw_value))
                if(view_count in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',view_count))
                avg_views_value=card.find_element(By.CLASS_NAME,'card-parameter-twitch').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[0].text
                peak_views_value=card.find_element(By.CLASS_NAME,'card-parameter-twitch').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[1].text
                hours_stream_value=card.find_element(By.CLASS_NAME,'card-parameter-twitch').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[2].text
                hours_watch_value=card.find_element(By.CLASS_NAME,'card-parameter-twitch').find_element(By.CLASS_NAME,'attr-values').find_elements(By.TAG_NAME,'li')[3].text
                if(avg_views_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_views_value: ',avg_views_value))
                if(peak_views_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_likes_value: ',peak_views_value))
                if(hours_stream_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_comments_value: ',hours_stream_value))
                if(hours_watch_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' avg_shares_value: ',hours_watch_value))
            elif platform == 'clubhouse':
                follower_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[0].text
                following_value=card.find_element(By.CLASS_NAME,'card-parameter-'+platform).find_element(By.CLASS_NAME,'hsfwer').find_elements(By.TAG_NAME,'p')[2].text
                if follower_value in self.none_list:
                    self.file_open_write('{0} {1} {2}\n'.format(user,' Follower Count: ',follower_value))
                if(following_value in self.none_list):
                    self.file_open_write('{0} {1} {2}\n'.format(user,' ER: ',following_value))

        return cards
    def delete_from_list(self):
        inf_rights=self.selenium.find_elements(By.CLASS_NAME,'influencer-right')
        prv_len_infs=len(inf_rights)
        rand_inf_index=random.randint(0,prv_len_infs-1)
        inf_nick=self.selenium.find_elements(By.CLASS_NAME,'influencer-nick')[rand_inf_index].text
        inf_social=self.selenium.find_elements(By.CLASS_NAME,'influencer-social')[rand_inf_index].find_element(By.TAG_NAME,'a').get_attribute('href')
        self.selenium.execute_script("arguments[0].scrollIntoView();", inf_rights[rand_inf_index])
        time.sleep(1)
        inf_rights[rand_inf_index].find_element(By.CLASS_NAME,'remove_influencer_button').click()
        wait_count=0
        while(wait_count<30 and prv_len_infs==len(inf_rights)):
            inf_rights=self.selenium.find_elements(By.CLASS_NAME,'influencer-right')
            time.sleep(0.1)
            wait_count+=1
        if prv_len_infs!=len(inf_rights):
            print(inf_nick,'Influencer deleted from list. Social href: ',inf_social)
    def delete_list(self):
        current_url = self.selenium.current_url
        list_name=self.selenium.find_element(By.ID,'listTitle').text
        self.selenium.find_element(By.CLASS_NAME,'remove_list_button').click()
        WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
        time.sleep(1)
        lists=self.selenium.find_elements(By.CLASS_NAME,'list-title')
        for name in lists:
            name=name.text
            if name.lower() == list_name.lower():
                print(list_name,'List not deleted')
    def click_add_list_button(self,card,platform,list_name):
        self.scroll_and_click(card.find_element(By.CLASS_NAME,'card-detail-btn'))
        time.sleep(1)
        card.find_element(By.CLASS_NAME,'hover-'+platform).find_element(By.CLASS_NAME,'addToList').click()
        list_names=self.selenium.find_elements(By.CLASS_NAME,'list_name')
        list_div=None
        for ln in list_names:
            print(ln.text,list_name)
            if ln.text==list_name:
                list_div=ln
                print('There is list called',list_name)
                break
        if list_div is None:
            print('List not exist')
            input=self.selenium.find_element(By.CLASS_NAME,'list_name_input')
            input.send_keys(list_name)
            self.selenium.find_element(By.CLASS_NAME,'create_and_add_button').click()
        else:
            list_div.click()
    def file_open_write(self,text):
        with open(self.file_name, "a") as file:
            file.write(text)
    def scroll_and_click(self,element):
        self.selenium.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        element.click()
    def make_sorts(self,platform):
        self.selenium.find_element(By.ID,'sortby').click()
        sorts=self.selenium.find_element(By.CLASS_NAME,'influencer-sort').find_elements(By.TAG_NAME,'div')
        for a in range(len(sorts)*2):
            index=int(a/2)
            sorts=self.selenium.find_element(By.CLASS_NAME,'influencer-sort').find_elements(By.TAG_NAME,'div')
            current_url = self.selenium.current_url
            self.file_open_write('{0} {1} \n'.format(sorts[index].text,' sort is started'))
            sorts[index].click()
            WebDriverWait(self.selenium, 30).until(EC.url_changes(current_url))
            time.sleep(3)
            self.get_card_details(platform)


#m=MySeleniumTests()