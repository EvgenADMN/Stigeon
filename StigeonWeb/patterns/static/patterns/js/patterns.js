function add_person() {
    var MainBlock = document.getElementById('person-block');
    var CountOfEmployees = document.getElementsByClassName('person').length;
    const newPerson = document.createElement("div");
    newPerson.classList.add('person')
    newPerson.setAttribute('id', 'person_' + (CountOfEmployees + 1))

    const newInputBlock = document.createElement("div");
    newInputBlock.classList.add('input-block')

    const newP = document.createElement("p");
    const newPText = document.createTextNode("Сотрудник:");

    const newFio = document.createElement("input");
    newFio.classList.add('fio')
    newFio.setAttribute('name', 'employee_' + (CountOfEmployees + 1))
    newFio.setAttribute('list', 'employee')

    const newButtonBlock = document.createElement("div");
    newButtonBlock.classList.add('button-block')

    const newXButton = document.createElement("p");
    newXButton.classList.add('delete-person');
    newXButton.setAttribute('title', 'Убрать строку');
    newXButton.setAttribute('onclick', 'DeletePerson("person_' + (CountOfEmployees + 1) + '")');
    const newXButtonText = document.createTextNode("✕");



    MainBlock.appendChild(newPerson)
    newPerson.appendChild(newInputBlock)
    newPerson.appendChild(newButtonBlock)
    newInputBlock.appendChild(newP)
    newP.appendChild(newPText)
    newInputBlock.appendChild(newFio)
    newButtonBlock.appendChild(newXButton)
    newXButton.appendChild(newXButtonText)
}

function add_device() {
    var DevicesBlock = document.getElementById('device_id');
    var SelectedText = DevicesBlock.options[DevicesBlock.selectedIndex].text;
    var BlockOfChosen = document.getElementById('chosen-devices');
    var Disabled = document.getElementById('disabled');

    if (SelectedText == 'Выберите считыватель') {
        return
    }

    var DeviceFromList = document.getElementsByTagName("option");
    for (var i = 0; i < DeviceFromList.length; i++) {
        if (DeviceFromList[i].textContent == SelectedText) {
            //DeviceFromList[i].remove();
            DeviceFromList[i].disabled = 'true';

        }
    }

    const Device = document.createElement("div");
    Device.classList.add('chosen-device-block');
    Device.setAttribute('id', 'chosen-device-block_' + (document.getElementsByClassName('chosen-device-block').length + 1));

    const InputField = document.createElement("input");
    InputField.classList.add('chosen-device');
    InputField.setAttribute('readonly', '');
    InputField.setAttribute('id', 'chosen_device_' + (document.getElementsByClassName('chosen-device-block').length + 1));
    InputField.setAttribute('value', SelectedText);

    const HiddenInputField = document.createElement("input");
    HiddenInputField.setAttribute('name', 'chosen_device_' + (document.getElementsByClassName('chosen-device-block').length + 1));
    HiddenInputField.setAttribute('type', 'hidden')
    HiddenInputField.setAttribute('value', DevicesBlock.value);

    const XField = document.createElement("div");
    XField.classList.add('chosen-device-button');
    const Text = document.createElement("p");
    Text.setAttribute('id', 'del-chosen-device-block_' + (document.getElementsByClassName('chosen-device-block').length + 1))
    Text.setAttribute('onclick', 'DeleteDevice("del-chosen-device-block_' + (document.getElementsByClassName('chosen-device-block').length + 1) + '")')
    const newXButtonText = document.createTextNode("✕");

    BlockOfChosen.appendChild(Device);
    Device.appendChild(InputField);
    Device.appendChild(HiddenInputField);

    Device.appendChild(XField);
    XField.appendChild(Text);
    Text.appendChild(newXButtonText);
    DevicesBlock.value = 'Выберите считыватель'
   // alert()
}

function DeleteDevice(device_id) {
    var elem = document.getElementById(device_id.slice(4));
    var SelectedText = document.getElementById(device_id.slice(4, 10) + '_' + device_id.slice(11, 17) + '_' + device_id.slice(-1)).value;
    var DeviceFromList = document.getElementsByTagName("option");
    for (let i = 0; i < DeviceFromList.length; i++) {
        if (DeviceFromList[i].textContent == SelectedText) {
            DeviceFromList[i].disabled = false;
        }
    }
    elem.parentNode.removeChild(elem);
}

function DeletePerson(person_id) {
    document.getElementById(person_id).parentNode.removeChild(document.getElementById(person_id));
    var Persons = document.getElementsByClassName('person');
    var Onclick = document.getElementsByClassName('delete-person');
    for (let i = 0; i < Persons.length; i++) {
        Persons[i].id = 'person_' + (i + 1)
    };
    for (let i = 0; i < Onclick.length; i++) {
        Onclick[i].setAttribute('onclick', 'DeletePerson("person_' + (i + 1) + '")')
    };
};

if (document.getElementsByClassName('chosen-device').length > 0) {
    var ChosenDevices = document.getElementsByClassName('chosen-device');
    var ChosenDevicesList = [];
    var DeviceFromList = document.getElementsByTagName("option");;

    for (let i = 0; i < ChosenDevices.length; i++) {
        ChosenDevicesList.push(ChosenDevices[i].value)
    };
    for (let i = 0; i < DeviceFromList.length; i++) {
        if (ChosenDevicesList.includes(DeviceFromList[i].textContent)) {
            DeviceFromList[i].disabled = true;
        };
    };
};

