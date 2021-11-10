# lava-docs
Documentation source for Lava https://github.com/lava-nc/

# Generate Docs
```bash
pip install -r requirements.txt
```
# Test Doc Build
```bash
pyb sphinx_generate_documentation
```

# Make Docs
They will be in `_build/html`
```bash
make html
```
## Syncing Notebooks to the build
You can either manually create entry for IPython notebooks or add it to
`tutorial_list` entry. Once notebook is in the list, it will sync the notebook
with the main repo and include it in the build.