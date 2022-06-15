import streamlit
import pandas
streamlit.title('New healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('omega 3 & blueberry oatmeal')
streamlit.text('Kale, spinach & Rocket Smoothie') 
streamlit.text('hard-boiled free-range eggs')
streamlit.header('Build your own fruit smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Lets put a pick list here so they can pick the fruit they want to include
#streamlib.multiselect("Pick from fruits : ", list(my_fruist_list.index))
# Display the list on the page 
streamlit.dataframe(my_fruit_list)
