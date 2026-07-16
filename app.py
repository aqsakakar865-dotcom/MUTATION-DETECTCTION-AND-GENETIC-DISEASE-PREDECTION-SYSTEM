from flask import Flask

app=Flask(_name_)

@app.route("/")
def home():
    return "Mutation Detection System"

if _name=="main_":
    app.run()
