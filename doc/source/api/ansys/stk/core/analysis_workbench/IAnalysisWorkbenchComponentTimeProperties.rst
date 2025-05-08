IAnalysisWorkbenchComponentTimeProperties
=========================================

.. py:class:: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties

   Define methods to compute time properties such as availability and special times.

.. py:currentmodule:: IAnalysisWorkbenchComponentTimeProperties

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties.get_availability`
              - Return a collection of availability intervals.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import IAnalysisWorkbenchComponentTimeProperties



Method detail
-------------

.. py:method:: get_availability(self) -> TimeToolIntervalCollection
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties.get_availability

    Return a collection of availability intervals.

    :Returns:

        :obj:`~TimeToolIntervalCollection`

