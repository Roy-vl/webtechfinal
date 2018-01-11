console.log("AH")

function disliked() {
  $(".stampD").css("display", "block");
  $(".stampD").css("opacity", "1");

  setTimeout(
  function()
  {
  $(".dislikebuttonhack").click();
}, 1000);

}

$(function() {

    $( "#draggable2" ).draggable({ revert: "invalid"}, {scroll: false});

    $( "#droppable" ).droppable({

      drop: function( event, ui ) {
        console.log("AAAAHPANEIEK")
        location.reload();
      },
      over: function(event, ui) {
        $(".btn-danger").children().addClass("fa-spin");
        $(".memepage").css("background-color", "rgb(251, 5, 5)");
        console.log("PLS");
      },
      out: function(event, ui) {
        $(".btn-danger").children().removeClass("fa-spin");
        $(".memepage").css("background-color", "rgb(255, 255, 255)");
      }
    });

    $( "#droppable2" ).droppable({

      drop: function( event, ui ) {
        location.reload();
      },
      over: function(event, ui) {
        $(".btn-success").children().addClass("fa-spin");
        $(".memepage").css("background-color", "rgb(76, 251, 5)");
        console.log("PLS");
      },
      out: function(event, ui) {
        $(".btn-success").children().removeClass("fa-spin");
        $(".memepage").css("background-color", "rgb(255, 255, 255)");
      }
    });

    $( "#droppablemob" ).droppable({


      drop: function( event, ui ) {
        location.reload();
      },
      over: function(event, ui) {
        $(".btn-success").children().addClass("fa-spin");
        $(".memepage").css("background-color", "rgb(76, 251, 5)");
        console.log("PLS");
      },
      out: function(event, ui) {
        $(".btn-success").children().removeClass("fa-spin");
        $(".memepage").css("background-color", "rgb(255, 255, 255)");
      }
    });

    $( "#droppablemob2" ).droppable({

      drop: function( event, ui ) {
        location.reload();
      },
      over: function(event, ui) {
        $(".btn-danger").children().addClass("fa-spin");
        $(".memepage").css("background-color", "rgb(251, 5, 5)");
        console.log("PLS");
      },
      out: function(event, ui) {
        $(".btn-danger").children().removeClass("fa-spin");
        $(".memepage").css("background-color", "rgb(255, 255, 255)");
      }
    });
  });

$(function(){
  $(".btn-circle").mouseenter(
    function(startspin) {
      $( this ).children().addClass("fa-spin");
      console.log("SPIN MY CHILD");
  });

  $(".btn-circle").mouseleave(
    function(stopspin) {
      $( this ).children().removeClass("fa-spin");
      console.log("STOP PLSS ITS ENOUGHHH!");
    });
});
