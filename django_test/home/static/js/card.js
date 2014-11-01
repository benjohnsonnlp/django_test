$(document).ready(function(){
	$('input#firstcard').keyup(function(){
		tryCards();
	})
	$('input#secondcard').keyup(function(){
		tryCards();
	})
})

function tryCards(){
	var firstCard = $('input#firstcard').val()
	var secondCard = $('input#secondcard').val()
	//alert(firstCard + ' ' + secondCard);

	$.ajax({
		url:'compare',
		type: "GET",
		data: {
			firstCard: firstCard,
			secondCard: secondCard
		},
		success: function(response){
			$('#winnerName').text(response);
		}
	})
}