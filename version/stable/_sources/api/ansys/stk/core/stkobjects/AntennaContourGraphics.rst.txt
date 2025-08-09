AntennaContourGraphics
======================

.. py:class:: ansys.stk.core.stkobjects.AntennaContourGraphics

   Class defining contour Graphics properties of a Antenna.

.. py:currentmodule:: AntennaContourGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGraphics.is_contour_type_supported`
              - Return true if the supplied contour type is supported by this object, false otherwise.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGraphics.set_contour_type`
              - Set the current contour type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGraphics.show`
              - Opt whether to display volume graphics for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGraphics.supported_contour_types`
              - Get an array of the supported contour types.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGraphics.contour`
              - Get the current contour type's properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaContourGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.AntennaContourGraphics.show
    :type: bool

    Opt whether to display volume graphics for the antenna.

.. py:property:: supported_contour_types
    :canonical: ansys.stk.core.stkobjects.AntennaContourGraphics.supported_contour_types
    :type: list

    Get an array of the supported contour types.

.. py:property:: contour
    :canonical: ansys.stk.core.stkobjects.AntennaContourGraphics.contour
    :type: IAntennaContour

    Get the current contour type's properties.


Method detail
-------------



.. py:method:: is_contour_type_supported(self, value: AntennaContourType) -> bool
    :canonical: ansys.stk.core.stkobjects.AntennaContourGraphics.is_contour_type_supported

    Return true if the supplied contour type is supported by this object, false otherwise.

    :Parameters:

        **value** : :obj:`~AntennaContourType`


    :Returns:

        :obj:`~bool`


.. py:method:: set_contour_type(self, value: AntennaContourType) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaContourGraphics.set_contour_type

    Set the current contour type.

    :Parameters:

        **value** : :obj:`~AntennaContourType`


    :Returns:

        :obj:`~None`


