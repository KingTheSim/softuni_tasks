import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db import models
from main_app.models import Author, Article, Review
from django.db.models import Count, Avg


def get_authors(search_name, search_email):
    if search_name is None and search_email is None:
        return ""

    if search_name and search_email:
        authors = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email).order_by(
            '-full_name')
    elif search_name:
        authors = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')

    elif search_email:
        authors = Author.objects.filter(email__icontains=search_email).order_by('-full_name')

    if not authors:
        return ""

    res = []
    for author in authors:
        res.append(
            f'Author: {author.full_name}, email: {author.email}, status: {"Banned" if author.is_banned else "Not Banned"}')

    return "\n".join(res)


def get_top_publisher():
    top_publisher = Author.objects.annotate(num_of_articles=Count('article_author')).order_by('-num_of_articles',
                                                                                              'email').first()

    if top_publisher and top_publisher.num_of_articles > 0:
        return f"Top Author: {top_publisher.full_name} with {top_publisher.num_of_articles} published articles."
    else:
        return ""


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(num_of_reviews=Count('review_author')).order_by('-num_of_reviews',
                                                                                           'email').first()

    if top_reviewer and top_reviewer.num_of_reviews > 0:
        return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.num_of_reviews} published reviews."
    else:
        return ""


def get_latest_article():
    latest_article = Article.objects.last()

    if Article.objects.count() == 0 or not latest_article:
        return ""

    authors_names = ", ".join(author.full_name for author in latest_article.authors.all().order_by('full_name'))
    num_reviews = latest_article.review_article.count()
    avg_rating = latest_article.review_article.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0.0

    return f"The latest article is: {latest_article.title}. Authors: {authors_names}. Reviewed: {num_reviews} times. Average Rating: {avg_rating:.2f}."


def get_top_rated_article():
    top_rated_article = Article.objects.annotate(avg_rating=Avg('review_article__rating')).order_by('-avg_rating',
                                                                                                      'title').first()

    if not top_rated_article or top_rated_article.avg_rating is None:
        return ""

    return f"The top-rated article is: {top_rated_article.title}, with an average rating of {top_rated_article.avg_rating:.2f}, reviewed {top_rated_article.review_article.count()} times."


def ban_author(email):
    if email is None:
        return "No authors banned."

    author_ban = Author.objects.filter(email=email).first()

    if not author_ban:
        return "No authors banned."

    num_reviews_deleted = author_ban.review_author.count()

    author_ban.is_banned = True
    author_ban.save()

    author_ban.review_author.all().delete()

    return f"Author: {author_ban.full_name} is banned! {num_reviews_deleted} reviews deleted."
