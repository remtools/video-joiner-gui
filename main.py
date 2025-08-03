import os
import threading
from tkinter import Tk, Label, Button, filedialog, messagebox, StringVar, ttk
from moviepy.editor import VideoFileClip, concatenate_videoclips
from contextlib import ExitStack

class VideoJoinerApp:
    def __init__(self, master):
        self.master = master
        master.title("🎬 Video Joiner")

        self.folder_path = StringVar()
        self.output_path = StringVar()

        Label(master, text="1. Select video folder:").pack()
        Button(master, text="📂 Browse Folder", command=self.browse_folder).pack()
        Label(master, textvariable=self.folder_path).pack()

        Label(master, text="2. Choose output file:").pack()
        Button(master, text="💾 Save As...", command=self.choose_output_file).pack()
        Label(master, textvariable=self.output_path).pack()

        self.progress = ttk.Progressbar(master, length=300, mode='determinate')
        self.progress.pack(pady=10)

        self.status = StringVar()
        Label(master, textvariable=self.status).pack()

        Button(master, text="▶️ Join Videos", command=self.run_joining).pack(pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def choose_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4",
                                                 filetypes=[("MP4 files", "*.mp4")])
        if file_path:
            self.output_path.set(file_path)

    def run_joining(self):
        folder = self.folder_path.get()
        output = self.output_path.get()
        if not folder or not output:
            messagebox.showerror("Error", "Please select both a folder and output file.")
            return

        threading.Thread(target=self.join_videos_thread, args=(folder, output)).start()

    def join_videos_thread(self, folder_path, output_file):
        try:
            self.status.set("🔍 Scanning folder...")
            self.progress["value"] = 0
            self.master.update()

            video_extensions = ['.mp4', '.mov', '.avi', '.mkv']
            video_files = sorted([
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in video_extensions
            ])

            if not video_files:
                messagebox.showerror("Error", "No video files found in folder.")
                return

            total_files = len(video_files)
            self.status.set(f"📂 Loading {total_files} clips...")

            clips = []
            with ExitStack() as stack:
                for idx, file in enumerate(video_files):
                    clip = stack.enter_context(VideoFileClip(file))
                    clips.append(clip)
                    self.progress["value"] = ((idx + 1) / total_files) * 50  # Load progress up to 50%
                    self.master.update()

                self.status.set("🛠️ Joining clips...")
                final_clip = concatenate_videoclips(clips, method="compose")

                self.status.set("💾 Exporting video...")
                final_clip.write_videofile(output_file, codec="libx264", fps=24, logger=None)

            self.progress["value"] = 100
            self.status.set("✅ Done! Video saved.")
            messagebox.showinfo("Success", "Videos successfully joined!")

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")
            self.status.set("❌ Failed.")

# Run the app
if __name__ == "__main__":
    root = Tk()
    app = VideoJoinerApp(root)
    root.mainloop()
