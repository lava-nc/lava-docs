# lava-docs
Documentation source for Lava https://github.com/lava-nc/

# Make Docs
They will be in `_build/html`
```bash
make html
```



If new files have been created in the source code repositories (such as lava, lava-on-loihi, lava-optimization), sphinx-apidoc must be re-run.


```bash
sphinx-apidoc -o <output_path? <path-to-src-repo>/src/lava -t _templates -H -d 10 --implicit-namespace
```

Afterwards, the html files must be built:

```bash
make clean
make html
```



## Syncing Notebooks to the build
You can either manually create entry for IPython notebooks or add it to
`tutorial_list` entry. Once notebook is in the list, it will sync the notebook
with the main repo and include it in the build.
