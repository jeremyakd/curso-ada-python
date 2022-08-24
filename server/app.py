from flask import *

app = Flask(__name__)

# Decorador
@app.route('/')
def home():
    template_data = {
        'titulo' : 'Esto es Python en Ada',
    }
    html = """
    <h1>Esta es mi primera web</h1>
    <h2>La hicimos con el capo de Jere</h2>
    """
    return html
    #render_template('home.html', **template_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)