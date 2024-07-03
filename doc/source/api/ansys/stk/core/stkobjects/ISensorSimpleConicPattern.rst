ISensorSimpleConicPattern
=========================

.. py:class:: ansys.stk.core.stkobjects.ISensorSimpleConicPattern

   object
   
   IAgSnSimpleConicPattern Interface for a sensor pattern defined by a simple cone angle.

.. py:currentmodule:: ISensorSimpleConicPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSimpleConicPattern.cone_angle`
              - Simple cone angle defining the sensor pattern. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSimpleConicPattern.angular_resolution`
              - Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorSimpleConicPattern


Property detail
---------------

.. py:property:: cone_angle
    :canonical: ansys.stk.core.stkobjects.ISensorSimpleConicPattern.cone_angle
    :type: typing.Any

    Simple cone angle defining the sensor pattern. Uses Angle Dimension.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.ISensorSimpleConicPattern.angular_resolution
    :type: typing.Any

    Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


