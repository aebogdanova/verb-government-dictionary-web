let btns = document.querySelectorAll(".moreLessButton");

for (btn of btns) {
    btn.addEventListener('click', function() {
        let nouns = this.closest(".nouns");
        let dots = nouns.querySelector(".dots");
        let more = nouns.querySelector(".more");

        if (dots.style.display === "none") {
            dots.style.display = "inline";
            more.style.display = "none";
            this.textContent = "Показать ещё";
        } else {
            dots.style.display = "none";
            more.style.display = "inline";
            this.textContent = "Скрыть";
        }
    });
}
