from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'Chemistry'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        if 'my_list' not in session:
            session['my_list'] = []
        else:
            session['my_list'].append(123)
            session.modified = True
        print(session, session['my_list'], session.get('my_list'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()