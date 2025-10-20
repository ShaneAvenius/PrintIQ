import streamlit as st
import streamlit.components.v1 as components
import os

# Configure page
st.set_page_config(
    page_title="PrintIQ Material Selector",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PrintIQ - 3D Printing Material Selector")

# Load your HTML file directly
try:
    # This is the corrected line with the lowercase 'i'
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error("ERROR: The 'index.html' file was not found in the repository.")
    st.info("Please make sure 'index.html' (all lowercase) is in the root of your GitHub repository.")
    html_content = None
except Exception as e:
    st.error(f"An error occurred while loading the HTML file: {e}")
    html_content = None


if html_content:
    components.html(html_content, height=1200, scrolling=True)
else:
    st.warning("Application content could not be loaded.")
