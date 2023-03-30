const list = document.getElementById("tasklist");
const addButton = document.querySelector("button");
const input = document.querySelector("input");

function addTask() {
    const item = document.createElement("li");
    item.innerText = input.value;
    const checkbox = document.createElement("input");
    checkbox.classList.add("checkbox");
    checkbox.type = "checkbox";
    checkbox.addEventListener("click", completeItem);
    const deleteButton = document.createElement("button");
    deleteButton.classList.add("delete");
    deleteButton.innerText = "X";
    deleteButton.addEventListener("click", deleteTask);
    item.appendChild(checkbox);
    item.appendChild(deleteButton);
    list.appendChild(item);
    input.value = "";
}

function completeItem(event) {
    const checkbox = event.target;
    const item = checkbox.parentElement;
    if (checkbox.checked) {
        item.classList.add("completed");
    } else {
        item.classList.remove("completed");
    }
}

function deleteTask(event) {
    const deleteButton = event.target;
    const item = deleteButton.parentElement;
    item.remove();
}

addButton.addEventListener("click", addTask);