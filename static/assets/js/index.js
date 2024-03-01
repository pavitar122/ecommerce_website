document.addEventListener('DOMContentLoaded', function () {
    const addToCartBtns = document.querySelectorAll('.add-to-cart');
    const plusBtns = document.querySelectorAll('.plus');
    const minusBtns = document.querySelectorAll('.minus');
    // const clearCartBtn = document.getElementById('clear-cart');
    const totalQuantitySpan = document.getElementById('total-quantity');
    const cartValue = document.getElementById('cart');

    // Check if there is a cart in the local storage
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Update the total quantity based on the cart
    updateTotalQuantity();

    // Add to Cart button click event for each product
    addToCartBtns.forEach(addToCartBtn => {
      addToCartBtn.addEventListener('click', function () {
        const productContainer = addToCartBtn.closest('.product');
        const productId = productContainer.dataset.id;
        const productPrice = productContainer.dataset.price;
        const productName = productContainer.dataset.name;

        console.log("ff")

        // Check if the product is already in the cart
        const existingProduct = cart.find(item => item.id === productId);

        if (existingProduct) {
          // If the product is already in the cart, increment the quantity
          existingProduct.quantity++;
          // addToCartBtn.innerHTML = "Add to cart" + "(" + existingProduct.quantity + ")"

        } else {
          // If the product is not in the cart, add it with quantity 1
          cart.push({ id: productId, quantity: 1, price: productPrice, name: productName });
          // addToCartBtn.innerHTML = "Add to cart" + "(1)"
        }
        // Update the total quantity
        updateTotalQuantity();

        // Update the local storage
        localStorage.setItem('cart', JSON.stringify(cart));
      });
    });

    // Plus button click event for each product
    plusBtns.forEach(plusBtn => {
      plusBtn.addEventListener('click', updateQuantity.bind(null, 1));
    });

    // Minus button click event for each product
    minusBtns.forEach(minusBtn => {
      minusBtn.addEventListener('click', updateQuantity.bind(null, -1));
    });

    // // Clear Cart button click event
    // clearCartBtn.addEventListener('click', function () {
    //   // Clear the cart
    //   cart = [];
    //   // Update the total quantity
    //   updateTotalQuantity();
    //   // Update the local storage
    //   localStorage.setItem('cart', JSON.stringify(cart));
    //   var addcart = document.querySelectorAll('.add-to-cart')
    //   addcart.forEach(function (element) {
    //     element.innerText = "Add to cart";
    //   });
    //   cartValue.innerHTML = "Cart";
    // });

    // Function to update the quantity based on the button clicked (+1 or -1)
    function updateQuantity(change, event) {
      const quantitySpan = event.target.closest('.quantity').querySelector('.quantity-value');
      let quantity = parseInt(quantitySpan.innerText);

      // Update the quantity, but not below 0
      if (quantity + change >= 0) {
        quantity += change;
        quantitySpan.innerText = quantity;

        // Update the cart based on the button clicked
        const productId = event.target.closest('.product').dataset.id;
        const existingProduct = cart.find(item => item.id === productId);

        if (existingProduct) {
          existingProduct.quantity = quantity;
        } else {
          cart.push({ id: productId, quantity: 1 });
        }

        // Update the total quantity
        updateTotalQuantity();

        // Update the local storage
        localStorage.setItem('cart', JSON.stringify(cart));
      }
    }

    // Function to update the total quantity in the UI
    function updateTotalQuantity() {
      const totalQuantity = cart.reduce((total, item) => total + item.quantity, 0);
      totalQuantitySpan.innerText = totalQuantity;
      if (totalQuantity == 0) {
        cartValue.innerText = "Cart";
      } else {
        cartValue.innerText = "Cart" + "("+ totalQuantity + ")";
      }
    }
  });


