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
    
    //SLIDESHOW//
    
    const left=document.querySelector('.left');
    const right =document.querySelector('.right');
    const slideContainer= document.querySelector('.slider');
    const products= document.querySelectorAll('.products')
    
    
    //EVENTS//
    right.addEventListener('click',moveRight);
    left.addEventListener('click',moveLeft)
    sectionPosition=0
    function moveRight(e){
        if(sectionPosition<products.length-1){
            sectionPosition=sectionPosition+1;
        }
        else if(sectionPosition==products.length-1){
            sectionPosition=0;
        }
        else{
            sectionPosition=products.length-1;
        }
        console.log(products)
        slideContainer.style.transform='translateX('+(sectionPosition)* products.length * -3+'%)';
    }
    
    function moveLeft(e){
        if(sectionPosition>0){
            sectionPosition=sectionPosition-1
        }
        else if(sectionPosition==0){
            sectionPosition=products.length-1;
        }
        else{
            sectionPosition=0;
        }
    
        slideContainer.style.transform='translateX('+(sectionPosition)*products.length*-3+'%)'
    }
    
    
    // FAQS //
    
    const toggleBar=document.querySelectorAll('.queries_container');
    
    
    var i=0
    
    for(i;i<toggleBar.length;i++){
     toggleBar[i].addEventListener('click',toggleQuiz);
    
    }
    
    
    function toggleQuiz(e){
        this.classList.toggle('active');
     
    
    }


