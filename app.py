import streamlit as st

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Posez votre question concernant de vos documents")
    with st.sidebar:
        st.subheader("Vos documents")
        st.file_uploader("Déposez vos documents ici")
        st.button("Executer")
        
