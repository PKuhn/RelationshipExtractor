from flask import Flask
app = Flack(__name__)

@app.route('/text', methods=['POST']):
def get_relations()
    jsn = request.get_json()
    text = jsn['text']
    return 'Hello world'

if __name__ == '__main__':
    app.run()
