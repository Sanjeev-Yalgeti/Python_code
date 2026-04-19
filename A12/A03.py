from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<body>
    <h2>Enter Your Name</h2>
    <form action="/greet" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

@app.route('/')
def home():
    return "<h1>Welcome to the Home Page</h1><br><a href='/form'>Go to Form</a> | <a href='/about'>About</a>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>My name is Sanjeev </p><p> I Study At Vidyalankar Institutre of Technology </p><p> I am Intrested in Python and the libraries it has to offer </p><p>This is a simple Flask web application .</p><br><a href='/'>Back to Home</a>"

@app.route('/form')
def form():
    return render_template_string(HTML_FORM)

@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form.get('name')
    return f"<h1>Hello {user_name}</h1><br><a href='/'>Back to Home</a>"

if __name__ == '__main__':
    app.run(debug=True)