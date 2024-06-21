ISiteRelToPrevProcedure
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure

   object
   
   Interface used to access the options for a Relative to Previous Procedure site.

.. py:currentmodule:: ISiteRelToPrevProcedure

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure.bearing_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure.bearing`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure.range`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteRelToPrevProcedure


Property detail
---------------

.. py:property:: bearing_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure.bearing_mode
    :type: REL_ABS_BEARING

    Gets or sets the bearing reference.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure.bearing
    :type: typing.Any

    Gets or sets the bearing to define the site.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure.range
    :type: float

    Gets or sets the range from the previous procedure.


Method detail
-------------







.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRelToPrevProcedure.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

