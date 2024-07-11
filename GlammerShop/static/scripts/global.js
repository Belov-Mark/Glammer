function toggleDropdownMenu(menuId) {
    var menu = document.getElementById(menuId);
    var computedStyle = window.getComputedStyle(menu);

    if (computedStyle.display === "flex" || computedStyle.display === "none") {
        menu.style.display = (computedStyle.display === "flex") ? "none" : "flex";
    } else {
        menu.style.display = "flex";
    }

    // Переключение анимации иконки бургера, если menuId равен 'catalog'
    if (menuId === "catalog") {
        var burgerIcon = document.getElementById("burgerIcon");
        burgerIcon.classList.toggle("open");
    }

    function changeCity(cityName) {
        if (cityName === 'Москва') {
            document.getElementById('currentCity').innerText = cityName;
            document.getElementById('cityMenu').style.display = 'none';
        } else if (cityName === 'Московская область') {
            document.getElementById('currentCity').innerText = 'Моск. обл.';
            document.getElementById('cityMenu').style.display = 'none';
        }
    }
    
    // Публикация функций, чтобы они были доступны из других скриптов
    window.toggleDropdownMenu = toggleDropdownMenu;
    window.changeCity = changeCity;
}