from flask import Flask, render_template, jsonify

todos = ['study vue', 'study flask', 'study toy problems']

#all of our static stuff that doesn't change is going to live inside of 
# dist/static as will our templates folder
app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist"
)

@app.route('/')
def serve_vue_app():
    """
    Server our vue app
     """
    return(render_template('index.html'))

@app.after_request
def add_header(req):
    """
    Clear Cache for hot-reloading
    """
    req.headers["Cache-Control"] = "no-cache"
    return req   

if __name__ =="__main__":
    app.run(debug=True)    