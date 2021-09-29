module.exports = function (grunt) {
    grunt.initConfig({
      pkg: grunt.file.readJSON('package.json'),
      copy: {
        main: {
          files: [{
              expand: true,
              src: ['resources/**'],
              dest: 'build/'
            },
            {
              expand: true,
              src: ['src/**/*.html'],
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
            cwd: 'src',
            src: ['**/*.html', '**/*.js'],
            dest: 'build/'
          }]
        }
      }
    });
  
    grunt.loadNpmTasks('grunt-contrib-copy');
  
    grunt.registerTask('default', ['copy']);
  };
  
  