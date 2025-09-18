// This is the main JavaScript file to call the backend Python file.
// Calling to Python file when the fortune get button is pressed.
document.getElementById("getFortuneBtn").addEventListener("click", async () => {
    const fortuneElem = document.getElementById("fortune");
    //Loading message while calling the Flask.
    fortuneElem.innerText = "🤔 Thinking your fortune...";
    // Using the try catch method to safely call the backend files.
    try {
        const response = await fetch("http://127.0.0.1:5000/get_fortune");
        const data = await response.json();
        fortuneElem.innerText = data.fortune;
    } catch (error) {
        fortuneElem.innerText = "So Sorry! Something went wrong.";
        console.error(error);
    }
});
