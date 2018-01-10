console.log("AH")

$(function() {

    $( "#draggable2" ).draggable({ revert: "invalid" });

    $( "#droppable" ).droppable({
      activeClass: "ui-state-default",
      hoverClass: "ui-state-hover",
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "p" )
            .html( "Dropped!" );
      }
    });

    $( "#droppable2" ).droppable({
      activeClass: "green",
      hoverClass: "ui-state-hover",
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "p" )
            .html( "Dropped!" );
      }
    });

    $( "#droppablemob" ).droppable({
      activeClass: "green",
      hoverClass: "ui-state-hover",
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "p" )
            .html( "Dropped!" );
      },
      over: function(event, ui) {
        $(".btn-success").children().addClass("fa-spin");
        console.log("PLS");
      },
      out: function(event, ui) {
        $(".btn-success").children().removeClass("fa-spin");
      }
    });

    $( "#droppablemob2" ).droppable({
      activeClass: "green",
      hoverClass: "ui-state-hover",
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "p" )
            .html( "Dropped!" );
      },
      over: function(event, ui) {
        $(".btn-danger").children().addClass("fa-spin");
        $(".btn-danger").toggle("explode", {pieces: 100}, 10000);
        console.log("PLS");
      },
      out: function(event, ui) {
        $(".btn-danger").children().removeClass("fa-spin");
        $(".btn-danger").toggle("explode", {pieces: 100}, 10000);
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
