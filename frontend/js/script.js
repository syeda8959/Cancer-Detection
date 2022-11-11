let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
}





const bookFormDoctor = document.getElementById("bookFormDoctor");
bookFormDoctor.addEventListener("submit", bookDoctor);
function bookDoctor(e) {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const number = document.getElementById("number").value;
    const email = document.getElementById("email").value;
    const doctor = document.getElementById("doctor").value;
    const date = document.getElementById("date").value;

    
    const url = `http://localhost:8000/api/book/doctor`;
    fetch(url, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            "name": name,
            "age": age,
            "number": number,
            "email": email,
            "doctor": doctor,
            "date": date,
        })
    }).then(response => { return response.text() })
        .then((response) => {
            console.log(response);
            notie.alert({ text: "<h1>" + response + "</h1>", position: 'bottom', time: 3, type: 1 });
            return false;
        });
}

const bookFormHospital = document.getElementById("bookFormHospital");
bookFormHospital.addEventListener("submit", bookHospital);
function bookHospital(e) {
    e.preventDefault();
    const name = document.getElementById("nameH").value;
    const age = document.getElementById("ageH").value;
    const number = document.getElementById("numberH").value;
    const location = document.getElementById("locationH").value;
    const email = document.getElementById("emailH").value;
    const hospital = document.getElementById("hospitalH").value;
    const date = document.getElementById("dateH").value;


    const url = `http://localhost:8000/api/book/hospital`;
    fetch(url, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            "name": name,
            "age": age,
            "number": number,
            "location": location,
            "email": email,
            "doctor": doctor,
            "date": date,
        })
    }).then(response => { return response.text() })
        .then((response) => {
            console.log(response);
            notie.alert({ text: "<h1>" + response + "</h1>", position: 'bottom', time: 3, type: 1 });
            return false;
        });
}



