import matplotlib.pyplot as plt
import os

RECOMMENDED = 150  # Recommended daily liters per person

def calculate_total(data):
    """Sum all usage values"""
    return sum(data.values())

def check_recommendation(total):
    """Compare with recommended level"""
    if total > RECOMMENDED:
        return f"⚠️ You used {total - RECOMMENDED}L above the recommended {RECOMMENDED}L/day. Try reducing usage."
    else:
        return f"✅ Great job! You are within the recommended {RECOMMENDED}L/day."

def get_tips(data):
    """Provide water-saving tips based on usage"""
    tips = []
    if data["shower"] > 50:
        tips.append("🚿 Take shorter showers to save up to 20L/day.")
    if data["laundry"] > 40:
        tips.append("👕 Run full loads of laundry instead of small ones.")
    if data["dishes"] > 30:
        tips.append("🍽️ Use a basin or dishwasher instead of running tap water.")
    if data["cooking"] > 20:
        tips.append("🍲 Use only the water you need for cooking.")
    if not tips:
        tips.append("🌱 Excellent habits! Keep saving water.")
    return tips

def create_chart(data):
    """Generate and save a bar chart of usage"""
    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(6,4))
    plt.bar(labels, values, color="#0077b6")
    plt.title("Daily Water Usage by Activity")
    plt.ylabel("Liters")
    plt.tight_layout()

    # Save chart to static folder
    chart_path = os.path.join("static", "chart.png")
    plt.savefig(chart_path)
    plt.close()

    return chart_path
