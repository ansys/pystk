IAnalysisWorkbenchInstance
==========================

.. py:class:: ansys.stk.core.vgt.IAnalysisWorkbenchInstance

   object
   
   The IAgCrdnInstance interface enables to obtain information about the parent object that owns the VGT component.

.. py:currentmodule:: IAnalysisWorkbenchInstance

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchInstance.instance_path`
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchInstance.template`


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
    :type: IAnalysisWorkbenchComponent

    Returns a template object the VGT component was created from or null if the VGT component was not created from a template.


