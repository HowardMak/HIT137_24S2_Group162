# AI Chat Bot Application Documentation

## Introduction

This Python application is an AI chatbot that uses the `tkinter` library to create a graphical interface and connects to the Google Gemini Generative AI API for generating AI-driven responses. Below is an introduction to each function of the application and how users can interact with it:

## Functionality Overview

### 1. App Initialization (`__init__`)
When the application starts, it initializes the chat interface, API connection, and conversation history. The window is centered, and widgets like buttons, text fields, and labels are created for user interaction. Users can enter their Google Gemini API key to connect to the chatbot.

### 2. Adjusting Window Position (`adjust_app_position`)
The window is automatically centered on the screen when the app is launched. No user action is required for this; it's handled internally to provide a more user-friendly interface.

### 3. Creating Widgets (`create_widgets`)
This function creates all the components the user will interact with:

- **Sidebar (Chat History):** Displays previous conversations. Users can click on a chat to load its content.
- **API Key Input:** Users can enter their Google Gemini API key in the text field and click "Connect" to establish a connection with the AI API.
- **Chat Area:** A read-only area where the conversation with the AI appears.
- **Message Input:** Users can type messages to send to the chatbot.
- **Buttons:**
  - **"Connect":** Connects to the Google Gemini API using the entered API key.
  - **"Get my Gemini API Key":** Opens a web page for users to generate or retrieve an API key.
  - **"New Chat":** Starts a new conversation with the AI.
  - **"Send":** Sends the typed message to the AI for a response.
  - **"Delete Selected Chat":** Deletes a selected chat from the history.

### 4. Loading API Key (`load_api_key`)
If an API key has previously been saved, this function automatically loads it when the application starts. Users don’t need to enter the API key again if it's already stored.

### 5. Connecting to API (`connect_to_api`)
Users must enter a valid API key and click the "Connect" button to establish a connection with the AI service. If successful, the app will save the key and show a confirmation message.

### 6. Opening API Website (`open_api_website`)
If users do not have an API key, they can click the "Get my Gemini API Key" button, which will open the Google Makersuite website in their default browser to retrieve the key.

### 7. Sending a Message (`send_message`)
After entering a message in the input field, users can click "Send" to communicate with the AI. The message and response will be displayed in the chat area. If the user hasn’t connected to the API, they will be prompted to do so.

### 8. Receiving AI Responses (`respond_to_user`)
This function interacts with the AI model to generate a response based on the user’s input. The response is then displayed in the chat area.

### 9. Starting a New Chat (`new_chat`)
Users can click "New Chat" to clear the current conversation and start fresh. This resets the chat area and allows users to begin a new interaction with the AI.

### 10. Loading Selected Conversation (`load_selected_conversation`)
When users click on a previous chat in the sidebar, this function loads the conversation into the chat area for review. It helps users revisit past discussions.

### 11. Deleting a Selected Chat (`delete_selected_chat`)
By selecting a chat from the sidebar and clicking "Delete Selected Chat," users can permanently remove a chat from the history. A confirmation dialog will appear to avoid accidental deletion.

## Application Usage Flow

1. Enter or load your API key.
2. Connect to the API by clicking "Connect."
3. Type a message in the input field and click "Send."
4. Review AI responses in the chat area.
5. Start a new conversation with "New Chat" or revisit past ones from the chat history.
6. Optionally, delete unwanted chats from the sidebar.

This chatbot application provides a simple interface for AI conversations, with features to manage and interact with chat history easily.