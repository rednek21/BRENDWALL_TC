async function getProducts() {
    try {
    const response = await fetch('api/v1/products/', {
      method: 'GET',
    });

    if (response.ok) {
      const result = await response.json();

      document.getElementById('product_list').replaceChildren(showProducts(result));
      console.log('Ответ от сервера: ', result);
    } else {
      document.getElementById('response').textContent = 'Ошибка при отправке';
      console.error('Ошибка: ', response.statusText);
    }
  } catch (error) {
    document.getElementById('response').textContent = 'Ошибка запроса';
    console.error('Ошибка запроса: ', error);
  }
}

function showProducts(products) {
    let productList = document.createElement("table")
    products.forEach((product) => {
        let productItem = document.createElement("tr")
        let productTitle = document.createElement("td")
        let productPrice = document.createElement("td")
        let productDesc = document.createElement("td")

        productTitle.innerHTML = product.title
        productPrice.innerHTML = product.price
        productDesc.innerHTML = product.description

        productItem.append(productTitle)
        productItem.append(productPrice)
        productItem.append(productDesc)

        productList.append(productItem)
    })
    return productList
}

getProducts()

document.getElementById('product_form').addEventListener('submit', async function(event) {
  event.preventDefault();

  const form = event.target;

  const formData = new FormData(form);

  try {
    const response = await fetch('api/v1/products/create/', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const result = await response.json();
      document.getElementById('response').textContent = 'Успешно отправлено';
      console.log('Ответ от сервера: ', result);
      getProducts()
    } else {
      document.getElementById('response').textContent = 'Ошибка при отправке';
      console.error('Ошибка: ', response.statusText);
    }
  } catch (error) {
    document.getElementById('response').textContent = 'Ошибка запроса';
    console.error('Ошибка запроса: ', error);
  }
});

