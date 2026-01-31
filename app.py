from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Table App</title>
</head>
<body>
    <h2>Enter a Number</h2>

    <form method="POST">
        <input type="number" name="number" required>
        <button type="submit">Print Table</button>
    </form>

    {% if table %}
        <h3>Multiplication Table</h3>
        <ul>
            {% for line in table %}
                <li>{{ line }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def table():
    table = None
    if request.method == "POST":
        num = request.form.get("number")
        if num:
            n = int(num)
            table = [f"{n} x {i} = {n*i}" for i in range(1, 11)]
    return render_template_string(html_template, table=table)

