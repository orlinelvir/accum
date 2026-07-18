import re

def translate_details():
    filename = "blog-details.html"
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Translate Content Area
    # Intro
    content = content.replace(
        "<p>A Elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique. Tortor posuere ac ut consequat semper viverra nam libero justo. Mauris commodo quis imperdiet massa tincidunt nunc pulvinar sapien et. Aliquam purus sit amet luctus venenatis lectus magna fringilla urna. Purus sit amet luctus venenatis lectus. Nunc aliquet bibendum enim facilisis. Pretium viverra suspendisse potenti nullam ac tortor vitae. Purus sit amet luctus venenatis lectus. Nunc aliquet bibendum enim facilisis. Pretium viverra suspendisse potenti nullam ac tortor vitae.</p>",
        "<p>El llamado a las naciones es urgente y el continente europeo presenta un desafío misionero único. A menudo visto como un lugar históricamente cristiano, hoy en día se ha convertido en uno de los campos misioneros más necesitados de la verdad del evangelio. El secularismo y el abandono de la fe han dejado un vacío espiritual enorme en las nuevas generaciones.</p>"
    )
    
    # Heading 1
    content = content.replace(
        "<h2>Ocean pollution is every corner around the world</h2>",
        "<h2>El Desafío Misionero en el Continente Europeo</h2>"
    )
    
    # Body 1
    content = content.replace(
        "<p>On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best. <br><br>On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances.</p>",
        "<p>Durante nuestro viaje misionero a España en 2011, pudimos constatar de primera mano la necesidad espiritual extrema en regiones como Cataluña y Tarragona. Los templos históricos que antes albergaban congregaciones numerosas hoy están vacíos o convertidos en museos. Las nuevas generaciones crecen sin conocer los fundamentos de la fe. No obstante, vemos este tiempo como una oportunidad sin precedentes para movilizar obreros transculturales que lleven esperanza y planten nuevas iglesias locales.</p>"
    )
    
    # Quote
    quote_old = """<blockquote>
              <svg class="cs_accent_color" width="41" height="37" viewBox="0 0 41 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M37.0872 18.5001H30.707V13.3959C30.707 10.5806 32.9959 8.29175 35.8112 8.29175H36.4492C37.5099 8.29175 38.3633 7.4384 38.3633 6.37769V2.54956C38.3633 1.48885 37.5099 0.635498 36.4492 0.635498H35.8112C28.7611 0.635498 23.0508 6.34578 23.0508 13.3959V32.5365C23.0508 34.65 24.7655 36.3647 26.8789 36.3647H37.0872C39.2007 36.3647 40.9154 34.65 40.9154 32.5365V22.3282C40.9154 20.2148 39.2007 18.5001 37.0872 18.5001ZM14.1185 18.5001H7.73828V13.3959C7.73828 10.5806 10.0272 8.29175 12.8424 8.29175H13.4805C14.5412 8.29175 15.3945 7.4384 15.3945 6.37769V2.54956C15.3945 1.48885 14.5412 0.635498 13.4805 0.635498H12.8424C5.79232 0.635498 0.0820312 6.34578 0.0820312 13.3959V32.5365C0.0820312 34.65 1.79671 36.3647 3.91016 36.3647H14.1185C16.2319 36.3647 17.9466 34.65 17.9466 32.5365V22.3282C17.9466 20.2148 16.2319 18.5001 14.1185 18.5001Z" fill="currentColor"/>
              </svg>                  
              But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, who expound the actual teachings of the great explorer of the truth, the master. <small>Andrew Hobar</small>
            </blockquote>"""
            
    quote_new = """<blockquote>
              <svg class="cs_accent_color" width="41" height="37" viewBox="0 0 41 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M37.0872 18.5001H30.707V13.3959C30.707 10.5806 32.9959 8.29175 35.8112 8.29175H36.4492C37.5099 8.29175 38.3633 7.4384 38.3633 6.37769V2.54956C38.3633 1.48885 37.5099 0.635498 36.4492 0.635498H35.8112C28.7611 0.635498 23.0508 6.34578 23.0508 13.3959V32.5365C23.0508 34.65 24.7655 36.3647 26.8789 36.3647H37.0872C39.2007 36.3647 40.9154 34.65 40.9154 32.5365V22.3282C40.9154 20.2148 39.2007 18.5001 37.0872 18.5001ZM14.1185 18.5001H7.73828V13.3959C7.73828 10.5806 10.0272 8.29175 12.8424 8.29175H13.4805C14.5412 8.29175 15.3945 7.4384 15.3945 6.37769V2.54956C15.3945 1.48885 14.5412 0.635498 13.4805 0.635498H12.8424C5.79232 0.635498 0.0820312 6.34578 0.0820312 13.3959V32.5365C0.0820312 34.65 1.79671 36.3647 3.91016 36.3647H14.1185C16.2319 36.3647 17.9466 34.65 17.9466 32.5365V22.3282C17.9466 20.2148 16.2319 18.5001 14.1185 18.5001Z" fill="currentColor"/>
              </svg>                  
              «Todos tenemos una tarea en la Gran Comisión: algunos van a los campos misioneros, algunos envían a los obreros, y todos nos unimos en oración y apoyo constante.» <small>Lisbeth Velázquez Girot</small>
            </blockquote>"""
            
    content = content.replace(quote_old, quote_new)
    
    # Heading 2
    content = content.replace(
        "<h2>Stop now throwing plastic on ocean</h2>",
        "<h2>La Preparación a través del Taller LPS</h2>"
    )
    
    # Body 2
    content = content.replace(
        "<p>We denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances.</p>",
        "<p>Para enfrentar este desafío de forma efectiva, ACCUM ha estructurado su Ruta Formativa. Antes de enviar a un misionero, pasa por una mentoría y por el taller intensivo \"Listos para Salir\" (LPS). Este taller prepara mental, cultural y espiritualmente a los obreros para la adaptación a nuevos entornos transculturales de servicio.</p>"
    )
    
    # Video Section
    video_old = """<a href="https://www.youtube.com/embed/xcwUALN1q5Q" class="cs_video_block cs_style_1 cs_bg_filed cs_video_open cs_center cs_radius_15 position-relative" data-src="assets/img/post_details_2.jpg">
              <span class="cs_player_btn cs_style_3 cs_white_color">
                <svg width="70" height="70" viewBox="0 0 70 70" fill="none" xmlns="http://www.w3.org/2000/svg">
                   <path d="M35 0C15.7004 0 0 15.7004 0 35C0 54.2996 15.7004 70 35 70C54.2996 70 70 54.2996 70 35C70 15.7004 54.2996 0 35 0ZM35 64.1667C18.9175 64.1667 5.83333 51.0825 5.83333 35C5.83333 18.9175 18.9175 5.83333 35 5.83333C51.0825 5.83333 64.1667 18.9175 64.1667 35C64.1667 51.0825 51.0825 64.1667 35 64.1667ZM23.3333 51.4704L52.6167 35L23.3333 18.5296V51.4733V51.4704ZM29.1667 28.5017L40.7167 35L29.1667 41.4983V28.5017Z" fill="currentColor"/>
                </svg>                  
              </span>
            </a>"""
            
    video_new = """<div class="cs_video_block cs_style_1 cs_bg_filed cs_radius_15 position-relative" data-src="assets/img/post_details_2.jpg">
            </div>"""
            
    content = content.replace(video_old, video_new)
    
    # Body 3
    content = content.replace(
        "<p>So, blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain amount of people.</p>",
        "<p>Una vez completado el entrenamiento, los obreros son movilizados a alianzas estratégicas en el extranjero. Cada viaje no es una excursión independiente; se realiza bajo el amparo de la iglesia local y con el respaldo pastoral necesario para dar sostenibilidad a la obra a largo plazo.</p>"
    )
    
    # Body 4 Intro
    content = content.replace(
        "<p>Our Proposed Solution: Our experienced team of web developers and booking system integration experts will collaborate closely with you to design a website that reflects the professionalism of your cleaning services. Our solution will include:</p>",
        "<p>Nuestros objetivos claves en la capacitación y envío de obreros incluyen:</p>"
    )
    
    # List items
    list_old = """<ul>
              <li>An intuitive and visually appealing website design.</li>
              <li>Seamless integration of a booking system, allowing customers to schedule appointments effortlessly.</li>
              <li>Responsive design for optimal user experiences across various devices.</li>
              <li>Rigorous testing to ensure the website and booking system perform flawlessly.</li>
              <li>A content management system for easy updates and maintenance.</li>
              <li>Search engine optimization strategies to enhance online visibility.</li>
            </ul>"""
            
    list_new = """<ul>
              <li>Formación bíblica y teológica profunda enfocada en misiones.</li>
              <li>Taller intensivo de adaptación cultural y choque lingüístico.</li>
              <li>Pasantías prácticas de mediano plazo (de 2 a 3 meses) en zonas de Europa.</li>
              <li>Mentoreo y acompañamiento pastoral antes, durante y después del viaje.</li>
              <li>Alianzas estratégicas con ministerios e iglesias locales europeas.</li>
              <li>Estrategias de movilización y comités misioneros locales en las iglesias de origen.</li>
            </ul>"""
            
    content = content.replace(list_old, list_new)
    
    # Categories bottom
    content = content.replace(
        '<a href="#" class="cs_category cs_radius_3">Motion</a>\n              <a href="#" class="cs_category cs_radius_3">Graphic</a>\n              <a href="#" class="cs_category cs_radius_3">Video</a>',
        '<a href="#" class="cs_category cs_radius_3">Misiones</a>\n              <a href="#" class="cs_category cs_radius_3">Formación</a>\n              <a href="#" class="cs_category cs_radius_3">LPS</a>'
    )
    
    # Author Card
    author_old = """          <div class="cs_author_card">
            <img src="assets/img/avatar_4.png" alt="Author">
            <div>
              <h3 class="cs_fs_21 cs_semibold">Anthony Kuber</h3>
              <p>Hi, my name is Ahon Bentham. I am environmental activist and ocean <br>lover. I love to travel and writing blogging.</p>"""
              
    author_new = """          <div class="cs_author_card">
            <img src="assets/img/avatar_2.png" alt="Author">
            <div>
              <h3 class="cs_fs_21 cs_semibold">Lisbeth Velázquez Girot</h3>
              <p>Misionera, Directora y Fundadora de ACCUM Global Missions. Apasionada por movilizar, capacitar y enviar obreros a la cosecha del Señor.</p>"""
              
    content = content.replace(author_old, author_new)
    
    # Comments form
    content = content.replace(
        '<h2 class="cs_fs_38  cs_semibold cs_mb_10">Write your opinion</h2>',
        '<h2 class="cs_fs_38  cs_semibold cs_mb_10">Escribe tu opinión</h2>'
    )
    content = content.replace(
        '<p class="cs_mb_34">Your email address will not be published. Required fields are marked *</p>',
        '<p class="cs_mb_34">Tu dirección de correo electrónico no será publicada. Los campos obligatorios están marcados con *</p>'
    )
    content = content.replace(
        'placeholder="Write Your Comment*"',
        'placeholder="Escribe tu comentario*"'
    )
    content = content.replace(
        'placeholder="Your Name*"',
        'placeholder="Tu nombre*"'
    )
    content = content.replace(
        'placeholder="Your Email*"',
        'placeholder="Tu correo electrónico*"'
    )
    content = content.replace(
        '<span class="cs_btn_text">Post Comment</span>',
        '<span class="cs_btn_text">Publicar Comentario</span>'
    )
    
    # Sidebar
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
        
    print(f"[Success] Translated content and sidebar elements in {filename}")

if __name__ == "__main__":
    translate_details()
