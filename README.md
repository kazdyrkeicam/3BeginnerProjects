# 3 Simple AI Agents

---

## Agent Calculator Tool
This is a simple calculator tool that uses the OpenAI API to perform calculations. It can handle basic arithmetic operations.

### Usage
Inside the project directory, run the following command to start the calculator tool:
```bash
uv run main.py
```
Example conversation:
```

```

### Dependencies
```bash
uv add langgraph langchain langchain-openai python-dotenv
```

---

## Resume Critiquer
Web app that allows users to upload their resumes in PDF or TXT and analyzes the content using OpenAI.

### Usage
Inside the project directory, run the following command to start the resume critiquer:
```bash
uv run hello.py
```

Example output:


### Dependencies
```bash
uv add streamlit openai PyPDF2 python-dotenv
```


---

## Image Classifier
Web app that allows users to upload images and classifies them using OpenAI.

### Usage
Inside the project directory, run the following command to start the image classifier:
```bash
uv run hello.py
```

Example output:

### Dependencies
```bash
uv add streamlit opencv-python
```
In my case I had to install tensorflow using `pip`. Used `uv` to install it inside the venv.
```bash
uv pip install tensorflow
```
