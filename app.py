from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Updated Questions
QUESTIONS = [
    {"question": "What does print('Python'[::-1]) do?", "options": ["Reverses the string", "Prints 'Python'", "Throws an error", "None"], "correct": 0},
    {"question": "Which of these is not a Python framework?", "options": ["Django", "Flask", "React", "FastAPI"], "correct": 2},
    {"question": "What is PEP in Python?", "options": ["Python Enhanced Proposal", "Python Error Protocol", "Python Execution Plan", "None"], "correct": 0},
    {"question": "What is the output of print(type([]))?", "options": ["List", "Dictionary", "<class 'list'>", "<class 'dict'>"], "correct": 2},
    {"question": "Which module is used for working with dates in Python?", "options": ["datetime", "time", "calendar", "All of these"], "correct": 3},
    {"question": "What is the result of 'Python' + 'Quiz'?", "options": ["PythonQuiz", "Python Quiz", "Error", "None"], "correct": 0},
    {"question": "Which keyword is used to handle exceptions in Python?", "options": ["catch", "handle", "except", "error"], "correct": 2},
    {"question": "What does the open() function do?", "options": ["Open a file", "Close a file", "Create a file", "Delete a file"], "correct": 0},
    {"question": "How do you start a for loop in Python?", "options": ["for (i = 0; i < 10; i++)", "for i in range(10)", "foreach i in range(10)", "for (i in range)"], "correct": 1},
    {"question": "What is the output of print('Python'.upper())?", "options": ["PYTHON", "python", "Python", "Error"], "correct": 0},
    {"question": "Which module is used for working with JSON in Python?", "options": ["json", "os", "sys", "re"], "correct": 0},
    {"question": "What is the output of print(10 % 3)?", "options": ["1", "3", "0", "Error"], "correct": 0},
    {"question": "Which method is used to remove whitespace from the beginning or end of a string?", "options": ["strip()", "trim()", "remove()", "delete()"], "correct": 0},
    {"question": "What is the default value of the `end` parameter in the `print()` function?", "options": ["\\n", " ", "\\t", "None"], "correct": 0},
    {"question": "What does the `is` keyword do in Python?", "options": ["Compares memory locations", "Checks equality", "Assigns values", "None of the above"], "correct": 0},
    {"question": "How do you create a tuple in Python?", "options": ["[]", "{}", "()", "<>"], "correct": 2},
    {"question": "Which Python function is used to iterate over iterable objects?", "options": ["loop()", "for()", "iter()", "next()"], "correct": 2},
    {"question": "What is the output of print(bool(0))?", "options": ["True", "False", "Error", "None"], "correct": 1},
    {"question": "What does the `lambda` keyword in Python define?", "options": ["An anonymous function", "A named function", "A class", "A variable"], "correct": 0},
    {"question": "Which Python library is commonly used for machine learning?", "options": ["Pandas", "NumPy", "Scikit-learn", "Seaborn"], "correct": 2},
    {"question": "What is the output of print('5' * 3)?", "options": ["555", "15", "Error", "None"], "correct": 0},
    {"question": "What does the `break` statement do in a loop?", "options": ["Skips iteration", "Exits the loop", "Restarts the loop", "Continues iteration"], "correct": 1},
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get-questions')
def get_questions():
    import random
    random.shuffle(QUESTIONS)
    return jsonify(QUESTIONS[:10]) 

if __name__ == '__main__':
    app.run(debug=True)
