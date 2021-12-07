let element = document.querySelector('.formulario');

function analisar(n){
  
  //Temperatura
  if (n === '1'){
    var valorUm = document.querySelector('#valorUm').value;
    let deTemp = document.querySelector('#deTemp').value;
    let paraTemp = document.querySelector('#paraTemp').value;

      if (valorUm === ''){
          alert("Você não digitou nada!");
      }
      else if (deTemp === '0'){
          alert("Campo QUERO CONVERTER vazio!");
      }
      else if (paraTemp === '0'){
        alert("Campo PARA vazio!");
      }
      else{
        element.setAttribute('action','cgi-bin/result.py');
        element.setAttribute('method','post');
      }
  }

  //Comrprimento
  else if (n === '2'){
    var valorDois = document.querySelector('#valorDois').value;
    let deComp = document.querySelector('#deComp').value;
    let paraComp = document.querySelector('#paraComp').value;

    if (valorDois === ''){
        alert("Você não digitou nada!");
    }
    else if (deComp === '0'){
        alert("Campo QUERO CONVERTER vazio!");
    }
    else if (paraComp === '0'){
      alert("Campo PARA vazio!");
    }else{
      element.setAttribute('action','cgi-bin/result.py');
      element.setAttribute('method','post');
    }
  }

  //Massa
  else if (n === '3'){
    var valorTres = document.querySelector('#valorTres').value;
    let deMassa = document.querySelector('#deMassa').value;
    let paraMassa = document.querySelector('#paraMassa').value;

    if (valorTres === ''){
        alert("Você não digitou nada!");
    }
    else if (deMassa === '0'){
        alert("Campo QUERO CONVERTER vazio!");
    }
    else if (paraMassa === '0'){
      alert("Campo PARA vazio!");
    }
    else{
      element.setAttribute('action','cgi-bin/result.py');
      element.setAttribute('method','post');
    }
  }
}
