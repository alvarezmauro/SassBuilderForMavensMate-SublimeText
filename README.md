# SassBuilderForMavensMate-SublimeText

Sublime Text SASS compiler for Salesforce developers. Based on @bnlucas plugin SassBuilder

## How it works?
=============
Every time you save/update a SASS/SCSS file, this plugin will check if there is a "local" configuration file (.SassBuilderForMavensMate-config.json) wich should be in the same folder that contains the file that you are saving/updating. If there isn't, the plugin will check if there is a "global" configuration file, wich should be located in the root folder of the mavenMate project.

If a configuration file is found, this plugin will be use it to compile the SASS/SCSS file.

## Configuration file

```json
{
    "project_path": "",
    "output_path": "",
    "ignore_path": "",
    "output_extension": "",
    "options": {
        "cache":         false,
        "debug":         false,
        "line-comments": false,
        "line-numbers":  false,
        "sourcemap":     false,
        "style":         "compressed"
    }
}
```

## Options

| Option  | Description | Values |
| ------------- | ------------- |
| project_path | Name of the folder from where you want to read the SASS/SCSS files | (string) Folder path |
| output_path | Name of the folder where you want to save the compiled version of the SASS/SCSS files | (string) Folder path |
| ignore_path | Name of the folder from where you want to ignore | (string) Folder path |
| output_extension | Extension that you want to use for the compiled SASS/SCSS file | (string) extension name (e.g. css, resource) |
| Options | Object with all the SASS options | (Object) |


