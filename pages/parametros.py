import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None)


st.markdown(
    """
        <style>
                .stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                    background-image: url(http://placekitten.com/200/200);
                    background-position: 20px 20px;
                    visibility: visible;  /* Ensure the header is visible */
                }

               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 4rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
)

#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Miraki - Parametros")

selected3 = option_menu(None, ["Home", "Palabras Claves","Excluidas","Sectores","Ejes","PalabrasporSector","Proyectos" ], 
      icons=['house', 'alphabet' ,'x-circle','diagram-3','list-check','alphabet-uppercase','building-fill' ] , menu_icon="cast",orientation="horizontal", default_index = -2,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)

if selected3=="Home":
    st.switch_page("miraki.py") 
if selected3=="Palabras Claves":
    st.switch_page("./pages/palabrasclaves.py")  
if selected3=="Excluidas":
    st.switch_page("./pages/editar_fuentes.py")  
if selected3=="Sectores":
    st.switch_page("./pages/sectores.py")  
if selected3=="Ejes":
    st.switch_page("./pages/ejes.py")
if selected3=="Palabras por Sector":
    st.switch_page("./pages/ejes.py")
if selected3=="Proyectos":
    st.switch_page("./pages/proyectos.py")

pfuente = st.text_input("ingrese el nombre de la fuente")

