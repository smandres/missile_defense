import streamlit as st


def main():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Missile Defense', icon='☄️')
        st.page_link('pages/spiral_one.py', label='Spiral One', icon='🌠')
        st.page_link('pages/spiral_two.py', label='Spiral Two', icon='👩‍🚀')

    st.title(f'🌠 Spiral One')
    st.markdown("""**Instructions here**, Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
    st.markdown("""**Instructions here**, Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
    st.markdown("""**Instructions here**, Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
    st.header("Functions")

    option = st.selectbox(
    "This is an option to view individual functions!",
    ("draw_missiles()", "draw_meteors()", "draw_cities()", "draw_explosions()"),
    index=None,
    placeholder="Select a function...",
)
    st.write("At this point the page will render and only display the function:", option)
    st.code("""draw_missiles(missiles)\n'''Add description'''""")
    st.code("""draw_meteors(meteors)\n'''Add description'''""")
    st.code("""draw_cities(cities)\n'''Add description'''""")
    st.code(""""draw_explosions(explosions)\n'''Add description'''""")

if __name__ == '__main__':
    main()