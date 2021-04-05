from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'K>~EEAnH_x,Z{q.43;NmyQiNz1^Yr7'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['button'] == 'add':
            new_item = request.form['new_item'].title()
            current_list = session['groceries']
            if new_item not in current_list:
                current_list.append(new_item)
        else:
            del_items = request.form.getlist('del_items')
            current_list = session['groceries']
            for item in del_items:
                if item in current_list:
                    current_list.remove(item)
        session['groceries'] = current_list
        session['groceries'].sort()
    else:
        if 'groceries' not in session:
            session['groceries'] = []

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
