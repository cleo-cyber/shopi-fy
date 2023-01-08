const search=document.querySelector('.search')
const searchInput=document.querySelector('.search_input')
search.addEventListener('click',showSearch)

function showSearch(e){

searchInput.classList.toggle('open-search')

}

const cartBtn=document.querySelector(".cartbox");
const dialog= document.querySelector('.dialog');

cartBtn.addEventListener('click',openDialog);

function openDialog(e){
    dialog.classList.toggle('visible')
}