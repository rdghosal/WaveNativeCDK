#!/usr/bin/env python3

from aws_cdk import core

from wave_native_cdk.wave_native_stack import WaveNativeStack


app = core.App()
WaveNativeStack(app, "wave-native-cdk")

app.synth()
