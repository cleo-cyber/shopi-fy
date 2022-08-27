const search=document.querySelector('.search')
const searchInput=document.querySelector('.search_input')
search.addEventListener('click',showSearch)

function showSearch(e){

searchInput.classList.toggle('open-search')
}
