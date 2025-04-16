import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog

class TextReverser:
    """Backend class that handles text reversing functionality."""
    
    @staticmethod
    def reverse_characters(text):
        """Reverse the characters in the text."""
        if not text:
            return ""
        return text[::-1]
    
    @staticmethod
    def reverse_words(text):
        """Reverse the order of words while maintaining original spelling."""
        if not text:
            return ""
        words = text.split()
        return " ".join(words[::-1])
    
    @staticmethod
    def save_to_file(text, filename):
        """Save text to a file."""
        try:
            with open(filename, 'w') as file:
                file.write(text)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False


class TextReverserGUI:
    """Frontend GUI for the Text Reverser application."""
    
    def __init__(self, root):
        self.root = root
        self.reverser = TextReverser()
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        self.root.title("Text Reverser")
        self.root.geometry("600x500")
        self.root.configure(padx=20, pady=20)
        
        # Input section
        tk.Label(self.root, text="Enter Text:", font=("Arial", 12)).pack(anchor="w")
        self.input_text = scrolledtext.ScrolledText(self.root, height=6, width=60, font=("Arial", 11))
        self.input_text.pack(pady=(0, 10), fill=tk.BOTH, expand=True)
        
        # Option selection
        self.option_frame = tk.Frame(self.root)
        self.option_frame.pack(fill=tk.X, pady=10)
        
        self.option_var = tk.StringVar(value="char")
        tk.Radiobutton(
            self.option_frame, 
            text="Reverse Characters", 
            variable=self.option_var, 
            value="char",
            font=("Arial", 11)
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        tk.Radiobutton(
            self.option_frame, 
            text="Reverse Words", 
            variable=self.option_var, 
            value="word",
            font=("Arial", 11)
        ).pack(side=tk.LEFT)
        
        # Action buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(
            self.button_frame, 
            text="Reverse Text", 
            command=self.reverse_text,
            font=("Arial", 11),
            bg="#4CAF50",
            fg="white",
            padx=10,
            pady=5
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            self.button_frame, 
            text="Save to File", 
            command=self.save_text,
            font=("Arial", 11),
            bg="#2196F3",
            fg="white",
            padx=10,
            pady=5
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            self.button_frame, 
            text="Clear", 
            command=self.clear_fields,
            font=("Arial", 11),
            bg="#f44336",
            fg="white",
            padx=10,
            pady=5
        ).pack(side=tk.LEFT)
        
        # Output section
        tk.Label(self.root, text="Reversed Text:", font=("Arial", 12)).pack(anchor="w", pady=(10, 0))
        self.output_text = scrolledtext.ScrolledText(self.root, height=6, width=60, font=("Arial", 11))
        self.output_text.pack(pady=(0, 10), fill=tk.BOTH, expand=True)
        
    def reverse_text(self):
        """Handle the text reversal operation."""
        text = self.input_text.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Empty Input", "Please enter some text to reverse.")
            return
        
        if self.option_var.get() == "char":
            result = self.reverser.reverse_characters(text)
        else:
            result = self.reverser.reverse_words(text)
            
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", result)
        
    def save_text(self):
        """Save the reversed text to a file."""
        text = self.output_text.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Empty Output", "There is no reversed text to save.")
            return
            
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if filename:
                if self.reverser.save_to_file(text, filename):
                    messagebox.showinfo("Success", f"Text successfully saved to {filename}")
                else:
                    messagebox.showerror("Error", "Failed to save the file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def clear_fields(self):
        """Clear both input and output fields."""
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)


def run_command_line():
    """Run the text reverser in command line mode."""
    reverser = TextReverser()
    
    while True:
        print("\n=== Text Reverser ===")
        print("1. Reverse characters")
        print("2. Reverse words")
        print("3. Save to file")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "1":
            text = input("Enter text to reverse characters: ")
            result = reverser.reverse_characters(text)
            print(f"\nReversed: {result}")
        
        elif choice == "2":
            text = input("Enter text to reverse word order: ")
            result = reverser.reverse_words(text)
            print(f"\nReversed: {result}")
        
        elif choice == "3":
            text = input("Enter text to save: ")
            filename = input("Enter filename: ")
            if reverser.save_to_file(text, filename):
                print(f"Text saved to {filename}")
            else:
                print("Failed to save file")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    # Determine whether to run GUI or command line version
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_command_line()
    else:
        # Default to GUI mode
        root = tk.Tk()
        app = TextReverserGUI(root)
        root.mainloop()