import streamlit as st


def main():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Missile Defense', icon='☄️')
        st.page_link('pages/spiral_one.py', label='Spiral One', icon='🌠')
        st.page_link('pages/spiral_two.py', label='Spiral Two', icon='👩‍🚀')

    st.title(f'☄️ Missile Defense')

    st.header("Help Policy")

    st.header("Documentation Policy")

    st.header("Instructions")


if __name__ == '__main__':
    main()