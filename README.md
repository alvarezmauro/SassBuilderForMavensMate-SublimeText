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

## Use cases

### You want to use SASS/SCSS for one of your lighning component
Just create a config file in the folder of your lighning component with the following configuration:
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

### You want to use SASS/SCSS for all of your lighning component
Easy, create a config file in the root folder of your mavensMate project with the following configuration:
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

### You want to use SASS/SCSS to create a static resource (very usefull)
This is one of the main reasons why I created this plugin. If you want to use a "global CSS file" for your entire projects, follow the following steps:

- Create a folder in the root level of your MavensMate Project (i.e.: "my-css-framework")
- Create a your SASS/SCSS framework inside of that folder:
    .
    ├── src
    └── my-css-framework
            ├── my-css-framework.scss                # Main SASS/SCSS file wich will include all the other SASS/SCSS files of your framework
            ├── buttons.scss
            ├── inputs.scss
            ├── fonts.scss
            └── etc...

- Create a configuration file in your SASS/SCSS framework folder with the following content:
```json
{
    "project_path": "",
    "output_path": "../src/staticresources/",
    "output_extension": "resource",
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
    "ignore_path": "my-css-framework",
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

- Create a static resource using the development console with the name of your framework (i.e.: "my-css-framework")

And that's it, now everytime you modify your SASS/SCSS framework, this one will be compiled, saved into the resources folder and compiled/uploaded into your salesforce project


## Install with Sublime Package Control
1. Add this repo using "Package Control: Add Repository" https://github.com/alvarezmauro/SassBuilderForMavensMate-SublimeText
2. You can then add this package using Package Control as usual. Find "Package Control: Add Package" and search for "SassBuilderForMavensMate-SublimeText"


