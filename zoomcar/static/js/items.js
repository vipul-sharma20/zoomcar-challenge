$(document).ready(function(){
    $(".content").hide();
    $("[name='item']").click(function(e){
        $("[name='extended']").hide();
        e.preventDefault();
        var lat = $(this).attr("lat");
        var lng = $(this).attr("lng");
        var t = $(this).attr("canvas");
        $("[id="+t+"]").show();
        var map_id = "id_"+t;
        function initialize() {
  var mapProp = {
    center:new google.maps.LatLng(lat,lng),
    zoom:5,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById(map_id),mapProp);
}
google.maps.event.addDomListener(window, 'load', initialize);

var newYear = new Date(); 
newYear = new Date(newYear.getFullYear() + 1, 1 - 1, 1); 
$('#defaultCountdown').countdown({until: newYear}); 
 
    $('#removeCountdown').click(function() { 
            var destroy = $(this).text() === 'Remove'; 
                $(this).text(destroy ? 'Re-attach' : 'Remove'); 
                    $('#defaultCountdown').countdown(destroy ? 'destroy' : {until: newYear}); 
    });

	});
});
