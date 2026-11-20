"""Aqara E1-series wireless remote."""
from zigpy.profiles import zha
from zigpy.zcl.clusters.general import (
    Basic,
    Identify,
    MultistateInput,
    OnOff,
    Ota,
    PowerConfiguration,
)

from zhaquirks.const import (
    ALT_DOUBLE_PRESS,
    ALT_SHORT_PRESS,
    ARGS,
    BUTTON,
    COMMAND,
    COMMAND_OFF,
    COMMAND_TOGGLE,
    DEVICE_TYPE,
    DOUBLE_PRESS,
    ENDPOINT_ID,
    ENDPOINTS,
    INPUT_CLUSTERS,
    LEFT,
    LONG_PRESS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
    RIGHT,
    SHORT_PRESS,
    TRIPLE_PRESS,
)
from zhaquirks.xiaomi import (
    LUMI,
    BasicCluster,
    XiaomiCustomDevice,
)
from zhaquirks.xiaomi.aqara.opple_remote import (
    COMMAND_1_DOUBLE,
    COMMAND_1_HOLD,
    COMMAND_1_SINGLE,
    COMMAND_1_TRIPLE,
    COMMAND_2_DOUBLE,
    COMMAND_2_HOLD,
    COMMAND_2_SINGLE,
    COMMAND_2_TRIPLE,
    COMMAND_3_DOUBLE,
    COMMAND_3_HOLD,
    COMMAND_3_SINGLE,
    COMMAND_3_TRIPLE,
    MultistateInputCluster,
)
from zhaquirks.xiaomi.aqara.remote_h1 import (
    AqaraRemoteManuSpecificCluster,
    PowerConfigurationClusterH1Remote,
)

BOTH_BUTTONS = "both_buttons"


class RemoteE1SingleRocker1(XiaomiCustomDevice):
    """Aqara E1 Wireless Remote Double Rocker."""

    manufacturer_id_override = 0x115F

    signature = {
        MODELS_INFO: [(LUMI, "lumi.remote.acn003")],
        ENDPOINTS: {
            1: {
                # SizePrefixedSimpleDescriptor(
                #   endpoint=1, profile=260, device_type=0,
                #   input_clusters=["0x0000", "0x0001", "0x0003", "0x0012", "0xfcc0"],
                #   output_clusters=["0x0003", "0x0006", "0x0019"])
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    MultistateInput.cluster_id,
                    AqaraRemoteManuSpecificCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                ],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_SWITCH,
                INPUT_CLUSTERS: [
                    BasicCluster,
                    Identify.cluster_id,
                    PowerConfigurationClusterH1Remote,
                    MultistateInputCluster,
                    AqaraRemoteManuSpecificCluster,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                ],
            },
        }
    }
    device_automation_triggers = {
        # triggers when operation_mode == event
        # the button doesn't send an release event after hold
        (SHORT_PRESS, LEFT): {COMMAND: COMMAND_1_SINGLE},
        (DOUBLE_PRESS, LEFT): {COMMAND: COMMAND_1_DOUBLE},
        (TRIPLE_PRESS, LEFT): {COMMAND: COMMAND_1_TRIPLE},
        (LONG_PRESS, LEFT): {COMMAND: COMMAND_1_HOLD},
        # triggers when operation_mode == command
        (ALT_SHORT_PRESS, BUTTON): {COMMAND: COMMAND_TOGGLE, ENDPOINT_ID: 1, ARGS: []},
        (ALT_DOUBLE_PRESS, BUTTON): {COMMAND: COMMAND_OFF, ENDPOINT_ID: 1, ARGS: []},
    }
