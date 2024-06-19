IRadarClutterMapInheritable
===========================

.. py:class:: IRadarClutterMapInheritable

   object
   
   Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar inheritable clutter map.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~inherit`
            * - :py:meth:`~clutter_map`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarClutterMapInheritable


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.IRadarClutterMapInheritable.inherit
    :type: bool

    Gets or set the option to inherit the clutter map from the scenario object.

.. py:property:: clutter_map
    :canonical: ansys.stk.core.stkobjects.IRadarClutterMapInheritable.clutter_map
    :type: IAgRadarClutterMap

    Gets the radar clutter map.


