import streamlit as st

def show(classes_data):
    st.subheader("Classes Disponíveis")
    
    selected_class = st.selectbox(
        "Selecione uma Classe:", 
        list(classes_data.keys())
    )
    
    cl = classes_data[selected_class]
    
    st.markdown(f"### {selected_class}")

    # Render illustrative image
    if "img" in cl:
        st.markdown(
            f"""
            <div style="text-align: center; margin: 10px 0;">
                <img src="{cl['img']}" width="{cl['width']}" height="{cl['height']}" 
                    style="border: 2px solid white; border-radius: 8px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Status")
        for stat, value in cl["Status"].items():
            st.progress(value/5, f"{stat}: {value}/5")
        
        st.subheader("Habilidades")
        for skill, level in cl["Habilidades"].items():
            st.markdown(f"- **{skill}**: {'⭐' * level}")
        
        st.subheader("Nativas")
        for ability in cl["Nativas"]:
            st.markdown(f"- {ability}")
    
    with col2:
        st.subheader("Combate")
        st.markdown(f"**Ações por turno:** {cl['Combate']['Ações']}")
        for attack in cl["Combate"]["Habilidades"]:
            st.markdown(f"- {attack}")
        
        st.subheader("Customização")
        st.markdown(f"**Gênero:** {cl['Customização']['Gênero']}")
        
        st.write("**Opções de Nativa Bônus:**")
        for option in cl["Customização"]["Opções de Nativa Bônus"]:
            st.markdown(f"- {option}")
        
        st.write("**Triunfos (Escolha 1):**")
        for triumph in cl["Customização"]["Triunfos"]:
            st.markdown(f"- {triumph}")
        
        st.write("**Vergonhas (Escolha 1):**")
        for shame in cl["Customização"]["Vergonhas"]:
            st.markdown(f"- {shame}")
            