from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import string

# Creating a webdriver instance
driver = webdriver.Chrome("/Volumes/Macintosh HD - Data/learning/python/webscrape/chromedriver")
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://www.linkedin.com/login")


# waiting for the page to load
time.sleep(5)

# # entering username
username = driver.find_element_by_id("username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("shravan.venkatesan@gmail.com")

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("Vinyas@416")		

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.

alphabets_lst = list(string.ascii_lowercase)
looper_dict={}
for alphabet in alphabets_lst:    
    list_url = f"https://www.linkedin.com/directory/companies/{alphabet}-1?trk=companies_directory_page_num_nav"
    driver.get(list_url)

    src = driver.page_source
    # Now using beautiful soup
    soup = BeautifulSoup(src, 'lxml')

    a = soup.find_all('a', {'class': 'pagination-links__link'})
    looper_dict[alphabet] =a[-1].get_text()



for alaphab,rang in looper_dict.items():
    file_name=f"csv/{alaphab}.csv"
    with open (file_name,"w",newline ='') as f:
        csvwriter = csv.writer(f)

    # csvwriter.writerow(alaphab) 
        company_name_lst=[]
        for i in range(1,int(rang)+1):
            print(f"https://www.linkedin.com/directory/companies/{alaphab}-{i}?trk=companies_directory_page_num_nav")
            list_url = f"https://www.linkedin.com/directory/companies/{alaphab}-{i}?trk=companies_directory_page_num_nav"
            driver.get(list_url)

            src = driver.page_source
            # Now using beautiful soup
            soup = BeautifulSoup(src, 'lxml')
            ul = soup.find('ul', {'class': 'listings'})
            li = ul.findChildren("li" , recursive=False)


            for child in li:
                child_list=[child.text.strip()]
                company_name_lst.append(child_list)


            file_name="companies.csv"
            headings= list(string.ascii_lowercase)
            list_companies=[]

        
        csvwriter.writerows(company_name_lst)

