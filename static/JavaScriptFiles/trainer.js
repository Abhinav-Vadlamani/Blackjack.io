function saveState() {
    const state = {
        whiteChips: document.getElementById("white-count").innerText,
        redChips: document.getElementById("red-count").innerText,
        greenChips: document.getElementById("green-count").innerText,
        blackChips: document.getElementById("black-count").innerText,
        purpleChips: document.getElementById("purple-count").innerText,
        bankroll: document.getElementById("bankroll").innerText.replace('Bankroll: $', '')
    };
    localStorage.setItem('trainerState', JSON.stringify(state));
}

function loadState() {
    const savedState = localStorage.getItem('trainerState');
    if (savedState) {
        const state = JSON.parse(savedState);
        document.getElementById("white-count").innerText = state.whiteChips;
        document.getElementById("red-count").innerText = state.redChips;
        document.getElementById("green-count").innerText = state.greenChips;
        document.getElementById("black-count").innerText = state.blackChips;
        document.getElementById("purple-count").innerText = state.purpleChips;
        document.getElementById("bankroll").innerText = `Bankroll: $${state.bankroll}`;
        return true;
    }
    return false;
}

function saveStateAndNavigate(path) {
    saveState();
    window.location.href = path;
}

// Show the modal when the page loads
window.onload = async function() {
    const hasState = loadState();

    // Check current bankroll from database
    try {
        const response = await fetch('/current_bankroll');
        const data = await response.json();
        
        // Show modal if either localStorage is empty OR bankroll is 0/empty in database
        if (!hasState || data.bankroll === 0) {
            document.getElementById("moneyModal").style.display = "flex";
        } else {
            // If we have data, update the display
            document.getElementById('bankroll').innerText = `Bankroll: $${data.bankroll}`;
        }
    } catch (error) {
        console.error("Error checking bankroll:", error);
        // If there's an error fetching from database, show modal
        document.getElementById("moneyModal").style.display = "flex";
    }
};

async function fetchBankroll() {
    const response = await fetch('/current_bankroll');
    const data = await response.json();
    document.getElementById('bankroll').innerText = `Bankroll: $${data.bankroll}`;
    saveState();
}

// Handle the submit button click
document.getElementById("submitMoney").onclick = function() {
    const moneyAmount = document.getElementById("moneyInput").value;
    if (moneyAmount && moneyAmount > 0) {
        errorMessage.style.display = "none";

        fetch('/calculate_chips', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({amount: parseInt(moneyAmount)})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok')
            }
            return response.json()
        })
        .then(data => {
            console.log("Chip Counts:", data);
            document.getElementById("white-count").innerText = data.white_chips;
            document.getElementById("red-count").innerText = data.red_chips;
            document.getElementById("green-count").innerText = data.green_chips;
            document.getElementById("black-count").innerText = data.black_chips;
            document.getElementById("purple-count").innerText = data.purple_chips;
            fetchBankroll();
            saveState();
        })
        .catch(error => {
        console.error("Error:", error);
        });
        document.getElementById("moneyModal").style.display = "none";
    } else {
        errorMessage.style.display = "block";
    }
};

function showLogoutModal() {
    document.getElementById("logoutModal").style.display = "block";
}

// Hide the logout confirmation modal
function hideLogoutModal() {
    document.getElementById("logoutModal").style.display = "none";
}

// Confirm logout
function confirmLogout() {
    // Redirect to the logout route
    localStorage.removeItem('trainerState');
    window.location.href = "/logout";
}

document.getElementById("addBankrollBtn").onclick = function() {
    document.getElementById("bankrollModalOverlay").style.display = "flex";
};

// Submit bankroll button click handler
document.getElementById("submitBankroll").onclick = function() {
    const additionalAmount = document.getElementById("bankrollInput").value;

    if (additionalAmount && additionalAmount > 0) {
        fetch('/update_bankroll', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({additional_amount: parseInt(additionalAmount)})
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error("Error updating bankroll:", data.error);
            } else {
                // Update chip counts on the screen
                document.getElementById("white-count").innerText = data.white_chips;
                document.getElementById("red-count").innerText = data.red_chips;
                document.getElementById("green-count").innerText = data.green_chips;
                document.getElementById("black-count").innerText = data.black_chips;
                document.getElementById("purple-count").innerText = data.purple_chips;

                fetchBankroll();
            }
        })
        .catch(error => console.error("Error:", error));

        // Hide the modal
        document.getElementById("bankrollModalOverlay").style.display = "none";
    }
};

// Cancel bankroll modal
document.getElementById("cancelBankroll").onclick = function() {
    document.getElementById("bankrollModalOverlay").style.display = "none";
};

// chip button pressed
function buttonPressed(typeButton){
    console.log(typeButton)
    fetch('/chip_pressed', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({button_type: typeButton})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok')
        }
        return response.json()
    })
    .then(data => {
        console.log("Chip Counts:", data);
        document.getElementById("white-count").innerText = data.white_chips;
        document.getElementById("red-count").innerText = data.red_chips;
        document.getElementById("green-count").innerText = data.green_chips;
        document.getElementById("black-count").innerText = data.black_chips;
        document.getElementById("purple-count").innerText = data.purple_chips;
        fetchBankroll();
        saveState();
    })
    .catch(error => {
        console.error("Error:", error);
    });
};

// white chip
document.getElementById("white-chip").onclick = function () {
    buttonPressed("white")
};

// red chip
document.getElementById("red-chip").onclick = function () {
    buttonPressed("red")
};

// green chip
document.getElementById("green-chip").onclick = function () {
    buttonPressed("green")
};

// black chip
document.getElementById("black-chip").onclick = function () {
    buttonPressed("black")
};

// purple chip
document.getElementById("purple-chip").onclick = function () {
    buttonPressed("purple")
};