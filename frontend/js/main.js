fetch("http://localhost:5000/api/mood")
    .then(response => response.json())
    .then(data => {
        document.getElementById("mood").textContent = data.mood;
    })
    .catch(() => {
        document.getElementById("mood").textContent = "Error loading mood";
    });