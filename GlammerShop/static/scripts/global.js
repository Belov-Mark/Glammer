function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdownContent");
    var burgerIcon = document.getElementById("burgerIcon");

    // Переключение класса для анимации иконки бургера
    burgerIcon.classList.toggle("open");

    // Переключение отображения выпадающего меню
    if (dropdownContent.style.display === "flex") {
        dropdownContent.style.display = "none";
    } else {
        dropdownContent.style.display = "flex";
    }
}