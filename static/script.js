const video = document.getElementById("video");
const canvas = document.getElementById("canvas");

let currentPrediction = "";
let sentence = "";

navigator.mediaDevices.getUserMedia({
    video:true
})
.then(stream=>{
    video.srcObject = stream;
});

async function sendFrame(){

    const ctx = canvas.getContext("2d");

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    ctx.save();

    ctx.scale(-1, 1);

    ctx.drawImage(
        video,
        -canvas.width,
        0,
        canvas.width,
        canvas.height
    );

    ctx.restore();

    const image = canvas.toDataURL("image/jpeg");

    const response = await fetch("/predict",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            image:image
        })

    });

    const data = await response.json();

    currentPrediction = data.prediction;

    document.getElementById(
        "prediction"
    ).innerText = currentPrediction;

}

setInterval(sendFrame,200);

function addLetter(){

    sentence += currentPrediction;

    document.getElementById(
        "sentence"
    ).innerText = sentence;
}

function addSpace(){

    sentence += " ";

    document.getElementById(
        "sentence"
    ).innerText = sentence;
}

function clearSentence(){

    sentence = "";

    document.getElementById(
        "sentence"
    ).innerText = sentence;
}

function backspaceSentence(){

    sentence = sentence.slice(0,-1);

    document.getElementById(
        "sentence"
    ).innerText = sentence;
}