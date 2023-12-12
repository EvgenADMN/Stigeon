var DateFrom = document.getElementById("date-from");
var DateTo = document.getElementById("date-to");

DateFrom.addEventListener('change', SetMinDate);
function SetMinDate() {
    DateTo.disabled = false;
    DateTo.setAttribute('min', document.getElementsByName("date-from")[0].value);
};

function Loading() {
    var LoadScreen = document.getElementById("loading");
    var Table = document.getElementById("patterns-table");
    var Header = document.getElementById("header");
    LoadScreen.style.display = 'flex';
    Table.style.display = 'none';
    Header.style.display = 'none';
};

// ====================

