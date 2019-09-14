window.addEventListener('load', () => {
    let long;
    let lat;
    let tempdegree = document.querySelector(".degree");
    let locationtime = document.querySelector(".location-timezone");

    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            long = position.coords.longitude;
            lat = position.coords.latitude;

            const proxy = 'https://cors-anywhere.herokuapp.com/';
            const api = proxy+'https://api.darksky.net/forecast/e7d8d22d4d7468930b5ffc9d4cb56a9e/'+lat+','+long;

            fetch(api)
                .then(response => {
                    return response.json();
            })
                .then(data => {
                    console.log(data);
                    const {temperature} = data.currently;
                    tempdegree.textContent = temperature;
                    locationtime.textContent = data.timezone;
            });
        });
    };
});