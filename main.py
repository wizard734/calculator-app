from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Calculator</title>
  <style>
    body {
      background: #f4f7f9;
      font-family: Arial, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    .calculator {
      background: #fff;
      padding: 30px 40px;
      border-radius: 10px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
      text-align: center;
    }
    h2 {
      margin-bottom: 20px;
      color: #333;
    }
    input[type="number"],
    select {
      width: 80px;
      padding: 10px;
      margin: 5px;
      border-radius: 5px;
      border: 1px solid #ccc;
      font-size: 16px;
    }
    select {
      width: 60px;
    }
    input[type="submit"] {
      background-color: #4CAF50;
      color: white;
      padding: 10px 25px;
      margin-top: 15px;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.3s;
    }
    input[type="submit"]:hover {
      background-color: #45a049;
    }
    .result {
      margin-top: 20px;
      font-size: 20px;
      color: #0074D9;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <h2>Simple Calculator</h2>
    <form method="post">
      <input type="number" name="num1" required>
      <select name="operation">
        <option value="add">+</option>
        <option value="sub">−</option>
        <option value="mul">×</option>
        <option value="div">÷</option>
      </select>
      <input type="number" name="num2" required>
      <br>
      <input type="submit" value="Calculate">
    </form>

    {% if result is not none %}
      <div class="result">Result: {{ result }}</div>
    {% endif %}
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        op = request.form['operation']
        if op == 'add':
            result = num1 + num2
        elif op == 'sub':
            result = num1 - num2
        elif op == 'mul':
            result = num1 * num2
        elif op == 'div':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    return render_template_string(TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
