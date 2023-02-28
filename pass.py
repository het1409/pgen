import random
import string
import streamlit as st

def generate_password(length):
    """Generate a random password of the specified length"""
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use the random module to generate a password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Set the title and description of the app
st.title("Password Generator")
st.write("Enter the desired length of your password and click on 'Generate' to generate a new password.")

# Add a slider to allow the user to select the length of the password
password_length = st.slider("Password length", 6, 30, 12)

# Add a button to generate a new password
if st.button("Generate"):
    # Generate the password
    password = generate_password(password_length)

    # Display the password to the user
    st.write("Your password is:", password)
