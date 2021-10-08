function menuFunction() {
        var checkBox = document.getElementById("menuToggle");
        var text = document.getElementById("menu");

        if (checkBox.checked == true) {
                text.style.display = "block";
        } else {
                text.style.display = "none";

        }
}
