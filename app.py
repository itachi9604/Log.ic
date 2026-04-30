import re
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, template_folder='templates')

LOG_FILE = "logs/log_file.log"
LOG_LEVELS = ["INFO", "DEBUG", "ERROR"]

LOG_PATTERN = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<level>INFO|ERROR|DEBUG)\s+(?P<message>.+)$"
)


def parse_logs(filter_levels=None):
    entries = []
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                line = line.rstrip("\n")
                match = LOG_PATTERN.match(line)
                if match:
                    entry = {
                        "date": match.group("date"),
                        "time": match.group("time"),
                        "level": match.group("level"),
                        "message": match.group("message"),
                    }
                else:
                    entry = {
                        "date": "",
                        "time": "",
                        "level": "NO_FORMAT",
                        "message": line,
                    }
                if filter_levels and entry["level"] not in filter_levels:
                    continue
                entries.append(entry)
    except FileNotFoundError:
        return None, f"{LOG_FILE} not found."
    return entries, None


def get_counts():
    all_entries, _ = parse_logs()
    counts = {lvl: 0 for lvl in LOG_LEVELS}
    if all_entries:
        for e in all_entries:
            if e["level"] in counts:
                counts[e["level"]] += 1
    return counts


@app.route('/')
def display_logs():
    selected_levels = request.args.getlist('log_levels') or LOG_LEVELS
    logs, error = parse_logs(selected_levels)
    counts = get_counts()
    return render_template(
        "logs.html",
        logs=logs or [],
        error=error,
        log_levels=LOG_LEVELS,
        selected_levels=selected_levels,
        counts=counts,
    )


@app.route('/logs')
def logs_api():
    selected_levels = request.args.getlist('log_levels') or LOG_LEVELS
    logs, error = parse_logs(selected_levels)
    if error:
        return jsonify({"error": error}), 500
    counts = get_counts()
    return jsonify({"logs": logs, "counts": counts})


@app.route('/refresh')
def refresh_logs():
    selected_levels = request.args.getlist('log_levels') or LOG_LEVELS
    return redirect(url_for('display_logs', log_levels=selected_levels))


if __name__ == '__main__':
    app.run(debug=True)
