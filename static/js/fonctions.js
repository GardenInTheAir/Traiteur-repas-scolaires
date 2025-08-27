var parent = document.getElementById("parent");

parent.onfocus = function() {
  document.getElementById("message-nom-parent").style.display = "block";
};

parent.onblur = function() {
  document.getElementById("message-nom-parent").style.display = "none";
};

var enfant = document.getElementById("enfant");

enfant.onfocus = function() {
  document.getElementById("message-nom-enfant").style.display = "block";
};
  
enfant.onblur = function() {
  document.getElementById("message-nom-enfant").style.display = "none";
};

var age = document.getElementById("age");

age.onfocus = function() {
  document.getElementById("message-age").style.display = "block";
};

age.onblur = function() {
  document.getElementById("message-age").style.display = "none";
};

var ecole = document.getElementById("ecole");

ecole.onfocus = function() {
  document.getElementById("message-nom-ecole").style.display = "block";
};
  
ecole.onblur = function() {
  document.getElementById("message-nom-ecole").style.display = "none";
};
