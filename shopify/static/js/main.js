// HEADER//
const slider=()=>{
    const navLink=document.querySelector('.nav_links');
    const burger=document.querySelector('.burger');
    const links=document.querySelectorAll('.nav_links li');
    //toggle navigation bar
    burger.addEventListener('click',()=>{
        navLink.classList.toggle('nav-active');
    
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
    
    // //SLIDESHOW//
    
    // const left=document.querySelector('.left');
    // const right =document.querySelector('.right');
    // const slideContainer= document.querySelector('.slider');
    // const products= document.querySelectorAll('.products')
    
    
    // //EVENTS//
    // right.addEventListener('click',moveRight);
    // left.addEventListener('click',moveLeft)
    // sectionPosition=0
    // function moveRight(e){
    //     if(sectionPosition<products.length-1){
    //         sectionPosition=sectionPosition+1;
    //     }
    //     else if(sectionPosition==products.length-1){
    //         sectionPosition=0;
    //     }
    //     else{
    //         sectionPosition=products.length-1;
    //     }
    //     console.log(products)
    //     slideContainer.style.transform='translateX('+(sectionPosition)* products.length * -3+'%)';
    // }
    
    // function moveLeft(e){
    //     if(sectionPosition>0){
    //         sectionPosition=sectionPosition-1
    //     }
    //     else if(sectionPosition==0){
    //         sectionPosition=products.length-1;
    //     }
    //     else{
    //         sectionPosition=0;
    //     }
    
    //     slideContainer.style.transform='translateX('+(sectionPosition)*products.length*-3+'%)'
    // }
    
    
    const slideContainer=document.querySelector('.slider');
    const sliderItems=Array.from(document.querySelectorAll('.products'));

    let=isDragging=false,
    startPosition=0,
    currentTranslate=0,
    previousTranslate=0,
    animationID=0,
    currentIndex=0;

    sliderItems.forEach(function(slide,index){
        const slideImage=slide.querySelector('img')
        slideImage.addEventListener('dragstart',function(e){
            e.preventDefault()
        });
            
    // EVENTS//

    // Touch Events
    slide.addEventListener('touchstart',touchStart(index));
    slide.addEventListener('touchend',touchEnd);
    slide.addEventListener('touchmove',touchMove);

    // Mouse Events

    slide.addEventListener('mousedown',touchStart(index))
    slide.addEventListener('mouseup',touchEnd)
    slide.addEventListener('mousemove',touchMove)
    });


function touchStart(index){
   return function(e){
    currentIndex=index
    startPosition=getPositionX(e)
    isDragging=true
    animationID=requestAnimationFrame(animation)
   }

}

function touchEnd(){
    isDragging=false
    const movedBy=currentTranslate-previousTranslate;

    if(movedBy<-100 && currentIndex<sliderItems.length-1){
        currentIndex+=1;
    }
    if(movedBy >100 && currentIndex>0){
        currentIndex-=1
    }

    setPostionByIndex()

}

function touchMove(){
   if(isDragging){
    cancelAnimationFrame(animationID)
    const currentPosition=getPositionX(e)
    currentTranslate=currentPosition+previousTranslate-startPosition
   }
}


function getPositionX(e){
    return e.type.includes('mouse')? e.pageX :e.touches[0].clientX;
}

function animation(){
    setSliderPosition()
    if(isDragging){
        requestAnimationFrame(animation)
    }
}
function setSliderPosition(){
    slideContainer.style.transform=`translateX(${currentTranslate}px)`
}
function setPostionByIndex(){
    currentTranslate=currentIndex * -window.innerWidth
    previousTransalte=currentTranslate
    setSliderPosition()
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