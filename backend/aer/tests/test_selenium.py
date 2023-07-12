from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import unittest

# E2E tests in selenium with python WebDriver
class PythonTes(unittest.TestCase):
    def setUp(self):
        chroptions=Options()
        chroptions.add_argument('--ignore-certificate-errors-spki-list')
        chroptions.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(options=chroptions)
 
    # Test cases
    def test_check_image_mode_negative(self):
        driver = self.driver
        driver.get('http://localhost:3000/')
        driver.find_element(By.XPATH,"// a[contains(text(),\'Upload image')]").click()
        assert driver.page_source.find("Image") 
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/form/div/input").click()
        assert driver.page_source.find("Wypełnij to pole")

    def test_check_video_mode_negative(self):
        driver = self.driver
        driver.get('http://localhost:3000/')
        driver.find_element(By.XPATH,"// a[contains(text(),\'Upload video')]").click()
        assert driver.page_source.find("Video") 
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/form/div/input").click()
        assert driver.page_source.find("Wypełnij to pole")

    def test_check_sending_message_in_contact_page(self):
        driver = self.driver
        driver.get('http://localhost:3000/')
        driver.find_element(By.XPATH,"// a[contains(text(),\'Contact')]").click()
        assert driver.page_source.find("Contact:") 
        driver.find_element(By.XPATH,"//*[@id='contact-form']/div[1]/input").send_keys("name_selenium")
        driver.find_element(By.XPATH,"//*[@id='contact-form']/div[2]/input").send_keys("email_selenium@mail.com")
        driver.find_element(By.XPATH,"//*[@id='contact-form']/div[3]/textarea").send_keys("message_selenium")
        driver.find_element(By.XPATH,"//*[@id='contact-form']/div[4]/button").click()
        time.sleep(1)
        text1=driver.find_element(By.XPATH,"//*[@id='contact-form']/div[1]/input").text
        text2=driver.find_element(By.XPATH,"//*[@id='contact-form']/div[2]/input").text
        text3=driver.find_element(By.XPATH,"//*[@id='contact-form']/div[3]/textarea").text
        self.assertEqual(text1,'')
        self.assertEqual(text2,'')
        self.assertEqual(text3,'')

    def test_check_image_mode(self):
        driver = self.driver
        driver.get('http://localhost:3000/')
        driver.find_element(By.XPATH,"// a[contains(text(),\'Upload image')]").click()
        assert driver.page_source.find("Image") 
        driver.find_element(By.XPATH,"//*[@id='title']").send_keys("test_image_with_selenium")
        driver.find_element(By.XPATH,"//*[@id='image']").send_keys(os.getcwd()+'\\testdata\\testimage\\2.jpg')
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/form/div/input").click()
        time.sleep(2)
        assert driver.page_source.find("Download") 
        assert driver.page_source.find("Reupload")
        driver.find_element(By.XPATH,"// a[contains(text(),\'History')]").click()
        first_record=driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]").text
        self.assertEqual(first_record,'test_image_with_selenium')

    def test_check_video_mode(self):
        driver = self.driver
        driver.get('http://localhost:3000/')
        driver.find_element(By.XPATH,"// a[contains(text(),\'Upload video')]").click()
        assert driver.page_source.find("Video") 
        driver.find_element(By.XPATH,"//*[@id='title']").send_keys("test_video_with_selenium")
        driver.find_element(By.XPATH,"//*[@id='image']").send_keys(os.getcwd()+'\\testdata\\testvideo\\video.mp4')
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/form/div/input").click()
        time.sleep(15)
        assert driver.page_source.find("Download") 
        assert driver.page_source.find("Reupload")
        driver.find_element(By.XPATH,"// a[contains(text(),\'History')]").click()
        first_record=driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]").text
        self.assertEqual(first_record,'test_video_with_selenium')

    def test_about_page_display(self):
        driver=self.driver
        driver.get('http://localhost:3000/')
        driver.find_element(By.XPATH,"// a[contains(text(),\'About')]").click()
        assert driver.page_source.find("What is AER app?")
        assert driver.page_source.find("Defined requests: GET, DELETE and POST")
        assert driver.page_source.find("I. Image mode")
        assert driver.page_source.find("II. Video mode")

    def test_check_history_filters(self):
        driver = self.driver
        driver.get('http://localhost:3000/')
        driver.find_element(By.XPATH,"// a[contains(text(),\'History')]").click()
        assert driver.page_source.find("Image") 
        assert driver.page_source.find("Video") 
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/div/div[1]/button[1]").click()
        time.sleep(1)
        assert driver.page_source.find("Image")  
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/div/div[1]/button[2]").click()
        time.sleep(1)
        assert driver.page_source.find("Video") 
    def tearDown(self):
        self.driver.close()

'''
    def test_check_history_delete(self):
        driver = self.driver
        driver.get('http://localhost:3000/')
        driver.find_element(By.XPATH,"// a[contains(text(),\'History')]").click()
        assert driver.page_source.find("Image") 
        assert driver.page_source.find("Video") 
        time.sleep(2)
        title_before=driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]").text
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/div/td[2]/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div[2]/button[2]").click()
        time.sleep(1)
        title_after=driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]").text
        self.assertNotEqual(title_before,title_after)
'''

if __name__ == "__main__":
    unittest.main()
