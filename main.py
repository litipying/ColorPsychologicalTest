import streamlit as st

# Set the title of the app
st.title("Color-Based Psychological Test")

st.write("""
Welcome to the Color-Based Psychological Test! 
Select the color that appeals to you the most, and we'll reveal a brief psychological insight based on your choice.
""")

# Define the color options
colors = {
    "Red": {"desc": "Energy, passion, and action. Indicates a person who is confident, determined, and enjoys excitement.", "hex": "#FF0000"},
    "Blue": {"desc": "Calm, reliability, and serenity. Suggests a person who is trustworthy, caring, and values stability.", "hex": "#0000FF"},
    "Green": {"desc": "Growth, balance, and harmony. Suggests a person who seeks peace, nature, and personal development.", "hex": "#008000"},
    "Yellow": {"desc": "Joy, positivity, and creativity. Indicates a person who is optimistic, cheerful, and loves to share ideas.", "hex": "#FFFF00"},
    "Purple": {"desc": "Spirituality, luxury, and creativity. Suggests a person who is imaginative, sensitive, and values uniqueness.", "hex": "#800080"},
    "Black": {"desc": "Power, mystery, and elegance. Indicates a person who is strong, ambitious, and appreciates sophistication.", "hex": "#000000"},
    "White": {"desc": "Purity, simplicity, and new beginnings. Suggests a person who values honesty, clarity, and openness.", "hex": "#FFFFFF"}
}

# Create color selection using columns for better visual representation
selected_color = None
cols = st.columns(len(colors))
for idx, (color_name, color_info) in enumerate(colors.items()):
    with cols[idx]:
        if st.button(color_name, key=color_name):
            selected_color = color_name
        # Add a border for the white color to make it visible
        border_style = "border: 1px solid lightgrey;" if color_name == "White" else ""
        st.markdown(
            f"<div style='width: 30px; height: 30px; background-color: {color_info['hex']}; margin: auto; {border_style}'></div>", 
            unsafe_allow_html=True
        )

# Show psychological interpretation based on selected color
if selected_color:
    st.subheader(f"You selected: {selected_color}")
    st.write(colors[selected_color]["desc"])

    # Add more space above the text prompt for feedback
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("Do you agree with this insight? Let us know your thoughts below!")
    feedback = st.text_area("Your thoughts:")
    if feedback:
        st.write("Thank you for sharing your thoughts!")
