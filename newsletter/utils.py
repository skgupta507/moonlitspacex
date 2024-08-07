import uuid
from typing import Union, Optional
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import get_connection, BadHeaderError, EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags


def generate_entry_id():
    return uuid.uuid4().int


def render_error_http_response(tempalte_name: str, context: dict[str, str]):
    error_html_content = render_to_string(tempalte_name, context)
    return HttpResponse(error_html_content)


def send_mail(
    subject: str,
    recipient_list: Union[list[str], str],
    template_name: str,
    context: Optional[dict] = None,
    error_template_name: Optional[str] = None,
):
    if not isinstance(recipient_list, list):
        recipient_list = [recipient_list]

    html_template = render_to_string(template_name, context)
    text_template = strip_tags(html_template)

    try:
        with get_connection() as connection:
            email = EmailMultiAlternatives(
                subject=subject,
                body=text_template,
                to=recipient_list,
                connection=connection,
            )
            email.attach_alternative(html_template, "text/html")
            email.send()

        return True, None
    except BadHeaderError:
        if error_template_name:
            return False, render_error_http_response(
                error_template_name,
                {"title": "Oh no!", "message": "Invalid header found"},
            )
        else:
            return False, None
    except Exception as e:
        """handle other possible exceptions"""
        if settings.DEBUG:
            print(e)
        if error_template_name:
            return False, render_error_http_response(
                error_template_name,
                {
                    "title": "Oops!",
                    "message": "Something went wrong, please re-check email and try again.",
                },
            )
        else:
            return False, None
