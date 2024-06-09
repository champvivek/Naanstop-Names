import streamlit as st
import langchain_helper

st.title("🍲 Naanstop Names 🍲")
st.subheader("No More Name Headaches, Just Naanstop Creations")

cuisine = st.sidebar.selectbox("Choose a culinary tradition", ("South Indian", "North Indian", "Central Indian", "Western Indian", "Eastern Indian"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.write("**Restaurant Names**")

    # Extracting and cleaning the first restaurant name
    restaurant_names = response['restaurant_name'].strip().split("\n")
    first_restaurant_name = restaurant_names[0].lstrip("* ").lstrip("restaurant ").strip()

    # Display the first restaurant name without bold
    st.write(first_restaurant_name)

    # Display the remaining restaurant names
    for name in restaurant_names[1:]:
        cleaned_name = name.lstrip("* ").strip()
        st.write(f"**{cleaned_name}**")

    # Process and display menu items
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item.strip())