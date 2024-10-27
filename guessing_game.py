import streamlit as st
import random
st.title("Number Guessing Game")

if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.guess_count = 0

guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.guess_count += 1
    if guess < st.session_state.number_to_guess:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.warning("Too high! Try again.")
    else:
        st.success(f"Congratulations! You've guessed the number {st.session_state.number_to_guess} in {st.session_state.guess_count} attempts!")
    
        if st.button("Play Again"):
            st.session_state.number_to_guess = random.randint(1, 100)
            st.session_state.guess_count = 0

st.write(f"Number of attempts: {st.session_state.guess_count}")
