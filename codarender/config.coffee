exports.config =
  # See http://brunch.readthedocs.org/en/latest/config.html for documentation.
  files:
    javascripts:
      defaultExtension: 'coffee'
      joinTo:
        'javascripts/app.js': /^app/
        'javascripts/spine.js': /^vendor\/js\/spine/
        'javascripts/vendor.js': /^vendor/
        'test/javascripts/test.js': /^test(\/|\\)(?!vendor)/
        'test/javascripts/test-vendor.js': /^test(\/|\\)(?=vendor)/
      order:
        before: [
          'vendor/js/spine/spine.js',
          'vendor/js/spine/ajax.js',
          'vendor/js/spine/local.js',
          'vendor/js/spine/manager.js',
          'vendor/js/spine/route.js',
          'vendor/js/spine/tmpl.js'
        ]
        
        after: ['vendor/js/bootstrap.js']
        

    stylesheets:
      joinTo:
        'stylesheets/app.css': /^app/
        'stylesheets/vendor.css': /^vendor/
        'test/stylesheets/test.css': /^test/
      order:
        before: []
        after: []

    templates:
      defaultExtension: 'jade' 
      joinTo: 'javascripts/app.js'
