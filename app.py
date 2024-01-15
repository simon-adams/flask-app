#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/set-team" method="POST">
         <label for="team">Football team</label>
         <input name="team" id="team" />
         <input type="submit" value="Submit!" />
     </form>
     '''

@app.route("/set-team", methods=["POST"])
def set_team():
    input_text = request.form.get("team", "")
    return "Team set to: " + input_text
