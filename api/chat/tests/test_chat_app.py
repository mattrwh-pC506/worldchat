from chat.apps import ChatConfig

def test_app_config(app_config_factory):
    assert app_config_factory(ChatConfig) == True
