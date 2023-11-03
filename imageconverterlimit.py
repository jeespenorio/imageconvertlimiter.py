import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import time

# Define the ImageConverterApp class
class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter ni Hot Papi")

        # Section 1: Input
        self.label_input = tk.Label(root, text="Select a PNG image:")
        self.label_input.pack()
        self.input_button = tk.Button(root, text="Browse", command=self.load_image)
        self.input_button.pack()

        # Section 2: Output
        self.label_output = tk.Label(root, text="Output directory:")
        self.label_output.pack()
        self.output_button = tk.Button(root, text="Browse", command=self.choose_output_directory)
        self.output_button.pack()

        # Section 3: Convert button
        self.convert_button = tk.Button(root, text="Convert to JPG", command=self.convert_to_jpg)
        self.convert_button.pack()

        # Countdown timer
        self.timer_label = tk.Label(root, text="")
        self.timer_label.pack()
        self.start_time = None
        self.time_limit = 1 * 60  # 10 minutes in seconds

        # Initialize variables
        self.input_file = ""
        self.output_dir = ""

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(0, self.time_limit - elapsed_time)
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        self.timer_label.config(text=f"Time left: {minutes:02d}:{seconds:02d}")

        # Check if the time limit has been reached
        if elapsed_time >= self.time_limit:
            self.timer_label.config(text="Time limit exceeded. Buy Now!!!")
            self.convert_button.config(state=tk.DISABLED)
            self.input_button.config(state=tk.DISABLED)
        else:
            self.root.after(1000, self.update_timer)

    def start_timer(self):
        self.start_time = time.time()
        self.update_timer()

    # Function for loading the input image
    def load_image(self):
        self.input_file = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        self.label_input.config(text=f"Selected image: {self.input_file}")
        self.start_timer()

    # Function for choosing the output directory
    def choose_output_directory(self):
        self.output_dir = filedialog.askdirectory()
        self.label_output.config(text=f"Output directory: {self.output_dir}")

    # Function for converting the input image to JPG
    def convert_to_jpg(self):
        if self.input_file and self.output_dir:
            try:
                img = Image.open(self.input_file)
                img = img.convert('RGB')

                output_file = f"{self.output_dir}/{self.get_file_name()}.jpg"
                img.save(output_file, "JPEG")
                tk.messagebox.showinfo("Success", "Image converted and saved as JPG.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            tk.messagebox.showerror("Error", "Please select an input image and an output directory.")

    # Function to get the file name from the input file path
    def get_file_name(self):
        return os.path.splitext(os.path.basename(self.input_file))[0]

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
