$(document).ready(function(){
  show = false;

  $(".hidden").hide();
  $('a').click(function(e) { window.open($(this).attr('href'),'_blank'); return false;});

  var menu = document.getElementById('menu'),
      showcode = document.getElementById('showcode');

  showcode.addEventListener('click', _toggleCode);
  function _toggleCode() {
    menu.classList.toggle('viewCode');
    if (show) {
      $(".hidden").hide();
      $(".visible").show("slow");
    } else {
      $(".hidden").show("slow");
      $(".visible").hide();
    }
    show = !show;
  }
});
