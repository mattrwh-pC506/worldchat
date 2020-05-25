import pytest
from importlib import import_module

@pytest.fixture
def app_config_factory():
    def all_clear(config, instance):
        return config.name == instance.name

    def initializer(config):
        name = config.name
        apps = import_module("{}.apps".format(name))
        return all_clear(config, config(name, apps))

    return initializer
