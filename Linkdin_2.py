#import web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from validate_email import validate_email


# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(executable_path=r"path")
driver.implicitly_wait(1)
# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')
# locate email form by_class_name
username = driver.find_element_by_name('session_key')


# send_keys() to simulate key strokes
username.send_keys('email')

# locate password form by_class_name
password = driver.find_element_by_name('session_password')

# send_keys() to simulate key strokes
password.send_keys('password')

# locate submit button by_class_name('sign-in-form__submit-btn')
log_in_button = driver.find_elements_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
#for button in log_in_button:
 #   button.click()

log_in_button[2].click()

driver.get('https://www.google.com')

# locate search form by_name
search_query = driver.find_element_by_name('q')

company = input("Enter company name: ")
#company = "intel"

# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com/in/ ' + company)

# .send_keys() to simulate the return key
search_query.send_keys(Keys.RETURN)
names = []
position = []
## Loop for pages
##for i in range(10):
##
#    linkedin_urls = driver.find_elements_by_class_name('LC20lb')
#    linkedin_urls = [url.text for url in linkedin_urls]
#
#
 #   for name in linkedin_urls:
  #      names.append(name.split(" ")[0]+ " " +name.split(" ")[1])
  #      position.append(name.split("-")[1])
#
 #   next_page = driver.find_element_by_xpath('//*[@type="Next"]')
  #  next_page.click()

## remove 5 next lines when returning the loop
linkedin_urls = driver.find_elements_by_class_name('LC20lb')
linkedin_urls = [url.text for url in linkedin_urls]


for name in linkedin_urls:
    names.append(name.split(" ")[0]+ " " +name.split(" ")[1])
    if len(name.split("-")) > 1: position.append( name.split("-")[1])
    else: position.append(name.split(" ")[3] + " " + name.split(" ")[4])


print(names)
print(position)




##Generate emails list from names
list_of_emails = []
for name in names:
    first , last = name.split(" ")
    list_of_emails.append(first+"."+last+"@"+company+".com")
    list_of_emails.append(first + last + "@" + company + ".com")


print(list_of_emails)

#Validate emails and save only the good ones
validate_emails = []

#for email in list_of_emails:
#    if validate_email(email):
#        validate_emails.append(email)

for name , pos in zip(names , position) :
    print(name + " is the " + pos + " of "+ company)