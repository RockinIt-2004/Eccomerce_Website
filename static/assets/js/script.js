document.addEventListener('DOMContentLoaded', function() {
  'use strict';

  // modal variables
  const modal = document.querySelector('[data-modal]');
  const modalCloseBtn = document.querySelector('[data-modal-close]');
  const modalCloseOverlay = document.querySelector('[data-modal-overlay]');

  // modal function
  const modalCloseFunc = function () { modal.classList.add('closed') }

  // modal eventListener
  if (modalCloseOverlay) {
    modalCloseOverlay.addEventListener('click', modalCloseFunc);
  }

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', modalCloseFunc);
  }

  // notification toast variables
  const notificationToast = document.querySelector('[data-toast]');
  const toastCloseBtn = document.querySelector('[data-toast-close]');

  // notification toast eventListener
  if (toastCloseBtn) {
    toastCloseBtn.addEventListener('click', function () {
      notificationToast.classList.add('closed');
    });
  }

  // mobile menu variables
  const mobileMenuOpenBtn = document.querySelectorAll('[data-mobile-menu-open-btn]');
  const mobileMenu = document.querySelectorAll('[data-mobile-menu]');
  const mobileMenuCloseBtn = document.querySelectorAll('[data-mobile-menu-close-btn]');
  const overlay = document.querySelector('[data-overlay]');

  for (let i = 0; i < mobileMenuOpenBtn.length; i++) {

    // mobile menu function
    const mobileMenuCloseFunc = function () {
      mobileMenu[i].classList.remove('active');
      overlay.classList.remove('active');
    }

    mobileMenuOpenBtn[i].addEventListener('click', function () {
      mobileMenu[i].classList.add('active');
      overlay.classList.add('active');
    });

    if (mobileMenuCloseBtn[i]) {
      mobileMenuCloseBtn[i].addEventListener('click', mobileMenuCloseFunc);
    }
    if (overlay) {
      overlay.addEventListener('click', mobileMenuCloseFunc);
    }
  }

  // accordion variables
  const accordionBtn = document.querySelectorAll('[data-accordion-btn]');
  const accordion = document.querySelectorAll('[data-accordion]');

  for (let i = 0; i < accordionBtn.length; i++) {

    accordionBtn[i].addEventListener('click', function () {

      const clickedBtn = this.nextElementSibling.classList.contains('active');

      for (let i = 0; i < accordion.length; i++) {

        if (clickedBtn) break;

        if (accordion[i].classList.contains('active')) {

          accordion[i].classList.remove('active');
          accordionBtn[i].classList.remove('active');

        }

      }

      this.nextElementSibling.classList.toggle('active');
      this.classList.toggle('active');

    });

  }

  // add to cart functionality
/*   $(".add-to-cart-btn").on("click", function() {
    let quantity = $("#product-quantity").val();
    let product_title = $(".product-title").val();
    let product_id = $(".product-id").val();
    let product_price = $("#current-product-price").text();
    let this_val = $(this);

    console.log("Quantity:", quantity);
    console.log("Title:", product_title);
    console.log("Price:", product_price);
    console.log("ID:", product_id);
    console.log("Current Element :", this_val);

    $.ajax({
      url: '/add-to-cart',
      data: {
        'id': product_id,
        'qty': quantity,
        'title': product_title,
        'price': product_price,
      },
      dataType: 'json',
      beforeSend: function(){
        console.log("Addding Product to Cart..");
      },
      success: function(response){
        this_val.html("Item added to cart")
        console.log("Added Product to Cart!...");
        $(".cart-items-count").text(response.totalcartitems)
      }
    })
  }); */
  $(".add-to-cart-btn").on("click", function() {

    let this_val = $(this);
    let index = this_val.attr("data-index")
    let quantity = $(".product-quantity-" + index).val();
    let product_title = $(".product-title-" + index).val();
    let product_id = $(".product-id-" + index).val();
    let product_price = $(".current-product-price-" + index).text();
    let product_image = $(".product-image-" + index).val();
    let product_pid = $(".product-pid-" + index).val();

    console.log("Quantity:", quantity);
    console.log("Title:", product_title);
    console.log("Price:", product_price);
    console.log("ID:", product_id);
    console.log("PID:", product_pid);
    console.log("Image:", product_image)
    console.log("IDEX:", index);
    console.log("Current Element :", this_val);

     $.ajax({
      url: '/add-to-cart',
      data: {
        'id': product_id,
        'pid': product_id,
        'image': product_image,
        'qty': quantity,
        'title': product_title,
        'price': product_price,
      },
      dataType: 'json',
      beforeSend: function(){
        console.log("Addding Product to Cart..");
      },
      success: function(response){
        this_val.html("✔")
        console.log("Added Product to Cart!...");
        $(".cart-items-count").text(response.totalcartitems)
      }
    }) 
  });


   $(document).on("click",'.delete-product', function(){
    let product_id = $(this).attr("data-product")
    let this_val = $(this)
  
    console.log("Product ID:", product_id);

    $.ajax({
      url: "/delete-from-cart",
      data:{
        "id": product_id
      },
      dataType: "json",
      beforeSend:function(){
        this_val.hide 
      },
      success: function(response){
        this_val.show()
        $(".cart-items-count").text(response.totalcartitems)
        $("#cart-list").html(response.data)
      }

    })
  
  });
});
