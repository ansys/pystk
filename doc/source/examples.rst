Examples
########

.. jinja:: main_toctree

    {% if build_examples %}

    Basic examples
    ==============
    
    This series of tutorials provides basic examples involving Ansys STK® application objects using Python and PySTK.
    
    .. nbgallery::
        :caption: Basic examples
    
        examples/create-load-scenarios
        examples/facility-to-satellite-access
        examples/results-graphs
        examples/sensor-access
    
    Coverage examples
    =================
    
    This series of tutorials explains different ways to calculate satellite coverage using Python and PySTK.
    
    .. nbgallery::
        :caption: Coverage examples
    
        examples/satellite-coverage-calculator
        examples/satellite-coverage-analysis
    
    Space mission
    =============
    
    This series of tutorials explains how to model and simulate orbital maneuvers using Python and PySTK.
    
    .. nbgallery::
        :caption: Orbital maneuvers
    
        examples/hohmann-transfer
        examples/bielliptic-transfer
        examples/lambert-transfer

    .. nbgallery::
        :caption: Mission analysis
    
        examples/porkchop-plots
    
    Communications and radar
    ========================
    
    This series of tutorials explains how to model and simulate communications and radar systems using Python and PySTK.
    
    .. nbgallery::
        :caption: Communications and radar
    
        examples/radar-cross-section-detection
        examples/communication-link-calculator
    
    Aviator mission planning
    ========================
    
    This series of tutorials explains how to model and simulate aircraft missions using Python and PySTK's Aviator capabilities.
    
    .. nbgallery::
        :caption: Aviator mission planning
    
        examples/aviator-fuel-calculator
        examples/aircraft-carrier-landing

    {% else %}

    .. warning::

        Set ``BUILD_EXAMPLES`` to ``true`` in your environment to build the
        examples.

    {% endif %}
