import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st
import time




def authenticate():
    try:
        # Setup Selenium WebDriver

        
        

        with st.spinner('Logging in ...'):

        # Update your Chrome WebDriver initialization with these options
            driver = webdriver.Chrome()
        
            
        # Navigate to the website
            website = 'https://trakcarelabwebview.nhls.ac.za/trakcarelab/csp/system.Home.cls#/Component/SSUser.Logon'
            driver.get(website)


            # Wait for the login page elements
            wait = WebDriverWait(driver,10)
            username_id = "SSUser_Logon_0-item-USERNAME"
            password_id = "SSUser_Logon_0-item-PASSWORD"
            username_element = wait.until(EC.presence_of_element_located((By.ID, username_id)))
            password_element = wait.until(EC.presence_of_element_located((By.ID, password_id)))

            # Enter the credentials
            username_element.clear()
            username_element.send_keys(st.session_state.username)
            password_element.clear()
            password_element.send_keys(st.session_state.password + Keys.ENTER) 
            ## This is where the credentials are send. If the credentials are wrong there will be an error at STEP 1

            # Add your scraping logic here
            # For demonstration, let's wait for a new page element that indicates a successful login


            wait = WebDriverWait(driver,3)
            record_id = "web_DEBDebtor_FindList_0-item-HospitalMRN"
            record_element = wait.until(EC.presence_of_element_located((By.ID, record_id))) ## STEP 1 - IF THIS COMPONENT YIELDS TRUE THEN AUTHETICATION Is right
            record_element.clear()
            st.success('Login successful!')

            st.session_state['authenticated'] = True


            # time.sleep(2)
            st.switch_page("pages/🧪_Labs.py")



    except Exception as e:
        print("Error with authentication")
        st.error("Invalid Username or Password")



## The following code determines the layout and hence calls the functions.
# st.set_page_config(
#     page_title="Multipage App"
# )
st.sidebar.title('LAB-LINK 🔗')

st.title('🏠 Home')
st.session_state['sheetmade'] = False
st.session_state['authenticated'] = False


# Display an image (adjust the path to your image file)

# Create text input for username
username = st.text_input('Username', placeholder='Username')

# Create password input
password = st.text_input('Password', type='password', placeholder='Password')


st.session_state['username'] = username
st.session_state['password'] = password

# Add a login button
if st.button('Login'):

    if username == '' or password == '':
        st.error('Username or Password cannot be blank')

    else:
        print("getting here")
        authenticate()


