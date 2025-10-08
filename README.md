# ✨ Capitalize Smartly — Jupyter Notebook Project
## 👥 Group Members

The project was developed by the following team:

- **Walter Nyamutamba**  
- **Sylvestre Mukiza**  
- **Mireille IRAKOZE**  
- **Joelle SAFI**

This project provides a **smart text capitalization algorithm**, implemented and demonstrated in a Jupyter Notebook. It automatically fixes common writing issues such as missing capitalization, excessive spacing, and standalone lowercase `i`.  

Perfect for cleaning up **informal or mobile-typed text** for reports, NLP preprocessing, or educational purposes.

---

## 📌 Features

- ✅ Trims leading and trailing spaces  
- ✅ Normalizes multiple spaces while preserving line breaks  
- ✅ Ensures proper spacing after sentence-ending punctuation (`.`, `!`, `?`)  
- ✅ Capitalizes the first non-space character and the first letter after punctuation  
- ✅ Replaces standalone lowercase `i` with uppercase `I`  
- ✅ Demonstrated interactively in a Jupyter Notebook

---

## 🧠 Algorithm Overview

The core logic is described in the `Capitalize_Smartly.ipynb` notebook.  

Pseudocode:

```text
FUNCTION capitalize_smartly(text: STRING) -> STRING
    1. Trim leading and trailing spaces
    2. Normalize multiple spaces (except line breaks)
    3. Ensure one space after punctuation (.!?)
    4. Capitalize the first non-space character
    5. Capitalize the first letter after punctuation
    6. Replace standalone 'i' with 'I'
    RETURN text
