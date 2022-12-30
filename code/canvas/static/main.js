 console.log('hello')

const eventBox =document.getElementById('event-box')
const countdownBox = document.getElementById('countdown-box')
const eventnameBox =  document.getElementById('event_name')
const gal = document.getElementById('img_gallery');
const end_date = document.getElementById('end_date')


event_name= eventnameBox.innerHTML


const eventDate= Date.parse(eventBox.textContent)
const endDate = Date.parse(end_date.textContent)

var folder = "./media";

setInterval(()=>{
    const now= new Date()
    console.log(now)
    // console.log(now)
    const diff = eventDate- now
    console.log(diff)

    const end_diff= endDate - now
    console.log(end_diff)



    const d= Math.floor((eventDate / (1000*60*60*24)) - (now /(1000*60*60*24)))
    const h= Math.floor((eventDate / (1000*60*60) - (now /(1000*60*60))) %24)
    const m= Math.floor((eventDate / (1000*60) - (now /(1000*60))) %60)
    const s= Math.floor((eventDate / (1000) - (now /(1000))) %60)

    if(diff>0){
       
        countdownBox.innerHTML = d + " days, " +h + " hours, "+ m + " minutes, " +s  +" seconds" 
        
    } 

    else if(end_diff<0){
        countdownBox.innerHTML = "Event has ended on " + end_date.innerHTML
      
    }

    else{
        // countdownBox.innerHTML = "Countdown Completed"
        gal.style.display= 'block'
    
    }


    

    

}, 1000)
