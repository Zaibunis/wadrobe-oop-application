import streamlit as st
import base64
import json
from wardrobe import User, Mood, Wardrobe, ClothingItem

# Load wardrobe
with open("wardrobe.json") as f:
    wardrobe_data = json.load(f)

wardrobe = Wardrobe(wardrobe_data)

def get_base64_bg(path):
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpg;base64,{encoded}"

bg_base64 = get_base64_bg("images/background.jpg")

st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("🧠 Mood to Color Wardrobe Suggestion")

# Mood Emojis for UI
mood_emoji_map = {
    "Happy": "😊",
    "Sad": "😢",
    "Angry": "😠",
    "Relaxed": "😌"
}

user_name = st.text_input("Enter your name")
selected_mood = st.selectbox("How are you feeling?", ["Happy", "Sad", "Angry", "Relaxed"])

if user_name and selected_mood:
    user = User(user_name)
    color = Mood.get_color(selected_mood)
    suggestions = wardrobe.get_by_color(color)

    # Display mood with emoji
    st.markdown(f"### 🎨 Mood Color: **{color.capitalize()}** {mood_emoji_map[selected_mood]}")

    st.markdown("#### 👕 Outfit Suggestions:")
    if suggestions:
        for item in suggestions:
            # Display clothing with image
            st.image(f"images/{item.images}", width=500)

            st.write(f"**{item.name}** ({item.type}) - **Size**: {item.size} - **Price**: ${item.price}")
    else:
        st.warning("No outfits found for this mood!")
