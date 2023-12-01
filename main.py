
import streamlit as st 
import pickle
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import home, about, account, trending,your_posts
st.set_page_config(
    page_title=("multi page")
)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
  
  
  
authenticator = stauth.Authenticate(
  config['credentials'],
  config['cookie']['name'],
  config['cookie']['key'],
  config['cookie']['expiry_days'],
  config['preauthorized']
)

name,authentication_status,username= authenticator.login("login","main")
    
    
if authentication_status == False:
    st.error("username/password is incorrect")
        
if authentication_status == None:
    st.warning("Please enter username and password")        
        
if authentication_status:
    
    class MultiApp:
        def __init__(self):
            self.apps=[]
        def add_app(self,title,func):
            self.apps.append({
                "title":title,
                "function":func
                })
        def run():
            with st.sidebar:
                app = option_menu(
                    menu_title="pondering",
                    options=['Account','Home','Trending','Your Posts','About'],
                    default_index=1)
            if app == 'Account':
                account.app()
            if app == 'home':
                home.app()
            if app == 'Trending':
                trending.app()
            if app == 'Your Posts':
                your_posts.app()
            if app == 'About':
                about.app()
        run()
            
    
