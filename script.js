


async function checkBMI() {
    let n = document.getElementById("Name").value;
    let a = document.getElementById("Age").value;
    let g = document.getElementById("Gender").value;
    let p = document.getElementById("Phno").value;
    let w = document.getElementById("Weight").value;
    let h = document.getElementById("Height").value;

    if (n === "" || a === "" || g === "" || w === "" || h === "") {
        alert("Please Enter All Required Details");
        return;
    }

    let data = {
        name: n,
        age: Number(a),
        gender: g,
        phone: p,
        weight: Number(w),
        height: Number(h)
    };

    let response = await fetch("http://127.0.0.1:8000/Details", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    let result = await response.json();

    sessionStorage.setItem("userDetails", JSON.stringify(data));
    sessionStorage.setItem("bmiResult", JSON.stringify(result));

    window.location.href = "Result.html";
}
