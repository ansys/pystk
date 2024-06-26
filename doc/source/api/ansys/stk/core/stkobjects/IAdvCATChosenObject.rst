IAdvCATChosenObject
===================

.. py:class:: ansys.stk.core.stkobjects.IAdvCATChosenObject

   object
   
   Chosen object.

.. py:currentmodule:: IAdvCATChosenObject

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.name`
              - Get the chosen object name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.ellipsoid_class`
              - Determine Ellipsoid Sizing method class.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.tangential`
              - Semi-major Axes Size along A.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.cross_track`
              - Semi-major Axes Size along B.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.normal`
              - Semi-major Axes Size along C.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.type`
              - Get the File Type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.hard_body_radius`
              - Used in prob of collision.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.number_id`
              - An IRON or other numeric id.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATChosenObject.string_id`
              - A VEID, or other character id.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAdvCATChosenObject


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.name
    :type: str

    Get the chosen object name.

.. py:property:: ellipsoid_class
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.ellipsoid_class
    :type: ADV_CAT_ELLIPSOID_CLASS

    Determine Ellipsoid Sizing method class.

.. py:property:: tangential
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.tangential
    :type: float

    Semi-major Axes Size along A.

.. py:property:: cross_track
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.cross_track
    :type: float

    Semi-major Axes Size along B.

.. py:property:: normal
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.normal
    :type: float

    Semi-major Axes Size along C.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.type
    :type: str

    Get the File Type.

.. py:property:: hard_body_radius
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.hard_body_radius
    :type: float

    Used in prob of collision.

.. py:property:: number_id
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.number_id
    :type: int

    An IRON or other numeric id.

.. py:property:: string_id
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObject.string_id
    :type: str

    A VEID, or other character id.


