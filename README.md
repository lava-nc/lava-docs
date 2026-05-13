# THIS PROJECT IS ARCHIVED   
Intel will not provide or guarantee development of or support for this project, including but not limited to, maintenance, bug fixes, new releases or updates. Patches to this project are no longer accepted by Intel. If you have an ongoing need to use this project, are interested in independently developing it, or would like to maintain patches for the community, please create your own fork of the project.  

## What's next
Intel is developing the next-generation Loihi architecture and SDK to power the coming era physical AI. The new SDK is built on open-standard AI frameworks to lower the adoption barrier while enabling maximum performance and efficiency on Loihi.
	
All Lava repositories are archived. Stay tuned for announcements about our new SDK and next generation Loihi processor.

Thank you all for your contribution to Lava over the past years!

---

# lava-docs
Documentation source for Lava https://github.com/lava-nc/

# Make Docs
They will be in `_build/html`
```bash
make html
```



If new files have been created in the source code repositories (such as lava, lava-on-loihi, lava-optimization), sphinx-apidoc must be re-run.


```bash
sphinx-apidoc -o <output_path> <path-to-src-repo>/src/lava -t _templates -d 10 --implicit-namespace
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
