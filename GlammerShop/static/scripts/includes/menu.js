function toggleDropdownMenu(menuId) {
    var menu = document.getElementById(menuId);
    
    if (!menu) {
        console.error('Menu element not found.');
        return;
    }

    var computedStyle = window.getComputedStyle(menu);

    if ((computedStyle.display === "flex" || computedStyle.display === "none") && (computedStyle.opacity === "0" || computedStyle.opacity === "1")) {
        menu.style.display = (computedStyle.display === "flex") ? "none" : "flex";
        menu.style.opacity = (computedStyle.opacity === "1") ? "0" : "1";

    } else {
        menu.style.display = "flex";
        menu.style.opacity = "1";
    }

    // Toggle burger icon animation if menuId is 'catalog'
    if (menuId === "catalog") {
        var burgerIcon = document.getElementById("burgerIcon");
        if (burgerIcon) {
            burgerIcon.classList.toggle("open");
        }
    }
}


function changeCity(cityName) {
    document.getElementById('currentCity').innerText = cityName;
    var cityMenu = document.getElementById('cityMenu');
    if (cityMenu) {
        cityMenu.style.display = 'none';
    } else {
        console.error('City menu element not found.');
    }
}

// Publish functions to make them accessible from other scripts
window.toggleDropdownMenu = toggleDropdownMenu;
window.changeCity = changeCity;