"""
AI Chatbot Application using Tkinter and Google Generative AI API.

This program provides a GUI-based chatbot interface to interact with a
Generative AI model.

Users can connect to the API, send messages, and manage conversation history.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser
import os
import google.generativeai as genai

# Locate current directory
CURRENT_DIR = os.path.dirname(__file__)
# Define a file to store and retrieve the API key
API_KEY_FILE = os.path.join(CURRENT_DIR, 'AI_api_key.txt')


class Application(tk.Frame):
    """
    Main application class that handles the AI interaction and GUI.
    """
    # pylint: disable=too-many-instance-attributes
    # Four is reasonable in this case.
    def __init__(self, master):
        """
        Initialize the application and its components.
        """
        super().__init__(master)
        self.master = master
        self.model = None  # AI model instance
        self.chat_history = {}  # Store conversation history
        self.current_chat_key = None  # Key to access current chat history
        master.title('Chat With AI')

        # Set window position and size
        self.adjust_app_position()
        # Create all widgets (labels, buttons, text fields)
        self.create_widgets()
        # Load API key from file, if available
        self.load_api_key()

    def adjust_app_position(self):
        """
        Center the application window on the screen.
        """
        window_width, window_height = 900, 500
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(
            f'{window_width}x{window_height}+{position_x}+{position_y}'
        )

    def create_widgets(self):
        """
        Create and organize all widgets (buttons, text areas, labels) in the
        application.
        """
        # Sidebar for chat history
        self.sidebar_label = tk.Label(self.master, text="Chat History:")
        self.sidebar_label.grid(row=0, column=3, padx=10, pady=5, sticky='w')
        self.sidebar = tk.Listbox(self.master, height=20, width=20)
        self.sidebar.grid(
            row=1, column=3, rowspan=4, padx=10, pady=5, sticky='n'
        )
        self.sidebar.bind('<<ListboxSelect>>', self.load_selected_conversation)

        # API key input
        self.api_key_label = tk.Label(self.master, text="Enter API Key:")
        self.api_key_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.api_key = tk.Text(self.master, height=1, width=35)
        self.api_key.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Button to connect to the API
        self.connect_to_api_button = tk.Button(
            self.master, text="Connect", command=self.connect_to_api
        )
        self.connect_to_api_button.grid(
            row=0, column=2, padx=10, pady=5, sticky='w'
        )

        # API Key info section
        self.get_api_label = tk.Label(
            self.master, text="Haven't got a Gemini API Key?"
        )
        self.get_api_label.grid(
            row=1, column=0, padx=10, pady=5, sticky='w'
        )
        self.get_api_button = tk.Button(
            self.master,
            text="Get my Gemini API Key",
            command=self.open_api_website
        )
        self.get_api_button.grid(
            row=1, column=1, padx=10, pady=5, sticky='w'
        )

        # Chat area
        self.chat_area_label = tk.Label(self.master, text="Chat Area:")
        self.chat_area_label.grid(
            row=2, column=0, padx=10, pady=5, sticky='w'
        )
        self.chat_area = scrolledtext.ScrolledText(
            self.master, wrap=tk.WORD, state=tk.DISABLED, width=60, height=15
        )
        self.chat_area.grid(
            row=3, column=0, columnspan=3, padx=10, pady=5
        )

        # Input field for user message
        self.user_input_label = tk.Label(self.master, text="Your Message:")
        self.user_input_label.grid(
            row=4, column=0, padx=10, pady=5, sticky='w'
        )
        self.user_input = tk.Text(self.master, height=2, width=40)
        self.user_input.grid(
            row=4, column=1, columnspan=2, padx=10, pady=5, sticky='w'
        )

        # Button to start a new chat
        self.new_chat_button = tk.Button(
            self.master, text="New Chat", command=self.new_chat
        )
        self.new_chat_button.grid(
            row=5, column=1, padx=10, pady=10, sticky='w'
        )

        # Button to send message to the API
        self.send_button = tk.Button(
            self.master, text="Send", command=self.send_message
        )
        self.send_button.grid(
            row=5, column=2, padx=10, pady=10, sticky='w'
        )

        # Button to delete a selected chat history
        self.delete_button = tk.Button(
            self.master,
            text="Delete Selected Chat",
            command=self.delete_selected_chat
        )
        self.delete_button.grid(
            row=6, column=3, padx=10, pady=10, sticky='n'
        )

    def load_api_key(self):
        """
        Load the saved API key from file, if it exists.
        """
        if os.path.exists(API_KEY_FILE):
            with open(API_KEY_FILE, mode='r', encoding='utf-8') as file:
                api_key = file.read().strip()
                self.api_key.delete("1.0", tk.END)
                self.api_key.insert(tk.END, api_key)
                messagebox.showinfo(
                    "API Key Loaded",
                    "API key loaded from file."
                )

    def connect_to_api(self):
        """
        Connect to the AI API using the provided API key.
        """
        try:
            api_key_value = self.api_key.get("1.0", "end-1c").strip()
            if not api_key_value:
                raise ValueError("API key is required!")
            genai.configure(api_key=api_key_value)
            self.model = genai.GenerativeModel("gemini-1.5-flash")

            # Save API key to file
            with open(API_KEY_FILE, mode='w', encoding='utf-8') as file:
                file.write(api_key_value)

            messagebox.showinfo(
                "Success",
                "Successfully connected to the API!"
            )
        except (ValueError, OSError) as error:
            messagebox.showerror("Error", f"Failed to connect: {str(error)}")

    def open_api_website(self):
        """
        Open the website to obtain a new API key.
        """
        webbrowser.open("https://makersuite.google.com/app/apikey")

    def send_message(self):
        """
        Send a message to the AI model and display the response.
        """
        if not self.model:
            messagebox.showerror(
                "API Error",
                "You need to connect to the API first."
            )
            return

        user_message = self.user_input.get("1.0", "end-1c").strip()
        if not user_message:
            messagebox.showwarning(
                "Input Error",
                "Please enter a message before sending."
            )
            return

        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "You: " + user_message + "\n")

        try:
            response = self.respond_to_user(user_message)
            self.chat_area.insert(tk.END, "Bot: " + response + "\n\n")
        except ValueError:
            messagebox.showerror(
                "Input Error",
                f"Invalid input: {str(ValueError)}"
            )
        except ConnectionError:
            messagebox.showerror(
                "Connection Error",
                f"Network issue: {str(ConnectionError)}"
            )
        except RuntimeError:
            messagebox.showerror(
                "Runtime Error",
                f"Runtime issue: {str(RuntimeError)}"
            )

        self.chat_area.config(state=tk.DISABLED)
        self.user_input.delete("1.0", tk.END)

        # Save the conversation history
        self.save_conversation(user_message, response)

    def save_conversation(self, user_message, response):
        """
        Save the user's message and the AI's response to the chat history.
        """
        if self.current_chat_key is None:
            self.current_chat_key = user_message
            self.chat_history[
                self.current_chat_key
            ] = [f"You: {user_message}\nBot: {response}\n"]
            self.sidebar.insert(tk.END, self.current_chat_key)
        else:
            self.chat_history[
                self.current_chat_key
            ].append(f"You: {user_message}\nBot: {response}\n")

    def respond_to_user(self, message: str) -> str:
        """
        Get the response from the AI model for the user's message.
        """
        response = self.model.generate_content(message)
        return response.text

    def new_chat(self):
        """
        Clear the chat area and start a new conversation.
        """
        self.current_chat_key = None
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state=tk.DISABLED)

    def load_selected_conversation(self):
        """
        Load and display a selected conversation from the sidebar.
        """
        selection = self.sidebar.curselection()
        if selection:
            selected_key = self.sidebar.get(selection[0])
            self.current_chat_key = selected_key
            conversation = self.chat_history.get(selected_key, [])

            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.delete(1.0, tk.END)
            self.chat_area.insert(tk.END, ''.join(conversation))
            self.chat_area.config(state=tk.DISABLED)

    def delete_selected_chat(self):
        """
        Delete the currently selected conversation from the history.
        """
        selection = self.sidebar.curselection()
        if selection:
            selected_key = self.sidebar.get(selection[0])
            del self.chat_history[selected_key]
            self.sidebar.delete(selection[0])

            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.delete(1.0, tk.END)
            self.chat_area.config(state=tk.DISABLED)

            messagebox.showinfo(
                "Deleted",
                f"Chat '{selected_key}' has been deleted."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
