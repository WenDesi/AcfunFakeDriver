
data = wds;
$.each(data,function(infoIndex,info){
	one_row = MakeOneRow(info)
	$('#tbody').append(one_row)
});


function MakeOneRow(json)
{
	html = '<div class="row"><div class="col-md-1"><p>'
	html += json['cid'] + '</p></div><div class="col-md-9"><p>'
	html += json['content'] + '</p></div><div class="col-md-2">'
	html += '<button class="yes">Y</button><button class="wrong">N</button></div></div>'
	return html
}