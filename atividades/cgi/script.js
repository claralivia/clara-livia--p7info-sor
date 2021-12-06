let select = document.querySelector('deTemp');
let select2 = document.querySelector('paraTemp');
let valor = document.querySelector('valor');
let para = document.querySelector('p');

select.addEventListener('change', setWeather);
select2.addEventListener('change', setWeather);
let valorFinal = 0;

function setWeather() {
  var choice = select.value;
  var choice2 = select2.value;

  if (choice === 'Celsius') {
    if (choice2 === 'Celsius') {
        valorFinal == valor*2;
        para.textContent = valorFinal;
    } else if (choice2 === 'Fahrenheit'){
        valorFinal == valor*3;
        para.textContent = 'Olá';
    }else {
        valorFinal == valor*2;
        para.textContent = valorFinal;
    }
  } else if (choice === 'Fahrenheit') {
    para.textContent = 'Rain is falling outside; take a rain coat and a brolly, and don\'t stay out for too long.';
  } else{
    para.textContent = 'The snow is coming down — it is freezing! Best to stay in with a cup of hot chocolate, or go build a snowman.';
  }}
