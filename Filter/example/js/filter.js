
data = wds;
result = [];

$.each(data,function(infoIndex,info){
	one_row = MakeOneRow(info)
	$('#tbody').append(one_row)
});

$('li').on('click',function(){
	select_radio(this);
})


function MakeOneRow(json)
{
	html = '<div class="row"><div class="col-md-1"><p>'
	html += json['cid'] + '</p></div><div class="col-md-9"><p>'
	html += json['content'] + '</p></div><div class="col-md-2"><form><ul class="dowebok">'
	html += '<li><input type="radio" name="radio" data-labelauty="Y"></li><li><input type="radio" name="radio" checked data-labelauty="N"></li></ul></form></div></div>'
	return html
}

function select_radio(e)
{
	id = get_id(e);
	is_selected = $(e).find('.labelauty-checked').text() == 'Y';

	if(is_selected)
		add_2_result(id);
	else
		del_from_result(id)
}

function get_id(e)
{
	return $(e).parent().parent().parent().parent().children().first().text();
}

function get_index(id)
{
	for (var i = 0; i < result.length; i++) 
	{
		if (result[i] == id)
			return i
	}
	return -1
}

function add_2_result(id)
{
	index = get_index(id);
	if(index < 0)
		result.push(id);
}

function del_from_result(id)
{
	index = get_index(id);
	if(index >= 0)
	{
		result.splice(index,1);
	}
}

function print_result()
{
	$('#result').text(result);
}