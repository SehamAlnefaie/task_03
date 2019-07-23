from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 'my_list': [{"restaurant_name":"A", "food_type":"type1"},
                            {"restaurant_name":"B", "food_type":"type2"},
                            {"restaurant_name":"C", "food_type":"type3"},
      ],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {'my_object': {"restaurant_name":"A", "food_type":"type1"},

    }
    return render(request, 'detail.html', context)
