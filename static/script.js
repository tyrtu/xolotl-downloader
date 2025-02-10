function downloadVideo() {
    let url = document.getElementById("url").value;
    if (!url) {
        document.getElementById("message").innerText = "⚠ Please enter a URL!";
        return;
    }

    let form = document.createElement("form");
    form.method = "POST";
    form.action = "/download";

    let input = document.createElement("input");
    input.type = "hidden";
    input.name = "url";
    input.value = url;
    
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
}