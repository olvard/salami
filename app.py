from flask import Flask, render_template
from scrape import scrape_data, get_date

app = Flask(__name__)


@app.route("/")
def index():
    scraped_data = scrape_data()
    today_date = get_date()
    return render_template("index.html", data=scraped_data, date=today_date)


if __name__ == "__main__":
    app.run(debug=True)
