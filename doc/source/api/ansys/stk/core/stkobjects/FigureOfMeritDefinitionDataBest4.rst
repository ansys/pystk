FigureOfMeritDefinitionDataBest4
================================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4

   Bases: :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionData`

   Navigation accuracy based on best 4 satellites.

.. py:currentmodule:: FigureOfMeritDefinitionDataBest4

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4.is_best_4_metric_supported`
              - Is the type of Best 4 metric supported?

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4.best_4_metric`
              - Get or set the minimization metric for the best 4 computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4.best_4_metric_supported_types`
              - Best 4 supported types.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritDefinitionDataBest4


Property detail
---------------

.. py:property:: best_4_metric
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4.best_4_metric
    :type: FigureOfMeritMethod

    Get or set the minimization metric for the best 4 computation.

.. py:property:: best_4_metric_supported_types
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4.best_4_metric_supported_types
    :type: list

    Best 4 supported types.


Method detail
-------------



.. py:method:: is_best_4_metric_supported(self, best_4_metric: FigureOfMeritMethod) -> bool
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4.is_best_4_metric_supported

    Is the type of Best 4 metric supported?

    :Parameters:

        **best_4_metric** : :obj:`~FigureOfMeritMethod`


    :Returns:

        :obj:`~bool`


