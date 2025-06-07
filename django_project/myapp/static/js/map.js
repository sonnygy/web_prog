ymaps.ready(init);
function init() {
    var myMap = new ymaps.Map("map", {
        center: [55.9110488957112, 39.1857685438444],
        zoom: 15
    });

    var myPlacemark = new ymaps.Placemark([55.9110488957112, 39.1857685438444], {
        hintContent: 'Мы здесь!',
        balloonContent: 'Это наш офис.'
    });

    myMap.geoObjects.add(myPlacemark); // Добавление маркера на карту
}