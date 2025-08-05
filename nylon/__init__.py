import os
from utils.Processor.ExperimentTypes import ExperimentTypes

def concat( path : str ):
    ROOT_DIR = os.path.dirname( os.path.abspath( __file__ ) )
    return os.path.join( ROOT_DIR, path )

def process():
    from utils.Processor.Instron import Instron
    from utils.Processor.Shimadzu import Shimadzu
    from utils.Processor.Experiments import CS_SHAPES
    from utils.Processor import parse_data

    ### COMPRESSION LDFJ ###
    with Shimadzu( concat( "./data/Compression-Cyl/data/samples.csv" ), concat( "./data/Compression-Cyl/dimensions.csv" ) ) as data:
        parse_data( data, concat( "./results/Compression-Cyl/result_{}.csv" ), CS_SHAPES.CIRCLE, ExperimentTypes.TENSILE )

    ### COMPRESSION VC ###
    with Shimadzu( concat( "./data/Compression-Cyl-VC/data/samples.csv" ), concat( "./data/Compression-Cyl-VC/dimensions.csv" ) ) as data:
        parse_data( data, concat( "./results/Compression-Cyl-VC/result_{}.csv" ), CS_SHAPES.CIRCLE, ExperimentTypes.TENSILE )

    with Shimadzu( concat( "./data/Compression-Cube-VC/data/samples.csv" ), concat( "./data/Compression-Cube-VC/dimensions.csv" ) ) as data:
        parse_data( data, concat( "./results/Compression-Cube-VC/result_{}.csv" ), CS_SHAPES.RECTANGLE, ExperimentTypes.TENSILE )

    ### BENDING LDFJ ###
    with Instron( concat( "./data/D790-Bending/data/" ), concat( "./data/D790-Bending/dimensions.csv" ) ) as data:
        parse_data( data, concat( "./results/D790-Bending/result_{}.csv" ), CS_SHAPES.RECTANGLE, ExperimentTypes.BENDING )

def plot():
    from utils.Processor.DataReader import DataReader
    from utils.Plotter.Plotter import Plotter
    from utils.Plotter.Limits import Limits
    from utils.Plotter.Templates.PlotTemplates import PlotTemplates

    ### COMPRESSION LDFJ ###
    with DataReader( "./results/Compression-Cyl/", ExperimentTypes.TENSILE ) as data:
        plt = Plotter( data )

        template = PlotTemplates.SimplePlot(
            title = "Compression Cylinder (0°)",
            limits = Limits( xlimit=0.2,ylimit=None )
        )
        plt.figure( "0deg" )
        plt.plot( Plotter.ENGINEER, template, [ 0,1,2,3,4 ] )
        
        template = PlotTemplates.SimplePlot(
            title = "Compression Cylinder (45°)",
            limits = Limits( xlimit=0.2,ylimit=None )
        )
        plt.figure( "45deg" )
        plt.plot( Plotter.ENGINEER, template, [ 5,6,7,8,9 ] )

        template = PlotTemplates.SimplePlot(
            title = "Compression Cylinder (90°)",
            limits = Limits( xlimit=0.2,ylimit=None )
        )
        plt.figure( "90deg" )
        plt.plot( Plotter.ENGINEER, template, [ 10,11,12,13,14 ] )

        plt.savefigs( "./results/figs/fig_{0}.png" )

def analyze():
    pass
