<!DOCTYPE html>
<html>
<head>
  <title>IP Address Table</title>
  
  <!-- Tailwind CSS -->
  <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet"> 
  
  <!-- jQuery -->
  <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
</head>

<body class="p-4">

  <h1 class="text-2xl font-bold mb-4">IP Address Search</h1>
  
  <div>
    <input id="ipInput" type="text" placeholder="Enter valid public IP" class="border p-2">
    <button id="searchBtn" class="bg-blue-500 text-white px-4 py-2">Search</button>
  </div>
  
  <table id="ipTable" class="hidden mt-8 table-auto border-collapse">
    <thead>
      <tr class="bg-gray-200">
        <th class="border p-2">IP Address</th>
        <th class="border p-2">Location</th>
        <th class="border p-2">ISP</th>
        <th class="border p-2">Tags</th>
      </tr>
    </thead>
    <tbody>
    </tbody>
  </table>

  <script>
    // Validate IP on input
    $('#ipInput').on('input', function() {
      var ip = $(this).val(); 
      if (!/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(ip)) {
        $(this).addClass('border-red-500');
      } else {
        $(this).removeClass('border-red-500');
      }
    });

    // Search click handler
    $('#searchBtn').click(function() {
      var ip = $('#ipInput').val();
      if (/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(ip)) {
        $.getJSON('db.json', function(data) {
          var info = data[ip];
          
          // Clear table
          $('#ipTable tbody').empty(); 
          
          // Add row to table
          var row = '<tr>';
          row += '<td class="border p-2">' + ip + '</td>';
          row += '<td class="border p-2">' + info.location + '</td>';
          row += '<td class="border p-2">' + info.isp + '</td>';
          row += '<td class="border p-2">' + info.tags.join(', ') + '</td>';
          row += '</tr>';
          $('#ipTable tbody').append(row);
          
          // Show table
          $('#ipTable').removeClass('hidden');
        });
      }
    });
  </script>

</body>
</html>
