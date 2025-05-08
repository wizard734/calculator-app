from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<title>Calculator</title>
<h2>Simple Calculator</h2>
<form method="post">
  <input type="number" name="num1" required>
  <select name="operation">
    <option value="add">+</option>
    <option value="sub">-</option>
    <option value="mul">*</option>
    <option value="div">/</option>
  </select>
  <input type="number" name="num2" required>
  <input type="submit" value="Calculate">
</form>

{% if result is not none %}
  <h3>Result: {{ result }}</h3>
{% endif %}
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