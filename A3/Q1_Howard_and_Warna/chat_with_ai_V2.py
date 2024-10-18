import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser
import os
import google.generativeai as genai

# Locate the current directory
CURRENT_DIR = os.path.dirname(__file__)
# Define a file to store and get the API key
API_KEY_FILE = os.path.join(CURRENT_DIR, 'AI_api_key.txt')


class Application(tk.Frame):
    """
    This is the application class that handles the interaction functions with AI
    """
    def __init__(self, master):
        """
        App initialization
        """
        super().__init__(master)
        self.master = master
        self.model = None
        # Store conversation history
        self.chat_history = {}
        # The key for chat history retrieval
        self.current_chat_key = None
        master.title('Chat With AI')
        self.adjust_app_position()
        self.create_widgets()
        self.load_api_key()

    def adjust_app_position(self):
        """
        Center the window on the screen
        """
        window_width = 900
        window_height = 500
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.master.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')

    def create_widgets(self):
        """
        Create labels, text fields, buttons, and ribbons
        """
        # Define color scheme similar to Facebook
        header_color = "#1877F2"
        button_bg = "#1877F2"
        button_fg = "#FFFFFF"
        chat_area_bg = "#F0F2F5"
        sidebar_bg = "#F7F7F7"
        footer_color = "#E4E6EB"

        # --- Top Ribbon (Facebook-style header) ---
        self.top_ribbon = tk.Frame(self.master, bg=header_color, height=50)
        self.top_ribbon.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        self.top_ribbon_label = tk.Label(self.top_ribbon, text="Chat with AI", fg="#FFFFFF", bg=header_color, font=("Helvetica Neue", 18, "bold"))
        self.top_ribbon_label.grid(row=0, column=0, padx=20, pady=10)

        # --- Sidebar (Chat History) ---
        self.sidebar_label = tk.Label(self.master, text="Chat History:", font=("Helvetica Neue", 12, "bold"), fg="#4B4B4B", bg=sidebar_bg)
        self.sidebar_label.grid(row=1, column=3, padx=10, pady=5, sticky='w')
        
        self.sidebar = tk.Listbox(self.master, height=20, width=20, font=("Helvetica Neue", 10), bd=0, bg=sidebar_bg)
        self.sidebar.grid(row=2, column=3, rowspan=4, padx=10, pady=5, sticky='n')

        self.sidebar.bind('<<ListboxSelect>>', self.load_selected_conversation)

        # --- API Key Input ---
        self.api_key_label = tk.Label(self.master, text="Enter API Key:", font=("Helvetica Neue", 12, "bold"), fg="#4B4B4B", bg=sidebar_bg)
        self.api_key_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        
        self.api_key = tk.Text(self.master, height=1, width=35, font=("Helvetica Neue", 10))
        self.api_key.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # --- Connect Button ---
        self.connect_to_api_button = tk.Button(self.master, text="Connect", bg=button_bg, fg=button_fg, font=("Helvetica Neue", 12, "bold"),
                                                relief="flat", activebackground="#145D9E", activeforeground=button_fg,
                                                command=self.connect_to_api, width=15, height=2, borderwidth=0, highlightthickness=0)
        self.connect_to_api_button.grid(row=1, column=2, padx=10, pady=5, sticky='w')

        # --- Get API Button ---
        self.get_api_label = tk.Label(self.master, text="Haven't got a Gemini API Key?", font=("Helvetica Neue", 12, "bold"),
                                      fg="#4B4B4B", bg=sidebar_bg)
        self.get_api_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        
        self.get_api_button = tk.Button(self.master, text="Get my Gemini API Key", font=("Helvetica Neue", 10), relief="flat",
                                        bg=button_bg, fg=button_fg, activebackground="#145D9E", activeforeground=button_fg,
                                        command=self.open_api_website)
        self.get_api_button.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        # --- Chat Area Label ---
        self.chat_area_label = tk.Label(self.master, text="Chat Area:", font=("Helvetica Neue", 12, "bold"), fg="#4B4B4B", bg=sidebar_bg)
        self.chat_area_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        
        self.chat_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, state=tk.DISABLED, width=60, height=15,
                                                  bg=chat_area_bg, font=("Helvetica Neue", 12))
        self.chat_area.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

        # --- User Input ---
        self.user_input_label = tk.Label(self.master, text="Your Message:", font=("Helvetica Neue", 12, "bold"), fg="#4B4B4B", bg=sidebar_bg)
        self.user_input_label.grid(row=5, column=0, padx=10, pady=5, sticky='w')

        self.user_input = tk.Text(self.master, height=2, width=40, font=("Helvetica Neue", 12))
        self.user_input.grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky='w')

        # --- New Chat Button ---
        self.new_chat_button = tk.Button(self.master, text="New Chat", bg=button_bg, fg=button_fg, font=("Helvetica Neue", 12, "bold"),
                                         relief="flat", activebackground="#145D9E", activeforeground=button_fg, command=self.new_chat,
                                         width=15, height=2, borderwidth=0, highlightthickness=0)
        self.new_chat_button.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        # --- Send Button ---
        self.send_button = tk.Button(self.master, text="Send", bg=button_bg, fg=button_fg, font=("Helvetica Neue", 12, "bold"),
                                     relief="flat", activebackground="#145D9E", activeforeground=button_fg, command=self.send_message,
                                     width=15, height=2, borderwidth=0, highlightthickness=0)
        self.send_button.grid(row=6, column=2, padx=10, pady=10, sticky='w')

        # --- Bottom Ribbon (Footer-like area) ---
        self.bottom_ribbon = tk.Frame(self.master, bg=footer_color, height=40)
        self.bottom_ribbon.grid(row=7, column=0, columnspan=4, sticky="ew")
        
        self.bottom_ribbon_label = tk.Label(self.bottom_ribbon, text="Powered by Gemini API", fg="#4B4B4B", bg=footer_color,
                                            font=("Helvetica Neue", 10, "italic"))
        self.bottom_ribbon_label.grid(row=0, column=0, padx=20, pady=10)

    def load_api_key(self):
        """
        Load saved API key
        """
        if os.path.exists(API_KEY_FILE):
            with open(API_KEY_FILE, mode='r', encoding='utf-8') as file:
                api_key = file.read().strip()
                self.api_key.delete("1.0", tk.END)
                self.api_key.insert(tk.END, api_key)
                messagebox.showinfo("API Key Loaded", "API key loaded from file.")

    def connect_to_api(self):
        """
        Connect to the API
        """
        try:
            api_key_value = self.api_key.get("1.0", "end-1c").strip()
            if not api_key_value:
                raise ValueError("API key is required!")
            genai.configure(api_key=api_key_value)
            self.model = genai.GenerativeModel("gemini-1.5-flash")

            with open(API_KEY_FILE, mode='w', encoding='utf-8') as file:
                file.write(api_key_value)

            messagebox.showinfo("API Key Saved", "API key saved successfully.")
        except ValueError as e:
            messagebox.showerror("API Key Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def open_api_website(self):
        """
        Open the Gemini API website
        """
        webbrowser.open("https://developers.generativeai.com")

    def new_chat(self):
        """
        Reset the chat window and history
        """
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.config(state=tk.DISABLED)
        self.user_input.delete("1.0", tk.END)
        self.chat_history = {}
        self.sidebar.delete(0, tk.END)

    def send_message(self):
        """
        Send the user message and get AI response
        """
        user_message = self.user_input.get("1.0", "end-1c").strip()
        if user_message:
            response = self.model.generate_text(user_message)
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.insert(tk.END, f"You: {user_message}\nAI: {response.text}\n\n")
            self.chat_area.config(state=tk.DISABLED)
            self.user_input.delete("1.0", tk.END)
            self.save_conversation(user_message, response.text)
        else:
            messagebox.showwarning("Input Error", "Please enter a message.")

    def save_conversation(self, user_message, ai_message):
        """
        Save the conversation in chat history
        """
        if self.current_chat_key is None:
            self.current_chat_key = f"Chat {len(self.chat_history) + 1}"

        self.chat_history[self.current_chat_key] = {
            'user': user_message,
            'ai': ai_message
        }

        self.sidebar.insert(tk.END, self.current_chat_key)

    def load_selected_conversation(self, event):
        """
        Load the selected conversation
        """
        selected_chat = self.sidebar.get(self.sidebar.curselection())
        conversation = self.chat_history.get(selected_chat)
        if conversation:
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.delete("1.0", tk.END)
            self.chat_area.insert(tk.END, f"You: {conversation['user']}\nAI: {conversation['ai']}\n\n")
            self.chat_area.config(state=tk.DISABLED)
            self.current_chat_key = selected_chat

    def delete_selected_chat(self):
        """
        Delete selected chat from history
        """
        selected_chat = self.sidebar.get(self.sidebar.curselection())
        if selected_chat:
            del self.chat_history[selected_chat]
            self.sidebar.delete(self.sidebar.curselection())
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.delete("1.0", tk.END)
            self.chat_area.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
