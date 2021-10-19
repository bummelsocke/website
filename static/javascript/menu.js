function menuFunction() {
        var checkBox = document.getElementById("menuToggle");
        var text = document.getElementById("menu");
        var menuIcon = document.getElementById("navigationIcon");
        if (checkBox.checked == true) {
                text.style.display = "block";
                document.body.style.overflow = "hidden";
                menuIcon.style.color = "black";
        } else {
                text.style.display = "none";
                document.body.style.overflow = "auto";
        }
}
