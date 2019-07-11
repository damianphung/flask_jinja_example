from flask import Flask, render_template

# Doubts between jinjda templates and react
# https://stackoverflow.com/questions/32705233/how-to-use-jinja2-server-side-rendering-alongside-react-without-violating-inline

# Client vs Server side rendering
# https://medium.com/@gagan_goku/react-and-server-side-rendering-ssr-444d8c48abfc
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # flask.render_template(template_name_or_list,**content)
    list_example = ['hello', 'world']
    return render_template('index.html', list_example=list_example)

if __name__ == '__main__':
 app.run(debug=True)