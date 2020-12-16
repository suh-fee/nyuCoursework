var newTaskButton = document.getElementById("newTask");
newTaskButton.addEventListener("click", addNewItem);


// function deletes item, sender is button of item that triggered function
function deleteItem(sender) {
    var list = document.getElementById("myUL");
    var length = list.childElementCount;
    var items = list.getElementsByClassName("delbutton")
    var index;
    var itemToDelete;
    
    for (var i = 0; i < length; i++) { // loop through items in list and find index if item that is going to be deleted
        if (items[i] == sender) {
            index = i;
            itemToDelete = items[i].parentElement;
            break;
        }
    }
    xhttp = new XMLHttpRequest(); 
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) { // if everything is ok
            var response = JSON.parse(this.responseText);
            if (response['result'] == "succes")
                renderDeleteItem(itemToDelete);
            else
                alert ("Failed to delete item.");
        }
    };
    xhttp.open("DELETE", "/todo/delete", true);
    xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({item:index}));
}

// deletes item from web page
function renderDeleteItem(item) {
    item.parentNode.removeChild(item);
}

// Function send request to server and adds new item
function addNewItem(event) {
    text = document.getElementById("input").value;
    text = text.trim()
    if (text == "")
        return
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(this.responseText);
            if (response['result'] == "succes")
                renderNewItem(text)
            else
                alert ("fail")
        }
    };
    xhttp.open("POST", "/todo/create", true);
    xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({content:text}));
}

// show new item on web page
function renderNewItem(text) {
    var list = document.getElementById("myUL")
    var item = document.createElement('li')
    item.innerHTML = text + '<button type="button" onclick="deleteItem(this)" class="delbutton">-</button><button type="button" onclick="openModal(this)" class="updateButton">update</button>'
    list.appendChild(item)
}

var modal = document.getElementById('myModal'); // modal window for updating item

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var itemToBeUpdated;

// function opens modal window 
function openModal(sender) {
    modal.style.display = "block";
    console.log(sender);
    itemToBeUpdated = sender;
}

// function sends request to server and updates item also on page after receiving positive response
function updateItem() {
    var newText = document.getElementById("newValue").value.trim();
    var list = document.getElementById("myUL");
    var length = list.childElementCount;
    var items = list.getElementsByClassName("updateButton")
    var index;
    for (var i = 0; i < length; i++) {
        if (items[i] == itemToBeUpdated) {
            index = i;
            break;
        }
    }
    console.log('updatovat idem' + index);
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(this.responseText);
            console.log(response)
            if (response['result'] == "succes") {
                itemToBeUpdated.parentElement.innerHTML = newText + '<button type="button" onclick="deleteItem(this)" class="delbutton">-</button><button type="button" onclick="openModal(this)" class="updateButton">update</button>';
                modal.style.display = "none";
            }
            else {
                modal.style.display = "none";
                alert ("Failed to update item.");
            }
        }
    };
    xhttp.open("PUT", "/todo/update", true);
    xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({item_number:index, content:newText}));

}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}