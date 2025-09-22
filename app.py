from flask import Flask, render_template, request
from utils.calculator import calculate_total, check_recommendation, get_tips, create_chart

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    # Collect data from form
    data = {
        "shower": int(request.form.get("shower", 0)),
        "laundry": int(request.form.get("laundry", 0)),
        "cooking": int(request.form.get("cooking", 0)),
        "dishes": int(request.form.get("dishes", 0)),
        "other": int(request.form.get("other", 0)),
    }

    # Run calculations
    total = calculate_total(data)
    recommendation_msg = check_recommendation(total)
    tips = get_tips(data)

    # Generate chart
    chart_path = create_chart(data)

    return render_template(
        "result.html",
        total=total,
        recommendation=recommendation_msg,
        tips=tips,
        chart_path=chart_path,
    )

if __name__ == "__main__":
    app.run(debug=True)
