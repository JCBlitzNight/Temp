<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AMCharts Heatmap & XYChart Example</title>
  <!-- Tailwind CSS -->
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  <!-- AMCharts Core and Charts libraries -->
  <script src="https://cdn.amcharts.com/lib/4/core.js"></script>
  <script src="https://cdn.amcharts.com/lib/4/charts.js"></script>
  <!-- AMCharts Themes -->
  <script src="https://cdn.amcharts.com/lib/4/themes/animated.js"></script>
</head>
<body class="bg-gray-100 min-h-screen flex justify-center items-center">
  <div class="container mx-auto p-4">
    <h1 class="text-4xl font-bold mb-4">Chart Examples</h1>
    <!-- Heatmap Chart -->
    <div class="bg-white rounded-lg shadow-md p-4 mb-4">
      <h2 class="text-2xl font-bold mb-4">Heatmap Chart</h2>
      <div id="heatmapChart" class="w-full h-64"></div>
    </div>

    <!-- XYChart -->
    <div class="bg-white rounded-lg shadow-md p-4">
      <h2 class="text-2xl font-bold mb-4">XYChart</h2>
      <div id="xyChart" class="w-full h-64"></div>
    </div>
  </div>
