"""
A module that registers foundry settings from a list
"""


def register(settings: list, preffix: str):
    """
    Registers a list of settings
    :param settigns: A list of dictionaries with setting info:
        [{'name': 'string', 'default': 'value'}]
    """
    for option in settings:
        settings_options = {
            'name': option.get('id'),
            'default': option.get('default'),
            'config': True,
            'scope': option.get('scope', 'world')
            }
        game.settings.register(  # noqa
            preffix, option.get('id'), settings_options)  # noqa


def get_setting(preffix: str, name: str):
    """
    Returns the value of a setting
    :param preffix: Settings preffix
    :param name: Name of the settigns
    """
    return game.settings.js_get(preffix, name)  # noqa
