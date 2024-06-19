from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

# Initialize the OpenAI API client
ai = OpenAI(api_key=settings.OPENAI_API_KEY)


@csrf_exempt
def chatbot(request):
    # Clear the session for refresh conversation each time the chatbot page is loaded
    request.session.flush()

    # Retrieve conversation from session or initialize if not present
    conversation = request.session.get('conversation', [])
    return render(request, 'chatbot.html', {'conversation': conversation})


@csrf_exempt
def send_user_message(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # Retrieve conversation from session or initialize if not present
        conversation = request.session.get('conversation', [])

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
            # Extract the chatbot response
            chatbot_response = response.choices[0].message.content

            # Append user input and AI response to conversation history
            conversation.append({'user': 'You', 'user_input': user_input, 'ai': 'AI', 'chatbot_response': chatbot_response})

            # Save the updated conversation in the session
            request.session['conversation'] = conversation

            return JsonResponse({'user_input': user_input, 'chatbot_response': chatbot_response})

        except Exception as e:
            chatbot_response = f"An error occurred: {e}"
            conversation.append({'user': 'You', 'user_input': user_input, 'ai': 'AI', 'chatbot_response': chatbot_response})

            # Save the updated conversation in the session
            request.session['conversation'] = conversation

            return JsonResponse({'user_input': user_input, 'chatbot_response': chatbot_response})

    return JsonResponse({'error': 'Invalid request'}, status=400)
