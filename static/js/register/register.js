//!Register.js
let recaptcha_checkbox = document.querySelector('.rc-anchor-center-item rc-anchor-checkbox-holder')
const alertMessagesDjango = document.getElementsByClassName('alert-block')

if(alertMessagesDjango){
    alertMessagesDjango[0].classList.add('border','rounded','shadow')
    setTimeout(()=>{
        alertMessagesDjango[0].style.display = 'none'
    },5000)
}