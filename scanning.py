<!DOCTYPE html>
<html>
<head>
  <script src="https://www.amcharts.com/lib/5/index.js"></script>
  <script src="https://www.amcharts.com/lib/5/percent.js"></script>
  <script src="https://www.amcharts.com/lib/5/themes/Animated.js"></script>

  <style>
    #chartdiv {
      width: 100%;
      height: 500px;
    }
    
    #ipModal {
      display: none; 
      position: fixed; 
      z-index: 1;  
      left: 0;
      top: 0;
      width: 100%; 
      height: 100%;
      overflow: auto;
      background-color: rgb(0,0,0);
      background-color: rgba(0,0,0,0.4); 
    }
    
    .ipModalContent {
      background-color: #fefefe;
      margin: 15% auto;
      padding: 20px;
      border: 1px solid #888;
      width: 80%; 
    }
  </style>
</head>

<body>

  <div id="chartdiv"></div>
  
  <div id="ipModal">
    <div class="ipModalContent">
      <span class="ipClose">&times;</span>
      <input type="text" id="ipSearch" placeholder="Search IP.."> 
      <div id="ipAddresses"></div>
    </div>
  </div>

  <script>
    // Pie chart data
    var data = [
      {
        tag: "Tag 1",
        value: 10,
        ips: ["192.168.0.1", "192.168.0.2", "192.168.0.3"] 
      },
      {
        tag: "Tag 2", 
        value: 20,
        ips: ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]
      },
      {
        tag: "Tag 3",
        value: 30,
        ips: ["192.168.2.1", "192.168.2.2", "192.168.2.3", "192.168.2.4", "192.168.2.5"]  
      }
    ];
    
    // Create pie chart
    var chart = am5percent.PieChart.new(document.getElementById("chartdiv"));
    
    // Create series
    var series = chart.series.push(new am5percent.PieSeries());
    series.data.setAll(data);
    
    // Handle click events
    series.slices.template.events.on("click", function(ev) {
    
      // Show modal and populate IPs
      var ipModal = document.getElementById("ipModal");
      ipModal.style.display = "block";
      
      var ipAddressesDiv = document.getElementById("ipAddresses");
      ipAddressesDiv.innerHTML = "";
      
      var ips = ev.target.dataItem.dataContext.ips;
      for(var i=0; i<ips.length; i++) {
        var ipText = document.createTextNode(ips[i]);
        var ipPara = document.createElement("p");
        ipPara.appendChild(ipText);
        ipAddressesDiv.appendChild(ipPara);
      }
      
      // Handle search
      var searchBox = document.getElementById("ipSearch");
      searchBox.oninput = function() {
        var searchTerm = searchBox.value.toLowerCase();
        var ipParas = ipAddressesDiv.querySelectorAll("p");
        for(var i=0; i<ipParas.length; i++) {
          var ipText = ipParas[i].innerText; 
          if(ipText.toLowerCase().indexOf(searchTerm) > -1) {
            ipParas[i].style.display = "";
          } else {
            ipParas[i].style.display = "none";
          }
        }
      }
      
    });
    
    // Close modal
    var modal = document.getElementById("ipModal");
    var closeBtn = document.getElementsByClassName("ipClose")[0];
    closeBtn.onclick = function() {
      modal.style.display = "none";
    }
    
  </script>

</body>
</html>
