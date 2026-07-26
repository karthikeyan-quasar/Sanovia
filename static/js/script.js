const micButton = document.getElementById("microphone");
const micContainer = document.querySelector(".mic")
const responseText = document.getElementById("responsetext");
const recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();
const generation = document.getElementById("generation")
recognition.lang = "en-US";
recognition.interimResults = false;

recognition.maxAlternatives = 1;



micButton.onclick = function(){
    micContainer.classList.add("active");
    recognition.start();
}

recognition.onresult = async function(event){
    const spokenText = event.results[0][0].transcript;
    responseText.value = spokenText;
};

recognition.onend = () =>{
    micContainer.classList.remove("active");
};
recognition.onerror = () =>{
    micContainer.classList.remove("active");
};
const navbarToggle = document.querySelector('.navbar-toggle');
const navbarMenu = document.querySelector('.navbar-menu');

navbarToggle.addEventListener('click', () => {
    navbarToggle.classList.toggle('active');
    navbarMenu.classList.toggle('active');

});

sendResponse = async () => {
    const Text = responseText.value;
    try{

        const response = await fetch("/process",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                text:Text
            })

        });

        const data = await response.json();

        generation.innerHTML = data.result;

    }

    catch(error){

        responseText.innerHTML = "Server Error";
    }
};