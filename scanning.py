// Set colors based on continent information
bubbleSeries.events.on("beforevalidated", function (event) {
  bubbleSeries.dataItems.each(function (dataItem) {
    var continent = dataItem.get("continent");
    if (!colorsByContinent[continent]) {
      colorsByContinent[continent] = colors.getIndex(); // Assign new color to the continent
    }
    dataItem.get("circleTemplate").set("fill", colorsByContinent[continent]);
  });
});
