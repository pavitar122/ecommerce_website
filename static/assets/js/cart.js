

function getCartData() {
    const cartData = localStorage.getItem('cart');
    return cartData ? JSON.parse(cartData) : [];
  }


  // Function to display cart data in the table
  function displayCartData() {
    const cartTableBody = document.getElementById('cartTableBody');
    const totalAmountElement = document.getElementById('totalAmount');
    const checkout = document.getElementById('payment');
    
    

    // Get cart data from local storage
    const cartItems = getCartData();

    // Initialize total amount
    let totalAmount = 0;

    // Clear existing table rows
    cartTableBody.innerHTML = '';

    // Loop through cart items and display in the table
    cartItems.forEach(item => {
      const { name, price, quantity } = item;
      const total = price * quantity;
     
      // Update total amount
      totalAmount += total;
  
      // Create a table row
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${name}</td>
        <td>${price}</td>
        <td>${quantity}</td>
        <td>${total.toFixed(2)}</td>
      `;

      // Append the row to the table
      cartTableBody.appendChild(row);
    });

    // Display total amount
    if(totalAmount == "0"){
      checkout.style.visibility = "hidden";
    }
  
    totalAmountElement.textContent = totalAmount.toFixed(2);
  }

  // Call the function to display cart data on page load
  window.onload = displayCartData;

  function clearCart() {
    // Clear the 'cart' key from local storage
    const checkout = document.getElementById('payment');
    localStorage.removeItem('cart');
    cartTableBody.innerHTML = '';
    var total = document.getElementById('totalAmount');
    const cartValue = document.getElementById('cart');
    cartValue.innerText = "Cart"; 
    total.innerHTML = "0";
    checkout.style.visibility = "hidden";
    console.log(quantity)
}



// Attach the clearCart function to the button click event
document.getElementById('clearCartButton').addEventListener('click', clearCart);