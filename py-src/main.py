"""
The main module for the damage counter
"""


def paint_dmg_token(token, damage):
    """
    Paints the damage on a Token
    :param token: Token to paint
    :param damage: Token damage
    """
    if not token.dmg_txt:
        if damage > 0:
            token.dmg_txt = __new__(  # noqa
                PIXI.Text(str(damage), {'fontSize': 22, 'fill': '#FFFFFF',  # noqa
                                'fontWeight': 'bold'}))
            token.dmg_txt.y = token.height * .75
            token.dmg_txt.x = 5
            token.addChild(token.dmg_txt)
    else:
        if damage > 0:
            token.dmg_txt.text = damage
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
        hp = data.data.attributes.hp.value
    except:  # noqa
        return
    for token in actor.getActiveTokens():
        damage = actor.data.data.attributes.hp.max - hp
        paint_dmg_token(token, damage)


def update_token(_, token, data):
    """
    Called when a token is updated
    :param _:
    :param token: A js object that is like but not a token, because js
    :param data: Data in the actor that has been updated
    """
    try:
        hp = data.actorData.data.attributes.hp.value
    except:  # noqa
        return
    real_token = canvas.tokens.js_get(token._id)  # noqa
    damage = real_token.actor.data.data.attributes.hp.max - hp
    paint_dmg_token(real_token, damage)


def create_token(_, token):
    """
    Called when a new token is created
    :param _: Scene foundry object, ignored
    :param token: Token-like dictionary
    """
    if token.actorLink:
        real_token = canvas.tokens.js_get(token._id)  # noqa
        damage = real_token.actor.data.data.attributes.hp.max - \
            real_token.actor.data.data.attributes.hp.value
        __pragma__('js', '{}', '''
            setTimeout(() => {
                paint_dmg_token(real_token, damage);
            }, 2000)    
        ''')
        __pragma__('skip')
        paint_dmg_token(token, damage)
        __pragma__('noskip')


def canvas_ready(canvas):
    """
    Called when canvas is ready
    :param canvas: Canvas foundry object
    """
    for token in canvas.tokens.placeables:
        damage = token.actor.data.data.attributes.hp.max - \
            token.actor.data.data.attributes.hp.value
        paint_dmg_token(token, damage)


def on_ready():
    """
    Foundry is ready
    """
    print("Pathfinder 2 damage count is active")
    game.pf2_dmg_count = {'paint_dmg_token': paint_dmg_token}  # noqa


Hooks.on("ready", on_ready)  # noqa
Hooks.on("updateActor", update_actor)  # noqa
Hooks.on("updateToken", update_token)  # noqa
Hooks.on("createToken", create_token)  # noqa
Hooks.on("canvasReady", canvas_ready)  # noqa