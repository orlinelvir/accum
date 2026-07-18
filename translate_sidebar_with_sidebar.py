import re

def translate_sidebar():
    filename = "blog-with-sidebar.html"
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Sidebar Search
    content = content.replace('placeholder="Search..."', 'placeholder="Buscar..."')
    content = content.replace(
        '<h4 class="cs_sidebar_widget_title">Categories</h4>',
        '<h4 class="cs_sidebar_widget_title">Categorías</h4>'
    )
    
    # Categories list
    cats_old = """              <ul>
                <li class="cat_item"><a href="#">Charity</a></li>
                <li class="cat_item"><a href="#">Environment</a></li>
                <li class="cat_item"><a href="#">Planet</a></li>
                <li class="cat_item"><a href="#">Pollution</a></li>
                <li class="cat_item"><a href="#">Ocean</a></li>
                <li class="cat_item"><a href="#">Donation</a></li>
              </ul>"""
              
    cats_new = """              <ul>
                <li class="cat_item"><a href="#">Misiones</a></li>
                <li class="cat_item"><a href="#">Preparación</a></li>
                <li class="cat_item"><a href="#">Testimonios</a></li>
                <li class="cat_item"><a href="#">Iglesia</a></li>
                <li class="cat_item"><a href="#">Comunidad</a></li>
                <li class="cat_item"><a href="#">Formación</a></li>
              </ul>"""
              
    content = content.replace(cats_old, cats_new)
    
    # Recent Posts Title
    content = content.replace(
        '<h4 class="cs_sidebar_widget_title">Latest post</h4>',
        '<h4 class="cs_sidebar_widget_title">Artículos Recientes</h4>'
    )
    
    # Recent Post 1
    content = content.replace(
        '<h3 class="cs_recent_post_title cs_fs_21 cs_medium cs_heading_color"><a href="blog-details.html">How reforestation can save our planet</a></h3>\n                    <p class="cs_recent_post_date mb-0">Apr 10, 2024</p>',
        '<h3 class="cs_recent_post_title cs_fs_21 cs_medium cs_heading_color"><a href="blog-details.html">Misiones en Europa: La Necesidad en España y Francia</a></h3>\n                    <p class="cs_recent_post_date mb-0">Octubre 12, 2025</p>'
    )
    # Recent Post 2
    content = content.replace(
        '<h3 class="cs_recent_post_title cs_fs_21 cs_medium cs_heading_color"><a href="blog-details.html">Unmasking the hidden threat to our oceans</a></h3>\n                    <p class="cs_recent_post_date mb-0">Sep 7, 2023</p>',
        '<h3 class="cs_recent_post_title cs_fs_21 cs_medium cs_heading_color"><a href="blog-details.html">Preparación Espiritual: El Taller Listos para Salir (LPS)</a></h3>\n                    <p class="cs_recent_post_date mb-0">Noviembre 05, 2025</p>'
    )
    # Recent Post 3
    content = content.replace(
        '<h3 class="cs_recent_post_title cs_fs_21 cs_medium cs_heading_color"><a href="blog-details.html">Tips for sustainable green space in home</a></h3>\n                    <p class="cs_recent_post_date mb-0">July 1, 2023</p>',
        '<h3 class="cs_recent_post_title cs_fs_21 cs_medium cs_heading_color"><a href="blog-details.html">Testimonio en el Amazonas: Misionero 2010</a></h3>\n                    <p class="cs_recent_post_date mb-0">Enero 18, 2026</p>'
    )
    
    # Tags Cloud
    content = content.replace(
        '<h4 class="cs_sidebar_widget_title">Popular tags</h4>',
        '<h4 class="cs_sidebar_widget_title">Etiquetas Populares</h4>'
    )
    
    tags_old = """              <div class="tag_cloud">
                <a href="#" class="tag_cloud_link cs_radius_5">Business</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Environment</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Marketing</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Clean Water</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Research</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Pollution</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Charity</a>
              </div>"""
              
    tags_new = """              <div class="tag_cloud">
                <a href="#" class="tag_cloud_link cs_radius_5">Misiones</a>
                <a href="#" class="tag_cloud_link cs_radius_5">LPS</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Europa</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Ecuador</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Cuba</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Capacitación</a>
                <a href="#" class="tag_cloud_link cs_radius_5">Iglesia</a>
              </div>"""
              
    content = content.replace(tags_old, tags_new)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"[Success] Translated sidebar elements in {filename}")

if __name__ == "__main__":
    translate_sidebar()
