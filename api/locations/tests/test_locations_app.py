from locations.apps import LocationsConfig

def test_app_config(app_config_factory):
    assert app_config_factory(LocationsConfig) == True
