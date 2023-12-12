function DropdownPatterns() {
    if (document.getElementById("patterns").style.display != 'flex') {
        document.getElementById("patterns").style.display = 'flex';
    } else {
        document.getElementById("patterns").style.display = 'none';
    }
};

window.onclick = function(event) {
    if (!event.target.matches('.patterns-dropdown-button')) {
        document.getElementById("patterns").style.display = 'none';
    }
}