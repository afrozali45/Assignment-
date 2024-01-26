from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name is None:
        return "Error: 'n' parameter missing"

    file_path = f'/tmp/data/{file_name}.txt'

    try:
        with open(file_path, 'r') as file:
            if line_number is not None:
                lines = file.readlines()
                line_number = int(line_number) - 1
                if 0 <= line_number < len(lines):
                    return lines[line_number]
                else:
                    return f"Error: Line number {line_number + 1} not found in {file_name}.txt"
            else:
                return file.read()
    except FileNotFoundError:
        return f"Error: File {file_name}.txt not found"

if __name__ == '__main__':
    app.run(debug=True)
