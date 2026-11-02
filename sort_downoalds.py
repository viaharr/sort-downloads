import shutil
from pathlib import Path

DOWNLOADS = Path.home() / "Downloads"
TARGET = DOWNLOADS / "Sorted"

RULES = {
    ".doc":  "Documents", ".docx": "Documents", ".txt": "Documents",
    ".xls":  "Documents",     ".xlsx": "Documents",     ".csv": "Documents",
    ".jpg":  "Images",    ".jpeg": "Images",    ".png": "Images", ".gif": "Images",
    ".zip":  "Archives",  ".rar":  "Archives",  ".7z":  "Archives",
    ".exe":  "Installers", ".msi": "Installers", ".torrent": "Torrents"
}

def sort_downloads():
    TARGET.mkdir(exist_ok=True) # exist_ok=True = если папка уже существует ничего не делай
    
    for item in DOWNLOADS.iterdir():
        if item.is_dir():
            continue
        
        ext = item.suffix.lower()
        folder_name = RULES.get(ext)
        
        if folder_name is None:
            continue
        
        dest_dir = TARGET / folder_name
        dest_dir.mkdir(exist_ok=True)
        
        dest = dest_dir / item.name
        if dest.exists():
            dest = dest_dir / f"{item.stem}_1{item.suffix}"
            
        shutil.move(str(item), str(dest))
        
if __name__ == "__main__":
    sort_downloads()

