# 🫠 AI Command Prompt

This project is a smart **natural-language command-line tool** built with:

* 🪙 LLaMA 3 via [Ollama](https://ollama.com/)
* ⚙️ Flask (Python Web Framework)
* 🩼 Safety Checks before executing commands
* 🌐 A minimal browser-based UI

---

## 🚀 Features

✅ Convert natural language into terminal commands
✅ Automatically checks if a command is safe to run
✅ Runs the command and returns the output
✅ Web-based UI using `index.html` + Flask API
✅ Powered by **LLaMA 3 (locally)** through Ollama

---

## 🛠️ Requirements

* Python 3.9 or newer
* [Ollama](https://ollama.com/) installed and running locally
* LLaMA 3 model pulled via:

```bash
ollama pull llama3
```

---

## 🧪 How to Run Locally (Step-by-Step)

### 1. 🧬 Clone the Repository

```bash
git clone https://github.com/moksh1111/ai-cmd
cd ai-cmd
```

---

### 2. 🐍 Set Up Virtual Environment

#### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. 📅 Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. 🪙 Pull and Run LLaMA 3 with Ollama

Make sure you have [Ollama](https://ollama.com/) installed:

```bash
ollama pull llama3
```

Then keep Ollama running in the background:

```bash
ollama run llama3
```

This will start a local server at:
📍 [http://localhost:11434](http://localhost:11434)

---

### 5. 🛠️ Create `.env` File

Create a file named `.env` in the root directory with the following content:

```ini
OLLAMA_API_URL=http://localhost:11434
LLAMA_MODEL=llama3
```

---

### 6. 🧠 Start the Flask App

```bash
flask run
```

It will start the server at:
📍 [http://127.0.0.1:5000](http://127.0.0.1:5000)

Open that in your browser to access the app.

---

### 7. 💬 Using the App

Enter a natural language command like:

```text
list all files in the current directory
```

The app will:

* Use LLaMA 3 to generate a shell command
* Check if it's safe (`rm -rf`, etc. are blocked)
* Run it
* Show the output on screen

