import os
from streamlit_option_menu import option_menu
import streamlit as st


st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None)

st.markdown("""
<style>
	[data-testid="stDecoration"] {
		display: none;
	}

</style>""",
unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
</style>

"""
st.title("Test")
if st.checkbox('Remove padding'):
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)



clicked_menu_item = st.menu_items(['Item 1', 'Item 2', 'Item 3'], expanded=True, floating=True, emphasized_items=[0])

selected = option_menu(None, ["Home", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'gear' ,'gear'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )

selected1 = option_menu(None, ["Home", 'Ingresar','Editar', 'Informes','Parametros','Github' ], 
        icons=['house', 'gear' ,'gear'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )
