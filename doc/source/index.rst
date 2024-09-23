.. title:: PySTK documentation

.. meta::
    :description: PySTK provides a Python API to interact with Ansys Systems Tool Kit (STK).
    :keywords: PySTK, STK, AGI, Ansys, Python, API, MBSE, Satellite, Space, Mission, Analysis, Astrodynamics, Orbit, Propagation, Coverage, Access, Conjunction, Maneuver, Sensor, Communication, Ground Station, Facility, Facility, Scenario, Chain, Vector, Point, Area, Grid, Region, Terrain, Vehicle, Aircraft, Ship, Submarine, Missile

.. figure:: _static/logo.png
    :align: center
    :width: 640px 
   
PySTK provides a Python API to interact with `Ansys Systems Tool Kit`_ (STK).
STK provides a physics-based modeling environment for analyzing platforms
and payloads in a realistic mission context. You are viewing version |version|.

.. grid:: 1 1 3 3

    .. grid-item-card:: :fa:`power-off` Getting started
        :link: getting-started
        :link-type: doc
        :padding: 2 2 2 2

        Learn about PySTK, its prerequisites, and how to install it.

    .. grid-item-card:: :fa:`list-alt` User guide
        :link: user-guide
        :link-type: doc
        :padding: 2 2 2 2

        Understand key concepts and the main objects of PySTK.

    .. jinja:: main_toctree

    {% if build_api %}
    .. grid-item-card:: API reference :fa:`wrench`
        :link: api
        :link-type: doc
        :padding: 2 2 2 2

        A detailed guide describing the PySTK API. This guide documents all the
        methods and properties for each interface, class, and
        enumerations of each PySTK module.
    {% endif %}

    {% if build_examples %}
    .. grid-item-card:: :fa:`clone` Examples
        :link: examples
        :link-type: doc
        :padding: 2 2 2 2

        Learn how to use PySTK with examples that demonstrate its capabilities.
    {% endif %}

    .. grid-item-card:: :fa:`user-group` Contribute
        :link: contributing
        :link-type: doc
        :padding: 2 2 2 2

        Learn how to contribute to the project and become a part of the PySTK community.

    .. grid-item-card:: :fa:`download` Artifacts
        :link: artifacts
        :link-type: doc
        :padding: 2 2 2 2

        Download PySTK artifacts such as wheels and source distributions.


.. jinja:: main_toctree

    .. toctree::
       :hidden:
       :maxdepth: 3
    
       getting-started
       user-guide
       {% if build_api %}
       api
       {% endif %}
       {% if build_examples %}
       examples
       {% endif %}
       contributing
       artifacts

