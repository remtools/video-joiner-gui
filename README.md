# 🎬 Video Joiner GUI

A simple, open-source desktop app to join multiple video files into one using a drag-and-drop-friendly interface.  
Built with Python, MoviePy, and Tkinter — no coding experience needed.

---

## ✨ Features

- 📂 Select folder containing videos  
- 💾 Choose where to save the output file  
- 📊 Visual progress bar while loading and exporting  
- 🔃 Automatically joins videos in alphabetical order  
- 🎥 Supports `.mp4`, `.mov`, `.avi`, `.mkv`  
- 🛠 Build a portable `.exe` with PyInstaller  

---

## 🚀 How to Get It Working

### 🧱 Prerequisites

- **Python 3.7 or higher**  
- **pip** (comes with Python)  
- Works on **Windows**, should run on macOS/Linux with minor tweaks  

---

### 🔧 Installation

1. Clone or download the repository  
2. Navigate to the project folder in your terminal  
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### ▶️ Running the App (from source)

```bash
python index.py
```

- A window will open  
- Browse to a folder with video files  
- Choose where to save the output  
- Click **"Join Videos"** and wait for it to finish  

---

### 🛠 Building the `.exe` (Windows)

To create a standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed index.py
```

Your EXE will appear in the `dist/` folder.

---

## ❓ FAQ

### 💬 Q: I see `ModuleNotFoundError: No module named 'moviepy'`  
A: You need to install MoviePy first:

```bash
pip install moviepy
```

---

### 💬 Q: It says `ffmpeg` is missing  
A: On first run, MoviePy downloads `ffmpeg` via `imageio`. Just be connected to the internet the first time you use it.

---

### 💬 Q: App freezes during export?  
A: Some large video files can cause delays. Be patient, especially if joining many clips or large `.mov` files.

---

### 💬 Q: Output file not playing correctly?  
A: Make sure all your input clips:
- Have the same resolution
- Are not corrupted
- Are supported file types (`.mp4`, `.mov`, `.avi`, `.mkv`)

---

## 🔍 Troubleshooting Tips

- If the app doesn't launch, try running via terminal to see errors:
  ```bash
  python index.py
  ```

- To reset `ffmpeg` config:
  ```bash
  python -c "import imageio; imageio.plugins.ffmpeg.download()"
  ```

---

## 📁 Project Structure

```
video-joiner-gui/
├── index.py              # GUI script
├── requirements.txt      # Dependencies
├── README.md             # You're reading it
├── .gitignore
└── dist/ (optional)      # Built .exe goes here
```

---

## 🧾 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- [MoviePy](https://github.com/Zulko/moviepy)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
