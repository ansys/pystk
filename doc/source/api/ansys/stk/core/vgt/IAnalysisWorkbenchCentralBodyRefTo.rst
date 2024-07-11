IAnalysisWorkbenchCentralBodyRefTo
==================================

.. py:class:: ansys.stk.core.vgt.IAnalysisWorkbenchCentralBodyRefTo

   object
   
   Represents a reference to a VGT CentralBody.

.. py:currentmodule:: IAnalysisWorkbenchCentralBodyRefTo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchCentralBodyRefTo.set_path`
              - Set a new central body using specified path.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchCentralBodyRefTo.set_central_body`
              - Set a new central body.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchCentralBodyRefTo.get_central_body`
              - Return a central body or null if the central body is invalid.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAnalysisWorkbenchCentralBodyRefTo



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchCentralBodyRefTo.set_path

    Set a new central body using specified path.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_central_body(self, centralBody: IAnalysisWorkbenchCentralBody) -> None
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchCentralBodyRefTo.set_central_body

    Set a new central body.

    :Parameters:

    **centralBody** : :obj:`~IAnalysisWorkbenchCentralBody`

    :Returns:

        :obj:`~None`

.. py:method:: get_central_body(self) -> IAnalysisWorkbenchCentralBody
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchCentralBodyRefTo.get_central_body

    Return a central body or null if the central body is invalid.

    :Returns:

        :obj:`~IAnalysisWorkbenchCentralBody`

