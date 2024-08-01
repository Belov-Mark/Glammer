function toggleDropdownMenu() {
    const catalog = document.getElementById('catalog');
    catalog.classList.toggle('hidden');
  }

  function showSubcategories(categorySlug) {
    const subcategoryList = document.getElementById('subcategoryList');
    const categoryElements = document.querySelectorAll('.categoryButton');

    // Скрыть все подкатегории
    subcategoryList.innerHTML = '';

    // Загрузить подкатегории для выбранной категории
    fetch(`/subcategories/${categorySlug}/`)
      .then(response => response.json())
      .then(data => {
        if (data.subcategories.length > 0) {
          data.subcategories.forEach(subcategory => {
            const subcategoryElement = document.createElement('a');
            subcategoryElement.href = '#'; // Замените на актуальную ссылку
            subcategoryElement.innerHTML = `${subcategory.name} &#40;${subcategory.num_products}&#41;`;
            subcategoryList.appendChild(subcategoryElement);
          });
        } else {
          subcategoryList.innerHTML = '<p>Нет подкатегорий!</p>';
        }

        // Показываем подкатегории
        subcategoryList.classList.remove('hidden');
      })
      .catch(error => console.error('Error fetching subcategories:', error));
  }