import os
import django
from django.utils import timezone

# Configure settings for project
# This line ensures that Django settings are configured before accessing models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multilang_site1.settings')

# Setup Django
django.setup()

# Now import the Article model
from main.models import Article

articles = [
    {
        "title": "Exploring the Depths of the Mariana Trench",
        "content": "Scientists have embarked on a daring journey to explore the deepest parts of the ocean. The Mariana Trench expedition could uncover new species and secrets of the deep sea.",
        "publication_date": "2024-06-17T10:00:00Z"
    },
    {
        "title": "The Renaissance of Renewable Energy",
        "content": "Renewable energy sources have surpassed coal and gas in electricity generation this year, marking a significant milestone in the global shift towards sustainable energy.",
        "publication_date": "2024-06-18T10:00:00Z"
    },
    {
        "title": "Artificial Intelligence: The New Frontier in Medicine",
        "content": "AI is transforming the medical field with its ability to diagnose diseases with accuracy surpassing human doctors. This breakthrough is paving the way for a new era in healthcare.",
        "publication_date": "2024-06-19T10:00:00Z"
    },
    {
        "title": "The Impact of Quantum Computing on Cryptography",
        "content": "Quantum computers pose a significant threat to current cryptographic methods. Experts are racing to develop quantum-resistant encryption to secure digital communications.",
        "publication_date": "2024-06-20T10:00:00Z"
    },
    {
        "title": "The Quest for a Sustainable Future",
        "content": "As climate change accelerates, scientists and activists are calling for urgent action. The quest for a sustainable future is more critical than ever, with innovative solutions on the horizon.",
        "publication_date": "2024-06-21T10:00:00Z"
    }
]


def add_article(title, content, publication_date):
    article, created = Article.objects.get_or_create(
        title=title,
        content=content,
        publication_date=timezone.make_aware(timezone.datetime.strptime(publication_date, '%Y-%m-%dT%H:%M:%SZ'))
    )
    if created:
        article.save()


def populate():
    for article in articles:
        add_article(article['title'], article['content'], article['publication_date'])


if __name__ == '__main__':
    print("Populating the databases with articles...")
    populate()
    print("Populating complete.")
