from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

# Initialize the OpenAI API client
ai = OpenAI(api_key=settings.OPENAI_API_KEY)

conversation = []  # Store the conversation history globally

@csrf_exempt
def chatbot(request):
    global conversation

    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        print(user_input)
        try:
            # Create a chat completion
            response = ai.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="gpt-3.5-turbo",
                # model="gpt-4o",
            )
            print(response)
            # Extract the chatbot response
            chatbot_response = response.choices[0].message.content
            print(chatbot_response)

            # Append user input and AI response to conversation history
            conversation.append((user_input, chatbot_response))

        except Exception as e:
            chatbot_response = f"An error occurred: {e}"
            print(chatbot_response)

            # In case of error, still append user input to conversation history
            conversation.append((user_input, chatbot_response))

        # return HttpResponseRedirect(reverse('chatbot', args= {'conversation': conversation}))
        return render(request, 'chatbot.html', {'conversation': conversation})

    # Initial rendering of the page or GET request
    return render(request, 'chatbot.html', {'conversation': conversation})
