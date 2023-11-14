let toggleButton = document.getElementsByClassName('toggle-button')[0]
let navLinks = document.getElementsByClassName('nav_link')[0]
let scroller = document.getElementsByClassName('containerSection')

toggleButton.addEventListener('click',() => {
    navLinks.classList.toggle('active')
})