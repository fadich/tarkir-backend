__all__ = [
    'Admin',
]

from flask_admin import Admin as FlaskAdmin


class Admin(FlaskAdmin):

    def __init__(
        self,
        app=None,
        name=None,
        url=None,
        subdomain=None,
        index_view=None,
        translations_path=None,
        endpoint=None,
        static_url_path=None,
        base_template=None,
        template_mode=None,
        category_icon_classes=None,
        db=None
    ):
        super().__init__(
            app=app,
            name=name,
            url=url,
            subdomain=subdomain,
            index_view=index_view,
            translations_path=translations_path,
            endpoint=endpoint,
            static_url_path=static_url_path,
            base_template=base_template,
            template_mode=template_mode,
            category_icon_classes=category_icon_classes
        )

        self.db = db
