
function employee() {
    // Get the checkbox
    var checkBox = document.getElementById("tickisworking");
    // Get the output text
    var text = document.getElementById("working");

    // If the checkbox is checked, display the output text
    if (checkBox.checked == true) {
        text.style.display = "block";
    } else {
        text.style.display = "none";
    }
}

function vehicle() {
    // Get the checkbox
    var checkBox = document.getElementById("tickvehicle");
    // Get the output text
    var vehicleform = document.getElementById("havevehicle");
    // If the checkbox is checked, display the output text
    if (checkBox.checked == true) {
        vehicleform.style.display = "block";
        alert("1");
    }
    if (checkBox.checked == false) {
        vehicleform.style.display = "none";
        // alert("3");
    }
}

function verifyCheckcar() {
    document.getElementById('driverfill').style.display = 'block';
    document.getElementById('passportfill').style.display = 'none';
}

function verifyCheckpass() {
    document.getElementById('passportfill').style.display = 'block';
    document.getElementById('driverfill').style.display = 'none';
}


  // Multi-Step Form
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the crurrent tab

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;


  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}

