import streamlit as st

st.set_page_config(page_title="AGI Research Notebooks", layout='wide')

st.title("AGI Research Notebooks")

st.markdown("""
Welcome to the AGI Research Notebook Collection categorized by core knowledge types.
Explore each section and view the associated Jupyter notebooks hosted on GitHub.
""")

categories = {
    "1. Foundation Knowledge": "1-foundation-knowledge-1.ipynb",
    "2. Multimodal (Voice, Image, Text)": "2-multimodal-voice-image-text-2.ipynb",
    "3. Cognitive & Reasoning Tasks": "3-cognitive-reasoning-tasks.ipynb",
    "4. Social & Emotional Understanding": "4-social-emotional-understanding.ipynb",
    "5. Scientific & Technical Knowledge": "5-scientific-technical-knowledge.ipynb",
    "6. Environment Interaction Data": "6-environment-interaction-data.ipynb",
}

for category, notebook in categories.items():
    with st.expander(category):
        st.write(f"Notebook: **{notebook}**")
        st.markdown(f"[📖 View on GitHub](https://github.com/Ashok080/AGI/blob/main/{notebook})")

st.markdown("---")
st.markdown("Developed by **Ashok Miji** | Licensed under the MIT License")
