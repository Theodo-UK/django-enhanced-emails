from bs4 import BeautifulSoup
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EnhancedEmail(EmailMultiAlternatives):
    """A magic email classes that supports multi alternatives (text & html by default),
    attachments, rendering templates, etc.
    """

    attached_files = []
    base_context = {}

    def __init__(self, to, context, *args, **kwargs):
        self.context = dict(self.base_context)
        self.context.update(context)

        super().__init__(
            subject=self.get_subject(),
            body=self.get_txt_content(),
            to=to,
            *args,
            **kwargs
        )
        self.attach_alternative(
            self.get_html_content(),
            'text/html'
        )

        # Automatically attach files.
        for file in self.attached_files:
            self.attach_file(file)

    def get_subject(self):
        """Returns the subject line of the email.
        Meant to be overriden for dynamic subjects.
        """"
        return self.subject

    def get_txt_template(self):
        return getattr(self, 'txt_template', None)

    def get_txt_content(self):
        """Returns the text content of the email.
        Tries to render the text template with the context if it exists, otherwise
        extracts text from the html content.
        """
        txt_template = self.get_txt_template()

        if txt_template:
            return render_to_string(
                txt_template,
                self.context
            )
        else:
            soup = BeautifulSoup(self.get_html_content(), 'html.parser')
            return soup.get_text()

    def get_html_template(self):
        return self.html_template

    def get_html_content(self):
        """Returns the html content of the email.
        Renders the html templates with the context.
        """
        return render_to_string(
            self.get_html_template(),
            self.context
        )
