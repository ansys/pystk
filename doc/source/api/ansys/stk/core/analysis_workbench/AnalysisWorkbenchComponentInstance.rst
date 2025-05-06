AnalysisWorkbenchComponentInstance
==================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentInstance

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentContext`

   Enable to obtain information about the parent object that owns the VGT component.

.. py:currentmodule:: AnalysisWorkbenchComponentInstance

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentInstance.instance_path`
              - Return a path to the parent object that owns the VGT component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentInstance.template`
              - Return a template object the VGT component was created from or null if the VGT component was not created from a template.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchComponentInstance


Property detail
---------------

.. py:property:: instance_path
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentInstance.instance_path
    :type: str

    Return a path to the parent object that owns the VGT component.

.. py:property:: template
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentInstance.template
    :type: IAnalysisWorkbenchComponent

    Return a template object the VGT component was created from or null if the VGT component was not created from a template.


