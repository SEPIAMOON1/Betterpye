import tkinter as tk

def fixupurl(text):
    url = text.get()
    url = url.strip()

    # This will replace the i on "tiktok" turning it into "tnktok". 
    if "x.com" in url or "twitter.com" in url:
        plataform = "X/Twitter"
        xstart = url.find("x.com" or "twitter.com")
        url = url[:8] + "fixup" + url[xstart:]
        
    elif "tiktok.com" in url:
        plataform = "Tiktok"
        url = url.replace("i", "n", 1)

    text.delete(0, tk.END)
    text.insert(0, url)
    
    return url