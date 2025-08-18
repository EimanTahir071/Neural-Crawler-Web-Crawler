import subprocess
import json
import os

def run_crawl():
    output_file = "output.json"

    # Delete old output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    try:
        result = subprocess.run(
            ['scrapy', 'crawl', 'mycrawler', '-o', output_file],
            capture_output=True,
            text=True,
            timeout=60,  # 💡 wait max 20 seconds
            cwd=os.path.dirname(__file__)  # ensure it's in your project folder
        )
    except subprocess.TimeoutExpired:
        return "Spider timed out."

    if result.returncode != 0:
        return f"Error running spider:\n{result.stderr}"

    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return "Could not decode JSON. Spider ran, but no output."
    else:
        return "No output file generated."
