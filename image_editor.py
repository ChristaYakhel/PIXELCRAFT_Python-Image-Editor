import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageEnhance


class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PixelCraft - Python Image Editor")
        self.root.geometry("1100x700")
        self.root.minsize(950, 620)
        self.root.configure(bg="#0B1020")

        self.original_image = None
        self.edited_image = None
        self.current_filter = "Original"

        self.show_welcome_page()

    # COLORS
    
    BG = "#0B1020"
    CARD = "#151B2E"
    CARD2 = "#1C2438"
    PURPLE = "#7C3AED"
    BLUE = "#2563EB"
    CYAN = "#06B6D4"
    WHITE = "#FFFFFF"
    LIGHT = "#D1D5DB"
    GRAY = "#8B95A7"
    GREEN = "#22C55E"
    RED = "#EF4444"

    # CLEAR SCREEN
   

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

   
    # WELCOME PAGE
 

    def show_welcome_page(self):
        self.clear_screen()

        main = tk.Frame(self.root, bg=self.BG)
        main.pack(fill="both", expand=True)

        # Top title
        title_frame = tk.Frame(main, bg=self.BG)
        title_frame.pack(pady=(55, 10))

        tk.Label(
            title_frame,
            text="✦",
            font=("Segoe UI", 35, "bold"),
            fg="#A855F7",
            bg=self.BG
        ).pack()

        tk.Label(
            title_frame,
            text="Welcome to",
            font=("Segoe UI", 20),
            fg=self.LIGHT,
            bg=self.BG
        ).pack()

        tk.Label(
            title_frame,
            text="PIXELCRAFT",
            font=("Segoe UI", 42, "bold"),
            fg="#8B5CF6",
            bg=self.BG
        ).pack()

        tk.Label(
            title_frame,
            text="A simple and powerful Python image editor",
            font=("Segoe UI", 14),
            fg=self.GRAY,
            bg=self.BG
        ).pack(pady=5)

        # Buttons
        button_frame = tk.Frame(main, bg=self.BG)
        button_frame.pack(pady=30)

        open_button = tk.Button(
            button_frame,
            text="  Open Image  ",
            command=self.open_image,
            font=("Segoe UI", 14, "bold"),
            fg=self.WHITE,
            bg=self.PURPLE,
            activebackground="#9333EA",
            activeforeground=self.WHITE,
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=14
        )
        open_button.pack(pady=8)

        filter_button = tk.Button(
            button_frame,
            text="  Explore Filters  ",
            command=self.show_filter_info,
            font=("Segoe UI", 12),
            fg=self.WHITE,
            bg=self.CARD2,
            activebackground="#27324D",
            activeforeground=self.WHITE,
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10
        )
        filter_button.pack(pady=8)

        # Features
        feature_title = tk.Label(
            main,
            text="FEATURES",
            font=("Segoe UI", 13, "bold"),
            fg=self.WHITE,
            bg=self.BG
        )
        feature_title.pack(pady=(25, 12))

        features = tk.Frame(main, bg=self.BG)
        features.pack()

        self.create_feature_card(
            features,
            "✦",
            "Beautiful Filters",
            "Enhance your images",
            0
        )

        self.create_feature_card(
            features,
            "◉",
            "Easy to Use",
            "Simple and intuitive",
            1
        )

        self.create_feature_card(
            features,
            "▣",
            "Save Locally",
            "No database required",
            2
        )

        # Footer
        tk.Label(
            main,
            text="Made with Python + Tkinter + Pillow",
            font=("Segoe UI", 10),
            fg=self.GRAY,
            bg=self.BG
        ).pack(side="bottom", pady=20)

    def create_feature_card(self, parent, icon, title, description, column):
        card = tk.Frame(
            parent,
            bg=self.CARD,
            width=220,
            height=120
        )
        card.grid(row=0, column=column, padx=12)
        card.pack_propagate(False)

        tk.Label(
            card,
            text=icon,
            font=("Segoe UI", 24, "bold"),
            fg="#A855F7",
            bg=self.CARD
        ).pack(pady=(12, 2))

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 11, "bold"),
            fg=self.WHITE,
            bg=self.CARD
        ).pack()

        tk.Label(
            card,
            text=description,
            font=("Segoe UI", 9),
            fg=self.GRAY,
            bg=self.CARD
        ).pack(pady=3)

   
    # FILTER INFORMATION
  

    def show_filter_info(self):
        messagebox.showinfo(
            "Available Filters",
            "PixelCraft includes:\n\n"
            "• Grayscale\n"
            "• Blur\n"
            "• Sharpen\n"
            "• Edge Detection\n"
            "• Brightness\n\n"
            "Open an image to start editing."
        )

    
    # EDITOR PAGE
   

    def show_editor(self):
        self.clear_screen()

        # ---------------- TOP BAR ----------------

        top = tk.Frame(self.root, bg="#10172A", height=70)
        top.pack(fill="x")
        top.pack_propagate(False)

        tk.Label(
            top,
            text="✦  PIXELCRAFT",
            font=("Segoe UI", 20, "bold"),
            fg=self.WHITE,
            bg="#10172A"
        ).pack(side="left", padx=25)

        tk.Button(
            top,
            text="Home",
            command=self.show_welcome_page,
            font=("Segoe UI", 10),
            fg=self.WHITE,
            bg=self.CARD2,
            activebackground="#27324D",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(side="right", padx=10)

        tk.Button(
            top,
            text="Save Image",
            command=self.save_image,
            font=("Segoe UI", 10, "bold"),
            fg=self.WHITE,
            bg=self.PURPLE,
            activebackground="#9333EA",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(side="right", padx=5)

        tk.Button(
            top,
            text="Open Image",
            command=self.open_image,
            font=("Segoe UI", 10, "bold"),
            fg=self.WHITE,
            bg=self.BLUE,
            activebackground="#3B82F6",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(side="right", padx=5)

        # ---------------- MAIN AREA ----------------

        content = tk.Frame(self.root, bg=self.BG)
        content.pack(fill="both", expand=True, padx=20, pady=20)

        # Image area
        image_area = tk.Frame(content, bg=self.CARD)
        image_area.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 15)
        )

        tk.Label(
            image_area,
            text="Image Preview",
            font=("Segoe UI", 15, "bold"),
            fg=self.WHITE,
            bg=self.CARD
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.image_label = tk.Label(
            image_area,
            text="Open an image to begin editing",
            font=("Segoe UI", 13),
            fg=self.GRAY,
            bg="#10172A"
        )
        self.image_label.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 20)
        )

        # Right panel
        side = tk.Frame(
            content,
            bg=self.CARD,
            width=270
        )
        side.pack(side="right", fill="y")
        side.pack_propagate(False)

        tk.Label(
            side,
            text="Filters",
            font=("Segoe UI", 18, "bold"),
            fg=self.WHITE,
            bg=self.CARD
        ).pack(anchor="w", padx=20, pady=(20, 15))

        self.create_filter_button(side, "Original", self.reset_image)
        self.create_filter_button(side, "Grayscale", self.apply_grayscale)
        self.create_filter_button(side, "Blur", self.apply_blur)
        self.create_filter_button(side, "Sharpen", self.apply_sharpen)
        self.create_filter_button(side, "Edge Detection", self.apply_edges)
        self.create_filter_button(side, "Brighten", self.apply_brightness)

        # Separator
        tk.Frame(
            side,
            bg="#2B344D",
            height=1
        ).pack(fill="x", padx=20, pady=20)

        tk.Label(
            side,
            text="Image Controls",
            font=("Segoe UI", 13, "bold"),
            fg=self.WHITE,
            bg=self.CARD
        ).pack(anchor="w", padx=20, pady=(0, 10))

        tk.Button(
            side,
            text="↻  Reset Image",
            command=self.reset_image,
            font=("Segoe UI", 10),
            fg=self.WHITE,
            bg=self.CARD2,
            activebackground="#27324D",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=9
        ).pack(fill="x", padx=20, pady=5)

        tk.Button(
            side,
            text="💾  Save Image",
            command=self.save_image,
            font=("Segoe UI", 10, "bold"),
            fg=self.WHITE,
            bg=self.GREEN,
            activebackground="#16A34A",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=9
        ).pack(fill="x", padx=20, pady=5)

        # Status
        self.status_label = tk.Label(
            side,
            text="No image selected",
            font=("Segoe UI", 9),
            fg=self.GRAY,
            bg=self.CARD,
            wraplength=220,
            justify="left"
        )
        self.status_label.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        # Bottom
        bottom = tk.Frame(
            self.root,
            bg="#10172A",
            height=35
        )
        bottom.pack(fill="x")
        bottom.pack_propagate(False)

        tk.Label(
            bottom,
            text="PixelCraft • Python Image Editor",
            font=("Segoe UI", 9),
            fg=self.GRAY,
            bg="#10172A"
        ).pack(side="left", padx=20)

        tk.Label(
            bottom,
            text="Local Storage • No Database",
            font=("Segoe UI", 9),
            fg=self.GRAY,
            bg="#10172A"
        ).pack(side="right", padx=20)

  
    # FILTER BUTTON

    def create_filter_button(self, parent, text, command):
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 10),
            anchor="w",
            fg=self.WHITE,
            bg=self.CARD2,
            activebackground=self.PURPLE,
            activeforeground=self.WHITE,
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=10
        )

        button.pack(
            fill="x",
            padx=20,
            pady=4
        )

    # OPEN IMAGE

    def open_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("JPEG Files", "*.jpg *.jpeg"),
                ("PNG Files", "*.png"),
                ("All Files", "*.*")
            ]
        )

        if file_path:
            try:
                self.original_image = Image.open(file_path).convert("RGB")
                self.edited_image = self.original_image.copy()

                self.current_filter = "Original"

                self.show_editor()
                self.display_image()

                self.status_label.config(
                    text="Image loaded successfully.\n\n"
                         "Choose a filter from the panel."
                )

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Could not open the image.\n\n{e}"
                )

    # ==========================================================
    # DISPLAY IMAGE
    # ==========================================================

    def display_image(self):
        if self.edited_image is None:
            return

        image = self.edited_image.copy()

        # Resize image to fit preview
        max_width = 700
        max_height = 500

        image.thumbnail(
            (max_width, max_height),
            Image.Resampling.LANCZOS
        )

        self.photo = ImageTk.PhotoImage(image)

        self.image_label.config(
            image=self.photo,
            text=""
        )

    # FILTERS

    def apply_grayscale(self):
        if self.edited_image is None:
            self.no_image_message()
            return

        self.edited_image = self.edited_image.convert("L").convert("RGB")
        self.current_filter = "Grayscale"
        self.display_image()
        self.update_status("Grayscale filter applied.")

    def apply_blur(self):
        if self.edited_image is None:
            self.no_image_message()
            return

        self.edited_image = self.edited_image.filter(
            ImageFilter.GaussianBlur(radius=4)
        )

        self.current_filter = "Blur"
        self.display_image()
        self.update_status("Blur filter applied.")

    def apply_sharpen(self):
        if self.edited_image is None:
            self.no_image_message()
            return

        self.edited_image = self.edited_image.filter(
            ImageFilter.SHARPEN
        )

        self.current_filter = "Sharpen"
        self.display_image()
        self.update_status("Sharpen filter applied.")

    def apply_edges(self):
        if self.edited_image is None:
            self.no_image_message()
            return

        self.edited_image = self.edited_image.filter(
            ImageFilter.FIND_EDGES
        )

        self.current_filter = "Edge Detection"
        self.display_image()
        self.update_status("Edge detection applied.")

    def apply_brightness(self):
        if self.edited_image is None:
            self.no_image_message()
            return

        enhancer = ImageEnhance.Brightness(
            self.edited_image
        )

        self.edited_image = enhancer.enhance(1.4)

        self.current_filter = "Brightness"
        self.display_image()
        self.update_status("Brightness increased.")

    # ==========================================================
    # RESET
    # ==========================================================

    def reset_image(self):
        if self.original_image is None:
            self.no_image_message()
            return

        self.edited_image = self.original_image.copy()
        self.current_filter = "Original"

        self.display_image()
        self.update_status("Image restored to original.")
      
    # SAVE IMAGE
    

    def save_image(self):
        if self.edited_image is None:
            self.no_image_message()
            return

        file_path = filedialog.asksaveasfilename(
            title="Save Edited Image",
            defaultextension=".png",
            filetypes=[
                ("PNG Image", "*.png"),
                ("JPEG Image", "*.jpg"),
                ("JPEG Image", "*.jpeg")
            ]
        )

        if file_path:
            try:
                self.edited_image.save(file_path)

                messagebox.showinfo(
                    "Success",
                    "Your edited image has been saved successfully!"
                )

                self.update_status(
                    "Image saved locally.\n\n"
                    "Filter: " + self.current_filter
                )

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Could not save the image.\n\n{e}"
                )

    # STATUS
    

    def update_status(self, message):
        self.status_label.config(
            text=message
        )

    def no_image_message(self):
        messagebox.showwarning(
            "No Image",
            "Please open an image first."
        )



# START APPLICATION


if __name__ == "__main__":
    root = tk.Tk()

    app = ImageEditorApp(root)

    root.mainloop()
