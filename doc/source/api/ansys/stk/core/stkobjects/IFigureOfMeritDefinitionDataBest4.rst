IFigureOfMeritDefinitionDataBest4
=================================

.. py:class:: IFigureOfMeritDefinitionDataBest4

   IFigureOfMeritDefinitionData
   
   Navigation accuracy based on best four satellites.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_best4_metric_supported`
              - Is the type of Best 4 metric supported?

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~best4_metric`
            * - :py:meth:`~best4_metric_supported_types`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionDataBest4


Property detail
---------------

.. py:property:: best4_metric
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDataBest4.best4_metric
    :type: FIGURE_OF_MERIT_METHOD

    Gets or sets the minimization metric for the best 4 computation.

.. py:property:: best4_metric_supported_types
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDataBest4.best4_metric_supported_types
    :type: list

    Best 4 supported types.


Method detail
-------------



.. py:method:: is_best4_metric_supported(self, best4Metric: FIGURE_OF_MERIT_METHOD) -> bool
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDataBest4.is_best4_metric_supported

    Is the type of Best 4 metric supported?

    :Parameters:

    **best4Metric** : :obj:`~FIGURE_OF_MERIT_METHOD`

    :Returns:

        :obj:`~bool`


