from flask import Flask, render_template, url_for, request, redirect

app =Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        tel = request.form['telefone']
        link = 'https://api.whatsapp.com/send?phone=55' + tel
        return redirect(link)
    else: 
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)