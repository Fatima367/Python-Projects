import streamlit as st
import re

st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

common_passwords = [
    "123456", "password", "123456789", "12345", "12345678", "qwerty", "abc123", 
    "password123", "111111", "123123", "admin", "letmein", "welcome", "monkey", 
    "sunshine", "qwertyuiop", "1234", "1q2w3e4r", "password1", "dragon", "iloveyou"
]

def check_password_strength(password):
    score=0

    # blaclisting common passwords
    if password.lower() in common_passwords:
        st.markdown("❌ Your password is too common. Please choose a stronger one")
        return ""
    
    if len(password) >= 12:
        score += 1

    # checking length 
    if len(password) >= 8:
        score += 1
    else:
        st.markdown("❌ Password should be atleast 8 characters long")

    # uppercase and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.markdown("❌ Password must include both uppercase and lowercase letters")

    # checking digits
    if re.search(r"\d", password):
        score += 1
    else:
        st.markdown("❌ Add at least one number from (0-9)")
    
    # checking special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1 
    else:
        st.markdown("❌ Include at least one special character (!@#$%^&*)")

    if score == 5:
        st.info("✅ **Excellent Password!** You've created a top-tier password that meets all the criteria for maximum security! Keep it safe and secure 👏")
    elif score  == 4:
        st.info("✅ Strong Password!")
    elif score == 3:
        st.info("⚠️ Moderate Password - Consider adding more security features given in the sidebar..")
    else:
        st.info("❌ Weak Password - Improve it using the suggestions given in the sidebar.")
    return ""

def main():

    with st.sidebar:
        st.header("📌 Tips for a Strong Password:")
        st.info("""
        - **Length matters:** Use a password that is at least 12 characters long for better security.
        - **Mix it up:** Include uppercase and lowercase letters, numbers, and special characters (e.g., !, @, #, $).
        - **Avoid common patterns:** Don't use easily guessable information, such as your name, birthdate, or simple sequences (e.g., 1234, qwerty).
        - **Use a passphrase:** Consider a random combination of unrelated words or a memorable sentence to increase strength.
        - **Enable 2FA:** For an added layer of security, always enable two-factor authentication (2FA) where possible.
        - **Don’t reuse passwords:** Avoid using the same password across multiple accounts. Use a password manager to help you keep track of them.
        """)



    st.title("Password Strength Meter 🧭")
    st.write("Stronger passwords, safer you. Build it strong, keep it secure!")


    st.markdown("Check the strength of your password")
    input_password = st.text_input("Enter your password here", type="password", help="Password should be at least 8-12 characters long and include a mix of uppercase, lowercase, numbers, and special characters.")

    if st.button("Check Strength"):
        if input_password:
            result = check_password_strength(input_password)
            st.markdown(result)

if __name__ == "__main__":
    main()
