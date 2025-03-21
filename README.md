AI Assistant - Chat and Image Generation App
This is a Python-based application built with Tkinter, OpenAI's GPT-4 and DALL-E APIs, offering AI-driven features for chatting and generating images. The app allows users to interact with a chatbot, save chat history, and create images based on text prompts.

Features
Chat with AI: Send messages to the AI, receive responses, and manage conversation history.
Save Chat History: Save the conversation as a .docx file for future reference.
Create Images with AI: Generate images from a text prompt using OpenAI's DALL-E model.
Adjustable Image Settings: Choose the image size (square, vertical, horizontal) and quality (standard, high quality).
User-Friendly Interface: Built using Tkinter with a modern dark theme (via sv_ttk) for an intuitive experience.
Installation
To run the AI Assistant locally, follow the steps below:

1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/AI-Assistant.git
2. Navigate to the project directory
bash
Copy
Edit
cd AI-Assistant
3. Create a virtual environment
bash
Copy
Edit
python -m venv .venv
4. Activate the virtual environment
Windows:
bash
Copy
Edit
.venv\Scripts\activate
Mac/Linux:
bash
Copy
Edit
source .venv/bin/activate
5. Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
6. Add your OpenAI API Key
Replace the api_key variable in the code with your OpenAI API key. To obtain one, sign up at OpenAI.
You can store your API key securely using environment variables instead of hardcoding it into the script.
7. Run the application
bash
Copy
Edit
python main.py
Usage
Once the application starts, you can:

Chat Tab: Type your message and hit "Enter" to chat with the AI. Use the "Save Message" button to save the conversation history to a .docx file. You can also start a new chat by clicking "New Chat".
Image Tab: Enter a description of the image you want to generate, choose the size and quality, and hit the "Create Image!" button. The image will be displayed in the app, and you can save it to your local machine.
Screenshots
Chat Tab

Image Generation Tab

Technologies Used
Tkinter: GUI framework for building the desktop application.
OpenAI API: For generating AI responses (GPT-4) and images (DALL-E).
sv_ttk: Custom theme for Tkinter to apply a modern dark theme.
Pillow: For image handling and resizing.
requests: For downloading the generated images.
Contributions
Feel free to fork this repository and create a pull request if you wish to contribute. You can help improve the app by:

Fixing bugs or adding new features.
Improving the user interface.
Enhancing performance or adding error handling.
License
