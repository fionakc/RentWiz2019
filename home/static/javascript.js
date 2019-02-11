
  // var currentform = "screen1";
var currentform = "screen1";
function next() {
    // currentform = "screen1";
    var step1 = document.getElementById("progress1");
    var step2 = document.getElementById("progress2");
    var step3 = document.getElementById("progress3");
    var step4 = document.getElementById("progress4");
    var step5 = document.getElementById("progress5");
    if (currentform == "screen4"){
        step4.style.display = "none";
        step5.style.display = "block";
        currentform = "screen5";
        // alert(currentform);
    }
    if (currentform == "screen3"){
        step3.style.display = "none";
        step4.style.display = "block";
        currentform = "screen4";
        // alert(currentform);
    }
    if (currentform == "screen2"){
        step2.style.display = "none";
        step3.style.display = "block";
        currentform = "screen3";
        // alert(currentform);
    }
    if (currentform == "screen1"){
        step1.style.display = "none";
        step2.style.display = "block";
        currentform = "screen2";
        // alert(currentform);
    }
  }

  function back() {
    // currentform = "screen1";
    var step1 = document.getElementById("progress1");
    var step2 = document.getElementById("progress2");
    var step3 = document.getElementById("progress3");
    var step4 = document.getElementById("progress4");
    var step5 = document.getElementById("progress5");
    if (currentform == "screen2"){
        step2.style.display = "none";
        step1.style.display = "block";
        currentform = "screen1";
        // alert(currentform);
    }
    if (currentform == "screen3"){
        step3.style.display = "none";
        step2.style.display = "block";
        currentform = "screen2";
        // alert(currentform);
    }
    if (currentform == "screen4"){
        step4.style.display = "none";
        step3.style.display = "block";
        currentform = "screen3";
        // alert(currentform);
    }
    if (currentform == "screen5"){
        step5.style.display = "none";
        step4.style.display = "block";
        currentform = "screen4";
        // alert(currentform);
    }
  }


  function responsive() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }
// $(document).ready(function(){
//   $("button").click(function(){
//     $("p").hide();
//   });
// });

       function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#blah')
                        .attr('src', e.target.result);
                };

                reader.readAsDataURL(input.files[0]);
            }
        }

  var progressBar = {
  Bar: $('#progress-bar'),
  Reset: function () {
    if (this.Bar) {
      this.Bar.find('li').removeClass('active');
    }
  },
  Next: function () {
    $('#progress-bar li:not(.active):first').addClass('active');
  },
  Back: function () {
    $('#progress-bar li.active:last').removeClass('active');
  }
}


progressBar.Reset();


$("#Next").on('click', function () {
  progressBar.Next();
})
$("#Back").on('click', function () {
  progressBar.Back();
})
$("#Reset").on('click', function () {
  progressBar.Reset();
  subtype.style.display = "block";
  pickCut.style.display = "none";
})

