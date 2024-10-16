import streamlit as st


def main():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Missile Defense', icon='☄️')
        st.page_link('pages/spiral_one.py', label='Spiral One', icon='🌠')
        st.page_link('pages/spiral_two.py', label='Spiral Two', icon='👩‍🚀')

    st.title(f'☄️ Missile Defense')
    st.code("This is just an example of the app")
    st.header("Help Policy")

    st.markdown("""
                **Authorized Resources**: Any, **EXCEPT** another cadet’s code (in any form) or Large Language Models (e.g., ChatGPT, Bard, etc.)
    """)

    st.markdown("""
    Never copy another person’s work, including another cadet’s or a solution found online, and submit it as your own.
    Do not jointly create a program.
    LLMs, such as ChatGPT, are not allowed to write code for this assignment.
    """)

    st.markdown("""
    You must document all help received from sources other than an instructor.
    **DFCS will recommend a course grade of F for any cadet who egregiously violates this Help Policy or contributes to a violation by others.**
    """)

    st.header("Documentation Policy")

    st.header("Instructions")


if __name__ == '__main__':
    main()