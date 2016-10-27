/*$(document).ready(function () {
	var $button = $('#hello'), click_count = 0; //button selector
	
	$button.click(function () {
		
		click_count +=1;
		
		//$('.hello-class').text('123');
		$button
		//.removeClass('btn-primary').addClass('btn-danger').text('123');
		//.toggleClass('btn-primary').toggleClass('btn-danger').text('123');
		.toggleClass('btn-primary btn-danger').text('Click count: '+click_count);
		
		
		
	});
	//alert("Hello");
	//console.log('Hi');
	
});
*/


//lower buttons

/*
$(document).ready(function () {
	var $button = $('div.row a.btn'), click_count = 0; //button selector
	
	colors = ['primary', 'success', 'info', 'warning', 'danger'];
	
	$button.click(function () {
		var $this = $(this), current_color= colors[click_count % colors.length]; //context
		click_count +=1;
		
		
		//$button
		$this
		//.toggleClass('btn-default btn-danger').text('Click count: '+click_count);
		.removeClass().addClass('btn btn-' + current_color).text('Click count: '+click_count);
		
		
		return false; //все последующие события не выполняются (в т.ч. переход по хреф)
		
	});
	//alert("Hello");
	//console.log('Hi');
	
});
*/

//hover
/*
$(document).ready(function () {
	var $button = $('div.row a.btn'), click_count = 0; //button selector
	
	colors = ['primary', 'success', 'info', 'warning', 'danger'];
	
	$button.click(function () {
		var $this = $(this), current_color= colors[click_count % colors.length]; //context
		click_count +=1;
		
		
		//$button
		$this
		//.toggleClass('btn-default btn-danger').text('Click count: '+click_count);
		.removeClass().addClass('btn btn-' + current_color).text('Click count: '+click_count);
		
		
		return false; //все последующие события не выполняются (в т.ч. переход по хреф)
		
	});
	
	$button.hover(function () {
		$(this).closest('div').find('h2').text('Hello');
		//console.log('Over');
	}, function(){
		$(this).closest('div').find('h2').text('Heading');
		//console.log('Out');
	});
	//alert("Hello");
	//console.log('Hi');
	
});
*/

$(document).ready(function () {
	var $button = $('#testajax'), click_count = 0; //button selector
	
	$button.click(function () {
		
		//click_count +=1;
		
		//$('.hello-class').text('123');
		//$button
		//.removeClass('btn-primary').addClass('btn-danger').text('123');
		//.toggleClass('btn-primary').toggleClass('btn-danger').text('123');
		//.toggleClass('btn-primary btn-danger').text('Click count: '+click_count);

	//});
	//alert("Hello");
	console.log('Hi');
	//$('#testajax').text('123');
	});
	
	$("#more").click(function(){
        $("#panel").slideDown("slow");
    });
	
	
	$("#testajax").click(function(){
    $("#forajax").load("static/ajaxfile.txt", function(responseTxt, statusTxt, xhr){
        //if(statusTxt == "success")
            //alert("External content loaded successfully!");
        if(statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
    });
	});
    $("#testajaxS").click(function(){
    $("#forajaxS").load("static/ajaxfileS.txt", function(responseTxt, statusTxt, xhr){
        //if(statusTxt == "success")
            //alert("External content loaded successfully!");
        if(statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
    });
	});
    $("#testajaxH").click(function(){
    $("#forajaxH").load("static/ajaxfileH.txt", function(responseTxt, statusTxt, xhr){
        //if(statusTxt == "success")
            //alert("External content loaded successfully!");
        if(statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
    });
});
	
	
});



