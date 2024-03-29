//Récupérer les prix avant promo les barrer
let priceBeforePromotion = document.querySelectorAll(".old-price")

priceBeforePromotion.forEach(function(i){
    i.style.textDecoration="line-through";
})

//Récupérer les prix après promotion et les afficher en gras en rouge
let newPrice = document.querySelectorAll(".new-price")

newPrice.forEach(function(j){
    j.style.fontStyle="bold";
    j.style.color="rgb(220 38 38)";
    j.style.fontWeight="bold";
})

//mis en place des filtre et tri

let formSubmit = document.getElementById("filter")

// au submit du formulaire de filtre, empeche le chargement de toute la page
formSubmit.addEventListener('submit', function (event){
    event.preventDefault();

    let categorySelected = document.querySelector('select.form-select').value
    let sortSelected = document.querySelector('input[name="tri-choix"]:checked').value

    if (categorySelected !== "Choisir une catégorie" && sortSelected !== null) {
        fetch('/updated_selection', {
            method: 'POST',
            headers: {"Content-type": "application/json"},
            body: JSON.stringify({category: categorySelected, sortOrder: sortSelected}),
        })
            .then(response =>response.json())
            .then(data => { document.getElementById('product-display').innerHTML = data.productsHTML;})
            .catch(error => console.error('error:', error));
    }else{
        console.log("categorie non valide - tri valide")
        alert("Veuillez choisir une catégorie valide")
    }
})

