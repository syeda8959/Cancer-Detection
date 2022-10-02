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

function predict(form) {
    const age = parseInt(document.getElementById("age").value);
    const menopause = parseInt(document.getElementById("menopause").value);
    const tumor_size = parseInt(document.getElementById("tumor-size").value);
    const inv_nodes = parseInt(document.getElementById("inv-nodes").value);
    const node_cap = parseInt(document.getElementById("node-cap").value);
    const deg_malig = parseInt(document.getElementById("deg-malig").value);
    const breast = parseInt(document.getElementById("breast").value);
    const breast_quad = parseInt(document.getElementById("breast-quad").value);
    const irradiat = parseInt(document.getElementById("irradiat").value);
    

    const url = `http://localhost:8000/api/predict`;
    fetch(url, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            "age": age,
            "menopause": menopause,
            "tumor-size": tumor_size,
            "inv-nodes": inv_nodes,
            "node-caps": node_cap,
            "deg-malig": deg_malig,
            "breast": breast,
            "breast-quad": breast_quad,
            "irradiat": irradiat
        })
    }).then(response => response.text())
        .then((response) => {
            console.log(response);
            notie.alert({ text: "<h1>"+response+"</h1>", position: 'bottom', time: 4, type:1 });
        });

}