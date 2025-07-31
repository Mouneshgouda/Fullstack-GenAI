```python 

# Background & Styling
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1501785888041-af3ef285b470");
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
}
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: -1;
}
[data-testid="stForm"] {
    background-color: rgba(255, 255, 255, 0.08);
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}
input, select, textarea {
    background-color: #f0f0f0 !important;
    color: #000 !important;
    border-radius: 8px !important;
    padding: 6px !important;
    border: 1px solid #ccc !important;
}
label, .stRadio > label, .stCheckbox, .css-1cpxqw2, .st-bf, .st-c9 {
    color: #ffffff !important;
    font-size: 16px !important;
}
h1, h2, h3 {
    color: white !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

```
