const slider=()=>{
    const navLink=document.querySelector('.nav_links');
    const burger=document.querySelector('.burger');
    const links=document.querySelectorAll('.nav_links li');
    //toggle navigation bar
    burger.addEventListener('click',()=>{
        navLink.classList.toggle('nav-active');
        burger.classList.toggle('toggled');

    
    });
    
    links.forEach((link,index)=>{
        if(link.style.animation){
            link.style.animation=""
        }
        else{
            link.style.animation=`navLinkAnimation 0.5s ease forwards ${index/7 +1.5}s`;
        }
    })
    
    }
slider()