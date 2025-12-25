import os, json
from modules.spec_generator import generate_spec
from modules.formatter import spec_to_markdown
from modules.pdf_exporter import markdown_to_pdf

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)

    requirement = input("Enter high-level business requirement: ")

    print("📌 Generating technical specification...")
    spec = generate_spec(requirement)

    # Save JSON
    with open("output/spec.json", "w") as f:
        json.dump(spec, f, indent=2)

    # Save Markdown
    md = spec_to_markdown(spec)
    with open("output/spec.md", "w", encoding="utf-8") as f:
        f.write(md)

    # Save PDF
    markdown_to_pdf(md, "output/spec.pdf")

    print("✅ Saved output/spec.json")
    print("✅ Saved output/spec.md")
    print("✅ Saved output/spec.pdf")
