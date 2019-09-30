from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    	'my_list':[
    		 {
	    		'restaurant_name':'Alfredo Chicken Cafe',
	    		'food_type':'Pizza'
    		},
		 	 {
	    		'restaurant_name':'Central Perk ',
	    		'food_type':'Cafe',
		 	},
		 	{
	    		'restaurant_name':'Bubba Gump Shrimp',
	    		'food_type':'Shrimps',
    		},
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    	'my_object':{
    		'restaurant_name' : 'Bubba Gump Shrimp',
    		'food_type' : 'Shrimps'
    	}

    }
    return render(request, 'detail.html', context)
