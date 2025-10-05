import streamlit as st
import io
import base64

# -----------------------------------
# Capitalization Function
# -----------------------------------
def capitalize_smartly(text: str) -> str:
    # Step 0: strip leading/trailing spaces, preserve line breaks
    lines = [line.strip() for line in text.strip().splitlines()]

    corrected_lines = []
    for line in lines:
        if not line:
            corrected_lines.append("")  # keep blank lines
            continue

        # Step 1: normalize spaces inside the line
        words = line.split()
        line = " ".join(words)

        # Step 2: ensure space after ., !, or ? if another sentence follows
        fixed = ""
        i = 0
        while i < len(line):
            fixed += line[i]
            if line[i] in ".!?":
                # add one space if next char is a letter
                if i + 1 < len(line) and line[i+1] != " ":
                    fixed += " "
            i += 1
        line = fixed

        # Step 3: capitalize first non-space char
        if line and line[0].isalpha():
            line = line[0].upper() + line[1:]

        # Step 4: capitalize after ., !, ?
        result = ""
        capitalize_next = False
        for ch in line:
            if capitalize_next and ch.isalpha():
                result += ch.upper()
                capitalize_next = False
            else:
                result += ch
            if ch in ".!?":
                capitalize_next = True
        line = result

        # Step 5: replace standalone " i " with " I "
        words = line.split(" ")
        for j in range(len(words)):
            if words[j] == "i":
                words[j] = "I"
        line = " ".join(words)

        corrected_lines.append(line)

    return "\n".join(corrected_lines)



# Function to set background with overlay
def set_background_with_overlay(image_file):
    # Read image and encode in base64
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    
    # Combine background + overlay CSS
    page_bg_css = f"""
    <style>
    /* Background image */
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        position: relative;  /* Needed for overlay positioning */
    }}

    /* Overlay to dim background */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(255, 255, 255, 0.4);  /* 40% white */
        z-index: 0;
    }}

    /* Bring content above overlay */
    .block-container {{
        position: relative;
        z-index: 1;
    }}
    </style>
    """
    st.markdown(page_bg_css, unsafe_allow_html=True)

# ✅ Call the function
set_background_with_overlay("logo.png")
# -----------------------------------
# Streamlit App
# -----------------------------------
st.image("logo.png", use_container_width=True)
st.set_page_config(page_title="Smart Capitalizer", page_icon="📝", layout="centered")
st.title("📝 Smart Text Capitalizer")
st.write(
    "This app automatically fixes capitalization, spacing, and punctuation. "
    "You can either type text manually or upload a `.txt` file."
)

# Tabs for input method
tab1, tab2 = st.tabs(["✍️ Type Text", "📂 Upload File"])

input_text = ""  # variable to hold text

# Tab 1: Manual Input
with tab1:
    typed_text = st.text_area("Enter your text here:", height=200, placeholder="Type or paste your text...")
    if st.button("Capitalize Typed Text"):
        if typed_text.strip():
            input_text = typed_text
        else:
            st.warning("⚠️ Please type something before capitalizing.")

# Tab 2: File Upload
with tab2:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        file_text = uploaded_file.read().decode("utf-8")
        st.text_area("📄 File Content", value=file_text, height=200)
        if st.button("Capitalize Uploaded File"):
            if file_text.strip():
                input_text = file_text
            else:
                st.warning("⚠️ The file is empty.")

# -----------------------------------
# Output Section
# -----------------------------------
if input_text:
    corrected_text = capitalize_smartly(input_text)

    st.subheader("✅ Corrected Text:")
    st.text_area("Output", value=corrected_text, height=200)

    # Download Button
    output_buffer = io.StringIO(corrected_text)
    st.download_button(
        label="💾 Download Corrected Text",
        data=output_buffer.getvalue(),
        file_name="corrected_text.txt",
        mime="text/plain"
    )

