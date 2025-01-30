FigureOfMeritDefinitionDataBestN
================================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN

   Bases: :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionData`

   Navigation accuracy based on best N satellites.

.. py:currentmodule:: FigureOfMeritDefinitionDataBestN

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN.is_best_n_metric_supported`
              - Is the type of Best N metric supported?

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN.best_n`
              - Navigation accuracy based on the specified number of satellites that yields the minimum GDOP.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN.best_n_metric`
              - Gets or sets the minimization metric for the best N computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN.best_n_metric_supported_types`
              - Best N supported types.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritDefinitionDataBestN


Property detail
---------------

.. py:property:: best_n
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN.best_n
    :type: int

    Navigation accuracy based on the specified number of satellites that yields the minimum GDOP.

.. py:property:: best_n_metric
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN.best_n_metric
    :type: FigureOfMeritMethod

    Gets or sets the minimization metric for the best N computation.

.. py:property:: best_n_metric_supported_types
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN.best_n_metric_supported_types
    :type: list

    Best N supported types.


Method detail
-------------





.. py:method:: is_best_n_metric_supported(self, best_n_metric: FigureOfMeritMethod) -> bool
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN.is_best_n_metric_supported

    Is the type of Best N metric supported?

    :Parameters:

    **best_n_metric** : :obj:`~FigureOfMeritMethod`

    :Returns:

        :obj:`~bool`


