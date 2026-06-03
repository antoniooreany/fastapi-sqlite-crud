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
      
      const span = document.createElement("span");
      const strong = document.createElement("strong");
      strong.textContent = item.name;
      span.appendChild(strong);
      span.appendChild(document.createTextNode(` — $${item.price}`));
      li.appendChild(span);

      const actions = document.createElement("div");
      actions.className = "actions";

      const discountBtn = document.createElement("button");
      discountBtn.textContent = "Discount";
      discountBtn.onclick = () => discountItem(item.id);
      
      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "Delete";
      deleteBtn.onclick = () => deleteItem(item.id);

      actions.appendChild(discountBtn);
      actions.appendChild(deleteBtn);
      li.appendChild(actions);

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
        "Content-Type": "application/json",
        "Authorization": `Bearer ${localStorage.getItem("token")}`
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
    const responseGet = await fetch(`/items/${id}`, {
      headers: { "Authorization": `Bearer ${localStorage.getItem("token")}` }
    });
    if (!responseGet.ok) {
      throw new Error(`HTTP ${responseGet.status}`);
    }

    const item = await responseGet.json();
    const newPrice = Math.max(0, item.price - 100);

    const responsePatch = await fetch(`/items/${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${localStorage.getItem("token")}`
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
      method: "DELETE",
      headers: { "Authorization": `Bearer ${localStorage.getItem("token")}` }
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
