AnalysisWorkbenchComponentInstance
==================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchComponentInstance

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentContext`

   Enable to obtain information about the parent object that owns the VGT component.

.. py:currentmodule:: AnalysisWorkbenchComponentInstance

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentInstance.instance_path`
              - Returns a path to the parent object that owns the VGT component.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentInstance.template`
              - Returns a template object the VGT component was created from or null if the VGT component was not created from a template.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchComponentInstance


Property detail
---------------

.. py:property:: instance_path
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentInstance.instance_path
    :type: str

    Returns a path to the parent object that owns the VGT component.

.. py:property:: template
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentInstance.template
    :type: IAnalysisWorkbenchComponent

    Returns a template object the VGT component was created from or null if the VGT component was not created from a template.


