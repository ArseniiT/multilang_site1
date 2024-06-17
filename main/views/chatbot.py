import openai
from django.shortcuts import render
from django.conf import settings


def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        openai.api_key = settings.OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        chatbot_response = response['choices'][0]['message']['content']
        return render(request, 'chatbot.html', {'response': chatbot_response})
    return render(request, 'chatbot.html')
