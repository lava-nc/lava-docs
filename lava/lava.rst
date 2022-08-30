Lava API reference
==================

This page gives an overview over all public lava modules, classes and functions. 

Lava is divided into the sub-packages:

- :ref:`The process library <lava/lava.proc:Lava process library>` containing commonly used :ref:`Processes <lava/lava.magma.core.process:lava.magma.core.process.process>` and :ref:`ProcessModels <lava/lava.magma.core.model:lava.magma.core.model.model>`.
- :ref:`Magma <lava/lava.magma:Magma>`, containing the main components of Lava:
  
  - :ref:`Magma core <lava/lava.magma.core:lava.magma.core>`
    base classes, definitions and functionality 
  - :ref:`Magma compiler <lava/lava.magma.compiler:lava.magma.compiler>`
    compiling and building the network and communication channels
  - :ref:`Magma runtime <lava/lava.magma.runtime:lava.magma.runtime>`
    providing a frontend for execution and control

A fundamental description about Lava and its key componentes can be found in :ref:`Lava Architecture <lava architecture>`.

Explanatory tutorials and example code can be found in the :ref:`in-depth tutorials <lava/notebooks/in_depth/in_depth:In-depth tutorials>` and in the :ref:`End-to-end Tutorial notebooks <lava/notebooks/end_to_end/end_to_end:End to end tutorials>`. 


.. toctree::
   :maxdepth: 10

   lava.magma
   lava.proc
   lava.utils


.. automodule:: lava
   :members:
   :undoc-members:
   :show-inheritance:
