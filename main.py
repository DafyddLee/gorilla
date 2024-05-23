import selenium
import selenium.webdriver
import streamlit as st
import time 
st.title('Gorilla')

driver = selenium.webdriver.Chrome()
            
# Navigate to the website
website = 'https://trakcarelabwebview.nhls.ac.za/trakcarelab/csp/system.Home.cls#/Component/SSUser.Logon'
driver.get(website)

time.sleep(5)
driver.quit()
