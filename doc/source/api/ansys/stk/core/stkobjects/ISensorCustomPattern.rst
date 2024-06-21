ISensorCustomPattern
====================

.. py:class:: ansys.stk.core.stkobjects.ISensorCustomPattern

   object
   
   IAgSnCustomPattern Interface for custom sensor patterns.

.. py:currentmodule:: ISensorCustomPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorCustomPattern.filename`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorCustomPattern.angular_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorCustomPattern.use_native_resolution`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorCustomPattern


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.ISensorCustomPattern.filename
    :type: str

    Path and file name of the custom sensor pattern file.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.ISensorCustomPattern.angular_resolution
    :type: typing.Any

    Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...

.. py:property:: use_native_resolution
    :canonical: ansys.stk.core.stkobjects.ISensorCustomPattern.use_native_resolution
    :type: bool

    Controls pattern subsampling.


