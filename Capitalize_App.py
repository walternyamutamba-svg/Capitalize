import streamlit as st

# ---------------------------
# Your capitalization function
# ---------------------------
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


# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Smart Capitalizer", page_icon="📝", layout="centered")

st.title("📝 Smart Text Capitalizer")
st.write(
    "Paste your text below and click **Capitalize** to fix capitalization, spacing, and punctuation automatically."
)

# Text input area
user_input = st.text_area("Enter your text:", height=200, placeholder="Type or paste text here...")

# Button to process
if st.button("Capitalize"):
    if user_input.strip():
        result = capitalize_smartly(user_input)
        st.subheader("✅ Corrected Text:")
        st.text_area("Output", value=result, height=200)
    else:
        st.warning("⚠️ Please enter some text before capitalizing.")

# Optional: Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Python")

