import ckan.plugins as plugins

class SpatialUIPluginClass(plugins.SingletonPlugin):
    """
    Setup plugin
    """
    print '#############################'
    print '#    ckanext-spatialUI      #'
    print '#############################'

    plugins.implements(plugins.IConfigurer, inherit=True)

    def update_config(self, config):
        plugins.toolkit.add_template_directory(config, 'templates')

