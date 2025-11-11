from flask import Flask, render_template_string


app = Flask(__name__)

HTML_TEMPLATE = """ 
<!DOCTYPE html>
<html>
<head>
<title> Flask App </title>
<style>

body {
    background: pink;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
    padding-top: 10px;

}

.card {
    background: yellow;
    border-radius: 12px;
    padding: 2em;
    width: 100%
    margin: auto;
    

}
</style>
</head>
<body>
<h1> This is  Flask App! </h1>
<div class="card">
    <p> This is for testing docker & github </p>
    <p> Thank you for seeing this demo! </p>

</div>
</body>
</html>

"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
