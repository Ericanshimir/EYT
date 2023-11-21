from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitForm', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process the form data (e.g., save it to a database, send an email, etc.)
    print(f"Received form data: Name - {name}, Email - {email}, Message - {message}")
    # Return a JSON response or a success message
    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

