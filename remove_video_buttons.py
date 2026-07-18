import re

def remove_video_from_index():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
        
    # We want to remove the three video open button links in the slider
    # Let's search and replace them with empty string
    
    video_btn_pattern = r'<a href="https://www\.youtube\.com/embed/[^"]+"\s+class="cs_player_btn cs_style_1 cs_video_open[^>]+>\s*<img src="assets/img/icons/player_icon_1\.svg" alt="Player Icon">\s*</a>'
    
    # Run regex replace
    new_content, count = re.subn(video_btn_pattern, "", content)
    print(f"Removed {count} video play buttons from index.html")
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)

def remove_video_from_details():
    with open("blog-details.html", "r", encoding="utf-8") as f:
        content = f.read()
        
    # In blog-details.html, there is a video block:
    # <a href="https://www.youtube.com/embed/xcwUALN1q5Q" class="cs_video_block ..."> ... </a>
    # Let's replace it with a simple static image card div
    
    video_details_pattern = r'<a href="https://www\.youtube\.com/embed/xcwUALN1q5Q" class="cs_video_block cs_style_1 cs_bg_filed cs_video_open cs_center cs_radius_15 position-relative" data-src="assets/img/post_details_2\.jpg">.*?</a>'
    
    new_content, count = re.subn(
        video_details_pattern, 
        '<div class="cs_video_block cs_style_1 cs_bg_filed cs_radius_15 position-relative" data-src="assets/img/post_details_2.jpg" style="min-height: 400px;"></div>', 
        content, 
        flags=re.DOTALL
    )
    print(f"Replaced {count} video blocks with static image banner in blog-details.html")
    
    with open("blog-details.html", "w", encoding="utf-8") as f:
        f.write(new_content)

def translate_by_label(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace By with Por in authors
    new_content = content.replace("<span>By ", "<span>Por ")
    new_content = new_content.replace("<span>By", "<span>Por")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Translated 'By' to 'Por' in {filename}")

if __name__ == "__main__":
    remove_video_from_index()
    remove_video_from_details()
    translate_by_label("blog.html")
    translate_by_label("blog-with-sidebar.html")
