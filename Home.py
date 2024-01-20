import streamlit as st

st.set_page_config(
    page_title="Shirleen Data Web App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Shirleen Web App"
    }
)

import streamlit as st
import json
import math

def show_resume():
    st.title("Resume")

    # Biografi
    with st.container(border=True):
        st.header("")
        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown("""<img src="https://github.com/shirahub/portfolio-data-web-app/blob/main/public/Shirleen.jpeg?raw=true" style="border-radius: 50%;width:100%"></img>""", unsafe_allow_html=True)

        with col2:
            st.header("Shirleen Adriana")
            st.write("📍 Jakarta, Indonesia 🇮🇩")
            st.text("✉️ shirleen.adriana@gmail.com")
            st.write("I am a Mandarin teacher, became a web developer in 2020, and since then have been exploring any IT-related fields.  As a software developer, I witnessed the pivotal role that data plays in guiding decisions and fostering innovation. This insight fueled my enthusiasm to explore data science and engineering.")
            st.markdown("""
                        <a href="https://www.linkedin.com/in/shirleen-adriana-1bbb731b2/">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" style="width:30px">
                        </a>
                        """, unsafe_allow_html=True)
    # Work Experience
    with st.container(border=True):
        st.header("🏢 Professional Experience")
        st.divider()
        with open('public/work.json', "r") as f:
            data = f.read()
        
        data_json = json.loads(data)

        for i, v in enumerate(data_json):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(v['title'])
                st.subheader(v['position'])
                st.write(v['description'])

            with col2:
                st.write(v['start'] + '-' + v['end'])

            for h in v['highlights']:
                st.write('✨' + h)

            if i != len(data_json)-1:
                st.divider()
    
    # Education
    with st.container(border=True):
        st.header("👩‍🎓 Education")
        st.divider()
        with open('public/education.json', "r") as f:
            data = f.read()
        
        data_json = json.loads(data)

        for i, v in enumerate(data_json):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(v['title'])
                st.write(v['description'])

            with col2:
                st.write(v['start'] + '-' + v['end'])

            if i != len(data_json)-1:
                st.divider()

    # Skills
    with st.container(border=True):
        st.header("💻 Skills")
        st.divider()

        with open('public/skills.json', "r") as f:
            data = f.read()

        data_json = json.loads(data)

        # languages
        st.subheader("Languages")

        list = ""
        for i in data_json['languages']:
            line = "- {0} ({1})\n".format(i['language'], i['proficiency'])
            list = list + line

        st.markdown(
        f"""
        {list}
        """
        )

        st.divider()
        # programming
        st.subheader("Tech")
        columns_count = len(data_json['techs'])
        row_count = int(math.ceil(columns_count/4))
        index_data = 0

        for i in range(1, row_count+1):
            cols = st.columns(4)
            for ii in cols:
                if index_data < len(data_json['techs']):
                    ii.image(data_json['techs'][index_data]['logo_url'],width=100)
                    # ii.write(data_json['techs'][index_data]['name'])
                    index_data +=1

    # Projects
    # with st.container(border=True):a
    #     st.header("Projects")

show_resume()