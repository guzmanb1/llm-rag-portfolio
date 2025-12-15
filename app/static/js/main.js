async function sendQuestion() {
    const question = document.getElementById("question").value;
    const responseBox = document.getElementById("response");

    responseBox.innerHTML = "Pensando...";

    const res = await fetch("/api/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ question })
    });

    const data = await res.json();
    responseBox.innerHTML = data.answer;
}
