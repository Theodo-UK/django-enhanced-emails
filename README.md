# django-enhanced-emails

## Getting started

- Install the package: `pipenv install django-enhanced-emails` (or, with you're still using pip: `pip install django-enhanced-emails`)
- Create a new email class:
  ```py
  from enhanced_emails import EnhancedEmail


  class WelcomeEmail(EnhancedEmail):
      subject = 'Welcome to our site!'
      html_template = 'emails/welcome.html'
  ```
  Where `emails/welcome.html` could be:
  ```html
  <strong>Welcome to our site {{first_name}}!</strong>

  Best,
  The OurSite team
  ```

- Instanciate a mail and send it:
  ```py
  email = WelcomeEmail(
      to=[user.email],
      context={
        'first_name': user.first_name
      }
  )
  email.send()
  ```
- ✨ All done! Our user received something like:
  ```email
  Content-Type: multipart/alternative;
  boundary="===============7747654958126582044=="
  MIME-Version: 1.0
  Subject: hello
  From: hello@oursite.com
  To: user@gmail.com
  Date: Wed, 11 Apr 2018 17:13:02 -0000
  Message-ID: <152346678269.275.17989388690220812241@cf7f5f3375c9>

  --===============7747654958126582044==
  Content-Type: text/plain; charset="utf-8"
  MIME-Version: 1.0
  Content-Transfer-Encoding: 7bit

  Welcome to our site Elon!

  Best,
  The OurSite team
  --===============7747654958126582044==
  Content-Type: text/html; charset="utf-8"
  MIME-Version: 1.0
  Content-Transfer-Encoding: 7bit

  <strong>Welcome to our site Elon!</strong>

  Best,
  The OurSite team
  --===============7747654958126582044==--
  ```
