from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/data')
def get_data():
    filename = request.args.get('n')
    line_number = request.args.get('m')

    if filename is None:
        return "Error: 'n' parameter is required."

    file_path = f'/tmp/data/{filename}.txt'

    if line_number is not None:
        try:
            line_number = int(line_number)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if 1 <= line_number <= len(lines):
                    return lines[line_number - 1]
                else:
                    return "Error: Invalid line number."
        except ValueError:
            return "Error: 'm' parameter must be an integer."

    else:
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Error: File not found."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
