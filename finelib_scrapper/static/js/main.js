// Show Menu
const showMenu = (headerToggle, navbarId) => {
    const toggleBtn = document.getElementById(headerToggle)
    nav = document.getElementById(navbarId)

    // Variable Validation
    if (headerToggle && navbarId){
        toggleBtn.addEventListener('click', () =>{
            // Call or add the show-menu class
            nav.classList.toggle('show-menu')

            // Change menu icon
            toggleBtn.classList.toggle('bx-x')
        })
    }
}

showMenu('header-toggle', 'navbar')


// Link Active
const linkColor = document.querySelectorAll('.nav__link')

function colorLink() {
    linkColor.forEach(l => l.classList.remove('active'))
    this.classList.add('active')
}

linkColor.forEach(l => l.addEventListener('click', colorLink))