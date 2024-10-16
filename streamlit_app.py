import streamlit as st


def main():
    # builds the sidebar menu
    VIDEO_URL = "https://www.youtube.com/watch?v=fxEiYim3Z3M"

    with st.sidebar:
        st.page_link('streamlit_app.py', label='Missile Defense', icon='☄️')
        st.page_link('pages/spiral_one.py', label='Spiral One', icon='🌠')
        st.page_link('pages/spiral_two.py', label='Spiral Two', icon='👩‍🚀')
        st.page_link('pages/spiral_three.py', label='Spiral Three', icon='🚀')

    st.title("CS 110 - Introduction to Computing Spring 2025")
    st.title(f"☄️ Missile Defense - 250 Points")
    st.header("Help Policy")

    st.markdown(
        "**Authorized Resources**: Any, **EXCEPT** another cadet’s code (in any form) or Large Language Models (e.g., ChatGPT, Bard, etc.)"
    )
    st.markdown(
        """
    Never copy another person’s work, including another cadet’s or a solution found online, and submit it as your own.  
    Do not jointly create a program.  
    LLMs, such as ChatGPT, are not allowed to write code for this assignment.  
    You must document all help received from sources other than an instructor. 
    """
    )
    st.markdown(
        "**DFCS will recommend a course grade of F for any cadet who egregiously violates this Help Policy or contributes to a violation by others.**"
    )

    st.header("Documentation Policy")
    st.markdown(
        """
    Provide your Documentation Statement in Canvas as a comment with each Spiral.
    The documentation statement must explicitly describe **what** assistance was provided, **where** in the assignment the assistance was provided (e.g. line numbers), and **who** provided the assistance.
    If no help was received on this assignment, the documentation statement must state "NONE".
    """
    )
    st.markdown(
        "Vague documentation statements must be corrected before the assignment will be graded, and will result in an up to 5% deduction on the assignment."
    )

    st.header("Instructions")
    st.markdown(
        """
    You will create a game from scratch using pythonGraph.  
    This assignment is broken into 3 submissions. Each submission will build and often update the previous submission.  
    Additional information for all of the submissions is provided in this document. Additional information may be provided in future updates to this document.
    """
    )
    st.markdown("**Submit your solutions** via the Project pages in Canvas.")
    st.header("Placeholder Video")
    st.video(VIDEO_URL)

    st.header("Introduction")
    st.markdown(
        """
        0. **MISSILE DEFENSE**  
        “Missile Defense” is a computer version of the 1980 Atari game Missile Command. In the game, the player is the commander of a missile battery designed to intercept meteors.
        The goal is to keep meteor impacts from destroying four cities entrusted to the missile commander. On the player’s input, missiles will fly to a predetermined coordinate
        the commander clicks.  If the timing is right, the explosion from the missile will destroy nearby meteors and cause secondary explosions.  The player continues until all 
        four cities are destroyed.

        1. **BACKGROUND**  
        This project simulates how software applications are developed. A customer (person or company) will describe what is necessary for a software application to be acceptable
        to meet their needs.  Requirements are hard to develop and clearly articulate. The development team asks many clarifying questions.  If anything is unclear about
        the requirements, the developer (you) should ask clarifying questions as soon as possible! **Implementing incorrect requirements due to a misunderstanding will look
        bad for your company and may result in you getting fired (or losing points).** 

        2. **SPIRALS**  
        “Spiral” is a paradigm where a program with some of its desired functionality is released before all functionality is finished.  Such a release is called a ‘spiral.’ 
        In this project there will be three spirals where subsequent releases (submissions) build on previous releases.  Just like a software company, you should make plans 
        for future functionality when completing early spirals to avoid having to re-write poorly written or poorly documented code.
    """
    )

    st.header("Spiral Goals Summary")
    st.markdown(
        """
        0. **SPIRAL 1**  
        The customer wants a screenshot of the game.  This means a view of meteors, missiles, and cities.

        1. **SPIRAL 2**  
        For the second delivery, the customer wants the mouse interface and missiles implemented.  Missiles should be launched via a mouse click and explode at their destination.

        2. **SPIRAL 3**  
        The customer requires a fully playable game with meteors, missiles, cities, and all of the prescribed interactions between the pieces.
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
    - **Shall** contain the list of any features for which extra credit is sought [3]
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
    - **Shall** launch missile at coordinates clicked [2,3]
    - **Shall** have missiles originate from bottom center of screen [2,3]
    - **Shall** have missile explode when missile reaches destination [2,3]
    - **Shall** have explosion expand and shrink [2,3]
    - **Shall** destroy meteors caught in explosion [2,3]
    - **Shall** create secondary explosion originating from destroyed meteor [2,3]
    - **Shall** visually indicate location of cities [1,3]
    - **Shall** visually indicate whether each city is undamaged or destroyed [3]
    - **Shall** display ‘game over’ status when game is complete [3]
    - **Shall** show meteors with line from meteor origin [1,3]
    - **Shall** randomly generate meteors to appear at the top of the screen at random times [3]
    - **Shall** have meteors travel on a path to a random location at the bottom of the screen [3]
    - **Shall** have missiles travel at a constant speed (not constant in just y direction) [2,3]
    - **Shall** have meteors travel at a constant speed (not constant in just y direction) [3]
    - **Shall** add additional feature or features [3]
    - **Shall** indicate when the game is over (all 4 cities destroyed) [3]
    """
    )


if __name__ == "__main__":
    main()
