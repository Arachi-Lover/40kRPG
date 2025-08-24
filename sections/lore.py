import streamlit as st
from utils.constants import lore_content, factions

def show():
    st.markdown(lore_content)
    
    st.subheader("Facções")
    cols = st.columns(3)
    for i, (faction, data) in enumerate(factions.items()):
        with cols[i % 3]:
            with st.expander(f"**{faction}**"):
                st.markdown(
                    f"""
                    <div style="text-align:center">
                        <img src="{data['img']}" 
                            alt="{faction}" 
                            width="{data['width']}" 
                            height="{data['height']}"
                            style="border: 2px solid white; border-radius: 8px;">
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.caption(data["desc"])
                