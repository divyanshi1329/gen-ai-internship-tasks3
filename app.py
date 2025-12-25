import streamlit as st
import os, json
from modules.spec_generator import generate_spec
from modules.formatter import spec_to_markdown
from modules.pdf_exporter import markdown_to_pdf

st.set_page_config(page_title="Requirement → Technical Spec Tool", layout="wide")

st.title("🧠 Requirement → Technical Spec Generator")
st.write("Convert high-level business requirements into modules, schemas, APIs, and pseudocode.")

requirement = st.text_area("Enter Business Requirement", height=200, placeholder="Example: Build a job portal with login, job posting, search, and applications...")

if st.button("🚀 Generate Technical Spec"):
    if not requirement.strip():
        st.warning("Please enter a requirement first.")
    else:
        os.makedirs("output", exist_ok=True)

        with st.spinner("Generating specification..."):
            spec = generate_spec(requirement)

            # Save JSON
            with open("output/spec.json", "w") as f:
                json.dump(spec, f, indent=2)

            # Markdown
            md = spec_to_markdown(spec)
            with open("output/spec.md", "w", encoding="utf-8") as f:
                f.write(md)

            # PDF
            pdf_path = "output/spec.pdf"
            markdown_to_pdf(md, pdf_path)

        st.success("✅ Generated spec successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📄 Markdown Spec Preview")
            st.text(md[:3000] + "\n...")

        with col2:
            st.subheader("🧾 JSON Output Preview")
            st.json(spec)

        st.subheader("⬇️ Download Outputs")
        st.download_button("Download JSON", data=json.dumps(spec, indent=2), file_name="spec.json")
        st.download_button("Download Markdown", data=md, file_name="spec.md")

        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF", data=f, file_name="spec.pdf")
