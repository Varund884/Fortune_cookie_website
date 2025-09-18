# Fortune_cookie_website
Do you want to know your fortune? Look no further! Simply press the button on the website and discover what your fortune holds. 🥠 This is a fun and simple web app where, with a single click, you receive your AI-generated fortune.
<img width="1917" height="997" alt="screenshotcookie" src="https://github.com/user-attachments/assets/2207b855-c243-4b02-ad02-e2cf33cfc726" />


## ⚙️ Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Varund884/Fortune_cookie_website.git
cd Fortune_cookie_website
```

### 2. Create a virtual environment in your IDE
inside your main project folder.
```bash
python -m venv venv
```

### 3. Activate the virtual environment
For Windows
```bash
venv\Scripts\activate
```
For Mac/Linux
```bash
source venv/bin/activate
```

### 4. Install the Dependencies
Navigate back to the backend folder and please install the required Python packages.
```bash
cd backend
pip install -r requirements.txt
```

### 5. Set Up Environment Variables
Create a .env file inside the backend/ folder and add your Cohere API key. (Keep this file secret as mentioned in .gitignore.)
```bash
COHERE_API_KEY=your_api_key_here
```

## Congratulations !!
Let's now run the program.

### Start the backend/app.py
Run the Python program and type the code:
```bash
cd backend
python app.py
```

### Open the frontend/index.html 
Now simply run the program.

## 📦 Dependencies

### Backend (Python)
- Flask
- Flask-CORS
- Cohere
- python-dotenv

### Frontend
- HTML
- CSS
- JavaScript
