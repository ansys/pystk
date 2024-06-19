IFigureOfMeritDefinitionDataBestN
=================================

.. py:class:: IFigureOfMeritDefinitionDataBestN

   IFigureOfMeritDefinitionData
   
   Navigation accuracy based on best N satellites.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_best_n_metric_supported`
              - Is the type of Best N metric supported?

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~best_n`
            * - :py:meth:`~best_n_metric`
            * - :py:meth:`~best_n_metric_supported_types`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionDataBestN


Property detail
---------------

.. py:property:: best_n
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDataBestN.best_n
    :type: int

    Navigation accuracy based on the specified number of satellites that yields the minimum GDOP.

.. py:property:: best_n_metric
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDataBestN.best_n_metric
    :type: FIGURE_OF_MERIT_METHOD

    Gets or sets the minimization metric for the best N computation.

.. py:property:: best_n_metric_supported_types
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDataBestN.best_n_metric_supported_types
    :type: list

    Best N supported types.


Method detail
-------------





.. py:method:: is_best_n_metric_supported(self, bestNMetric: FIGURE_OF_MERIT_METHOD) -> bool
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDataBestN.is_best_n_metric_supported

    Is the type of Best N metric supported?

    :Parameters:

    **bestNMetric** : :obj:`~FIGURE_OF_MERIT_METHOD`

    :Returns:

        :obj:`~bool`


