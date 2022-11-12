const documento = document.querySelector('#master')
console.log(documento)
new Sortable(document.querySelector('#master'), {
    animation: 150,
    group: 'teste', 
    ghostClass: 'blue-background-class'
});

const documento2 = document.querySelector('#master2')
console.log(documento)
new Sortable(document.querySelector('#master2'), {
    animation: 150,
    group: 'teste', 
    ghostClass: 'blue-background-class',
});

const arrastaveis = document.getElementsByClassName('childdiv')

for (let x=0; x<arrastaveis.length; x++){
    arrastaveis[x].addEventListener('dragstart', function(e){
        e.dataTransfer.clearData();
        console.log(e.target.children[2].id)
    const temp = document.querySelector('#temp')
    temp.value = e.target.children[2].id
    
    })
}

const dropaveis = document.getElementsByClassName('masterdiv')

for (let x=0; x<dropaveis.length; x++){
dropaveis[x].addEventListener('dragover', function(e){
    e.preventDefault()
})
dropaveis[x].addEventListener('drop', function(e){
    const temp = document.querySelector('#temp')
    const target = document.getElementById(temp.value)
    console.log(target)
    if (target.parentElement.parentElement.id == 'master' && target.value == 'FE' ){
        target.value = 'AF'
        console.log('mudou')

    }

    if(target.parentElement.parentElement.id == 'master2' && target.value == 'AF'){
        target.value = 'FE'
        console.log('mudou')        
    }

})
}
