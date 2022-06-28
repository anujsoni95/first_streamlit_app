import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError
streamlit.title('New healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('omega 3 & blueberry oatmeal')
streamlit.text('Kale, spinach & Rocket Smoothie') 
streamlit.text('hard-boiled free-range eggs')
streamlit.header('Build your own fruit smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Lets put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick from fruits : ", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the list on the page 
def get_fruityvice_data(this_fruit_choice): 
           fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)     
           fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
           return fruityvice_normalized
streamlit.header('fruityvice fruit advice!')

try: 
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
       streamlit.error('Please select a fruit for information')
    else:
       back_from_function = get_fruityvice_data(fruit_choice) 
       #streamlit.write('The user entered ', fruit_choice)
       streamlit.dataframe(back_from_function) 
except URLError as e:
    streamlit.error()


streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
       with my_cnx.cursor() as my_cur:
            my_cur.execute("SELECT * from fruit_load_list")           
            return my_cur.fetchall() 
if streamlit.button('get fruit load list'):
       snowflake.connector.connect(**streamlit.secrets["snowflake"])
       my_data_rows = get_fruit_load_list()
       streamlit.dataframe(my_data_rows)          


