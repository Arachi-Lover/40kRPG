import streamlit as st
from utils.data_loader import load_classes_data
from utils.constants import menu_options
from sections import campaign, classes, lore, rules

# Configuração inicial da página
st.set_page_config(
    page_title="RPG Warhammer 40k",
    page_icon="💀",
    layout="wide"
)

# Carregar dados
classes_data = load_classes_data()

# Interface Streamlit com sidebar
st.title("💀 RPG Warhammer 40k")

# Criar a sidebar
with st.sidebar:
    st.header("Páginas")
    selected_option = st.radio(
        "Selecione uma página:",
        options=list(menu_options.keys()),
        help="Cada página é dedicada a explicar um conjunto de informações específico sobre o sistema."
    )
    # Mostrar descrição da opção selecionada
    st.caption(menu_options[selected_option])

# Navegação entre páginas
if selected_option == "Lore":
    lore.show()
elif selected_option == "Regras":
    rules.show()
elif selected_option == "Classes":
    classes.show(classes_data)
elif selected_option == "Campanha":
    campaign.show()
