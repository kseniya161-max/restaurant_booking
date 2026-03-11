document.addEventListener("DOMContentLoaded", function(){

const buttons = document.querySelectorAll(".select-table")

buttons.forEach(function(button){

button.addEventListener("click", function(){

const tableId = this.dataset.table

const select = document.querySelector("#id_table")

select.value = tableId

window.scrollTo({
top: document.querySelector(".contact-form").offsetTop - 80,
behavior: "smooth"
})

})

})

})