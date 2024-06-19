IStateCalcCurvilinearRelMotion
==============================

.. py:class:: IStateCalcCurvilinearRelMotion

   object
   
   Properties for Curvilinear Relative Motion  calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~reference_ellipse`
            * - :py:meth:`~location_source`
            * - :py:meth:`~reference_selection`
            * - :py:meth:`~reference`
            * - :py:meth:`~element_type`
            * - :py:meth:`~sign_convention`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcCurvilinearRelMotion


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: reference_ellipse
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference_ellipse
    :type: CALC_OBJECT_REFERENCE_ELLIPSE

    Selection of the satellite orbit that is used as the reference ellipse.

.. py:property:: location_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.location_source
    :type: CALC_OBJECT_LOCATION_SOURCE

    Selection of the satellite whose location is being reported with respect to the reference ellipse.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference
    :type: IAgLinkToObject

    Get the reference object.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.element_type
    :type: CALC_OBJECT_ELEM

    Choice of osculating or mean elements.

.. py:property:: sign_convention
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.sign_convention
    :type: CALC_OBJECT_ANGLE_SIGN

    Gets or sets the sign of the angle when the relative position has a positive component along the orbit normal.


