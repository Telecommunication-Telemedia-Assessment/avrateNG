import inspect

class ConfigPlugin(object):
    """ This plugin passes an config dictionary handle to route callbacks
        that accept a `config` keyword argument.
    """

    name = 'config'
    api = 2
    _config = None
    def __init__(self, config={}, keyword="config"):
         self.config = config
         ConfigPlugin._config = config
         self.keyword = keyword

    def setup(self, app):
        ''' Make sure that other installed plugins don't affect the same
            keyword argument.'''
        for other in app.plugins:
            if not isinstance(other, ConfigPlugin):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another config plugin with conflicting settings (non-unique keyword).")

    def apply(self, callback, context):
        # Override global configuration with route-specific values.
        conf = context.config.get('config') or {}
        config = conf.get('config', self.config)
        keyword = conf.get('keyword', self.keyword)

        # Test if the original callback accepts a 'db' keyword.
        # Ignore it if it does not need a database handle
        argspec = inspect.signature(context.callback)
        if keyword not in argspec.parameters:
            return callback

        def wrapper(*args, **kwargs):
            kwargs[keyword] = config
            return callback(*args, **kwargs)

        # Replace the route callback with the wrapped one.
        return wrapper