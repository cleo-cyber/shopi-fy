const quotcontainer=document.querySelector('.quot_container')
const quotes=Array.from(document.querySelectorAll('.quotes'))


// Global variables//

let isDragging=false,
startposition=0,
currentTranslate=0,
previousTranslate=0,
animationID=0,
currentIndex=0;

quotes.forEach(function(quote,index)
{
    window.oncontextmenu=function(e){
        e.preventDefault()
        e.stopPropagation()
        return false
    }

    // Touch Events //
quote.addEventListener('touchstart',touchStart(index))
quote.addEventListener('touchend',touchEnd)
quote.addEventListener('touchmove',touchMove)

// Mouse Events
quote.addEventListener('mousedown',touchStart(index))
quote.addEventListener('mouseup',touchEnd)
quote.addEventListener('mousemove',touchMove)

})

function touchStart(index){
    return function(e){
      currentIndex=index
      startposition=getPositionX(e)
      isDragging=true
      animationID=requestAnimationFrame(animation)
    }
}
function touchEnd(){
    isDragging=false
    cancelAnimationFrame(animationID)
    const movedBy=currentTranslate-previousTranslate
    if(movedBy<-100 && currentIndex<quotes.length-1){
        currentIndex+=1
    }
    if(movedBy>100 && currentIndex>0){
        currentIndex-=1

    }
    setPositionByIndex()
}
function touchMove(e){
 if(isDragging){
    const currentPosition=getPositionX(e)
    currentTranslate=previousTranslate+currentPosition-startposition
 }
}
function animation(){
setSliderPosition()
if(isDragging){
    requestAnimationFrame(animation)
}
}

function getPositionX(e){
    return e.type.includes('mouse')?e.pageX:e.touches[0].clientX;
}
function setSliderPosition(){
    quotcontainer.style.transform=`translateX(${currentTranslate}px)`
}
function setPositionByIndex(){
currentTranslate=currentIndex* -window.innerWidth;
previousTranslate=currentTranslate
}