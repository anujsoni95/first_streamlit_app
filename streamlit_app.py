import streamlit
import requests
import pandas
import snowflake.connector
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
streamlit.dataframe(fruits_to_show)fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

streamlit.header('fruityvice fruit advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
