function showSynopsis(synopsis) {
    document.getElementById('synopsis-text').innerText = synopsis;
    document.getElementById('synopsis-modal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('synopsis-modal').style.display = 'none';
}
