ITileset3D
==========

.. py:class:: ITileset3D

   object
   
   IAg3DTileset Interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~source_type`
            * - :py:meth:`~uri`
            * - :py:meth:`~reference_frame`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITileset3D


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.ITileset3D.name
    :type: str

    Name of the 3DTileset.

.. py:property:: source_type
    :canonical: ansys.stk.core.stkobjects.ITileset3D.source_type
    :type: "TILESET_3D_SOURCE_TYPE"

    Source type of the 3DTileset. A member of the AgE3DTilesetSourceType enumeration.

.. py:property:: uri
    :canonical: ansys.stk.core.stkobjects.ITileset3D.uri
    :type: str

    URI of the 3DTileset asset.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.ITileset3D.reference_frame
    :type: str

    Reference Frame (VGT System) of the 3DTileset.


