import streamlit as st


def main():
    # builds the sidebar menu
    VIDEO_URL = "https://www.youtube.com/watch?v=fxEiYim3Z3M"
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Missile Defense', icon='☄️')
        st.page_link('pages/spiral_one.py', label='Spiral One', icon='🌠')
        st.page_link('pages/spiral_two.py', label='Spiral Two', icon='👩‍🚀')
        st.page_link('pages/spiral_three.py', label='Spiral Three', icon='🚀')

    st.title(f'🌠 Spiral One')
    st.header("This would be a quick video of the endgoal of Spiral One")
    st.video(VIDEO_URL)
    st.header("Spiral One Goals")
    st.markdown(
        """
        0. **SPIRAL 1**  
        The customer wants a screenshot of the game.  This means a view of meteors, missiles, and cities.
    """
    )

    st.header("Overall Requirements")
    st.markdown(
        """
    Requirements using the word **Shall**, must be satisfied to receive full points for this project. Those with the word **May**,
    indicate optional (not required) options in development. Numbers in brackets (i.e. [2,3]) indicate in what spiral(s) each requirement
    must be implemented. Up to 10 extra credit points may be given to each student in spiral 3. Coordinate with your instructor (the customer)
    to find out how valuable additional features may be.

    ### 0. DOCUMENTATION
    - **Shall** be submitted in Canvas for each submission [1,2,3]  
        - **Shall** be cumulative (i.e., also contain doc statements for all prior spirals).
    - **Shall** include your name `and section` at the top of each file [1,2,3]
    - **Shall** list any shall requirements that are not fully functional and describe the deficiency [1,2,3]

    ### 1. THE GAME GRAPH WINDOW
    - **Shall** display 600 pixel high X 800 pixel wide screen.
    - **Shall** be able to scale the screen by 2/3 (two thirds) or 3/2 (three halves) these dimensions and maintain scale. `i.e. when we change the dimensions
    of the game window size, the images draw on screen the same, just smaller or bigger depending on the game window size.`
        - **Note**: missile/meteor sizes need not be adjusted.
    - **Shall** store and reference the `window` dimension values in appropriately named CONSTANTS. [1,2,3]
    - **Shall** have a window title consisting of three elements separated by hyphens [1,2,3]:
        - The course/game information: “CS110 (S25) Missile Defense”
        - The assignment identifier: e.g., “Spiral#3”
        - Your name: e.g., “C4C Tanya Smith” or “C4C Fred Jones”
    
    Example: `“CS110 (S24) Battle Boats – Spiral#3 – C4C Tanya Smith”`

    ### 2. GAME PLAY
    - **Shall** visually indicate location of cities [1,3]
    - **Shall** show meteors with line from meteor origin [1,3]
    """
    )

    st.header("Spiral One Functions")

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
    st.code("""draw_explosions(explosions)\n'''Add description'''""")

if __name__ == '__main__':
    main()