<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.jsdelivr.net/npm/fuse.js"></script>
  
  <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">

</head>

<body>

<div class="container mx-auto px-4 max-w-4xl py-8">

  <h1 class="text-4xl mb-6">IP Address Table</h1>

  <div class="bg-white shadow rounded-lg overflow-x-auto">

    <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
      <h3 class="text-lg leading-6 font-medium text-gray-900">
        IP Address Information  
      </h3>
      <input class="search-input py-2 px-3 border border-gray-300 rounded-md" placeholder="Search IP...">
    </div>

    <table class="min-w-full divide-y divide-gray-200">
      <thead>
        <tr>
          <th class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase">IP</th>
          <th class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase">Location</th>
          <th class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase">ISP</th>
          <th class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase">Tags</th>
        </tr>
      </thead>

      <tbody id="table-rows" class="bg-white divide-y divide-gray-200">
        <!-- Rows inserted here -->  
      </tbody>
    
    </table>

    <div id="pagination" class="px-4 py-3 text-xs font-medium"></div>

  </div>

</div>

<script>

const ipData = [
  {
    ip: "192.168.1.1",  
    location: "New York, NY",
    isp: "Spectrum",
    tags: ["home", "wireless"]
  },
  // more rows  
];

const resultsPerPage = 10;
const totalPages = Math.ceil(ipData.length / resultsPerPage); 

// Display paginated rows  
function displayPage(pageNum) {
  const startIndex = (pageNum - 1) * resultsPerPage;
  const endIndex = startIndex + resultsPerPage;
  const resultsToDisplay = ipData.slice(startIndex, endIndex);

  let rowsHtml = '';
  resultsToDisplay.forEach(item => {
    rowsHtml += `
      <tr>
        <td class="px-6 py-4 whitespace-nowrap border-b">
          ${item.ip} 
        </td>
        // etc...  
      </tr>
    `;
  });

  document.querySelector('#table-rows').innerHTML = rowsHtml;
}

// Generate pagination
function generatePagination(currentPage) {
  let paginationHtml = '';
  for (let i = 1; i <= totalPages; i++) {
    const activeClass = i === currentPage ? 'bg-blue-500 text-white' : '';
    paginationHtml += `<a class="page-link ${activeClass} cursor-pointer" data-page="${i}">${i}</a>`;
  }  

  document.querySelector('#pagination').innerHTML = paginationHtml; 
}

// Initially display first page  
displayPage(1);
generatePagination(1);

// Handle search  
const searchInput = document.querySelector('.search-input');

searchInput.addEventListener('input', (e) => {

  const searchTerm = e.target.value;

  // Fuse.js filter
  const fuse = new Fuse(ipData, options); 
  const results = fuse.search(searchTerm);

  // Display results
  displayPage(1); 
  generatePagination(1);

  if (results.length > 0) {
    displayPage(1, results); 
  } else {
    document.querySelector('#table-rows').innerHTML = `
      <tr>
        <td class="px-6 py-4 border-b" colspan="4">No results found</td>  
      </tr>
    `;
  }
  
});

</script>

</body>
</html>
