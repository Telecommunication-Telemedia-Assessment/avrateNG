"""
    config plugin for bottle
    see also projects from https://github.com/stg7

    This file is part of avrateNG.
    avrateNG is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    avrateNG is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with avrateNG.  If not, see <http://www.gnu.org/licenses/>.
"""
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