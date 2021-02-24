$(() => {
  setTimeout(() => {
    $.get('/products/', function(products) {
      $(".product ul").append(products)
    });
  }, 2000)
})