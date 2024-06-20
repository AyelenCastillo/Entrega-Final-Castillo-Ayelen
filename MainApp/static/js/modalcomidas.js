document.addEventListener("DOMContentLoaded", (event) => {

    event.preventDefault();

    const openModalButton = document.getElementById("openModalButton");

    const modal = document.getElementById("myModal");

    const closeModalButton = document.getElementById("closeModalButton");



    modal.style.display = "none";



    openModalButton.addEventListener("click", () => {

        modal.style.display = "block";

    });

    closeModalButton.addEventListener("click", () => {

        modal.style.display = "none";

    });

});

document.addEventListener('DOMContentLoaded', function() {
    const recetaTextarea = document.getElementById('receta');
    const ingredientesTextarea = document.getElementById('ingredientes');
    
 
    recetaTextarea.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); 
            const textarea = event.target;
            textarea.value += '\n'; 
        }
    });

    
    ingredientesTextarea.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); 
            const textarea = event.target;
            textarea.value += '\n';
        }
    });
});


function requireLogin() {
    alert("Debes iniciar sesión para compartir tus recetas.");
}