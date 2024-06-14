IGoldenSectionResult
====================

.. py:class:: IGoldenSectionResult

   object
   
   Properties for result parameters of a Golden Section profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable`
            * - :py:meth:`~name`
            * - :py:meth:`~parent_name`
            * - :py:meth:`~current_value`
            * - :py:meth:`~desired_operation`
            * - :py:meth:`~use_custom_display_unit`
            * - :py:meth:`~custom_display_unit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IGoldenSectionResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionResult.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionResult.current_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: desired_operation
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionResult.desired_operation
    :type: "GOLDEN_SECTION_DESIRED_OPERATION"

    Gets or sets the Desired Operation/Objective of golden section.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionResult.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.


