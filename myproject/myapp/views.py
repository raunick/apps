import openai
from django.shortcuts import render

openai.api_key = "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"


def recycling_info_view(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        recycling_info = get_recycling_info(product_name)
        recycling_story = get_recycling_story(product_name)

        context = {
            'product_name': product_name,
            'recycling_info': recycling_info,
            'recycling_story': recycling_story,
        }

        return render(request, 'myapp/recycling_info.html', context)
    else:
        return render(request, 'myapp/recycling_info.html')


def recycling_info_view2(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        recycling_info = get_recycling_info(product_name)
        recycling_story = get_recycling_story(product_name)
        print(recycling_info)

        opcoes = recycling_info.split('\n')
        context = {
            'opcoes': opcoes,
            'product_name': product_name,
            'recycling_info': recycling_info,
            'recycling_story': recycling_story,
        }

        return render(request, 'myapp/recycling.html', context)
    else:
        return render(request, 'myapp/recycling.html')


def get_recycling_info(product_name):
    prompt = "como recliclar " + product_name + \
        " usado,poderia listar algumas formas?"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=1,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    recycling_info = response.choices[0].text.strip()
    return recycling_info


def get_recycling_story(product_name):
    prompt = "me conte uma breve curiosidade sobre o " + product_name+"inclua muitos emojis"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    recycling_story = response.choices[0].text.strip()
    return recycling_story
