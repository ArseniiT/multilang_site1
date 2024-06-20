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
        "title": "The Future of AI: Beyond GPT-4",
        "content": "Researchers are already working on the next generation of AI models, aiming to surpass the capabilities of GPT-4 with even more advanced features.",
        "publication_date": "2024-06-17T10:00:00Z"
    },
    {
        "title": "AI in Healthcare: Revolutionizing Diagnosis",
        "content": "Artificial intelligence is set to revolutionize healthcare by providing accurate and rapid diagnosis of diseases, greatly improving patient outcomes.",
        "publication_date": "2024-06-18T10:00:00Z"
    },
    {
        "title": "Quantum Computing and AI: A Powerful Combination",
        "content": "The integration of quantum computing with AI promises to unlock new potentials in data processing and problem-solving capabilities.",
        "publication_date": "2024-06-19T10:00:00Z"
    },
    {
        "title": "Ethical Implications of Advanced AI",
        "content": "As AI technology advances, it raises important ethical questions about privacy, bias, and the potential for misuse.",
        "publication_date": "2024-06-20T10:00:00Z"
    },
    {
        "title": "GPT-4 in Education: Personalized Learning Experiences",
        "content": "GPT-4 is being used to create personalized learning experiences for students, adapting to their individual needs and learning styles.",
        "publication_date": "2024-06-21T10:00:00Z"
    },
    {
        "title": "AI and Cybersecurity: Defending Against Future Threats",
        "content": "Artificial intelligence is playing a crucial role in cybersecurity, helping to detect and defend against sophisticated cyber threats.",
        "publication_date": "2024-06-22T10:00:00Z"
    },
    {
        "title": "The Role of AI in Climate Change Mitigation",
        "content": "AI technologies are being leveraged to model and predict climate change, aiding in the development of effective mitigation strategies.",
        "publication_date": "2024-06-23T10:00:00Z"
    },
    {
        "title": "Natural Language Processing: Beyond Text Analysis",
        "content": "Advancements in natural language processing are enabling machines to understand and generate human language with increasing accuracy.",
        "publication_date": "2024-06-24T10:00:00Z"
    },
    {
        "title": "The Impact of AI on the Job Market",
        "content": "AI is transforming the job market, automating routine tasks and creating new opportunities in various industries.",
        "publication_date": "2024-06-25T10:00:00Z"
    },
    {
        "title": "AI in Finance: Transforming Investment Strategies",
        "content": "AI is revolutionizing finance by enhancing investment strategies through data analysis and predictive modeling.",
        "publication_date": "2024-06-26T10:00:00Z"
    }
]


def populate():
    articles_to_create = [
        Article(
            title=article['title'],
            content=article['content'],
            publication_date=timezone.make_aware(timezone.datetime.strptime(article['publication_date'], '%Y-%m-%dT%H:%M:%SZ'))
        ) for article in articles
    ]
    Article.objects.bulk_create(articles_to_create)


if __name__ == '__main__':
    print("Populating the databases with articles...")
    populate()
    print("Populating complete.")
