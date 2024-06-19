from django.shortcuts import render
from django.conf import settings
from openai import OpenAI
from django.utils.translation import gettext as _
from main.models import Article

# Initialize the OpenAI API client
ai = OpenAI(api_key=settings.OPENAI_API_KEY)


def search_view(request):
    query = request.GET.get('q', '')

    # Search the database for relevant articles
    articles = Article.objects.filter(content__icontains=query)

    # Determine the language and set the content message accordingly
    if request.LANGUAGE_CODE == 'fr':
        content_message = _('Fournir un résumé des articles suivants liés à: {query}\n\n'.format(query=query))
    else:
        content_message = _('Provide a summary for the following articles related to: {query}\n\n'.format(query=query))

    # Create the content for OpenAI
    content = content_message + '\n\n'.join(article.content for article in articles)

    # Augment search results using OpenAI
    try:
        response = ai.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content': content,
                }
            ],
            model='gpt-3.5-turbo',
        )
        augmented_results = response.choices[0].message.content
    except Exception as e:
        augmented_results = str(e)

    return render(request, 'search_results.html', {'query': query, 'articles': articles, 'augmented_results': augmented_results})
