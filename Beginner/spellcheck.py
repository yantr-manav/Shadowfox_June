from spellchecker import SpellChecker
import streamlit as st
import re
# Initialize spell checker
spell = SpellChecker()
st.title( "AutoX: Autocorrect Keyboard System")
# Input field
input = st.text_area("Enter your sentence", height = 80)
# Button logic
if st.button("Autocorrect it for me"):
    for i in range(3):
        if input is not None and input.strip() != "":
            
            words = re.findall(r'\b\w+\b', input.lower())
            mispelled = spell.unknown(words)
            
            st.write("Mispelled words: ", mispelled)
            
            corrected_words = []
            
            for word in words:
                if word in spell:
                    corrected_words.append(word)
                else: 
                    corrected = spell.correction(word)
                    corrected_words.append(corrected if corrected else word)
                    
            corrected_sentence = " ".join(corrected_words)
            st.success(f'Do you mean:  {corrected_sentence}')
        
        else:
            st.error("Please enter a sentence to autocorrect. ")

