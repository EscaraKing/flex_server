from flask import Flask, render_template, url_for, request
import sys
application = Flask(__name__)


@application.route("/")
def main():
    return render_template("main.html")


@application.route("/input")
def input():
    return render_template("input.html")


@application.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open("userdata.txt", "r", encoding="utf-8") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                words = line.split()
                name = words[0].replace(',', '')
                if name == username:
                    return render_template('private.html', value=words)
                else:
                    print("name is "+name)
        return render_template('loginerror.html')
    else:
        return render_template('login.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
