from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__, static_folder='static')

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Run the app when the script is executed
if __name__ == '__main__':
    app.run(debug=True)
