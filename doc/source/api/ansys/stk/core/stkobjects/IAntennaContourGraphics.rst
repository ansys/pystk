IAntennaContourGraphics
=======================

.. py:class:: ansys.stk.core.stkobjects.IAntennaContourGraphics

   object
   
   IAgAntennaContourGraphics Interface for a antenna's contour properties.

.. py:currentmodule:: IAntennaContourGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGraphics.is_contour_type_supported`
              - Return true if the supplied contour type is supported by this object, false otherwise.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGraphics.set_contour_type`
              - Set the current contour type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGraphics.show`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGraphics.supported_contour_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGraphics.contour`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContourGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGraphics.show
    :type: bool

    Opt whether to display volume graphics for the antenna.

.. py:property:: supported_contour_types
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGraphics.supported_contour_types
    :type: list

    Gets an array of the supported contour types.

.. py:property:: contour
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGraphics.contour
    :type: IAntennaContour

    Gets the current contour type's properties.


Method detail
-------------



.. py:method:: is_contour_type_supported(self, val: ANTENNA_CONTOUR_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGraphics.is_contour_type_supported

    Return true if the supplied contour type is supported by this object, false otherwise.

    :Parameters:

    **val** : :obj:`~ANTENNA_CONTOUR_TYPE`

    :Returns:

        :obj:`~bool`


.. py:method:: set_contour_type(self, val: ANTENNA_CONTOUR_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGraphics.set_contour_type

    Set the current contour type.

    :Parameters:

    **val** : :obj:`~ANTENNA_CONTOUR_TYPE`

    :Returns:

        :obj:`~None`


