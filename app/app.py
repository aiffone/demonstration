from flask import Flask

# Create a new Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route("/")
def hello_world():
    return "Hello, Kayode!"

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Expose the app on port 8080
