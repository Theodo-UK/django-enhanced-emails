from .emails import EnhancedEmail, WebVersionEnhancedEmail, WebVersionMixin

__all__ = ["EnhancedEmail", "WebVersionEnhancedEmail", "WebVersionMixin"]

default_app_config = "enhanced_emails.apps.EnhancedEmailsConfig"
