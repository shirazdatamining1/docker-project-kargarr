from flask import Flask, request, render_template
import cmath

app = Flask(__name__)

# صفحه اصلی
@app.route('/')
def home():
    return render_template('index.html')

# حل معادله درجه دوم
@app.route('/solve', methods=['POST'])
def solve():
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        delta = b**2 - 4*a*c
        root1 = (-b + cmath.sqrt(delta)) / (2 * a)
        root2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return render_template('result.html', root1=root1, root2=root2)
    except ValueError:
        return "Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
