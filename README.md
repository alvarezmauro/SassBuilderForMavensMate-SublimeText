# SassBuilderForMavensMate-SublimeText

Sublime Text SASS compiler for Salesforce developers (Based on @bnlucas sublimetext plugin SassBuilder)

## How it works?
Every time you update a SASS/SCSS file, this plugin will check if there is a "local" configuration file (.SassBuilderForMavensMate-config.json) wich should be in the same folder that contains the file that you are updating. If there isn't a configuration file there, this plugin will check if there is a "global" configuration file, wich should be located in the root folder of your mavensMate project.

If a configuration file is found, this plugin will use it to compile the SASS/SCSS file and save it. Once the file is saved, the sublimetext plugin for mavensMate will compile it (upload it to your salesforce project).

## Configuration file

```json
{
    "project_path": "",
    "output_path": "",
    "ignore_path": "",
    "output_extension": "css",
    "force_compile_file_name": "",
    "generate_resource_xml_file": false,
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
| ------- | ----------- | ------ |
| project_path | Name of the folder from where you want to read the SASS/SCSS files | (string) Folder path (empty == folder that contains the configuration file)|
| output_path | Name of the folder where you want to save the compiled version of the SASS/SCSS files | (string) Folder path (empty == folder that contains the configuration file) |
| ignore_path | Name of the folder that you want to ignore | (string) Relative folder path |
| output_extension | Extension that you want to use for the compiled SASS/SCSS file | (string) Extension name (e.g. css, resource) |
| force_compile_file_name | Use it if instead of compile the file that you are saving you want to compile a specific file | (string) file name with extension |
| generate_resource_xml_file | Generate a .resource-meta.xml file. This is useful if you want to create an static resource (check the examples of how to use it) | (bool) |
| Options | Object with all the SASS options | (Object) Object with the SASS configuration |


## Install with Sublime Package Control

1. Add this repo using "Package Control: Add Repository" https://github.com/alvarezmauro/SassBuilderForMavensMate-SublimeText
2. You can then add this package using Package Control as usual. Find "Package Control: Add Package" and search for "SassBuilderForMavensMate-SublimeText"

## Examples of how to use it

### You want to use SASS/SCSS for one of your lighning component
Just create a configuration file (.SassBuilderForMavensMate-config.json) in the folder of your lightning component with the following:
```json
{
    "project_path": "",
    "output_path": "",
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
```
Now everytime you save a SASS/CSS file located in that folder, it will be compiled and uploaded to your Salesforce thanks to MavensMate.

### You want to use SASS/SCSS for all of your lighning component
Easy, create a configuration file (.SassBuilderForMavensMate-config.json) in the root folder of your MavensMate project with the following configuration:
```json
{
    "project_path": "",
    "output_path": "",
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
```
Now everytime you save a SASS/CSS file, it will be compiled and uploaded to your Salesforce thanks to MavensMate.


### You want to use SASS/SCSS to create a static resource (very usefull to create your own CSS Framework)
This is one of the main reasons why I created this plugin. If you want to use a "global CSS file" for your entire projects, follow the following steps:

- Create a folder in the root level of your MavensMate Project (i.e.: "myCssFramework")
- Create your SASS/SCSS framework inside of that folder:
    .
    ├── src
    └── myCssFramework
            ├── myCssFramework.scss                # Main SASS/SCSS file wich will include all the other SASS/SCSS files of your framework
            ├── buttons.scss
            ├── inputs.scss
            ├── fonts.scss
            └── etc...

    ** REMEMBER: Files uploaded to static resources should use characteres only! (that's why I use camelCase to name them)

- Create a configuration file in your SASS/SCSS framework folder with the following content:
```json
{
    "project_path": "",
    "output_path": "../src/staticresources",
    "ignore_path": "",
    "output_extension": "resource",
    "force_compile_file_name": "myCssFramework.scss",
    "generate_resource_xml_file": true,
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
- Create a configuration file in the root folder of your MavensMate project with the following content:
```json
{
    "project_path": "",
    "output_path": "",
    "ignore_path": "myCssFramework",
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
```

- Include your static resource in your project

Done! now you can use SASS on each individual lightning component and use your SASS/SCSS framework for your whole project.
