from flask import Flask, request
import json

app = Flask(__name__)

def swap_case(string):
    return string.swapcase()

@app.route('/', methods=['POST'])
def swap_case_handler():
    try:
        data = request.get_json()
        string = data.get('string')

        if string is None or not isinstance(string, str):
            raise ValueError("You did not specify a parameter or it is not string")

        result = swap_case(string)
        response = {'swapped_string': result}
        return json.dumps(response), 200, {'Content-Type': 'application/json'}

    except Exception as e:
        error_response = {'error': str(e)}
        return json.dumps(error_response), 400, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(host='127.0.0.0', port=8000)