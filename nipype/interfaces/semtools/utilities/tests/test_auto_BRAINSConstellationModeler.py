# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brains import BRAINSConstellationModeler


def test_BRAINSConstellationModeler_inputs():
    input_map = dict(
        BackgroundFillValue=dict(argstr='--BackgroundFillValue %s', ),
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        inputTrainingList=dict(argstr='--inputTrainingList %s', ),
        mspQualityLevel=dict(argstr='--mspQualityLevel %d', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        optimizedLandmarksFilenameExtender=dict(
            argstr='--optimizedLandmarksFilenameExtender %s', ),
        outputModel=dict(
            argstr='--outputModel %s',
            hash_files=False,
        ),
        rescaleIntensities=dict(argstr='--rescaleIntensities ', ),
        rescaleIntensitiesOutputRange=dict(
            argstr='--rescaleIntensitiesOutputRange %s',
            sep=',',
        ),
        resultsDir=dict(
            argstr='--resultsDir %s',
            hash_files=False,
        ),
        saveOptimizedLandmarks=dict(argstr='--saveOptimizedLandmarks ', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        trimRescaledIntensities=dict(argstr='--trimRescaledIntensities %f', ),
        verbose=dict(argstr='--verbose ', ),
        writedebuggingImagesLevel=dict(
            argstr='--writedebuggingImagesLevel %d', ),
    )
    inputs = BRAINSConstellationModeler.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BRAINSConstellationModeler_outputs():
    output_map = dict(
        outputModel=dict(),
        resultsDir=dict(),
    )
    outputs = BRAINSConstellationModeler.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
