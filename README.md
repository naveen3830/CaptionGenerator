# Caption Crafter Bot 🤖
🌐 **Website**: [Caption Crafter Bot](https://captioncrafter.streamlit.app/)

Caption Crafter Bot is a Streamlit-based application that generates creative social media captions based on three descriptive words provided by the user. It uses the LangChain library and the ChatGroq language model to create engaging captions for your social media posts.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Description

This project allows users to input three descriptive words and generates a creative social media caption using those words. It's perfect for anyone looking to enhance their social media presence with catchy and relevant captions.

## Features

- Easy-to-use Streamlit interface
- Generates captions based on user-provided words
- Uses the powerful LangChain and ChatGroq language models
- Responsive design suitable for various devices

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/caption-crafter-bot.git
    cd caption-crafter-bot
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project root directory and add your GROQ API key:
      ```env
      GROQ_API_KEY=your_groq_api_key_here
      ```

    - Alternatively, set the GROQ API key in Streamlit secrets:
      ```json
      {
        "groq_api_key": "your_groq_api_key_here"
      }
      ```

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Open the web browser to the provided URL (usually `http://localhost:8501`) to interact with the app.**

3. **Enter three descriptive words and click "Generate Caption" to get a creative social media caption.**

## Files

- `.gitignore`: Specifies files and directories to be ignored by Git.
- `app.py`: Main application file containing the Streamlit app code.
- `requirements.txt`: List of Python dependencies required for the project.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the awesome app framework.
- [LangChain](https://github.com/hwchase17/langchain) for the language model toolkit.
- [ChatGroq](https://www.groq.com/) for the language model.

---

Made with ❤️ by [@Naveen](https://github.com/naveen3830)
