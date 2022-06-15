from aqt import mw

def get_config() -> dict:
    config: dict = mw.addonManager.getConfig(__name__) or dict()
    ## Addon fix
    config['addon_more_overview_stats'] = True if config.get('addon_more_overview_stats', "false").lower() == "true" else False
    ## Customization
    config['font'] = config.get('font', "Segoe UI")
    config['font_size'] = int(config.get('font_size', "12"))
    config['theme'] = config.get('theme', 'Anki')
    config['theme_reload'] = True if config.get('theme_reload', "false").lower() == "true" else False

    return config

def write_config(config):
    for key in config.keys():
        if not isinstance(config[key], str):
            config[key] = str(config[key])
    mw.addonManager.writeConfig(__name__, config)

config = get_config()
