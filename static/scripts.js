// checks if password and confirm password are same or not
function validate_password() {
  var pass = document.getElementById("password").value;
  var confirm_pass = document.getElementById("cnf_password").value;
  var createButton = document.getElementById("submit-button");

  if (pass !== confirm_pass) {
    document.getElementById("wrong_pass_alert").style.color = "red";
    document.getElementById("wrong_pass_alert").innerHTML =
      "Password and Confirm Password are different";
    // createButton.disabled = true;
    // createButton.style.opacity = 0.4;
  } else {
    document.getElementById("wrong_pass_alert").style.color = "green";
    document.getElementById("wrong_pass_alert").innerHTML = "Password Matched";
    // createButton.disabled = false;
    // createButton.style.opacity = 1;
  }
}

// to check if adress is longer than 15 words or not
function countwords() {
  let res = [];
  let str = document
    .querySelector("#address")
    .value.replace(/[\t\n\r\.\?\!]/gm, " ")
    .split(" ");
  str.map((s) => {
    let trimStr = s.trim();
    if (trimStr.length > 0) {
      res.push(trimStr);
    }
  });
  if (res.length < 15) {
    document.getElementById("short_add").style.color = "red";
    document.getElementById("short_add").innerHTML =
      "Address should be longer than 15 words";
  } else {
    document.getElementById("short_add").innerHTML = "";
  }
}
function ValidateEmail(inputText) {
  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  if (inputText.value.match(mailformat)) {
    alert("Valid email address!");
    document.form1.text1.focus();
    return true;
  } else {
    alert("You have entered an invalid email address!");
    document.form1.text1.focus();
    return false;
  }
}

// verifies that minimum 1 checkbox must be checked
function checkifbox() {
  var f1Checked = document.getElementById("f1").checked;
  var wrcChecked = document.getElementById("wrc").checked;
  var dkrChecked = document.getElementById("dkr").checked;
  var otrChecked = document.getElementById("otr").checked;
  var createButton = document.getElementById("submit-button");
  var flag = "";
  if (!f1Checked && !wrcChecked && !dkrChecked && !otrChecked) {
    // createButton.disabled = true;
    // createButton.style.opacity = 0.4;
    flag = true;
  } else {
    // createButton.disabled = false;
    createButton.style.opacity = 1;
    flag = false;
  }
  if (flag == true) {
    document.getElementById("tick_hobby").style.color = "red";
    document.getElementById("tick_hobby").innerHTML =
      "Please check at least one checkbox for Hobbies";
  } else {
    document.getElementById("tick_hobby").innerHTML = "";
  }
}
