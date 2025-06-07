document.getElementById('sign-up__form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const car = document.getElementById('car').value;
    const year = document.getElementById('year').value;
    const service = document.getElementById('service').value;
    const comment = document.getElementById('comment').value;
    const time = document.getElementById('time').value;
    const notification = document.getElementById('notification').value;

    let isValid = true;

    if (!/^[A-ZА-ЯЁ][a-zа-яё]+$/.test(name)) {
        document.getElementById('nameError').innerText = 'Имя должно начинаться с заглавной буквы и содержать только буквы!';
        isValid = false;
    } else {
        document.getElementById('nameError').innerText = '';
    }

    if (!/^\+?[0-9]{10,15}$/.test(phone)) {
        document.getElementById('phoneError').innerText = 'Введите корректный номер телефона (10-15 цифр, может начинаться с +)!';
        isValid = false;
    } else {
        document.getElementById('phoneError').innerText = '';
    }

    if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').innerText = 'Введите корректный email!';
        isValid = false;
    } else {
        document.getElementById('emailError').innerText = '';
    }

    if (year < 1900 || year > new Date().getFullYear()) {
        document.getElementById('yearError').innerText = 'Введите корректный год выпуска!';
        isValid = false;
    } else {
        document.getElementById('yearError').innerText = '';
    }

    if (isValid) {
        document.getElementById('responseMessage').innerText = 'Форма успешно отправлена!';
    } else {
        document.getElementById('responseMessage').innerText = 'Пожалуйста, исправьте ошибки в форме!';
    }
});