async function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const uploadSection = document.getElementById("upload-section");
    const questionInput = document.getElementById("question");
    const sendBtn = document.getElementById("sendBtn");
    const responseBox = document.getElementById("response");

    if (!fileInput.files.length) {
        alert("Selecciona un archivo primero");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    responseBox.innerHTML = "Procesando documento...";

    const res = await fetch("/api/upload", {
        method: "POST",
        body: formData
    });

    if (!res.ok) {
        responseBox.innerHTML = "Error al procesar el documento";
        return;
    }

    // Documento cargado correctamente
    uploadSection.style.display = "none";
    questionInput.disabled = false;
    sendBtn.disabled = false;

    responseBox.innerHTML = "Documento cargado. Ya puedes hacer preguntas.";
}

async function sendQuestion() {
    const questionInput = document.getElementById("question");
    const responseBox = document.getElementById("response");
    const question = questionInput.value.trim();

    if (!question) return;

    responseBox.innerHTML = "Pensando...";

    const res = await fetch("/api/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ question })
    });

    const data = await res.json();
    responseBox.innerHTML = data.answer;
}
