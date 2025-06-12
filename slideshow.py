#!/usr/bin/env python3

import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
from pathlib import Path

class Slideshow:
    def __init__(self, root, image_dir, delay):
        self.root = root
        self.image_dir = image_dir
        self.delay = int(delay * 1000)  # Convert seconds to milliseconds
        
        # Make window fullscreen
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='black')
        
        # Get screen dimensions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Create label for displaying images
        self.label = tk.Label(root, background='black')
        self.label.pack(expand=True, fill='both')
        
        # Get list of valid image files
        valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        self.image_files = sorted([
            f for f in Path(image_dir).iterdir()
            if f.suffix.lower() in valid_extensions
        ])
        
        if not self.image_files:
            print(f"Error: No valid image files found in {image_dir}")
            sys.exit(1)
        
        # Initialize index
        self.current_index = 0
        
        # Bind escape key to exit fullscreen
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        # Start slideshow
        self.show_next_image()
    
    def show_next_image(self):
        try:
            # Load image
            image_path = self.image_files[self.current_index]
            image = Image.open(image_path)
            
            # Calculate resize dimensions while maintaining aspect ratio
            img_ratio = image.width / image.height
            screen_ratio = self.screen_width / self.screen_height
            
            if screen_ratio > img_ratio:
                # Screen is wider than image
                height = self.screen_height
                width = int(height * img_ratio)
            else:
                # Screen is taller than image
                width = self.screen_width
                height = int(width / img_ratio)
            
            # Resize image
            image = image.resize((width, height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(image)
            
            # Update label
            self.label.configure(image=photo)
            self.label.image = photo  # Keep a reference
            
            # Update index for next image
            self.current_index = (self.current_index + 1) % len(self.image_files)
            
            # Schedule next image
            self.root.after(self.delay, self.show_next_image)
            
        except Exception as e:
            print(f"Error displaying image: {e}")
            self.current_index = (self.current_index + 1) % len(self.image_files)
            self.root.after(self.delay, self.show_next_image)

def main():
    if len(sys.argv) != 3:
        print("Usage: python slideshow.py <image_directory> <delay_in_seconds>")
        sys.exit(1)
    
    image_dir = sys.argv[1]
    try:
        delay = float(sys.argv[2])
        if delay <= 0:
            raise ValueError("Delay must be positive")
    except ValueError:
        print("Error: Delay must be a positive number")
        sys.exit(1)
    
    if not os.path.isdir(image_dir):
        print(f"Error: Directory not found: {image_dir}")
        sys.exit(1)
    
    root = tk.Tk()
    app = Slideshow(root, image_dir, delay)
    root.mainloop()

if __name__ == '__main__':
    main()

