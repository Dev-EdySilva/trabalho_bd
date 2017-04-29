 var fieldsVal = document.querySelectorAll('[money-mask]');
 var fieldsPhone = document.querySelectorAll('[fone-mask]');
 var fieldsCPF = document.querySelectorAll('[cpf-mask]');
 var fieldsHour = document.querySelectorAll('[hour-mask]');
 var fieldsCep = document.querySelectorAll('[cep-mask]');
 var fieldsDate = document.querySelectorAll('[date-mask]');
 

 console.log(fieldsHour);


var hourMask = function(e){
    
    var s = this.value;
    s = s.replace(/\D/g, '');
    s = s.replace(/^(\d\d)(\d)/,"$1:$2");
      
    
    this.value = s.substring(0, 5);

    
};


var checkHour = function(e){
    var v = this.value;
    
    var aux = v.split(":").map(function(item){
        return parseInt(item);
    });
    
    
    if( !( aux[0] >= 0 && aux[0] < 24 ) || !( aux[1] >= 0 && aux[1] < 60 ) ){
        this.value = "";
    }
    
};

    for(var i=0; i< fieldsHour.length; i++){
        fieldsHour[i].addEventListener("input", hourMask, false);
        fieldsHour[i].addEventListener("blur", checkHour, false);
    };

      for (var i = 0; i < fieldsPhone.length; i++) {
        fieldsPhone[i].addEventListener("input",function(e){

          var s = this.value;
          s = s.replace(/\D/g, '');
          s = s.replace(/^(\d\d)(\d)/, "($1) $2");
          s = s.replace(/(\d\d\d\d)(\d)/, "$1 - $2");

          if(s.length >= 17){
            s = s.replace(/\D/g, '');
            s = s.replace(/^(\d\d)(\d)/, "($1) $2");
            s = s.replace(/(\d\d\d\d\d)(\d)/, "$1 - $2");

          }

          s = s.substring(0, 17);

        


          this.value = s;


        }, false);
      }

      for (var i = 0; i < fieldsVal.length; i++) {
          fieldsVal[i].addEventListener("input", function(e){
            
            e.preventDefault();

            var s = this.value.replace(/\D/g, '');
            //v=v.replace(/\D/g,"") // permite digitar apenas numero
            // s=s.replace(/(\d{1})(\d{14})$/,"$1.$2") // coloca ponto antes dos ultimos digitos
            // s=s.replace(/(\d{1})(\d{11})$/,"$1.$2") // coloca ponto antes dos ultimos 11 digitos
            // s=s.replace(/(\d{1})(\d{8})$/,"$1.$2") // coloca ponto antes dos ultimos 8 digitos
            // s=s.replace(/(\d{1})(\d{5})$/,"$1.$2") // coloca ponto antes dos ultimos 5 digitos
            s=s.replace(/(\d{1})(\d{1,2})$/,"$1.$2") // coloca virgula antes dos ultimos 2 digitos
            this.value = s;

          }, false);
      };



      var onlyNumberMask = function(){
      	var s = this.value.replace(/\D/g, '');
      	this.value = s;
      };


      var cepMask = function(){
        var s = this.value.replace(/\D/g, '');
        s = s.replace(/(\d{2})(\d)/, "$1.$2"); // 11.1
        s = s.replace(/(\d{3})(\d)/, "$1-$2"); // 99.999-9

        this.value = s.substring(0,10);
      };

      var cpfMask = function(){
      	var s = this.value.replace(/\D/g, '');
      	s=s.replace(/(\d{3})(\d)/, "$1.$2");
      	s=s.replace(/(\d{3})(\d)/, "$1.$2");
      	s=s.replace(/(\d{3})(\d)/, "$1-$2");


      	this.value = s.substring(0,14);
      };


      var dateMask = function(){
          var s = this.value.replace(/\D/g, '');
          s = s.replace(/(\d{2})(\d)/, "$1/$2"); // ##/#
          s = s.replace(/(\d{2})(\d)/, "$1/$2"); // ##/##/#

          this.value = s.substring(0,10);
      };


      var fieldsNumber = document.querySelectorAll('[only-number-mask]');
      var fieldsCPF = document.querySelectorAll('[cpf-mask]');


      for (var i = 0; i < fieldsDate.length; i++) {
        fieldsDate[i].addEventListener('input', dateMask, false);
      }

      for (var i = 0; i < fieldsCep.length; i++) {
        fieldsCep[i].addEventListener('input', cepMask, false);
      }

      for (var i = 0; i < fieldsNumber.length; i++) {
      	fieldsNumber[i].addEventListener('input', onlyNumberMask, false);
      }

      for (var i = 0; i < fieldsCPF.length; i++) {
      	fieldsCPF[i].addEventListener('input', cpfMask, false);
      }