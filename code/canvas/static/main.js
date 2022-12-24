 console.log('hello')

const eventBox =document.getElementById('event-box')
const countdownBox = document.getElementById('countdown-box')
const eventnameBox =  document.getElementById('event_name')

const gal = document.getElementById('img_gallery');


event_name= eventnameBox.innerHTML
console.log(event_name)

const eventDate= Date.parse(eventBox.textContent)
console.log(eventDate)
var folder = "./media";

setInterval(()=>{
    const now= new Date().getTime()
    // console.log(now)
    const diff = eventDate- now

     console.log(diff)

    const d= Math.floor((eventDate / (1000*60*60*24)) - (now /(1000*60*60*24)))
    const h= Math.floor((eventDate / (1000*60*60) - (now /(1000*60*60))) %24)
    const m= Math.floor((eventDate / (1000*60) - (now /(1000*60))) %60)
    const s= Math.floor((eventDate / (1000) - (now /(1000))) %60)

    if(diff>0){
       
        countdownBox.innerHTML = d + " days, " +h + " hours, "+ m + " minutes, " +s  +" seconds" 
        gal.style.display= 'block'
    } 

    else{
        countdownBox.innerHTML = "Countdown Completed"
       

    
    }

    

}, 1000)
