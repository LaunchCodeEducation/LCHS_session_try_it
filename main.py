from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'K>~EEAnH_x,Z{q.43;NmyQiNz1^Yr7'

@app.route('/', methods=['GET', 'POST'])
def buttons():
    if request.method == 'POST':
        new_num = request.form['new_number']
        if new_num != 'delete':
            session['output'] += new_num
        else:
            session['output'] = session['output'][:-1]
    else:
        if 'output' not in session:
            session['output'] = ''

    return render_template('buttons.html')

if __name__ == '__main__':
    app.run()
