// const token = '5897db64d0634bc43bfbfffb738fd1b7ed0104da';
// // parameters = {
// //     "lat": '39.95',
// //     "lon": '-75.16',
// //     "limit": '10'
// // };
// fetch('https://app.climate.azavea.com/api/city/nearest/?lat=39.95&lon=-75.16&limit=10', {
//   headers: {
//     Authorization: `token ${token}`
//   }
// })
//   .then(res => res.json())
//   .then(json => console.log(json));
var p1 = 'user?'
var p2 = 'limit=10'
fetch('https://dummyapi.io/data/api/'+p1+p2,{
    headers: {
        'app-id': '5fb24b43de49cf803f3eb1e4'
    }
})
    .then(res => res.json())
    .then(json => console.log(json));
const friend = {
    name: {
        first: 'jim',
        last: 'jon'
    },
    age: 40,
    gender: 'male',
    location: {
        city: 'Reading',
        country: 'usa',
        address: '100 main st'
    }
};
var val1 = friend.name.first;
console.log(val1);

document.querySelector('#output').textContent = friend.location.country;

