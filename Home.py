import streamlit as st


st.set_page_config(
    page_title="Homepage",
    page_icon="👋"
)

form =  st.form(key="my_form")
anun = form.text_input("anun", "")
azganun = form.text_input("azganun", "")
haeranun = form.text_input("haeranun", "")
submit_button = form.form_submit_button(label = "Submit")



st.session_state["anun"] = anun
if submit_button:
    st.markdown("### Data is being analyzed, please go to the plots page to see them.")
    st.page_link("pages/2_plots.py")
    st.page_link("pages/1_contacts.py")

    st.session_state["anun"] = anun
    st.session_state["azganun"] = azganun
    st.session_state["haeranun"] = haeranun
    
