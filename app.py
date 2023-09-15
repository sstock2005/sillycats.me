from flask import Flask, send_file, request, session
import os, random, configparser

config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))


app = Flask(__name__)
app.secret_key = config.get("DEFAULT", "secret")
host = config.get("DEFAULT", "host")
@app.route('/')
def home():
    cat_noises = ["meow!", "meowwww", "grrr!", "miaow", "mrruh", "prrrup", "mrow", "mrrrrrr"]
    html_content = f"""
    <html>
    <head>
        <title>{random.choice(cat_noises)} - sillycats.me</title>
        <meta property="og:title" content="{random.choice(cat_noises)} - sillycats.me" />
        <meta property="og:type" content="image.png" />
        <meta property="og:url" content="https://sillycats.me />
        <meta property="og:image" content="https://sillycats.me/cat" />
    </head>
    <body style="background-color: #131516">
        <center><img src="{host}/cat" alt="silly cat"><br><a href="https://github.com/sstock2005" target="_blank" style="font-weight: bold;text-decoration: none;color: #FFFFFF;">My GitHub</a></center>
    </body>
    </html>
    """

    return html_content, 200, {'Content-Type': 'text/html'}

@app.route('/cat')
def cat():
    if 'last_cat' not in session:
        session['last_cat'] = None
    picture = random.choice(os.listdir("./pictures"))
    while picture == session['last_cat']:
        picture = random.choice(os.listdir("./pictures"))
    session['last_cat'] = picture
    return send_file("pictures/{}".format(picture), "image/png", False)

app.run('0.0.0.0', 7777, False)