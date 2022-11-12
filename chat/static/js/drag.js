
objeto = document.querySelector('.yellow')
objeto_drop = document.querySelector('.blue')
console.log(objeto_drop)
objeto.addEventListener('dragstart', function(e){
    console.log('ok')
    console.log(e.target)
    this.classList.add("hide")
    e.dataTransfer.clearData();
    e.dataTransfer.setData("text/plain", e.target.id)
})

objeto_drop.addEventListener('dragover', function(e){
    e.preventDefault()
})
objeto_drop.addEventListener('drop', function(e){
    e.preventDefault()
    const data = e.dataTransfer.getData('text')
    console.log(data)
    const source = document.getElementById(data)
    this.appendChild(source)
})



