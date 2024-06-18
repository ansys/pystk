IAnalysisWorkbenchInstance
==========================

.. py:class:: IAnalysisWorkbenchInstance

   object
   
   The IAgCrdnInstance interface enables to obtain information about the parent object that owns the VGT component.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~instance_path`
            * - :py:meth:`~template`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAnalysisWorkbenchInstance


Property detail
---------------

.. py:property:: instance_path
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchInstance.instance_path
    :type: str

    Returns a path to the parent object that owns the VGT component.

.. py:property:: template
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchInstance.template
    :type: "IAgCrdn"

    Returns a template object the VGT component was created from or null if the VGT component was not created from a template.


