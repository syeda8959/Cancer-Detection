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





const bookForm = document.getElementById("bookForm");
bookForm.addEventListener("submit", book);
function book(e) {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const number = document.getElementById("number").value;
    const email = document.getElementById("email").value;
    const doctor = document.getElementById("doctor").value;
    const date = document.getElementById("date").value;

    
    const url = `http://localhost:8000/api/book`;
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