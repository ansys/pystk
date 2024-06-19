ISiteRelToSTKObject
===================

.. py:class:: ISiteRelToSTKObject

   object
   
   Interface used to access the options for a Relative to Stationary STK Object site.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~object_name`
            * - :py:meth:`~valid_object_names`
            * - :py:meth:`~bearing`
            * - :py:meth:`~use_magnetic_bearing`
            * - :py:meth:`~range`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteRelToSTKObject


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToSTKObject.object_name
    :type: str

    Gets or sets the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToSTKObject.valid_object_names
    :type: list

    Returns the valid object names.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToSTKObject.bearing
    :type: typing.Any

    Gets or sets the bearing from the STK object.

.. py:property:: use_magnetic_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToSTKObject.use_magnetic_bearing
    :type: bool

    Gets or sets the option to use a magnetic bearing.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToSTKObject.range
    :type: float

    Gets or sets the range from the STK object.


Method detail
-------------










.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToSTKObject.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

