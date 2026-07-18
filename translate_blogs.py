import re

POSTS_TRANSLATIONS = [
    {
        "category": "Misiones",
        "date": "Octubre 12, 2025",
        "title": "Misiones en Europa: La Necesidad en España y Francia",
        "author": "Lisbeth Velázquez"
    },
    {
        "category": "Preparación",
        "date": "Noviembre 05, 2025",
        "title": "Preparación Espiritual: El Taller Listos para Salir (LPS)",
        "author": "ACCUM Missions"
    },
    {
        "category": "Testimonios",
        "date": "Enero 18, 2026",
        "title": "Testimonio en el Amazonas: Recordando el Viaje Misionero 2010",
        "author": "Líder de Viaje"
    },
    {
        "category": "Iglesia",
        "date": "Febrero 22, 2026",
        "title": "Movilización de la Iglesia: ¿Cómo enviar a tus propios misioneros?",
        "author": "Lisbeth Velázquez"
    },
    {
        "category": "Comunidad",
        "date": "Marzo 04, 2026",
        "title": "Transformación Comunitaria en Colombia: Impacto y Desafíos",
        "author": "Misionero Residente"
    },
    {
        "category": "Formación",
        "date": "Abril 15, 2026",
        "title": "Capacitación Transcultural: Formando a la Nueva Generación de Obreros",
        "author": "Docente Invitado"
    }
]

def translate_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We want to replace each post's details
    # The structure of a post card in Donaty is:
    # <div class="cs_post cs_style_1 ...">
    #   ...
    #   <img src="assets/img/post_img_(X).jpg" ...>
    #   <div class="cs_post_category ...">(Category)</div>
    #   ...
    #   <div class="cs_post_meta ...">(Date)</div>
    #   <h3 class="cs_post_title ..."><a href="...">(Title)</a></h3>
    #   ...
    #   <span>By (Author)</span>
    
    # We can do a regex loop based on the post_img_X.jpg matching.
    # Let's find all occurrences of cs_post and substitute them or replace sequentially.
    # Alternatively, we can search for blocks.
    # Let's write a parser that splits by `<div class="cs_post cs_style_1` and processes each block.
    
    parts = content.split('<div class="cs_post cs_style_1')
    new_content = parts[0]
    
    for part in parts[1:]:
        # Find which post_img this part has
        img_match = re.search(r'assets/img/post_img_(\d)\.jpg', part)
        if img_match:
            img_num = int(img_match.group(1))
            # Get translation details (1-indexed based on image number)
            # post_img_1.jpg corresponds to index 0, post_img_2.jpg to index 1, etc.
            idx = img_num - 1
            if 0 <= idx < len(POSTS_TRANSLATIONS):
                trans = POSTS_TRANSLATIONS[idx]
                
                # Replace Category
                part = re.sub(
                    r'(<div class="cs_post_category [^>]+>)[^<]+(</div>)',
                    r'\g<1>' + trans["category"] + r'\g<2>',
                    part
                )
                # Replace Date
                part = re.sub(
                    r'(<div class="cs_post_meta [^>]+>)[^<]+(</div>)',
                    r'\g<1>' + trans["date"] + r'\g<2>',
                    part
                )
                # Replace Title
                part = re.sub(
                    r'(<h3 class="cs_post_title [^>]+>\s*<a href="[^"]+">)[^<]+(</a>\s*</h3>)',
                    r'\g<1>' + trans["title"] + r'\g<2>',
                    part
                )
                # Replace Author
                part = re.sub(
                    r'(<span>By\s+)[^<]+(</span>)',
                    r'\g<1>' + trans["author"] + r'\g<2>',
                    part
                )
                
        new_content += '<div class="cs_post cs_style_1' + part
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"[Success] Translated post cards in {filename}")

if __name__ == "__main__":
    translate_file("blog.html")
    translate_file("blog-with-sidebar.html")
