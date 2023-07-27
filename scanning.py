<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.amcharts.com/lib/5/index.js"></script>
<script src="https://cdn.amcharts.com/lib/5/percent.js"></script>
<script src="https://cdn.amcharts.com/lib/5/themes/Animated.js"></script>

<!-- Tailwind CSS -->
<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet"> 

<style>
#chartdiv {
  width: 100%;
  height: 500px;
}
</style>

</head>

<body>

<div id="chartdiv"></div>

<!-- Modal -->
<div id="modal" class="fixed hidden inset-0 bg-gray-900 bg-opacity-50 overflow-y-auto">

  <div class="relative top-40 mx-auto p-5 border w-96 max-h-600px shadow-lg rounded-md bg-white">

    <h3 class="text-lg font-medium mb-2">IP Addresses</h3>

    <input id="search" type="text" class="border p-2 w-full mb-4" placeholder="Search IPs..."> 

    <div id="ips"></div>

    <div id="pagination"></div>

  </div>

</div>

<script>

// Chart code 

// IPs dataset
const ips = [
  /* IP array */ 
];

// Modal handlers
const modal = document.querySelector('#modal'); 
const ipsDiv = document.querySelector('#ips');

// Pagination
const ipsPerPage = 10;
let totalPages = Math.ceil(ips.length / ipsPerPage);
let currentPage = 1;

// Search
function searchIPs(searchTerm) {
  return ips.filter(ip => ip.includes(searchTerm));
}

// Display IPs
function renderIPs(ipPages) {
  let ipsHtml = "";
  ipPages.forEach(ip => {
    ipsHtml += `<p class="mb-2">${ip}</p>`;
  });
  
  ipsDiv.innerHTML = ipsHtml;
} 

// Pagination 
function handlePagination() {
  let startIndex = (currentPage - 1) * ipsPerPage;
  let endIndex = startIndex + ipsPerPage;
  let currentIPs = ips.slice(startIndex, endIndex);
  
  renderIPs(currentIPs);
  updatePagination();
}

function updatePagination() {
  let paginationHtml = "";
  
  for(let i=1; i<=totalPages; i++) {
     paginationHtml += `<a href="#" class="page-btn px-2 py-1" data-page="${i}">${i}</a>`; 
  }
  
  document.querySelector('#pagination').innerHTML = paginationHtml;
}

// Search
const searchBox = document.querySelector('#search');
searchBox.addEventListener("input", (e) => {
  const searchTerm = searchBox.value;
  const filteredIPs = searchIPs(searchTerm);
  
  currentPage = 1;
  
  renderIPs(filteredIPs);
  updatePagination();  
});

// Slice click handler
series.slices.template.events.on("click", (event) => {
  modal.classList.remove('hidden');
  
  // Show IPs
  const ipData = event.target.dataItem.dataContext; 
  renderIPs(ipData.ips);
  
  handlePagination();
});

</script>

</body>
</html>
