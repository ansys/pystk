IAdvCATChosenObject
===================

.. py:class:: IAdvCATChosenObject

   object
   
   Chosen object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~ellipsoid_class`
            * - :py:meth:`~tangential`
            * - :py:meth:`~cross_track`
            * - :py:meth:`~normal`
            * - :py:meth:`~type`
            * - :py:meth:`~hard_body_radius`
            * - :py:meth:`~number_id`
            * - :py:meth:`~string_id`


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


