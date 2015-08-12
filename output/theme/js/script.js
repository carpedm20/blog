$(document).ready(function(){
  show = false;
  $(".hidden").hide();
  var menu = document.getElementById('menu'),
      showcode = document.getElementById('showcode');

  showcode.addEventListener('click', _toggleCode);
  function _toggleCode() {
    menu.classList.toggle('viewCode');
    if (show) {
      $(".hidden").hide();
      $(".visible").show();
    } else {
      $(".hidden").show();
      $(".visible").hide();
    }
    show = !show;
  }
});
