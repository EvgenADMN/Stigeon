function ShowDescription() {
    var Chosen = MenuEdit.options[MenuEdit.selectedIndex].text
    document.getElementById('desc-id').innerText = Name_Desc[Chosen]
};

var Name_Desc = {};
var PatternNames = document.getElementsByClassName('pattern-name');
var PatternDescs = document.getElementsByClassName('patterns-description');
for (let i = 0; i < PatternNames.length; i++) {
    Name_Desc[PatternNames[i].value] = PatternDescs[i].value;
};

var MenuEdit = document.getElementById('edit-menu');

MenuEdit.addEventListener('change', ShowDescription);



