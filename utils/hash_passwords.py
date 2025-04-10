# utils/hash_passwords.py

import streamlit_authenticator as stauth

# Define users and their plaintext passwords
usernames = ["Sourjesh Mukherjee", "ViewerUser"]
roles = ["Admin", "Viewer"]
passwords = ["adminpass123", "viewerpass123"]  

# ✅ Correct usage — pass passwords list directly
hashed_passwords = stauth.Hasher(passwords).generate()

# Output config-ready YAML block
for username, role, hashed in zip(usernames, roles, hashed_passwords):
    print(f"""
  {username.lower().replace(" ", "_")}:
    name: {username}
    password: '{hashed}'
    role: {role}
""")
