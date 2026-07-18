import re
import os

def extract_section(content, start_tag, end_tag):
    pattern = re.escape(start_tag) + r"(.*?)" + re.escape(end_tag)
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def sync_all_pages():
    # Read index.html
    with open("index.html", "r", encoding="utf-8") as f:
        index_content = f.read()
        
    # 1. Extract Custom Style Block
    style_block = extract_section(index_content, "<style>", "</style>")
    if style_block:
        style_block = f"<style>{style_block}</style>"
    else:
        print("[Error] Custom style block not found in index.html")
        return

    # 2. Extract Header Section
    header_section = extract_section(index_content, "<!-- Start Header Section -->", "<!-- End Header Section -->")
    if header_section:
        # Make links point back to index.html sections
        header_section_adjusted = header_section.replace('href="#', 'href="index.html#')
        # Re-wrap in tags
        header_section_adjusted = f"<!-- Start Header Section -->{header_section_adjusted}<!-- End Header Section -->"
    else:
        print("[Error] Header section not found in index.html")
        return

    # 3. Extract Donation Modal
    donation_modal = extract_section(index_content, "<!-- Start Donation modal -->", "<!-- End Donation modal -->")
    if donation_modal:
        donation_modal_adjusted = f"<!-- Start Donation modal -->{donation_modal}<!-- End Donation modal -->"
    else:
        print("[Error] Donation modal not found in index.html")
        return

    # 4. Extract Footer Section
    footer_section = extract_section(index_content, "<!-- Start Footer Section -->", "<!-- End Footer Section -->")
    if footer_section:
        # Make links point back to index.html sections for footer as well
        footer_section_adjusted = footer_section.replace('href="#', 'href="index.html#')
        footer_section_adjusted = f"<!-- Start Footer Section -->{footer_section_adjusted}<!-- End Footer Section -->"
    else:
        print("[Error] Footer section not found in index.html")
        return

    # Secondary files to process
    files_to_sync = ["blog.html", "blog-with-sidebar.html", "blog-details.html"]
    
    for filename in files_to_sync:
        if not os.path.exists(filename):
            print(f"[Warning] File not found: {filename}")
            continue
            
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace styles
        if "<style>" in content and "</style>" in content:
            content = re.sub(r"<style>.*?</style>", style_block, content, flags=re.DOTALL)
        else:
            content = content.replace("</head>", f"  {style_block}\n</head>")
            
        # Replace Header
        content = re.sub(r"<!-- Start Header Section -->.*?<!-- End Header Section -->", header_section_adjusted, content, flags=re.DOTALL)
        
        # Replace Donation Modal
        content = re.sub(r"<!-- Start Donation modal -->.*?<!-- End Donation modal -->", donation_modal_adjusted, content, flags=re.DOTALL)
        
        # Replace Footer
        content = re.sub(r"<!-- Start Footer Section -->.*?<!-- End Footer Section -->", footer_section_adjusted, content, flags=re.DOTALL)
        
        # Translate general UI labels:
        content = content.replace('href="index.html">Home</a>', 'href="index.html">Inicio</a>')
        content = content.replace('active">Blog</li>', 'active">Noticias</li>')
        content = content.replace('active">Blog Details</li>', 'active">Detalles del Artículo</li>')
        
        content = content.replace("Blog Grid", "Noticias y Testimonios")
        content = content.replace("Blog Details", "Detalles del Artículo")
        content = content.replace("Blog With Sidebar", "Noticias del Ministerio")
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"[Success] Synchronized header, footer, modals and styles for {filename}")

if __name__ == "__main__":
    sync_all_pages()
