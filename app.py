from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded user for demonstration purposes
users = {'admin': 'admin123'}

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # Successful login
            return redirect(url_for('dashboard'))
        else:
            # Failed login
            return render_template('login.html', message='Invalid credentials')

    return render_template('login.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # For simplicity, let's assume all registrations are successful
        users[username] = password
        return redirect(url_for('login'))

    return render_template('registration.html')

from flask import render_template

@app.route('/profile')
def profile():
    # Fetch user details from your data source (e.g., database)
    user_details = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '(555) 123-4567',
        'dob': 'January 1, 1990',
        'address': '123 Main St, Cityville',
        # Add more details as needed
    }

    return render_template('profile.html', user=user_details)

# Example route for edit_profile
@app.route('/edit_profile')
def edit_profile():
    # Your view logic goes here
    return render_template('edit_profile.html')


# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_task')
def add_task():
    return render_template('add_task.html')

@app.route('/view_tasks')
def view_tasks():
    # Fetch tasks from your data source (e.g., database) and pass them to the template
    tasks = []  # Replace with your actual tasks data
    return render_template('view_tasks.html', tasks=tasks)

@app.route('/meeting_min')
def meeting_min():
    return render_template('meeting_min.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)
