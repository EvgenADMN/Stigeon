function ShowBlock() {
    if (MenuPeriods.value == 'create') {
        document.getElementById('add-period').style.display = 'flex';
        document.getElementById('edit-period').style.display = 'none';
        document.getElementById('delete-period').style.display = 'none';
    }
    if (MenuPeriods.value == 'change') {
        document.getElementById('edit-period').style.display = 'flex';
        document.getElementById('add-period').style.display = 'none';
        document.getElementById('delete-period').style.display = 'none';
    }
    if (MenuPeriods.value == 'delete') {
        document.getElementById('delete-period').style.display = 'flex';
        document.getElementById('add-period').style.display = 'none';
        document.getElementById('edit-period').style.display = 'none';
    }
}

var MenuPeriods = document.getElementById('menu');
MenuPeriods.addEventListener('change', ShowBlock);