
//affectation des date par defaut pour les dates de promotion

let promoStartDefaultDate = document.getElementById("promo_start");
let promoEndDefaultDate= document.getElementById("promo_end");

let currentDate = new Date();
let currentDateString = currentDate.toISOString().slice(0, 10);

promoStartDefaultDate.value = currentDateString;
promoEndDefaultDate.value = currentDateString;

//affectation montant par defaut de la promotion

let promoAmountDefault = document.getElementById("promo_amount")

promoAmountDefault.value = "0"

//Récupérer les prix avant promo les barrer
let priceBeforePromotion = document.querySelectorAll(".old-price")

priceBeforePromotion.forEach(function(i){
    i.style.textDecoration="line-through";
})

//Récupérer les prix après promotion et les afficher en gras en rouge
let newPrice = document.querySelectorAll(".new-price")

newPrice.forEach(function(j){
    j.style.fontStyle="bold";
    j.style.color="Red";
    j.style.fontWeight="bold";
})
