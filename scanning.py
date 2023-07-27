<!-- Tailwind CSS -->
<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">

<!-- Modal Markup -->

<div id="modal" class="fixed hidden inset-0 bg-gray-900 bg-opacity-50 overflow-y-auto h-full w-full">

  <div class="relative top-40 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">

    <h3 class="text-lg font-medium mb-2">IP Addresses</h3>
    
    <input id="search" type="text" class="border p-2 w-full mb-4" placeholder="Search IPs...">

    <div id="ips">
      <!-- IP list here -->
    </div>

    <!-- Pagination -->
    <div id="pagination">
      <a href="#" class="px-2 py-1 border">Prev</a>
      <a href="#" class="px-2 py-1 border">1</a> 
      <a href="#" class="px-2 py-1 border">2</a>
      <a href="#" class="px-2 py-1 border">3</a>
      <a href="#" class="px-2 py-1 border">Next</a>
    </div>

  </div>

</div>

<!-- Script to handle pagination -->

<script>
// Pagination logic  
const ipsPerPage = 10;
let currentPage = 1;

function handlePagination() {
  // Get current IP page
  const startIndex = (currentPage - 1) * ipsPerPage;
  const endIndex = startIndex + ipsPerPage;
  const ipsToDisplay = ips.slice(startIndex, endIndex);
  
  // Render page
  renderIPs(ipsToDisplay); 
  
  // Update pagination
  updatePagination();
}

function updatePagination() {
  // Update page links
  let paginationHtml = "";
  // Loop to generate page links
  paginationHtml += `<a href="#" data-page="1" class="px-2 py-1 border">Prev</a>`;

  document.querySelector("#pagination").innerHTML = paginationHtml; 
}

</script>
