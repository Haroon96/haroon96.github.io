module.exports = function (grunt) {
    grunt.initConfig({
      pkg: grunt.file.readJSON('package.json'),
      clean: ['build'],
      copy: {
        main: {
          files: [{
              expand: true,
              src: ['images/**'],
              dest: 'build/'
            },
            {
              expand: true,
              cwd: 'src',
              src: ['**/*.html', '**/*.js', '**/*.css'],
              dest: 'build/'
            },
            {
              src: ['index.html'],
              dest: 'build/index.html'
            }
          ]
        }
      },
      bake: {
        build: {
          options: {
            removeUndefined: false
          },
          files: [{
            expand: true,
            cwd: 'src/',
            src: ['**/*.html'],
            dest: 'build/'
          }]
        }
      }
    });
  
    grunt.loadNpmTasks('grunt-bake');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-clean');
  
    grunt.registerTask('default', ['clean', 'copy', 'bake']);
  };
  
  
