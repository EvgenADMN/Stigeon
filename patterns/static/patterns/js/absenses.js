function ShowBlockAbsense() {
    if (MenuAbsense.value == 'create') {
        document.getElementById('add-absense').style.display = 'flex';
        document.getElementById('edit-absense').style.display = 'none';
        document.getElementById('delete-absense').style.display = 'none';
    }
    if (MenuAbsense.value == 'change') {
        document.getElementById('edit-absense').style.display = 'flex';
        document.getElementById('add-absense').style.display = 'none';
        document.getElementById('delete-absense').style.display = 'none';
    }
    if (MenuAbsense.value == 'delete') {
        document.getElementById('delete-absense').style.display = 'flex';
        document.getElementById('add-absense').style.display = 'none';
        document.getElementById('edit-absense').style.display = 'none';
    }
}

var MenuAbsense = document.getElementById('menu-absense');
MenuAbsense.addEventListener('change', ShowBlockAbsense);