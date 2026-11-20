from zigpy.profiles import zha
from zigpy.zcl.clusters.general import Basic, Identify, Groups, Scenes
from zigpy.zcl.clusters.measurement import IlluminanceMeasurement
from zigpy.zcl.clusters.security import IasZone

from zhaquirks import CustomDevice
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)

from zhaquirks.tuya import (
    TuyaLocalCluster,
    TuyaOccupancyCluster,
    TuyaMCUCluster,
)


class TuyaPresenceCluster(TuyaOccupancyCluster):
    """Tuya human presence cluster"""
    _CONSTANT_ATTRIBUTES = {}


class TuyaTS0601Presence(CustomDevice):
    """TS0601 _TZE204_7gclukjs presence sensor"""

    signature = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.OCCUPANCY_SENSOR,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaMCUCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            }
        }
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.OCCUPANCY_SENSOR,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaMCUCluster,
                    TuyaPresenceCluster,
                    IlluminanceMeasurement.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            }
        }
    }
