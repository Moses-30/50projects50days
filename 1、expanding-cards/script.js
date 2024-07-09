const panels = document.querySelectorAll('.panel')

panels.forEach((panel, index) => {
    panel.addEventListener('click', () => {
        removeActiveClasses()
        panel.classList.add('active')
        console.log("index:", index)
    })
})

function removeActiveClasses() {
    panels.forEach(panel => {
        panel.classList.remove('active')
    })
}