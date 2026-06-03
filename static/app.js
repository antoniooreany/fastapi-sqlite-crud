const list = document.getElementById("items-list");
const form = document.getElementById("item-form");
const message = document.getElementById("message");

async function loadItems() {
  try {
    const response = await fetch("/items/");
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const items = await response.json();
    list.innerHTML = "";

    for (const item of items) {
      const li = document.createElement("li");
      li.innerHTML = `
        <span><strong>${item.name}</strong> — $${item.price}</span>
        <div class="actions">
          <button onclick="discountItem(${item.id})">Discount</button>
          <button onclick="deleteItem(${item.id})">Delete</button>
        </div>
      `;
      list.appendChild(li);
    }
  } catch (error) {
    message.textContent = "Failed to load items";
    console.error(error);
  }
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const price = Number(document.getElementById("price").value);

  try {
    const response = await fetch("/items/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name, price })
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    form.reset();
    message.textContent = "Item added";
    loadItems();
  } catch (error) {
    message.textContent = "Failed to add item";
    console.error(error);
  }
});

async function discountItem(id) {
  try {
    const responseGet = await fetch(`/items/${id}`);
    if (!responseGet.ok) {
      throw new Error(`HTTP ${responseGet.status}`);
    }

    const item = await responseGet.json();
    const newPrice = Math.max(0, item.price - 100);

    const responsePatch = await fetch(`/items/${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ price: newPrice })
    });

    if (!responsePatch.ok) {
      throw new Error(`HTTP ${responsePatch.status}`);
    }

    message.textContent = "Price updated";
    loadItems();
  } catch (error) {
    message.textContent = "Failed to update item";
    console.error(error);
  }
}

async function deleteItem(id) {
  try {
    const response = await fetch(`/items/${id}`, {
      method: "DELETE"
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    message.textContent = "Item deleted";
    loadItems();
  } catch (error) {
    message.textContent = "Failed to delete item";
    console.error(error);
  }
}

loadItems();
