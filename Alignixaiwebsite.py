import streamlit as st
from PIL import Image

# --- Load Logo ---
logo = Image.open("alignixai_logo.png")

# --- Page Setup ---
st.set_page_config(page_title="AlignixAI", layout="centered")

# --- Branding ---
st.image(logo, width=200)
st.markdown("""
<style>
    body {
        background-color: #f9f9f9;
    }
    .main {
        color: #1D093E; /* Deep purple */
    }
    h1, h2, h3 {
        color: #1D093E !important;
    }
    .stButton>button {
        background-color: #1D093E;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.title("Smarter Compliance. Streamlined Productivity.")
st.subheader("AI-driven solutions built for financial institutions and fintechs, starting with our MVP mockup.")

# --- What We Do ---
st.header("What We Do")
st.write("""
AlignixAI helps small to medium-sized financial firms and fintechs use artificial intelligence to automate and simplify
internal processes. Whether it's compliance, policy updates, or productivity tools — we make work smarter, not harder.
""")

# --- Who We Help ---
st.header("Who We Help")
st.write("""
We support:
- Small to mid-sized banks
- Compliance and KYC teams
- Fintech startups with lean teams
- Regulated businesses needing smarter systems

Our platform is built with flexibility, so it can grow with your business.
""")

# --- Why Choose Us ---
st.header("Why Choose Us")
st.write("""
- 18+ years of real-world banking and KYC experience
- Practical, no-fluff AI solutions — not buzzwords
- Built for teams who need trust, clarity, and efficiency
- Designed to grow beyond the MVP, into a full platform
""")

# --- Request a Demo / Contact ---
st.header("Request a Demo / Get in Touch")
st.write("If you're interested in seeing how AlignixAI can support your business, fill out the form below.")

contact_form = """
<form action="https://formspree.io/f/mkgjalon" method="POST">
  <label for=\"name\">Your Name</label><br>
  <input type=\"text\" name=\"name\" required><br>
  <label for=\"email\">Your Email</label><br>
  <input type=\"email\" name=\"email\" required><br>
  <label for=\"message\">Message</label><br>
  <textarea name=\"message\" rows=\"5\" required></textarea><br>
  <button type=\"submit\">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

st.markdown("---")
st.caption("AlignixAI | MVP Launch Stage | Built with Streamlit")
