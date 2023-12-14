const building_towns = document.querySelector('#building_town')


const towns = ['Select Building Location','Lekki',
'Ajah',
'Ikoyi',
'Alimosho',
'Magodo',
'Ibeju Lekki',
'Idimu',
'Ikeja',
'Gbagada',
'Ilupeju',
'Victoria Island (VI)',
'Isheri North',
'Ikotun',
'Surulere',
'Ikorodu',
'Ijaiye',
'Kosofe',
'Isolo',
'Ipaja',
'Eko Atlantic City',
'Isheri',
'Ifako-Ijaiye',
'Yaba',
'Ogudu',
'Ejigbo',
'Lagos Island',
'Ojo',
'Agege',
'Ojodu',
'Shomolu',
'Amuwo Odofin',
'Ayobo',
'Apapa',
'Epe',
'Maryland']


building_towns.innerHTML = towns.map(town => `<option value="${town}">${town}</option>`).join('')

let formEl = document.getElementById('build-form');

formEl.addEventListener('submit', async function(e){
    e.preventDefault();

    let selectedBuilding = document.getElementById('building_title');
    let selectedTown = document.getElementById('building_town');
    let seletedNumbersofBedrooms = document.getElementById('bedrooms');
    let seletedNumbersofBathrooms = document.getElementById('bathrooms');
    let seletedNumbersofToilets = document.getElementById('toilets');
    let seletedNumbersofParkingSpace = document.getElementById('parking_space');
    let price_slot = document.getElementById('price_slot');
    let price_div = document.getElementById('price_div');

    const fetcher = async () => {
    
        const result = await fetch('/getformdata', {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                bedrooms : seletedNumbersofBedrooms.value,
                bathrooms : seletedNumbersofBathrooms.value,
                toilets : seletedNumbersofToilets.value,
                parking_space : seletedNumbersofParkingSpace.value,
                title : selectedBuilding.value,
                town : selectedTown.value,
             })
        })

        return result.json();
    }
        const res = await fetcher();
        // console.log(res.data);
        // res.data ? price_slot.className = 'block' : price_slot.className = 'hidden'
        price_div.className = res.data ? 'block' : 'hidden'
        price_slot.innerHTML = res.data;
    // .then((res) => {
    //     console.log(res.json());
    // })
    // .catch((err) => {
    //     console.log(`Error: ${err}`);
    // })
})