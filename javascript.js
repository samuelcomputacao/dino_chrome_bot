var div = document.getElementsByClassName('bar-item last info')[0];
var ng = div.getElementsByTagName('ng-component')[0];
var a = ng.getElementsByClassName('account-type')[0];
var p = a.getElementsByTagName('p')[1];
var montante = p .innerText;

var montanteAntigo = parseFloat(montante.substring(3))*1000;

var sair = 0;
while(sair==0){
    var div1 = document.getElementsByClassName('bar-item last info')[0];
    var ng1 = div1.getElementsByTagName('ng-component')[0];
    var a1 = ng1.getElementsByClassName('account-type')[0];
    var p1 = a1.getElementsByTagName('p')[1];
    var montante1 = p1 .innerText;
    var montanteAtual = parseFloat(montante1.substring(3))*1000;
    if((montanteAtual-montanteAntigo) > 200){
        sair=1;
    }
}
if(sair>0){
window.open('https://globoesporte.globo.com/', '_blank');
}