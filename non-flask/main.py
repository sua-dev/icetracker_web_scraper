from web_scraper_data import *
import sys

NODE_ID = int(ROVER_22)
split_data(NODE_ID)

# Data points provided by web_scraper_data
labels = lat
data = voltage
timestp = timestamp
values = temperature

# Generate JavaScript code for the Chart.js chart
chart_script = f"""
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <canvas id="voltChart" width="900" height="400"></canvas>
    <canvas id="longlat" width="900" height="400"></canvas>
    <canvas id="temperature" width="900" height="400"></canvas>

    <script>
        var ctx = document.getElementById('voltChart').getContext('2d');
        var voltChart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: {timestp},
                datasets: [{{
                    label: 'Rover {NODE_ID} - Voltage over Time',
                    data: {data},
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2,
                    fill: false
                }}]
            }},
            options: {{
                scales: {{
                    y: {{
                        beginAtZero: false
                    }},
                    responsive: false
                }}
            }}
        }});
        var ctx2 = document.getElementById('temperature').getContext('2d');
        var temperature = new Chart(ctx2, {{
            type: 'line',
            data: {{
                labels: {timestp},
                datasets: [{{
                    label: 'Rover {NODE_ID} - Temperature over Time',
                    data: {values},
                    borderColor: 'rgb(50, 58, 168)',
                    borderWidth: 2,
                    fill: false
                }}]
            }},
            options: {{
                scales: {{
                    y: {{
                        beginAtZero: false
                    }},
                    responsive: false
                }}
            }}
        }});

        var ctx3 = document.getElementById('longlat').getContext('2d');
        var longlat = new Chart(ctx3, {{
            type: 'line',
            data: {{
                labels: {timestp},
                datasets: [{{
                    label: 'Rover {NODE_ID} - Latitude against Longitude',
                    data: {values},
                    borderColor: 'rgb(168, 72, 50)',
                    borderWidth: 2,
                    fill: false
                }}]
            }},
            options: {{
                scales: {{
                    y: {{
                        beginAtZero: false
                    }},
                    responsive: false
                }}
            }}
        }});
    </script>
"""

# Create the HTML file with the embedded Chart.js code
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chart.js Example</title>
</head>
<body>
    {chart_script}
</body>
</html>
"""

# Save the HTML content to a file
with open('chart.html', 'w') as f:
    f.write(html_content)
