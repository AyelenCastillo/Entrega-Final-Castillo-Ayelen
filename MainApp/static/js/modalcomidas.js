document.addEventListener('DOMContentLoaded', () => {
    const openModalButton = document.getElementById('openModalButton');
    const modal = document.getElementById('myModal'); 
    const closeModalButton = document.getElementById('closeModalButton');
    
    modal.style.display = 'none';

    openModalButton.addEventListener('click', () => {
        modal.style.display = 'block';
    });
    closeModalButton.addEventListener('click', () => {
    modal.style.display = 'none';
    });
});


