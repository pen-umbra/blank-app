import streamlit as st

# st.title("DestinE SP Onboarding - IAM Wizard")
# st.write(
#     "[docs.streamlit.io](https://docs.streamlit.io/)."
# )

st.set_page_config(layout="wide")

# Sidebar per la navigazione del Wizard
st.sidebar.header("IAM Wizard")
step = st.sidebar.radio(
    "Config Sections:",
    ["1. General Settings", "2. Capability Config", "3. Login Settings"]
)

st.title("Identity Config")
st.info("Fill the above fields")

# --- SEZIONE 1: GENERAL SETTINGS ---
if step == "1. General Settings":
    st.subheader("1. General Settings")
    with st.container(border=True):
        client_type = st.selectbox("Client type", ["OpenID Connect", "SAML"], help="Select AUTH protocol")
        client_id = st.text_input("Client ID *", placeholder="es. sp-meteo-sat-auth")
        name = st.text_input("Name", placeholder="Client name")
        description = st.text_area("Description", placeholder="Brief service description")
        display_on_ui = st.toggle("Always display in UI", value=False)
    
    if st.button("Save Draft"):
        st.success("Draft Saved")

# --- SEZIONE 2: CAPABILITY CONFIG ---
elif step == "2. Capability Config":
    st.subheader("2. Capability Config")
    with st.container(border=True):
        st.write("Configure client capabilities...")
        client_auth = st.checkbox("Client Authentication", value=True)
        authorization = st.checkbox("Authorization")
        service_accounts = st.checkbox("Service Accounts Enabled")
    
    if st.button("Save Draft"):
        st.success("Draft Saved")

# --- SEZIONE 3: LOGIN SETTINGS ---
elif step == "3. Login Settings":
    st.subheader("3. Login Settings")
    with st.container(border=True):
        root_url = st.text_input("Root URL")
        home_url = st.text_input("Home URL")
        valid_redirect = st.text_input("Valid Redirect URIs", placeholder="https://myapp.com/*")

    if st.button("Review and Submit"):
        st.balloons()
        st.success("Config Successfully Completed")