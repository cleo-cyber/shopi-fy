const burger=document.querySelector('.burger')
const dashboard=document.querySelector('.dashboard')

burger.addEventListener('click',ShowCloseDashboard)

function ShowCloseDashboard(e){
  dashboard.classList.toggle('open-dash')
}