from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.sphinx")
use_plugin('python.install_dependencies')

name = "Lava"
default_task = ["sphinx_generate_documentation"]
version = "0.1.0"
summary = "A Software Framework for Neuromorphic Computing"
url = "https://lava-nc.org"
license = "BSD-3-Clause"

@init
def set_properties(project):
    project.set_property("dir_source_main_python", "../lava")
    project.set_property("dir_source_unittest_python", "../tests")
    project.set_property("dir_source_main_scripts", "../scripts")
    project.set_property("dir_docs", "./")

    project.set_property("sphinx_config_path", "./")
    project.set_property("sphinx_source_dir", "./")
    project.set_property("sphinx_output_dir", "./_build")
    project.set_property("sphinx_doc_author", "Lava Project")
    project.set_property("sphinx_doc_builder", "html")
    project.set_property("sphinx_project_name", project.name)
    project.set_property("sphinx_project_version", project.version)

    project.depends_on_requirements("requirements.txt")
    project.build_depends_on("sphinx")
    project.plugin_depends_on("sphinx_rtd_theme")
    project.plugin_depends_on("sphinx_tabs")
