import streamlit as st
from utils.constants import rules_content

def show():
    st.markdown(rules_content)
    
    st.subheader("Mecânicas de Combate")
    st.markdown("""
    **Fluxo de Combate:**
    1. Determinar iniciativa;
    2. Personagem escolhe ações de combate;
    3. Teste de perícia para ataques;
    4. Teste de armadura do alvo;
    5. Aplicar dano/efeitos;
    6. Próximo personagem.
    
    **Exemplo de Ataque:**
    - Início de turno para um Marine (Perícia 1) [3 ações]
    - Marine usa Disparar à Vontade (Dificuldade 4+) [Custo de 2 ações]
    - Rola 5 no dado de acerto (5 + 1 = 8 >= 4 → acerto!)
    - Inimigo tem Armadura 2
    - Rola 3 no dado de dano (3 > 2 → causa 1 ferimento)
    - Marine tem 1 ação restante
    - Marine usa Disparo Singular (Dificuldade 5+) [Custo de 1 ação]
    - Rola 4 no dado de acerto (4 + 1 >= 5 → acerto!)
    - Rola 2 no dado de dano (2 = 2 → armadura bloqueou...)
    - Fim do turno do Marine
    """)
    