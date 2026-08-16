const navbarToggle = document.querySelector('.navbar-toggle');
const navbarMenu = document.querySelector('.navbar-menu');

navbarToggle.addEventListener('click', () => {
    navbarToggle.classList.toggle('active');
    navbarMenu.classList.toggle('active');

});

function sendfeedback(){
    let text = document.getElementById("feedback").value;
    let email = "sanovia.ai.feedback@gmail.com";
    let subject = "feedback";
    window.location.href=
        "mailto:"+ email+
        "?subject="+encodeURIComponent(subject)+
        "&body="+ encodeURIComponent(text);
}