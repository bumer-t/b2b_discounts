
from settings import MIDDLEWARE_CLASSES, INSTALLED_APPS, DEBUG

if DEBUG:
    MIDDLEWARE_CLASSES += (
        #### 'debug_toolbar.middleware.DebugToolbarMiddleware',
        'debug_panel.middleware.DebugPanelMiddleware',
    )
    INSTALLED_APPS += (
                       'debug_toolbar',
                       'debug_panel',
                       'template_timings_panel',
                       # 'django_coverage',
                       # 'livesettings',
                       )
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_PANELS = (
        #'debug_toolbar.panels.version.VersionDebugPanel', # not neccessary
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
]
    DEBUG_TOOLBAR_CONFIG = {
        'EXCLUDE_URLS': ('/admin',),
        'INTERCEPT_REDIRECTS': False,
    }

    # TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'

    # CACHES = {
    #     'default': {
    #         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #         'LOCATION': '127.0.0.1:11211',
    #     },
    #
    #     # this cache backend will be used by django-debug-panel
    #     # 'debug-panel': {
    #     #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #     #     'LOCATION': '/var/tmp/debug-panel-cache',
    #     #     'OPTIONS': {
    #     #         'MAX_ENTRIES': 200
    #     #     }
    #     # }
    # }

#
# LOGGER_REDIS_HOST = '10.61.130.180'
# LOGGER_REDIS_PORT = 6666
# LOGGER_UDP_HOST = '10.61.130.180'
# LOGGER_UDP_PORT = 6666

# SOUTH_TESTS_MIGRATE = False


print 'LOLOLO'*80