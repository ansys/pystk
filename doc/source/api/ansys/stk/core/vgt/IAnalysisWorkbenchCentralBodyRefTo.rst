IAnalysisWorkbenchCentralBodyRefTo
==================================

.. py:class:: IAnalysisWorkbenchCentralBodyRefTo

   object
   
   Represents a reference to a VGT CentralBody.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_path`
              - Set a new central body using specified path.
            * - :py:meth:`~set_central_body`
              - Set a new central body.
            * - :py:meth:`~get_central_body`
              - Return a central body or null if the central body is invalid.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAnalysisWorkbenchCentralBodyRefTo



Method detail
-------------

.. py:method:: set_path(self, path:str) -> None

    Set a new central body using specified path.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_central_body(self, centralBody:"IAnalysisWorkbenchCentralBody") -> None

    Set a new central body.

    :Parameters:

    **centralBody** : :obj:`~"IAnalysisWorkbenchCentralBody"`

    :Returns:

        :obj:`~None`

.. py:method:: get_central_body(self) -> "IAnalysisWorkbenchCentralBody"

    Return a central body or null if the central body is invalid.

    :Returns:

        :obj:`~"IAnalysisWorkbenchCentralBody"`

