import sublime, sublime_plugin

import os

skeleton = '''{
    "project_path": "",
    "output_path": "",
    "ignore_path": "",
    "output_extension": "css",
    "options": {
        "cache":         false,
        "debug":         false,
        "line-comments": false,
        "line-numbers":  false,
        "sourcemap":     false,
        "style":         "compressed"
    }
}
'''

class SassBuilderForMavensMateCreateCommand(sublime_plugin.WindowCommand):

    def run(self, paths=[]):
        if len(paths) != 0:
            for path in paths:
                if os.path.isdir(path):
                    filename = os.path.join(path, '.SassBuilderForMavensMate-config.json')

                    with open(filename, 'w+') as f:
                        f.write(skeleton)

                    view = self.window.open_file(filename)
                    view.set_syntax_file('Packages/Javascript/JSON.tmLanguage')
        else:
            view = self.window.new_file()
            view.settings().set('default_dir', self.window.folders()[0])
            view.set_syntax_file('Packages/Javascript/JSON.tmLanguage')
            view.set_name('.sassbuilder-config')
            view.run_command('insert_snippet', {'contents': skeleton})