import streamlit as st
import streamlit.components.v1 as components
import os


def load_html_file(file_path):
    """Helper function to safely read an HTML file."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return None

# Configure page
st.set_page_config(
    page_title="HTML App in Streamlit",
    page_icon="🌐",
    layout="wide"
)

def main():
    st.title("🌐 HTML App Integration with Streamlit")
    st.markdown("This application demonstrates how to integrate existing HTML code within Streamlit framework.")
    
    # Sidebar for navigation
    st.sidebar.title("Integration Methods")
    method = st.sidebar.selectbox(
        "Choose integration method:",
        ["Your Material Selector App", "Simple HTML", "HTML with CSS", "Interactive HTML with JavaScript", "File Upload"]
    )
    
    if method == "Your Material Selector App":
        show_material_selector()
    elif method == "Simple HTML":
        show_simple_html()
    elif method == "HTML with CSS":
        show_html_with_css()
    elif method == "Interactive HTML with JavaScript":
        show_interactive_html()
    elif method == "File Upload":
        show_file_upload()

def show_material_selector():
    st.header("PrintIQ - 3D Printing Material Selector")
    st.markdown("Your complete HTML application running within Streamlit:")

    # Load your HTML file directly
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        html_content = None

    if html_content:
        components.html(html_content, height=1200, scrolling=True)
        
        with st.expander("View Your HTML Code"):
            st.code(html_content[:2000] + "..." if len(html_content) > 2000 else html_content, language="html")
    else:
        st.error("Could not load your material selector HTML file.")

def show_simple_html():
    st.header("Simple HTML Integration")
    st.markdown("Using `st.html()` for basic HTML content:")
    
    # Simple HTML example
    simple_html = """
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 10px 0;">
        <h3 style="color: #1f77b4;">Welcome to your HTML content!</h3>
        <p>This is a simple HTML block rendered within Streamlit.</p>
        <ul>
            <li>Easy integration</li>
            <li>Preserves styling</li>
            <li>Works with Streamlit layout</li>
        </ul>
    </div>
    """
    
    st.html(simple_html)
    
    # Show the code
    with st.expander("View HTML Code"):
        st.code(simple_html, language="html")

def show_html_with_css():
    st.header("HTML with CSS Integration")
    st.markdown("Using `st.components.v1.html()` for more complex styling:")
    
    # Load HTML component with CSS
    html_content = load_html_file("html_components/sample_component.html")
    
    if html_content:
        components.html(html_content, height=400)
        
        with st.expander("View HTML/CSS Code"):
            st.code(html_content, language="html")
    else:
        st.error("Could not load HTML component file.")

def show_interactive_html():
    st.header("Interactive HTML with JavaScript")
    st.markdown("Demonstrating JavaScript functionality within Streamlit:")
    
    # Load interactive HTML component
    interactive_content = load_html_file("html_components/interactive_component.html")
    
    if interactive_content:
        # Use components.html for JavaScript functionality
        result = components.html(interactive_content, height=500)
        
        if result:
            st.write(f"Received data from HTML component: {result}")
        
        with st.expander("View Interactive HTML/JS Code"):
            st.code(interactive_content, language="html")
    else:
        st.error("Could not load interactive HTML component file.")

def show_file_upload():
    st.header("Upload Your HTML File")
    st.markdown("Upload an existing HTML file to see it rendered in Streamlit:")
    
    uploaded_file = st.file_uploader(
        "Choose an HTML file",
        type=['html', 'htm'],
        help="Upload your existing HTML file to see it rendered within Streamlit"
    )
    
    if uploaded_file is not None:
        # Read the uploaded HTML file
        html_content = uploaded_file.read().decode('utf-8')
        
        # Display options
        col1, col2 = st.columns(2)
        
        with col1:
            render_method = st.radio(
                "Rendering method:",
                ["st.html()", "st.components.v1.html()"]
            )
        
        with col2:
            height = st.slider("Component height (for components.html)", 200, 1000, 400)
        
        st.subheader("Rendered HTML:")
        
        if render_method == "st.html()":
            st.html(html_content)
        else:
            components.html(html_content, height=height)
        
        # Show the uploaded HTML code
        with st.expander("View Uploaded HTML Code"):
            st.code(html_content, language="html")
    
    # Instructions
    st.markdown("""
    ### Integration Tips:
    
    1. **For simple HTML**: Use `st.html()` - great for basic content with inline styles
    2. **For complex HTML**: Use `st.components.v1.html()` - supports external CSS/JS and better for interactive content
    3. **File organization**: Keep HTML files in a dedicated folder for better organization
    4. **JavaScript**: Use `st.components.v1.html()` with `bidirectional=True` for two-way communication
    5. **Responsive design**: Test your HTML content at different screen sizes within Streamlit
    """)

if __name__ == "__main__":
    main()
