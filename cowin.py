from beepy import beep
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' #REplace with your firefox binary path
driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)# Change this to your own geckodriver path!
sleep(2)
driver.get('https://www.cowin.gov.in/home')
sleep(3)
search_by_district = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[1]/div/label/div')
search_by_district.click()
sleep(1)
state = driver.find_element_by_xpath('//*[@id="mat-select-0"]')
state.click()
sleep(1)
maharashtra = driver.find_element_by_xpath('//*[@id="mat-option-21"]')#Replace with your state's option xpath
maharashtra.click()
sleep(1)
district = driver.find_element_by_xpath('//*[@id="mat-select-2"]')
district.click()
sleep(1)
nanded = driver.find_element_by_xpath('//*[@id="mat-option-55"]')#Replace with your district's option xpath
nanded.click()
sleep(1)


def search_for_availability():
    found = False
    search = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[3]/button')
    search.click()
    sleep(1)
    young_adult = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[3]/div/div[1]/label')
    young_adult.click()
    sleep(0.5)
    rows = driver.find_elements_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[6]/div/div/div')

    for each in rows:
        centre_text = each.find_elements_by_class_name('center-name-text')
        slot_available = each.find_elements_by_class_name('slot-available-wrap')
        for i in range(0, len(centre_text)):
            availabilities = slot_available[i].find_elements_by_tag_name('a')
            for each in availabilities:
                if each.text != 'NA' and each.text != 'Booked':
                    print(centre_text[i].text, each.text)
                    beep(5)
                    beep(2)
                    beep(3)
                    beep(6)
                    #found = True


    if not found:
        print('searching again..')
        search_for_availability()

search_for_availability()