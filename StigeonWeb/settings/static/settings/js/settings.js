var connect = document.getElementById('connect');
var get_devices = document.getElementById('get-devices');
var get_employees = document.getElementById('get-employees');
var colors = document.getElementById('colors');


function show_connect() {
    get_devices.style.display = 'none';
    get_employees.style.display = 'none';
    colors.style.display = 'none';
    connect.style.display = 'flex';
    document.getElementById('content-block').value = 'connect';
};

function show_get_devices() {
    connect.style.display = 'none';
    get_employees.style.display = 'none';
    colors.style.display = 'none';
    get_devices.style.display = 'flex';
    document.getElementById('content-block').value = 'get_devices';
};

function show_get_employee_list() {
    connect.style.display = 'none';
    get_devices.style.display = 'none';
    colors.style.display = 'none';
    get_employees.style.display = 'flex';
    document.getElementById('content-block').value = 'get_employee_list';
};

function show_colors() {
    connect.style.display = 'none';
    get_employees.style.display = 'none';
    colors.style.display = 'flex';
    document.getElementById('content-block').value = 'colors';
};

// ======================

function clear_checkbox() {
    var clear_checkbox=document.getElementsByTagName('input');
    for(var i=0;i<clear_checkbox.length;i++) {
        if(clear_checkbox[i].type=='checkbox') {
            clear_checkbox[i].checked=false
        }
    }
};

function select_checkbox() {
    var select_checkbox=document.getElementsByTagName('input');
    for(var i=0;i<select_checkbox.length;i++) {
        if(select_checkbox[i].type=='checkbox') {
            select_checkbox[i].checked=true
        }
    }
};