<!DOCTYPE html>
<html>
<head>
  <title>AmCharts 4 Pie Chart Example</title>
  <script src="path_to_amcharts_core.js"></script>
  <script src="path_to_amcharts_charts.js"></script>
  <script src="path_to_amcharts_animated.js"></script>
</head>
<body>
  <div id="chartdiv" style="width: 100%; height: 500px;"></div>
  <script>
    am4core.ready(function() {
      // Chart data will be dynamically added here using Python
      var chartData = {{data}};

      // Create a chart instance
      var chart = am4core.create("chartdiv", am4charts.PieChart);

      // Add data
      chart.data = chartData;

      // Create pie series
      var series = chart.series.push(new am4charts.PieSeries());
      series.dataFields.value = "value";
      series.dataFields.category = "category";

      // Add labels to the pie chart
      series.labels.template.disabled = true;
      series.ticks.template.disabled = true;
      series.slices.template.tooltipText = "{category}: {value.value}";

      // Enable animations
      chart.innerRadius = am4core.percent(40);
      series.hiddenState.properties.endAngle = -90;
    });
  </script>
</body>
</html>




import json

# Assuming the JSON data is in a file called "data.json"
with open('data.json', 'r') as file:
    json_data = json.load(file)

# Extract values for the keys "person" and "luck"
persons = [json_data[key]["person"] for key in json_data]
lucks = [json_data[key]["luck"] for key in json_data]

# Get Counters for unique values
unique_person_counter = Counter(persons)
unique_luck_counter = Counter(lucks)

# Get top 20 values for "person" and "luck"
top_20_person = unique_person_counter.most_common(20)
top_20_luck = unique_luck_counter.most_common(20)

# Generate data for the AmCharts pie chart
person_data = [{"category": person, "value": count} for person, count in top_20_person]
luck_data = [{"category": luck, "value": count} for luck, count in top_20_luck]

# Load the chart template and replace placeholders with the generated data
with open('chart_template.html', 'r') as template_file:
    chart_template = template_file.read()

chart_template = chart_template.replace("{{data}}", json.dumps(person_data))

# Save the chart data to a new HTML file
with open('generated_chart.html', 'w') as output_file:
    output_file.write(chart_template)
