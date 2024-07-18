AnalysisWorkbenchCentralBodyRefTo
=================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyRefTo

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchRefTo`

   Represents a central body reference.

.. py:currentmodule:: AnalysisWorkbenchCentralBodyRefTo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyRefTo.set_path`
              - Set a new central body using specified path.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyRefTo.set_central_body`
              - Set a new central body.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyRefTo.get_central_body`
              - Return a central body or null if the central body is invalid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchCentralBodyRefTo



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyRefTo.set_path

    Set a new central body using specified path.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_central_body(self, centralBody: AnalysisWorkbenchCentralBody) -> None
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyRefTo.set_central_body

    Set a new central body.

    :Parameters:

    **centralBody** : :obj:`~AnalysisWorkbenchCentralBody`

    :Returns:

        :obj:`~None`

.. py:method:: get_central_body(self) -> AnalysisWorkbenchCentralBody
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyRefTo.get_central_body

    Return a central body or null if the central body is invalid.

    :Returns:

        :obj:`~AnalysisWorkbenchCentralBody`

