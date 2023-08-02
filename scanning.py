// Download button
$('#download-btn').on('click', function() {

  // Get selected slice
  var selectedSlice = series.slices.getIndex(series.slices.getSelected());

  // Get data
  var ipData = selectedSlice.dataItem.dataContext;
  var ips = ipData.ips;

  // Create text blob
  var textBlob = new Blob([ips.join('\n')], {type: 'text/plain'});

  // Generate download link
  var downloadLink = $('<a>').attr({
    download: 'ips_' + ipData.tag + '.txt',
    href: window.URL.createObjectURL(textBlob)
  });

  // Click download link
  $('body').append(downloadLink);
  downloadLink[0].click();
  downloadLink.remove();

});

// Get selected slice
function getSelectedSlice() {
  return series.slices.getIndex(series.slices.getSelected()); 
}
