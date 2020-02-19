#!/usr/bin/env python3

from aws_cdk import core

from wave_native_cdk.wave_native_cdk_stack import WaveNativeCdkStack


app = core.App()
WaveNativeCdkStack(app, "wave-native-cdk")

app.synth()
