import os
import sys
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

# Map destinations to source images (only team, about, cards, services, gallery, avatars, cta, posts)
MAPPING = {
    # Hero backgrounds (1920x1001) - we keep these, but overlay a black filter on top in HTML/CSS
    "hero_img_1.jpg": "Entrenamientos Programa liderazgo misional/20131206_182149.jpg",
    "hero_img_2.jpg": "Entrenamientos Programa liderazgo misional/20131206_194444.jpg",
    
    # About Section images
    "about_img_1.jpg": "Fotos viaje españa 2011/136847.jpg",  # portrait (480x720) -> (954x1200)
    "about_img_2.jpg": "Segundo Viaje Misionero 2011 España Tarragona/136656.jpg", # portrait (480x720) -> (509x617)
    
    # Card / Ruta Formativa Section (624x450)
    "card_1.jpg": "Entrenamientos Programa liderazgo misional/20131206_204111.jpg",
    "card_2.jpg": "Entrenamientos Programa liderazgo misional/20131206_204229.jpg",
    "card_3.jpg": "Primer VIAJE ECUADOR ACCUM/136646.jpg",
    "card_4.jpg": "Viaje CUBA 2013/136680.jpg",
    "card_5.jpg": "Fotos viaje españa 2011/136854.jpg",
    
    # Team profile cards (420x420)
    "team_img_1.jpg": "Entrenamientos Programa liderazgo misional/20131207_124019-SMILE.jpg", # Lisbeth portrait
    "team_img_2.jpg": "Entrenamientos Programa liderazgo misional/20131206_202500.jpg", # Docentes
    "team_img_3.jpg": "Primer VIAJE ECUADOR ACCUM/136644.jpg", # Líderes
    "team_img_4.jpg": "Viaje CUBA 2013/136676.jpg", # Alianzas
    
    # Service image cards (624x624)
    "service_img_1.jpg": "Entrenamientos Programa liderazgo misional/20131206_194548.jpg",
    "service_img_2.jpg": "Segundo Viaje Misionero 2011 España Tarragona/136665.jpg",
    "service_img_3.jpg": "Viaje CUBA 2013/136682.jpg",
    "service_img_4.jpg": "Primer VIAJE ECUADOR ACCUM/136639.jpg",
    
    # Gallery Section (1236x852)
    "gallery_img_1.jpg": "Fotos Ecuador 2010 ACCUM PRIMER VIAJE/a2f45926-4f63-40f6-932a-b5a5bf932b80-1_all_200960.jpg",
    "gallery_img_2.jpg": "Fotos Ecuador 2010 ACCUM PRIMER VIAJE/a2f45926-4f63-40f6-932a-b5a5bf932b80-1_all_200970.jpg",
    "gallery_img_3.jpg": "Fotos viaje españa 2011/136857.jpg",
    "gallery_img_4.jpg": "Fotos viaje españa 2011/136855.jpg",
    "gallery_img_5.jpg": "Viaje CUBA 2013/136685.jpg",
    "gallery_img_6.jpg": "Viaje CUBA 2013/136691.jpg",
    "gallery_img_7.jpg": "Segundo Viaje Misionero 2011 España Tarragona/136667.jpg",
    "gallery_img_8.jpg": "Primer VIAJE ECUADOR ACCUM/136647.jpg",
    
    # CTA Section (Small action snapshots)
    "cta_img_1.jpg": "Viaje CUBA 2013/136688.jpg",
    "cta_img_2.jpg": "Fotos viaje españa 2011/136848.jpg",
    "cta_img_3.jpg": "Segundo Viaje Misionero 2011 España Tarragona/136662.jpg",
    "cta_img_4.jpg": "Primer VIAJE ECUADOR ACCUM/136653.jpg",
    
    # Blog / post images (624x488) - non-repeated, unique for different entries
    "post_img_1.jpg": "Segundo Viaje Misionero 2011 España Tarragona/136668.jpg",
    "post_img_2.jpg": "Entrenamientos Programa liderazgo misional/20131206_194507.jpg",
    "post_img_3.jpg": "Fotos Ecuador 2010 ACCUM PRIMER VIAJE/a2f45926-4f63-40f6-932a-b5a5bf932b80-1_all_200965.jpg",
    "post_img_4.jpg": "Segundo Viaje Misionero 2011 España Tarragona/136654.jpg",
    "post_img_5.jpg": "Fotos Ecuador 2010 ACCUM PRIMER VIAJE/a2f45926-4f63-40f6-932a-b5a5bf932b80-1_all_200971.jpg",
    "post_img_6.jpg": "Entrenamientos Programa liderazgo misional/20131206_204217.jpg",
    
    # Blog details and single post specifics
    "post_details_1.jpg": "Primer VIAJE ECUADOR ACCUM/136641.jpg",  # 1047x540
    "post_details_2.jpg": "Viaje CUBA 2013/136686.jpg",     # 1047x540
    
    # Contact Form left side image
    "contact_img_1.jpg": "Viaje CUBA 2013/136683.jpg",  # 948x892
    
    # Testimonial avatars (PNGs, 150x150)
    "avatar_1.png": "Primer VIAJE ECUADOR ACCUM/136637.jpg",
    "avatar_2.png": "Entrenamientos Programa liderazgo misional/20131207_124019-SMILE.jpg", # Lisbeth portrait
    "avatar_3.png": "Entrenamientos Programa liderazgo misional/20131206_204213-SMILE.jpg", # student portrait
    "avatar_4.png": "Fotos viaje españa 2011/136840.jpg",
}

