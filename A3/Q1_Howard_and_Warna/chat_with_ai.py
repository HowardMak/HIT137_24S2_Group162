import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser
import google.generativeai as genai
import os

# locate current directory
CURRENT_DIR = os.path.dirname(__file__)
# define a file to store and get the api key
API_KEY_FILE = os.path.join(CURRENT_DIR, 'AI_api_key.txt')

class Application(tk.Frame):
    def __init__(self, master):
        """
        App initialisation
        """
        super().__init__(master)
        self.master = master
        self.model = None
        # store conversation history
        self.chat_history = {}
        # the key for chat history retrival
        self.current_chat_key = None
        master.title('Chat With AI')
        self.adjust_app_position()
        self.create_widgets()
        self.load_api_key()

    def adjust_app_position(self):
        """
        center the window on the screen
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
        create labels, text fields, and buttons
        """
        # a sidebar for chat history
        self.sidebar_label = tk.Label(root, text="Chat History:")
        self.sidebar_label.grid(row=0, column=3, padx=10, pady=5, sticky='w')
        self.sidebar = tk.Listbox(root, height=20, width=20)
        self.sidebar.grid(row=1, column=3, rowspan=4, padx=10, pady=5, sticky='n')
        self.sidebar.bind('<<ListboxSelect>>', self.load_selected_conversation)

        # API key
        self.api_key_label = tk.Label(root, text="Enter API Key:")
        self.api_key_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.api_key = tk.Text(root, height=1, width=35)
        self.api_key.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # connect button
        self.connect_to_api_button = tk.Button(root, text="Connect", command=self.connect_to_api)
        self.connect_to_api_button.grid(row=0, column=2, padx=10, pady=5, sticky='w')

        # get an API key if the user des not have one
        self.get_api_label = tk.Label(root, text="Haven't got a Gemini API Key?")
        self.get_api_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.get_api_button = tk.Button(root, text="Get my Gemini API Key", command=self.open_api_website)
        self.get_api_button.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # chat area
        self.chat_area_label = tk.Label(root, text="Chat Area:")
        self.chat_area_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=60, height=15)
        self.chat_area.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        # a textfiled where the user can input a mesage to caht with the API
        self.user_input_label = tk.Label(root, text="Your Message:")
        self.user_input_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.user_input = tk.Text(root, height=2, width=40)
        self.user_input.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky='w')

        # change to a get a new chat
        self.new_chat_button = tk.Button(root, text="New Chat", command=self.new_chat)
        self.new_chat_button.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        # send message to the API
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=5, column=2, padx=10, pady=10, sticky='w')

        # delete a selected chat history
        self.delete_button = tk.Button(root, text="Delete Selected Chat", command=self.delete_selected_chat)
        self.delete_button.grid(row=6, column=3, padx=10, pady=10, sticky='n')

    def load_api_key(self):
        """
        load saved api key
        """
        # Load the API key from a file if it exists
        if os.path.exists(API_KEY_FILE):
            with open(API_KEY_FILE, 'r') as file:
                api_key = file.read().strip()
                self.api_key.delete("1.0", tk.END)
                self.api_key.insert(tk.END, api_key)
                messagebox.showinfo("API Key Loaded", "API key loaded from file.")

    def connect_to_api(self):
        """
        connect to the API
        """
        try:
            api_key_value = self.api_key.get("1.0", "end-1c").strip()
            if not api_key_value:
                raise ValueError("API key is required!")
            genai.configure(api_key=api_key_value)
            self.model = genai.GenerativeModel("gemini-1.5-flash")

            with open(API_KEY_FILE, 'w') as file:
                file.write(api_key_value)

            messagebox.showinfo("Success", "Successfully connected to the API!")
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect to the API: {str(e)}")

    def open_api_website(self):
        """
        open the website for the user to get his/her own API key
        """
        webbrowser.open("https://makersuite.google.com/app/apikey")

    def send_message(self):
        """
        send the message to the API
        """
        # if the model is not initialised, throw an error
        if not self.model:
            messagebox.showerror("API Error", "You need to connect to the API first")
            return
        
        user_message = self.user_input.get("1.0", "end-1c").strip()
        # if the message is empty, it cannot be sent
        if not user_message:
            messagebox.showwarning("Input Error", "Please enter a message before sending.")
            return
        # update the chat area
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "You: " + user_message + "\n")
        
        # use try-catch in case of the network error
        try:
            response = self.respond_to_user(user_message)
            self.chat_area.insert(tk.END, "Bot: " + response + "\n\n")
        except Exception as e:
            messagebox.showerror("Response Error", f"Error generating response: {str(e)}")
        # make the chat area disabled once it's been updated
        self.chat_area.config(state=tk.DISABLED)
        self.user_input.delete("1.0", tk.END)

        # save message to current conversation
        if self.current_chat_key is None:
            self.current_chat_key = user_message
            self.chat_history[self.current_chat_key] = [f"You: {user_message}\nBot: {response}\n"]
            self.sidebar.insert(tk.END, self.current_chat_key)
        else:
            # append to the current conversation
            self.chat_history[self.current_chat_key].append(f"You: {user_message}\nBot: {response}\n")

    def respond_to_user(self, message: str) -> str:
        """
        get the response from the API
        """
        response = self.model.generate_content(message)
        return response.text

    def new_chat(self):
        """
        start a new chat
        """
        self.current_chat_key = None
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state=tk.DISABLED)

    def load_selected_conversation(self, event):
        """
        load the selected conversation from the sidebar
        """
        selection = self.sidebar.curselection()
        if selection:
            selected_message = self.sidebar.get(selection[0])
            conversation = self.chat_history.get(selected_message, [])
            
            # show the conversation in the chat area
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.delete(1.0, tk.END)
            for message in conversation:
                self.chat_area.insert(tk.END, message)
            self.chat_area.config(state=tk.DISABLED)

    def delete_selected_chat(self):
        """
        delete a selected chat
        """
        selection = self.sidebar.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a chat to delete.")
            return
        
        selected_message = self.sidebar.get(selection[0])
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the chat '{selected_message}'?")
        if confirm:
            del self.chat_history[selected_message]
            self.sidebar.delete(selection[0])
            if self.current_chat_key == selected_message:
                self.new_chat()
            messagebox.showinfo("Deletion Successful", "Selected chat has been deleted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
