"""
The main module for the damage counter
"""

from register_settings import register, get_setting

MODULE_NAME = 'pf2-dmg-count'

SETTINGS = [
    {'id': 'font_size', 'default': "22"}, ]


def paint_dmg_token(token):
    """
    Paints the damage on a Token
    :param token: Token to paint
    """
    max_hp = token.actor.data.data.attributes.hp.max
    damage = max_hp - token.actor.data.data.attributes.hp.value
    if token.actor.hasPlayerOwner:
        damage_txt = str(damage) + " / " + str(max_hp)
        color = '#FFFFFF' if damage < (max_hp / 2) else '#EE0000'
    else:
        if damage < max_hp:
            damage_txt = str(damage)
            color = '#FFFFFF'
        else:
            damage_txt = "X"
            color = '#EE0000'
    if not token.dmg_txt:
        if damage > 0:
            font_size = int(get_setting(MODULE_NAME, 'font_size'))
            token.dmg_txt = __new__(  # noqa
                PIXI.Text(damage_txt,  # noqa
                          {'fontSize': font_size,
                           'fill': color}))
            token.dmg_txt.y = token.height * .75
            token.dmg_txt.x = 5
            token.addChild(token.dmg_txt)
    else:
        if damage > 0:
            token.dmg_txt.text = damage_txt
            token.dmg_txt.style.fill = color
        else:
            token.removeChild(token.dmg_txt)
            del token.dmg_txt


def update_actor(actor, data):
    """
    Called when an actor is updated
    :param actor: Actor updated
    :param data: Object with just the updated data.
    """
    try:
        _ = data.data.attributes.hp.value
    except:  # noqa
        return
    for token in actor.getActiveTokens():
        paint_dmg_token(token)


def update_token(_, token, data):
    """
    Called when a token is updated
    :param _:
    :param token: A js object that is like but not a token, because js
    :param data: Data in the actor that has been updated
    """
    try:
        _ = data.actorData.data.attributes.hp.value
    except:  # noqa
        return
    real_token = canvas.tokens.js_get(token._id)  # noqa
    paint_dmg_token(real_token)


def create_token(_, token):
    """
    Called when a new token is created
    :param _: Scene foundry object, ignored
    :param token: Token-like dictionary
    """
    if token.actorLink:
        real_token = canvas.tokens.js_get(token._id)  # noqa
        __pragma__('js', '{}', '''
            setTimeout(() => {
                paint_dmg_token(real_token);
            }, 2000)''')  # noqa


def canvas_ready(canvas):
    """
    Called when canvas is ready
    :param canvas: Canvas foundry object
    """
    for token in canvas.tokens.placeables:
        paint_dmg_token(token)


def on_ready():
    """
    Foundry is ready
    """
    print("Pathfinder 2 damage count is active")
    game.pf2_dmg_count = {'paint_dmg_token': paint_dmg_token}  # noqa


def on_init():
    """
    Foundry Initilization ended
    """
    register(SETTINGS, MODULE_NAME)


Hooks.once("ready", on_ready)  # noqa
Hooks.on("init", on_init)  # noqa
Hooks.on("updateActor", update_actor)  # noqa
Hooks.on("updateToken", update_token)  # noqa
Hooks.on("createToken", create_token)  # noqa
Hooks.on("canvasReady", canvas_ready)  # noqa
