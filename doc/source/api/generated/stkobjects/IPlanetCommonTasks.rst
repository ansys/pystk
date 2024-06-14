IPlanetCommonTasks
==================

.. py:class:: IPlanetCommonTasks

   object
   
   IAgPlCommonTasks.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_position_source_file`
              - Specify a planet ephemeris file, with a .pe extension.
            * - :py:meth:`~set_position_source_central_body`
              - Specify the planet using a central body and a desired ephemeris source.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPlanetCommonTasks



Method detail
-------------

.. py:method:: set_position_source_file(self, file:str) -> "IPlanetPositionFile"

    Specify a planet ephemeris file, with a .pe extension.

    :Parameters:

    **file** : :obj:`~str`

    :Returns:

        :obj:`~"IPlanetPositionFile"`

.. py:method:: set_position_source_central_body(self, centralBody:str, ephemSource:"EPHEM_SOURCE_TYPE") -> "IPlanetPositionCentralBody"

    Specify the planet using a central body and a desired ephemeris source.

    :Parameters:

    **centralBody** : :obj:`~str`
    **ephemSource** : :obj:`~"EPHEM_SOURCE_TYPE"`

    :Returns:

        :obj:`~"IPlanetPositionCentralBody"`

