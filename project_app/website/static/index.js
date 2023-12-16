const building_towns = document.querySelector('#building_town')


const towns = ['Select Building Location','Lekki','Agbara-Igbesa', 'Agege', 'Ajah', 'Alimosho', 'Amuwo Odofin', 'Apapa',
       'Ayobo', 'Badagry', 'Egbe', 'Ejigbo', 'Eko Atlantic City', 'Epe',
       'Gbagada', 'Ibeju', 'Ibeju Lekki', 'Idimu', 'Ifako-Ijaiye', 'Ijaiye',
       'Ijede', 'Ijesha', 'Ikeja', 'Ikorodu', 'Ikotun', 'Ikoyi', 'Ilupeju',
       'Imota', 'Ipaja', 'Isheri', 'Isheri North', 'Isolo', 'Ketu', 'Kosofe',
       'Lagos Island', 'Lekki', 'Magodo', 'Maryland', 'Mushin', 'Ogudu', 'Ojo',
       'Ojodu', 'Ojota', 'Oke-Odo', 'Orile', 'Oshodi', 'Shomolu', 'Surulere',
       'Victoria Island (VI)', 'Yaba']

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