
from spellchecker import SpellChecker
import streamlit as st


spell = SpellChecker()
st.title ("Autocorrect Keyboard System")
input = st.text_area("enter your sentence", height =70)
if st.button("autocorrect"):
    user_input = input.split()
    mispelled = spell.unknown(user_input)
    corrected_words = []
    for word in mispelled:
        corrected_words.append(spell.correction(word))
    
    
st.success(corrected_words)