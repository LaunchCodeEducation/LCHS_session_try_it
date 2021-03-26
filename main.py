from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'Chemistry'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_item = request.form['new_item']
        current_list = session['my_list']
        if new_item not in current_list:
            current_list.append(new_item)
        session['my_list'] = current_list
    else:
        if 'my_list' not in session:
            session['my_list'] = []

    return render_template('index.html')

if __name__ == '__main__':
    app.run()