# Image dimensions for target assets
DIMENSIONS = {
    "hero_img_1.jpg": (1920, 1001),
    "hero_img_2.jpg": (1920, 1001),
    "about_img_1.jpg": (954, 1200),
    "about_img_2.jpg": (509, 617),
    "card_1.jpg": (624, 450),
    "card_2.jpg": (624, 450),
    "card_3.jpg": (624, 450),
    "card_4.jpg": (624, 450),
    "card_5.jpg": (624, 450),
    "team_img_1.jpg": (420, 420),
    "team_img_2.jpg": (420, 420),
    "team_img_3.jpg": (420, 420),
    "team_img_4.jpg": (420, 420),
    "gallery_img_1.jpg": (1236, 852),
    "gallery_img_2.jpg": (1236, 852),
    "gallery_img_3.jpg": (1236, 852),
    "gallery_img_4.jpg": (1236, 852),
    "gallery_img_5.jpg": (1236, 852),
    "gallery_img_6.jpg": (1236, 852),
    "gallery_img_7.jpg": (1236, 852),
    "gallery_img_8.jpg": (1236, 852),
    "cta_img_1.jpg": (173, 189),
    "cta_img_2.jpg": (130, 127),
    "cta_img_3.jpg": (168, 164),
    "cta_img_4.jpg": (154, 189),
    "post_img_1.jpg": (624, 488),
    "post_img_2.jpg": (624, 488),
    "post_img_3.jpg": (624, 488),
    "post_img_4.jpg": (624, 488),
    "post_img_5.jpg": (624, 488),
    "post_img_6.jpg": (624, 488),
    "post_details_1.jpg": (1047, 540),
    "post_details_2.jpg": (1047, 540),
    "service_img_1.jpg": (624, 624),
    "service_img_2.jpg": (624, 624),
    "service_img_3.jpg": (624, 624),
    "service_img_4.jpg": (624, 624),
    
    "contact_img_1.jpg": (948, 892),
    
    # Testimonial avatars
    "avatar_1.png": (150, 150),
    "avatar_2.png": (150, 150),
    "avatar_3.png": (150, 150),
    "avatar_4.png": (150, 150),
}

def crop_and_resize(im, target_width, target_height):
    src_width, src_height = im.size
    src_aspect = src_width / src_height
    target_aspect = target_width / target_height
    
    if src_aspect > target_aspect:
        # Source is wider than target. Crop left/right
        new_width = int(src_height * target_aspect)
        left = (src_width - new_width) // 2
        right = left + new_width
        top = 0
        bottom = src_height
    else:
        # Source is taller than target. Crop top/bottom
        new_height = int(src_width / target_aspect)
        top = (src_height - new_height) // 2
        bottom = top + new_height
        left = 0
        right = src_width
        
    cropped = im.crop((left, top, right, bottom))
    resampling_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.ANTIALIAS
    return cropped.resize((target_width, target_height), resampling_method)

def enhance_image(im):
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im = ImageOps.autocontrast(im, cutoff=1)
    im = ImageEnhance.Color(im).enhance(1.15)
    im = ImageEnhance.Contrast(im).enhance(1.10)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=100, threshold=2))
    return im

def main():
    base_src_dir = r"E:\My Drive\Clientes Freelance\Lisbeth\ACCUM\Imagenes"
    base_dst_dir = r"E:\My Drive\Clientes Freelance\Lisbeth\ACCUM\assets\img"
    
    print("Starting photo enhancement and integration process...")
    success_count = 0
    
    for filename, rel_src in MAPPING.items():
        src_path = os.path.join(base_src_dir, rel_src)
        dst_path = os.path.join(base_dst_dir, filename)
        
        if not os.path.exists(src_path):
            print(f"[Warning] Source file not found: {src_path}")
            continue
            
        target_size = DIMENSIONS.get(filename)
        if not target_size:
            print(f"[Error] Target size not configured for: {filename}")
            continue
            
        try:
            with Image.open(src_path) as im:
                enhanced = enhance_image(im)
                final_img = crop_and_resize(enhanced, target_size[0], target_size[1])
                
                if dst_path.lower().endswith(".png"):
                    final_img.save(dst_path, "PNG")
                else:
                    final_img.save(dst_path, "JPEG", quality=88)
                    
                print(f"[Success] Processed {rel_src} -> {filename} ({target_size[0]}x{target_size[1]})")
                success_count += 1
        except Exception as e:
            print(f"[Error] Processing {rel_src}: {e}")
            
    print(f"\nCompleted! Enhanced and integrated {success_count} images successfully.")

if __name__ == "__main__":
    main()
