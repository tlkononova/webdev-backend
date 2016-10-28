$(document).ready(function () {
	
	var $button = $('#testajax'), click_count = 0; //button selector
	$button.click(function () {
		console.log('Click');
	});
	
	//slide up and down more info
	$("#more").click(function(){
        $("#panel").slideDown("slow");
    });
	
	$("#notmore").click(function(){
        $("#panel").slideUp("slow");
    });
	
	//Ajax for help
	$("#testajax").click(function(){
    $("#forajax").load("static/ajaxfile.txt", function(responseTxt, statusTxt, xhr){
        if(statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
		});
	});
	//Ajax for Saadi
    $("#testajaxS").click(function(){
		$("#forajaxS").load("static/ajaxfileS.txt", function(responseTxt, statusTxt, xhr){
			if(statusTxt == "error")
				alert("Error: " + xhr.status + ": " + xhr.statusText);
		});
	});
	//Ajax for Hafiz
    $("#testajaxH").click(function(){
		$("#forajaxH").load("static/ajaxfileH.txt", function(responseTxt, statusTxt, xhr){
			if(statusTxt == "error")
				alert("Error: " + xhr.status + ": " + xhr.statusText);
		});
	});
});



