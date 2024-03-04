from flask import Flask, render_template, request, redirect, url_for, Response

app = Flask(__name__, template_folder='templates')


def read_log_lines():
    try:
        with open("logs/log_file.log", 'r') as f:
            for line in f:
                yield line
    except FileNotFoundError:
        yield "Log file not found"
    except Exception as e:
        yield f"An error occurred while reading the log file: {str(e)}"


def split_log_line(line):
    try:
        return line.split(' ', 3) if len(line.split(' ', 3)) == 4 else ['', '', '[NO_FORMAT]', line]
    except Exception as e:
        return ['', '', '[NO_FORMAT]', f"Error while processing log line: {str(e)}"]


@app.route('/')
def display_logs():
    try:
        logs = [split_log_line(line) for line in read_log_lines()]
    except ValueError as ve:
        logs = [str(ve)]
    except Exception as e:
        logs = [f"An error occurred: {str(e)}"]

    selected_levels = request.args.getlist('log_levels') or ["INFO", "ERROR", "NO_FORMAT"]

    filtered_logs = [log for log in logs if any(level in log[2] for level in selected_levels)]
    beautified_logs = [log for log in filtered_logs]

    headers = ["Time", "Level", "Log"]
    log_levels = ["INFO", "DEBUG", "ERROR", "NO_FORMAT"]

    return render_template("logs.html", logs=logs, headers=headers, log_levels=log_levels,
                           selected_levels=selected_levels, beautified_logs=beautified_logs)


@app.route('/refresh')
def refresh_logs():
    selected_levels = request.args.getlist('log_levels') or ["INFO"]
    return redirect(url_for('display_logs', log_levels=selected_levels, _anchor='bottom'))


if __name__ == '__main__':
    app.run(debug=True)
