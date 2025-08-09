SensorCustomPattern
===================

.. py:class:: ansys.stk.core.stkobjects.SensorCustomPattern

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPattern`

   Class defining the custom pattern for a Sensor.

.. py:currentmodule:: SensorCustomPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCustomPattern.filename`
              - Path and file name of the custom sensor pattern file.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCustomPattern.angular_resolution`
              - Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCustomPattern.use_native_resolution`
              - Control pattern subsampling.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorCustomPattern


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.SensorCustomPattern.filename
    :type: str

    Path and file name of the custom sensor pattern file.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.SensorCustomPattern.angular_resolution
    :type: typing.Any

    Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...

.. py:property:: use_native_resolution
    :canonical: ansys.stk.core.stkobjects.SensorCustomPattern.use_native_resolution
    :type: bool

    Control pattern subsampling.


