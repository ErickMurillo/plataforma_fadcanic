var dicc;

(function($) {	
	$(document).ready(function(){
		$('#add_id_comunidad').removeAttr('onclick');
		$('#add_id_comunidad').attr('href', '#');
		
		$('#id_municipio').change(function(){
			var val = $(this).val();
			var name = $('#id_municipio option:selected').text();
			if(val!=''){
				dicc = {'id': val, 'name': name}
			}
		});
		$('#add_id_comunidad').click(function(){
			if($('#id_municipio').val()==''){
				alert('Debe seleccionar un municipio');
				return false;
			}
			showCustomPopup(dicc, this);
			return false;
		});
	})
})(jQuery || django.jQuery);

function showCustomPopup(dicc, triggeringLink) {
	var name = triggeringLink.id.replace(/^add_/, '');	
	var href = '/admin/lugar/comunidad/add/?_popup=1&id='+dicc.id+'&name='+dicc.name;
	var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}

// codigo nuevo
(function($) {	
$(document).ready( function() 
	{
		var valor_tipo = $('#id_tipo').val();
			if (valor_tipo === '1' ) {
				$('.field-persona_organiza').show();
				$('.field-comite').hide();
			}else{
				$('.field-persona_organiza').hide();
				$('.field-comite').show();
			};

		$('#id_tipo').change(function(){
			var valor_tipo = $('#id_tipo').val();
			if (valor_tipo === '1' ) {
				$('.field-persona_organiza').show();
				$('.field-comite').hide();
			}else{
				$('.field-persona_organiza').hide();
				$('.field-comite').show();
			};

			if (valor_tipo === '1') {
				$(".field-comite label").empty();
				$(".field-comite label").append("Persona que organiza la actividad:");
			}else if(valor_tipo === '2'){
				$(".field-comite label").empty();
				$(".field-comite label").append("Comité comunal que organiza la actividad:");
			}else if(valor_tipo === '3'){
				$(".field-comite label").empty();
				$(".field-comite label").append("Comité municipal que organiza la actividad:");
			}else if(valor_tipo === '4'){
				$(".field-comite label").empty();
				$(".field-comite label").append("Diplomado de promotoría que organiza la actividad:");
			}else if(valor_tipo === '5'){
				$(".field-comite label").empty();
				$(".field-comite label").append("Diplomado de comunicación que organiza la actividad:");
			};
		});

	} );

$(document).on('click','#id_tipo',function(){
		var id = $(this).val();
		if (id != '1') {
			$('#id_comite').empty();
			$.ajax({
			data : {'id' : id},
			url : '/admin/comite/',
			type : 'get',
			success : function(data){
				var html = ""
				 console.log(data);
				 for (var i = 0; i < data.length; i++) {
				 	html += '<option value="'+data[i].pk+'">'+data[i].fields.nombre+'</option>'
				 };
				 $('#id_comite').html(html);
				}
			});
		};
	});

})(jQuery || django.jQuery);