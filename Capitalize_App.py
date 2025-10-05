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





   

# -----------------------------------
# Streamlit App
# -----------------------------------
st.image("logo.png", use_container_width=True)
st.set_page_config(page_title="Smart Capitalizer", page_icon="📝", layout="centered")
st.markdown("""
**Group Members:**  
- Walter Nyamutamba  
- Sylvestre Mukiza 
- Mireille IRAKOZE  
- Joelle SAFI
""")
st.title("🤖 Meet Your Friendly Robot!")



st.markdown("""
**Name:** RoboHelper 3000  
**Function:** Assists humans with text processing, calculations, and keeping things tidy!  
**Special Features:**  
- 📝 Can fix your capitalization automatically  
- ⚡ Processes text at lightning speed  
 
**Fun Fact:**  
RoboHelper 3000 loves long walks through lines of text and debugging adventures!
""")



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






