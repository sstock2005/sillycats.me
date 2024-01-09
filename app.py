from flask import Flask, send_file, request, session
import os, random, configparser

config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))


app = Flask(__name__)
app.secret_key = config.get("DEFAULT", "secret")
host = config.get("DEFAULT", "host")
cat_noises = ["meow!", "meowwww", "grrr!", "miaow", "mrruh", "prrrup", "mrow", "mrrrrrr"]
@app.route('/', methods=["GET"])
def home():
    noise = random.choice(cat_noises)
    html_content = f"""
    <html>
    <head>
        <title>{noise} - sillycats.me</title>
        <meta property="og:title" content="{noise} - sillycats.me" />
        <meta property="og:type" content="image.png" />
        <meta property="og:url" content="https://sillycats.me" />
        <meta property="og:image" content="https://sillycats.me/api/cat" />
    </head>
    <body style="background-color: #131516; color: #FFFFFF">
        <center><br><h3>{noise}</h3><br><img width="300px" src="{host}/api/cat" alt="silly cat"><br><br><a href="https://github.com/sstock2005/sillycats.me" target="_blank" style="font-weight: bold;text-decoration: none;color: #FFFFFF;">Source Code</a>  |  <a href="https://github.com/sstock2005" target="_blank" style="font-weight: bold;text-decoration: none;color: #FFFFFF;">My GitHub</a><br><br></center>
    </body>
    </html>
    """

    return html_content, 200, {'Content-Type': 'text/html'}

@app.route('/api/cat')
def cat():
    if random.randint(0, 10000) == 6969:
        picture = "rare.png"
        return send_file(picture, "image/png", False), 418
    else:
        if 'last_cat' not in session:
            session['last_cat'] = None
        picture = random.choice(os.listdir("./pictures"))
        while picture == session['last_cat']:
            picture = random.choice(os.listdir("./pictures"))
        session['last_cat'] = picture
        return send_file("pictures/{}".format(picture), "image/png", False)

@app.route('/api/noise')
def noise():
    return random.choice(cat_noises), 200, {'Content-Type': 'text/plain'}
app.run('0.0.0.0', 7777, False)