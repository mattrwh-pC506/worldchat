from authentication.apps import AuthenticationConfig

def test_app_config(app_config_factory):
    assert app_config_factory(AuthenticationConfig) == True
