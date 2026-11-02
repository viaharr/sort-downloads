Sort Downloads

A minimal Python script to automatically organize the Downloads folder by file extensions.

Features

- Sorts files into `Downloads/Sorted/` subfolders.
- Categories: `Documents`, `Images`, `Archives`, `Installers`, `Torrents`.
- Ignores folders and unknown extensions.
- Prevents overwriting by appending `_1` to duplicate filenames.

Requirements

- Python 3.10+
- Standard library only (`shutil`, `pathlib`)

Usage

Run manually:

`python sort_downloads.py`

Setup Automated Run (Windows)

1. Press `Win + R`, type `taskschd.msc`, press Enter.
2. On the right, click "Create Task" (not "Create Basic Task").
3. **General** tab:
   - Name: `Sort Downloads`
   - Check "Run whether user is logged on or not".
   - Check "Hidden" (so no console window pops up).
4. **Triggers** tab -> New:
   - "Repeat task every" -> `15 minutes`
   - "for a duration of" -> `Indefinitely`
5. **Actions** tab -> New:
   - Program: `C:\Path\To\pythonw.exe` (find path below)
   - Arguments: `C:\Path\To\sort_downloads.py`
   - Start in: `C:\Path\To\`
6. Click OK and enter your Windows password.

How to find `pythonw.exe` path:

Open Command Prompt and run:

`where python`

Copy the output. Change `python.exe` to `pythonw.exe`. Example:
`C:\Users\Name\AppData\Local\Programs\Python\Python312\pythonw.exe`

Setup Automated Run (macOS / Linux)

1. Open terminal and run `crontab -e`.
2. Add this line:
`*/15 * * * * /usr/bin/python3 /path/to/sort_downloads.py`
3. Save and exit. Runs every 15 minutes.

Configuration

Edit the `RULES` dictionary in `sort_downloads.py` to add new extensions:

`".mp4": "Video",`
